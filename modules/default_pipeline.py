import modules.core as core
import os
import torch
import modules.path

from comfy.model_base import SDXL, SDXLRefiner
from modules.patch import cfg_patched
from modules.expansion import FooocusExpansion


xl_base: core.StableDiffusionModel = None
xl_base_hash = ''

xl_refiner: core.StableDiffusionModel = None
xl_refiner_hash = ''

xl_base_patched: core.StableDiffusionModel = None
xl_base_patched_hash = ''


def refresh_base_model(name):
    global xl_base, xl_base_hash, xl_base_patched, xl_base_patched_hash
    if xl_base_hash == str(name):
        return

    filename = os.path.join(modules.path.modelfile_path, name)

    if xl_base is not None:
        xl_base.to_meta()
        xl_base = None

    xl_base = core.load_model(filename)
    if not isinstance(xl_base.unet.model, SDXL):
        print('Model not supported. Fooocus only support SDXL model as the base model.')
        xl_base = None
        xl_base_hash = ''
        refresh_base_model(modules.path.default_base_model_name)
        xl_base_hash = name
        xl_base_patched = xl_base
        xl_base_patched_hash = ''
        return

    xl_base_hash = name
    xl_base_patched = xl_base
    xl_base_patched_hash = ''
    print(f'Base model loaded: {xl_base_hash}')
    return


def refresh_refiner_model(name):
    global xl_refiner, xl_refiner_hash
    if xl_refiner_hash == str(name):
        return

    if name == 'None':
        xl_refiner = None
        xl_refiner_hash = ''
        print(f'Refiner unloaded.')
        return

    filename = os.path.join(modules.path.modelfile_path, name)

    if xl_refiner is not None:
        xl_refiner.to_meta()
        xl_refiner = None

    xl_refiner = core.load_model(filename)
    if not isinstance(xl_refiner.unet.model, SDXLRefiner):
        print('Model not supported. Fooocus only support SDXL refiner as the refiner.')
        xl_refiner = None
        xl_refiner_hash = ''
        print(f'Refiner unloaded.')
        return

    xl_refiner_hash = name
    print(f'Refiner model loaded: {xl_refiner_hash}')

    xl_refiner.vae.first_stage_model.to('meta')
    xl_refiner.vae = None
    return


def refresh_loras(loras):
    global xl_base, xl_base_patched, xl_base_patched_hash
    if xl_base_patched_hash == str(loras):
        return

    model = xl_base
    for name, weight in loras:
        if name == 'None':
            continue

        filename = os.path.join(modules.path.lorafile_path, name)
        model = core.load_lora(model, filename, strength_model=weight, strength_clip=weight)
    xl_base_patched = model
    xl_base_patched_hash = str(loras)
    print(f'LoRAs loaded: {xl_base_patched_hash}')

    return


refresh_base_model(modules.path.default_base_model_name)
refresh_refiner_model(modules.path.default_refiner_model_name)
refresh_loras([(modules.path.default_lora_name, 0.5), ('None', 0.5), ('None', 0.5), ('None', 0.5), ('None', 0.5)])

expansion = FooocusExpansion()


@torch.no_grad()
def clip_encode_single(clip, text, verbose=False):
    cached = clip.fcs_cond_cache.get(text, None)
    if cached is not None:
        if verbose:
            print(f'[CLIP Cached] {text}')
        return cached
    tokens = clip.tokenize(text)
    result = clip.encode_from_tokens(tokens, return_pooled=True)
    clip.fcs_cond_cache[text] = result
    if verbose:
        print(f'[CLIP Encoded] {text}')
    return result


@torch.no_grad()
def clip_encode(sd, texts, pool_top_k=1):
    if sd is None:
        return None
    if sd.clip is None:
        return None
    if not isinstance(texts, list):
        return None
    if len(texts) == 0:
        return None

    clip = sd.clip
    cond_list = []
    pooled_acc = 0

    for i, text in enumerate(texts):
        cond, pooled = clip_encode_single(clip, text)
        cond_list.append(cond)
        if i < pool_top_k:
            pooled_acc += pooled

    return [[torch.cat(cond_list, dim=1), {"pooled_output": pooled_acc}]]


@torch.no_grad()
def clear_sd_cond_cache(sd):
    if sd is None:
        return None
    if sd.clip is None:
        return None
    sd.clip.fcs_cond_cache = {}
    return


@torch.no_grad()
def clear_all_caches():
    clear_sd_cond_cache(xl_base_patched)
    clear_sd_cond_cache(xl_refiner)


@torch.no_grad()
def process_diffusion(positive_cond, negative_cond, steps, switch, width, height, image_seed, callback):
    if xl_base is not None:
        xl_base.unet.model_options['sampler_cfg_function'] = cfg_patched

    if xl_base_patched is not None:
        xl_base_patched.unet.model_options['sampler_cfg_function'] = cfg_patched

    if xl_refiner is not None:
        xl_refiner.unet.model_options['sampler_cfg_function'] = cfg_patched

    empty_latent = core.generate_empty_latent(width=width, height=height, batch_size=1)

    if xl_refiner is not None:
        sampled_latent = core.ksampler_with_refiner(
            model=xl_base_patched.unet,
            positive=positive_cond[0],
            negative=negative_cond[0],
            refiner=xl_refiner.unet,
            refiner_positive=positive_cond[1],
            refiner_negative=negative_cond[1],
            refiner_switch_step=switch,
            latent=empty_latent,
            steps=steps, start_step=0, last_step=steps, disable_noise=False, force_full_denoise=True,
            seed=image_seed,
            callback_function=callback
        )
    else:
        sampled_latent = core.ksampler(
            model=xl_base_patched.unet,
            positive=positive_cond[0],
            negative=negative_cond[0],
            latent=empty_latent,
            steps=steps, start_step=0, last_step=steps, disable_noise=False, force_full_denoise=True,
            seed=image_seed,
            callback_function=callback
        )

    decoded_latent = core.decode_vae(vae=xl_base_patched.vae, latent_image=sampled_latent)
    images = core.image_to_numpy(decoded_latent)
    return images
