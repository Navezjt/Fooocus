import os
import json
import args_manager
import modules.flags
import modules.sdxl_styles

from modules.model_loader import load_file_from_url
from modules.util import get_files_from_folder


config_path = os.path.abspath("./config.txt")
config_example_path = os.path.abspath("config_modification_tutorial.txt")
config_dict = {}
always_save_keys = []
visited_keys = []

try:
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as json_file:
            config_dict = json.load(json_file)
            always_save_keys = list(config_dict.keys())
except Exception as e:
    print('Load path config failed')
    print(e)


def try_load_deprecated_user_path_config():
    global config_dict

    if not os.path.exists('user_path_config.txt'):
        return

    try:
        deprecated_config_dict = json.load(open('user_path_config.txt', "r", encoding="utf-8"))

        def replace_config(old_key, new_key):
            if old_key in deprecated_config_dict:
                config_dict[new_key] = deprecated_config_dict[old_key]
                del deprecated_config_dict[old_key]

        replace_config('modelfile_path', 'path_checkpoints')
        replace_config('lorafile_path', 'path_loras')
        replace_config('embeddings_path', 'path_embeddings')
        replace_config('vae_approx_path', 'path_vae_approx')
        replace_config('upscale_models_path', 'path_upscale_models')
        replace_config('inpaint_models_path', 'path_inpaint')
        replace_config('controlnet_models_path', 'path_controlnet')
        replace_config('clip_vision_models_path', 'path_clip_vision')
        replace_config('fooocus_expansion_path', 'path_fooocus_expansion')
        replace_config('temp_outputs_path', 'path_outputs')

        if deprecated_config_dict.get("default_model", None) == 'juggernautXL_version6Rundiffusion.safetensors':
            os.replace('user_path_config.txt', 'user_path_config-deprecated.txt')
            print('Config updated successfully in silence. '
                  'A backup of previous config is written to "user_path_config-deprecated.txt".')
            return

        if input("Newer models and configs are available. "
                 "Download and update files? [Y/n]:") in ['n', 'N', 'No', 'no', 'NO']:
            config_dict.update(deprecated_config_dict)
            print('Loading using deprecated old models and deprecated old configs.')
            return
        else:
            os.replace('user_path_config.txt', 'user_path_config-deprecated.txt')
            print('Config updated successfully by user. '
                  'A backup of previous config is written to "user_path_config-deprecated.txt".')
            return
    except Exception as e:
        print('Processing deprecated config failed')
        print(e)
    return


try_load_deprecated_user_path_config()

preset = args_manager.args.preset

if isinstance(preset, str):
    preset = os.path.abspath(f'./presets/{preset}.json')
    try:
        if os.path.exists(preset):
            with open(preset, "r", encoding="utf-8") as json_file:
                preset = json.load(json_file)
    except Exception as e:
        print('Load preset config failed')
        print(e)

preset = preset if isinstance(preset, dict) else None

if preset is not None:
    config_dict.update(preset)


def get_dir_or_set_default(key, default_value):
    global config_dict, visited_keys, always_save_keys

    if key not in visited_keys:
        visited_keys.append(key)

    if key not in always_save_keys:
        always_save_keys.append(key)

    v = config_dict.get(key, None)
    if isinstance(v, str) and os.path.exists(v) and os.path.isdir(v):
        return v
    else:
        dp = os.path.abspath(os.path.join(os.path.dirname(__file__), default_value))
        os.makedirs(dp, exist_ok=True)
        config_dict[key] = dp
        return dp


path_checkpoints = get_dir_or_set_default('path_checkpoints', '../models/checkpoints/')
path_loras = get_dir_or_set_default('path_loras', '../models/loras/')
path_embeddings = get_dir_or_set_default('path_embeddings', '../models/embeddings/')
path_vae_approx = get_dir_or_set_default('path_vae_approx', '../models/vae_approx/')
path_upscale_models = get_dir_or_set_default('path_upscale_models', '../models/upscale_models/')
path_inpaint = get_dir_or_set_default('path_inpaint', '../models/inpaint/')
path_controlnet = get_dir_or_set_default('path_controlnet', '../models/controlnet/')
path_clip_vision = get_dir_or_set_default('path_clip_vision', '../models/clip_vision/')
path_fooocus_expansion = get_dir_or_set_default('path_fooocus_expansion', '../models/prompt_expansion/fooocus_expansion')
path_outputs = get_dir_or_set_default('path_outputs', '../outputs/')


def get_config_item_or_set_default(key, default_value, validator, disable_empty_as_none=False):
    global config_dict, visited_keys

    if key not in visited_keys:
        visited_keys.append(key)
    
    if key not in config_dict:
        config_dict[key] = default_value
        return default_value

    v = config_dict.get(key, None)
    if not disable_empty_as_none:
        if v is None or v == '':
            v = 'None'
    if validator(v):
        return v
    else:
        config_dict[key] = default_value
        return default_value


