import gradio as gr
import random
import time
import shared
import argparse
import modules.path
import fooocus_version
import modules.html
import modules.async_worker as worker
import modules.flags as flags
import modules.gradio_hijack as grh
import comfy.model_management as model_management

from modules.sdxl_styles import style_keys, aspect_ratios, fooocus_expansion, default_styles


def generate_clicked(*args):
    execution_start_time = time.perf_counter()

    yield gr.update(visible=True, value=modules.html.make_progress_html(1, 'Initializing ...')), \
        gr.update(visible=True, value=None), \
        gr.update(visible=False)

    worker.buffer.append(list(args))
    finished = False

    while not finished:
        time.sleep(0.01)
        if len(worker.outputs) > 0:
            flag, product = worker.outputs.pop(0)
            if flag == 'preview':
                percentage, title, image = product
                yield gr.update(visible=True, value=modules.html.make_progress_html(percentage, title)), \
                    gr.update(visible=True, value=image) if image is not None else gr.update(), \
                    gr.update(visible=False)
            if flag == 'results':
                yield gr.update(visible=False), \
                    gr.update(visible=False), \
                    gr.update(visible=True, value=product)
                finished = True

    execution_time = time.perf_counter() - execution_start_time
    print(f'Total time: {execution_time:.2f} seconds')
    return


