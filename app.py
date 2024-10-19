import json
import gradio as gr
from gradio import ChatMessage
from typing import List

from react_graph.graph import build_react_graph


agent = build_react_graph()

css = """
#chatbot-container {
    width: 800px;
    height: 1000px;
}
"""

MAP_MODE = 'place'
MAPS_API_KEY = ""


def get_current_map(name):
    return f"""
                <iframe
                width="800"
                height="500"
                frameborder="0" style="border:1"
                referrerpolicy="no-referrer-when-downgrade"
                src="https://www.google.com/maps/embed/v1/{MAP_MODE}?key={MAPS_API_KEY}&q={name}&zoom=18"
                allowfullscreen>
                </iframe>
                """


def get_texts():
    return ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]


def extract_answer_from_graph(raw):
    return raw["agent_outcome"].return_values["output"]


async def interact(prompt, messages):
    messages.append(ChatMessage(role="user", content=prompt))
    yield messages, [], ""
    raw_response = agent.invoke({"input": prompt, "chat_history": messages})
    response = extract_answer_from_graph(raw_response)
    messages.append(ChatMessage(role="assistant", content=response))
    image_urls = raw_response.get("images")
    map_iframe = get_current_map(raw_response["description"].name)
    yield messages, gr.update(value=image_urls), gr.update(value=map_iframe)


with gr.Blocks(theme=gr.themes.Ocean(), css=css) as demo:

    gr.Markdown("# Goodplace AI")
    with gr.Row():
        with gr.Column(elem_id="chatbot-container"):
            images_list = gr.State([])
            chatbot = gr.Chatbot(type="messages", label="Agent", height=600)
            input = gr.Textbox(lines=1, label="Chat Message")
            submit_btn = gr.Button("Submit")
        with gr.Column():
            map_ = gr.HTML(
                """
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2440.579030749294!2d20.93485257725637!3d52.28734415342801!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x471eca2e69d7ff4f%3A0xa2c95dbb65cc48c!2sWergiliusza%2015%2C%2001-915%20Warszawa!5e0!3m2!1sen!2spl!4v1729110028936!5m2!1sen!2spl"
                    width="800"
                    height="500"
                    style="border:1;"
                    allowfullscreen=""
                    loading="lazy"
                ></iframe>
                """
            )
            gallery = gr.Gallery(
                [], label="Photo Roll", columns=3, height="200px", interactive=False
            )

            text_list = gr.Textbox(
                label="Relevant Comments:",
                value="\n".join(get_texts()),
                lines=5,  # Number of lines in the textbox
                interactive=False,  # Disable editing
            )

    input.submit(interact, inputs=[input, chatbot], outputs=[chatbot, gallery, map_])
    submit_btn.click(fn=interact, inputs=[input, chatbot], outputs=[chatbot, gallery, map_])


if __name__ == "__main__":
    demo.launch(share=True)