default_base_model_name = get_config_item_or_set_default(
    key='default_model',
    default_value='juggernautXL_version6Rundiffusion.safetensors',
    validator=lambda x: isinstance(x, str)
)
default_refiner_model_name = get_config_item_or_set_default(
    key='default_refiner',
    default_value='None',
    validator=lambda x: isinstance(x, str)
)
default_refiner_switch = get_config_item_or_set_default(
    key='default_refiner_switch',
    default_value=0.5,
    validator=lambda x: isinstance(x, float)
)
default_lora_name = get_config_item_or_set_default(
    key='default_lora',
    default_value='sd_xl_offset_example-lora_1.0.safetensors',
    validator=lambda x: isinstance(x, str)
)
default_lora_weight = get_config_item_or_set_default(
    key='default_lora_weight',
    default_value=0.1,
    validator=lambda x: isinstance(x, float)
)
default_cfg_scale = get_config_item_or_set_default(
    key='default_cfg_scale',
    default_value=4.0,
    validator=lambda x: isinstance(x, float)
)
default_sample_sharpness = get_config_item_or_set_default(
    key='default_sample_sharpness',
    default_value=2,
    validator=lambda x: isinstance(x, float)
)
default_sampler = get_config_item_or_set_default(
    key='default_sampler',
    default_value='dpmpp_2m_sde_gpu',
    validator=lambda x: x in modules.flags.sampler_list
)
default_scheduler = get_config_item_or_set_default(
    key='default_scheduler',
    default_value='karras',
    validator=lambda x: x in modules.flags.scheduler_list
)
default_styles = get_config_item_or_set_default(
    key='default_styles',
    default_value=['Fooocus V2', 'Fooocus Enhance', 'Fooocus Sharp'],
    validator=lambda x: isinstance(x, list) and all(y in modules.sdxl_styles.legal_style_names for y in x)
)
default_prompt_negative = get_config_item_or_set_default(
    key='default_prompt_negative',
    default_value='',
    validator=lambda x: isinstance(x, str),
    disable_empty_as_none=True
)
default_prompt = get_config_item_or_set_default(
    key='default_prompt',
    default_value='',
    validator=lambda x: isinstance(x, str),
    disable_empty_as_none=True
)
default_advanced_checkbox = get_config_item_or_set_default(
    key='default_advanced_checkbox',
    default_value=False,
    validator=lambda x: isinstance(x, bool)
)
default_image_number = get_config_item_or_set_default(
    key='default_image_number',
    default_value=2,
    validator=lambda x: isinstance(x, int) and x >= 1 and x <= 32
)
checkpoint_downloads = get_config_item_or_set_default(
    key='checkpoint_downloads',
    default_value={
        'juggernautXL_version6Rundiffusion.safetensors':
            'https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/juggernautXL_version6Rundiffusion.safetensors'
    },
    validator=lambda x: isinstance(x, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in x.items())
)
lora_downloads = get_config_item_or_set_default(
    key='lora_downloads',
    default_value={
        'sd_xl_offset_example-lora_1.0.safetensors':
            'https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors'
    },
    validator=lambda x: isinstance(x, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in x.items())
)
embeddings_downloads = get_config_item_or_set_default(
    key='embeddings_downloads',
    default_value={},
    validator=lambda x: isinstance(x, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in x.items())
)
available_aspect_ratios = get_config_item_or_set_default(
    key='available_aspect_ratios',
    default_value=['704*1408', '704*1344', '768*1344', '768*1280', '832*1216', '832*1152', '896*1152', '896*1088', '960*1088', '960*1024', '1024*1024', '1024*960', '1088*960', '1088*896', '1152*896', '1152*832', '1216*832', '1280*768', '1344*768', '1344*704', '1408*704', '1472*704', '1536*640', '1600*640', '1664*576', '1728*576'],
    validator=lambda x: isinstance(x, list) and all('*' in v for v in x) and len(x) > 1
)
default_aspect_ratio = get_config_item_or_set_default(
    key='default_aspect_ratio',
    default_value='1152*896' if '1152*896' in available_aspect_ratios else available_aspect_ratios[0],
    validator=lambda x: x in available_aspect_ratios
)

with open(config_path, "w", encoding="utf-8") as json_file:
    json.dump({k: config_dict[k] for k in always_save_keys}, json_file, indent=4)

with open(config_example_path, "w", encoding="utf-8") as json_file:
    cpa = config_path.replace("\\", "\\\\")
    json_file.write(f'You can modify your "{cpa}" using the below keys, formats, and examples.\n'
                    f'Do not modify this file. Modifications in this file will not take effect.\n'
                    f'This file is a tutorial and example. Please edit "{cpa}" to really change any settings.\n'
                    f'Remember to split the paths with "\\\\" rather than "\\".\n\n\n')
    json.dump({k: config_dict[k] for k in visited_keys}, json_file, indent=4)