shared.gradio_root = gr.Blocks(title='Fooocus ' + fooocus_version.version, css=modules.html.css).queue()
with shared.gradio_root:
    with gr.Row():
        with gr.Column():
            progress_window = grh.Image(label='Preview', show_label=True, height=640, visible=False)
            progress_html = gr.HTML(value=modules.html.make_progress_html(32, 'Progress 32%'), visible=False, elem_id='progress-bar', elem_classes='progress-bar')
            gallery = gr.Gallery(label='Gallery', show_label=False, object_fit='contain', height=720, visible=True)
            with gr.Row(elem_classes='type_row'):
                with gr.Column(scale=0.85):
                    prompt = gr.Textbox(show_label=False, placeholder="Type prompt here.", container=False, autofocus=True, elem_classes='type_row', lines=1024)
                with gr.Column(scale=0.15, min_width=0):
                    run_button = gr.Button(label="Generate", value="Generate", elem_classes='type_row', visible=True)
                    stop_button = gr.Button(label="Stop", value="Stop", elem_classes='type_row', visible=False)

                    def stop_clicked():
                        model_management.interrupt_current_processing()
                        return gr.update(interactive=False)

                    stop_button.click(stop_clicked, outputs=stop_button, queue=False)
            with gr.Row(elem_classes='advanced_check_row'):
                input_image_checkbox = gr.Checkbox(label='Input Image', value=False, container=False, elem_classes='min_check')
                advanced_checkbox = gr.Checkbox(label='Advanced', value=False, container=False, elem_classes='min_check')
            with gr.Row(visible=False) as image_input_panel:
                with gr.Tabs():
                    with gr.TabItem(label='Upscale or Variation') as uov_tab:
                        with gr.Row():
                            with gr.Column():
                                uov_input_image = grh.Image(label='Drag above image to here', source='upload', type='numpy')
                            with gr.Column():
                                uov_method = gr.Radio(label='Upscale or Variation:', choices=flags.uov_list, value=flags.disabled)
                                gr.HTML('<a href="https://github.com/lllyasviel/Fooocus/discussions/390">\U0001F4D4 Document</a>')
                    with gr.TabItem(label='Inpaint or Outpaint (beta)') as inpaint_tab:
                        inpaint_input_image = grh.Image(label='Drag above image to here', source='upload', type='numpy', tool='sketch', height=500, brush_color="#FFFFFF")
                        gr.HTML('Outpaint Expansion (<a href="https://github.com/lllyasviel/Fooocus/discussions/414">\U0001F4D4 Document</a>):')
                        outpaint_selections = gr.CheckboxGroup(choices=['Left', 'Right', 'Top', 'Bottom'], value=[], label='Outpaint', show_label=False, container=False)
                        gr.HTML('* \"Inpaint or Outpaint\" is powered by the sampler \"DPMPP Fooocus Seamless 2M SDE Karras Inpaint Sampler\" (beta)')

            input_image_checkbox.change(lambda x: gr.update(visible=x), inputs=input_image_checkbox, outputs=image_input_panel, queue=False,
                                        _js="(x) => {if(x){setTimeout(() => window.scrollTo({ top: window.scrollY + 500, behavior: 'smooth' }), 50);}else{setTimeout(() => window.scrollTo({ top: 0, behavior: 'smooth' }), 50);} return x}")

            current_tab = gr.Textbox(value='uov', visible=False)

            default_image = None

            def update_default_image(x):
                global default_image
                if isinstance(x, dict):
                    default_image = x['image']
                else:
                    default_image = x
                return

            def clear_default_image():
                global default_image
                default_image = None
                return

            uov_input_image.upload(update_default_image, inputs=uov_input_image, queue=False)
            inpaint_input_image.upload(update_default_image, inputs=inpaint_input_image, queue=False)

            uov_input_image.clear(clear_default_image, queue=False)
            inpaint_input_image.clear(clear_default_image, queue=False)

            uov_tab.select(lambda: ['uov', default_image], outputs=[current_tab, uov_input_image], queue=False)
            inpaint_tab.select(lambda: ['inpaint', default_image], outputs=[current_tab, inpaint_input_image], queue=False)

        with gr.Column(scale=0.5, visible=False) as right_col:
            with gr.Tab(label='Setting'):
                performance_selection = gr.Radio(label='Performance', choices=['Speed', 'Quality'], value='Speed')
                aspect_ratios_selection = gr.Radio(label='Aspect Ratios', choices=list(aspect_ratios.keys()),
                                                  value='1152×896', info='width × height')
                image_number = gr.Slider(label='Image Number', minimum=1, maximum=32, step=1, value=2)
                negative_prompt = gr.Textbox(label='Negative Prompt', show_label=True, placeholder="Type prompt here.",
                                             info='Describing objects that you do not want to see.')
                seed_random = gr.Checkbox(label='Random', value=True)
                image_seed = gr.Number(label='Seed', value=0, precision=0, visible=False)

                def random_checked(r):
                    return gr.update(visible=not r)

                def refresh_seed(r, s):
                    if r:
                        return random.randint(1, 1024*1024*1024)
                    else:
                        return s

                seed_random.change(random_checked, inputs=[seed_random], outputs=[image_seed], queue=False)

            with gr.Tab(label='Style'):
                style_selections = gr.CheckboxGroup(show_label=False, container=False,
                                                    choices=[fooocus_expansion] + style_keys,
                                                    value=[fooocus_expansion] + default_styles,
                                                    label='Image Style')
            with gr.Tab(label='Model'):
                with gr.Row():
                    base_model = gr.Dropdown(label='SDXL Base Model', choices=modules.path.model_filenames, value=modules.path.default_base_model_name, show_label=True)
                    refiner_model = gr.Dropdown(label='SDXL Refiner', choices=['None'] + modules.path.model_filenames, value=modules.path.default_refiner_model_name, show_label=True)
                with gr.Accordion(label='LoRAs', open=True):
                    lora_ctrls = []
                    for i in range(5):
                        with gr.Row():
                            lora_model = gr.Dropdown(label=f'SDXL LoRA {i+1}', choices=['None'] + modules.path.lora_filenames, value=modules.path.default_lora_name if i == 0 else 'None')
                            lora_weight = gr.Slider(label='Weight', minimum=-2, maximum=2, step=0.01, value=modules.path.default_lora_weight)
                            lora_ctrls += [lora_model, lora_weight]
                with gr.Row():
                    model_refresh = gr.Button(label='Refresh', value='\U0001f504 Refresh All Files', variant='secondary', elem_classes='refresh_button')
            with gr.Tab(label='Advanced'):
                sharpness = gr.Slider(label='Sampling Sharpness', minimum=0.0, maximum=30.0, step=0.001, value=2.0,
                                      info='Higher value means image and texture are sharper.')
                guidance_scale = gr.Slider(label='Guidance Scale', minimum=1.0, maximum=30.0, step=0.01, value=7.0,
                                      info='Higher value means style is cleaner, vivider, and more artistic.')

                gr.HTML('<a href="https://github.com/lllyasviel/Fooocus/discussions/117">\U0001F4D4 Document</a>')
                dev_mode = gr.Checkbox(label='Developer Debug Mode', value=False, container=False)

                with gr.Column(visible=False) as dev_tools:
                    with gr.Tab(label='Developer Control and Debug Tools'):
                        adm_scaler_positive = gr.Slider(label='Positive ADM Guidance Scaler', minimum=0.1, maximum=3.0,
                                                        step=0.001, value=1.5, info='The scaler multiplied to positive ADM (use 1.0 to disable). ')
                        adm_scaler_negative = gr.Slider(label='Negative ADM Guidance Scaler', minimum=0.1, maximum=3.0,
                                                        step=0.001, value=0.8, info='The scaler multiplied to negative ADM (use 1.0 to disable). ')
                        adm_scaler_end = gr.Slider(label='ADM Guidance End At Step', minimum=0.0, maximum=1.0,
                                                   step=0.001, value=0.3,
                                                   info='When to end the guidance from positive/negative ADM. ')
                        adaptive_cfg = gr.Slider(label='CFG Mimicking from TSNR', minimum=1.0, maximum=30.0, step=0.01, value=7.0,
                                                 info='Enabling Fooocus\'s implementation of CFG mimicking for TSNR '
                                                      '(effective when real CFG > mimicked CFG).')
                        sampler_name = gr.Dropdown(label='Sampler', choices=flags.sampler_list, value=flags.default_sampler, info='Only effective in non-inpaint mode.')
                        scheduler_name = gr.Dropdown(label='Scheduler', choices=flags.scheduler_list, value=flags.default_scheduler, info='Scheduler of Sampler.')

                        overwrite_step = gr.Slider(label='Forced Overwrite of Sampling Step',
                                                   minimum=-1, maximum=200, step=1, value=-1,
                                                   info='Set as -1 to disable. For developer debugging.')
                        overwrite_switch = gr.Slider(label='Forced Overwrite of Refiner Switch Step',
                                                     minimum=-1, maximum=200, step=1, value=-1,
                                                     info='Set as -1 to disable. For developer debugging.')
                        overwrite_width = gr.Slider(label='Forced Overwrite of Generating Width',
                                                    minimum=-1, maximum=2048, step=1, value=-1,
                                                    info='Set as -1 to disable. For developer debugging.')
                        overwrite_height = gr.Slider(label='Forced Overwrite of Generating Height',
                                                     minimum=-1, maximum=2048, step=1, value=-1,
                                                     info='Set as -1 to disable. For developer debugging.')
                        overwrite_vary_strength = gr.Slider(label='Forced Overwrite of Denoising Strength of "Vary"',
                                                            minimum=-1, maximum=1.0, step=0.001, value=-1,
                                                            info='Set as negative number to disable. For developer debugging.')
                        overwrite_upscale_strength = gr.Slider(label='Forced Overwrite of Denoising Strength of "Upscale"',
                                                               minimum=-1, maximum=1.0, step=0.001, value=-1,
                                                               info='Set as negative number to disable. For developer debugging.')

                        overwrite_ctrls = [overwrite_step, overwrite_switch, overwrite_width, overwrite_height, overwrite_vary_strength, overwrite_upscale_strength]

                def dev_mode_checked(r):
                    return gr.update(visible=r)


                dev_mode.change(dev_mode_checked, inputs=[dev_mode], outputs=[dev_tools], queue=False)

                def model_refresh_clicked():
                    modules.path.update_all_model_names()
                    results = []
                    results += [gr.update(choices=modules.path.model_filenames), gr.update(choices=['None'] + modules.path.model_filenames)]
                    for i in range(5):
                        results += [gr.update(choices=['None'] + modules.path.lora_filenames), gr.update()]
                    return results

                model_refresh.click(model_refresh_clicked, [], [base_model, refiner_model] + lora_ctrls, queue=False)

        advanced_checkbox.change(lambda x: gr.update(visible=x), advanced_checkbox, right_col, queue=False)
        ctrls = [
            prompt, negative_prompt, style_selections,
            performance_selection, aspect_ratios_selection, image_number, image_seed, sharpness, adm_scaler_positive, adm_scaler_negative, adm_scaler_end, guidance_scale, adaptive_cfg, sampler_name, scheduler_name
        ]
        ctrls += overwrite_ctrls
        ctrls += [base_model, refiner_model] + lora_ctrls
        ctrls += [input_image_checkbox, current_tab]
        ctrls += [uov_method, uov_input_image]
        ctrls += [outpaint_selections, inpaint_input_image]

        run_button.click(lambda: (gr.update(visible=True, interactive=True), gr.update(visible=False), []), outputs=[stop_button, run_button, gallery])\
            .then(fn=refresh_seed, inputs=[seed_random, image_seed], outputs=image_seed)\
            .then(fn=generate_clicked, inputs=ctrls, outputs=[progress_html, progress_window, gallery])\
            .then(lambda: (gr.update(visible=True), gr.update(visible=False)), outputs=[run_button, stop_button])


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=None, help="Set the listen port.")
parser.add_argument("--share", action='store_true', help="Set whether to share on Gradio.")
parser.add_argument("--listen", type=str, default=None, metavar="IP", nargs="?", const="0.0.0.0", help="Set the listen interface.")
args = parser.parse_args()
shared.gradio_root.launch(inbrowser=True, server_name=args.listen, server_port=args.port, share=args.share)
