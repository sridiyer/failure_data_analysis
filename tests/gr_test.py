import gradio as gr


def top_search_bar ():
    gr.Markdown("## Search Cobble Events")

    with gr.Accordion("Search Options"):
        with gr.Row():
            start_date = gr.DateTime(label="Start Date", value="2024-03-01", include_time = False, type="string")
            end_date = gr.DateTime(label="End Date", value="2024-03-31", include_time = False, type="string")
            earch_anomaly_id = gr.Textbox(label="Anomaly ID (88-165)", value="88")
            search_button = gr.Button("Search")

with gr.Blocks() as demo:
    top_search_bar()

if __name__ == "__main__":
    demo.launch()