os.makedirs(path_outputs, exist_ok=True)

model_filenames = []
lora_filenames = []

available_aspect_ratios = [x.replace('*', '×') for x in available_aspect_ratios]
default_aspect_ratio = default_aspect_ratio.replace('*', '×')


def get_model_filenames(folder_path, name_filter=None):
    return get_files_from_folder(folder_path, ['.pth', '.ckpt', '.bin', '.safetensors', '.fooocus.patch'], name_filter)


def update_all_model_names():
    global model_filenames, lora_filenames
    model_filenames = get_model_filenames(path_checkpoints)
    lora_filenames = get_model_filenames(path_loras)
    return


def downloading_inpaint_models(v):
    assert v in ['v1', 'v2.5', 'v2.6']

    load_file_from_url(
        url='https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/fooocus_inpaint_head.pth',
        model_dir=path_inpaint,
        file_name='fooocus_inpaint_head.pth'
    )
    head_file = os.path.join(path_inpaint, 'fooocus_inpaint_head.pth')
    patch_file = None

    if v == 'v1':
        load_file_from_url(
            url='https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint.fooocus.patch',
            model_dir=path_inpaint,
            file_name='inpaint.fooocus.patch'
        )
        patch_file = os.path.join(path_inpaint, 'inpaint.fooocus.patch')

    if v == 'v2.5':
        load_file_from_url(
            url='https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint_v25.fooocus.patch',
            model_dir=path_inpaint,
            file_name='inpaint_v25.fooocus.patch'
        )
        patch_file = os.path.join(path_inpaint, 'inpaint_v25.fooocus.patch')

    if v == 'v2.6':
        load_file_from_url(
            url='https://huggingface.co/lllyasviel/fooocus_inpaint/resolve/main/inpaint_v26.fooocus.patch',
            model_dir=path_inpaint,
            file_name='inpaint_v26.fooocus.patch'
        )
        patch_file = os.path.join(path_inpaint, 'inpaint_v26.fooocus.patch')

    return head_file, patch_file


def downloading_sdxl_lcm_lora():
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/sdxl_lcm_lora.safetensors',
        model_dir=path_loras,
        file_name='sdxl_lcm_lora.safetensors'
    )
    return os.path.join(path_loras, 'sdxl_lcm_lora.safetensors')


def downloading_controlnet_canny():
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/control-lora-canny-rank128.safetensors',
        model_dir=path_controlnet,
        file_name='control-lora-canny-rank128.safetensors'
    )
    return os.path.join(path_controlnet, 'control-lora-canny-rank128.safetensors')


def downloading_controlnet_cpds():
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_xl_cpds_128.safetensors',
        model_dir=path_controlnet,
        file_name='fooocus_xl_cpds_128.safetensors'
    )
    return os.path.join(path_controlnet, 'fooocus_xl_cpds_128.safetensors')


def downloading_ip_adapters(v):
    assert v in ['ip', 'face']

    results = []

    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/clip_vision_vit_h.safetensors',
        model_dir=path_clip_vision,
        file_name='clip_vision_vit_h.safetensors'
    )
    results += [os.path.join(path_clip_vision, 'clip_vision_vit_h.safetensors')]

    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_ip_negative.safetensors',
        model_dir=path_controlnet,
        file_name='fooocus_ip_negative.safetensors'
    )
    results += [os.path.join(path_controlnet, 'fooocus_ip_negative.safetensors')]

    if v == 'ip':
        load_file_from_url(
            url='https://huggingface.co/lllyasviel/misc/resolve/main/ip-adapter-plus_sdxl_vit-h.bin',
            model_dir=path_controlnet,
            file_name='ip-adapter-plus_sdxl_vit-h.bin'
        )
        results += [os.path.join(path_controlnet, 'ip-adapter-plus_sdxl_vit-h.bin')]

    if v == 'face':
        load_file_from_url(
            url='https://huggingface.co/lllyasviel/misc/resolve/main/ip-adapter-plus-face_sdxl_vit-h.bin',
            model_dir=path_controlnet,
            file_name='ip-adapter-plus-face_sdxl_vit-h.bin'
        )
        results += [os.path.join(path_controlnet, 'ip-adapter-plus-face_sdxl_vit-h.bin')]

    return results


def downloading_upscale_model():
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_upscaler_s409985e5.bin',
        model_dir=path_upscale_models,
        file_name='fooocus_upscaler_s409985e5.bin'
    )
    return os.path.join(path_upscale_models, 'fooocus_upscaler_s409985e5.bin')


update_all_model_names()
