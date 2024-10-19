import gradio as gr
from coords import get_location_from_ip

MAPS_API_KEY = "AIzaSyDzYxuvmi6YSfr0VyzkZrIg9DbHGGN7axE"
PARAMETERS = "q=Galeria Polnocna"
MAP_MODE = "place"
lat, longt = get_location_from_ip()

with gr.Blocks(theme=gr.themes.Ocean()) as demo:

    gr.Markdown("# Goodplace AI")
    with gr.Row():
        with gr.Column():
            map = gr.HTML(
                f"""
                <iframe
                width="800"
                height="800"
                frameborder="0" style="border:0"
                referrerpolicy="no-referrer-when-downgrade"
                src="https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAPS_API_KEY}&{PARAMETERS}&zoom=18"
                allowfullscreen>
                </iframe>
                """
            )

demo.launch(share=False)
