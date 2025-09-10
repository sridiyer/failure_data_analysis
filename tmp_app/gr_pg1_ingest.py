import gradio as gr






with gr.Blocks() as demo:
    """
    with gr.Sidebar():
        t1 = gr.Textbox(label=None, value="Hello from Page 1")
        t2 = gr.Textbox(label=None, value="Hello from Page 2")
        t3 = gr.Textbox(label=None, value="Hello from Page 3")
        t4 = gr.Textbox(label=None, value="Hello from Page 4")
        t5 = gr.Textbox(label=None, value="Hello from Page 5")
        t6 = gr.Textbox(label=None, value="Hello from Page 6")
    """   
    demo.load()
    gr.Markdown('### ML Model Training Assistant')
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Maintenance Data")
            maint_data_files = gr.Files(label="Upload Maintenance Data", file_types=[".csv", ".json", ".txt"], file_count="multiple")
            maint_upload_button = gr.UploadButton(
                "Upload Maintenance Data",
                file_types=[".csv", ".json", ".txt"], # optional: restrict file types
                file_count="multiple" # or "single"
            )
        
            # show a hidden dataframe with the data.
            gr.Markdown("### Connect Historical Time Series Data")
            con_type = gr.Dropdown(
                label="Select Connection Type",
                choices=["CSV", "JSON", "TXT"],
                value="CSV"
            )
            con_details_str = gr.Textbox(label="Connection Details", value="")
            con_test_button = gr.Button("Test Connection")
            gr.Markdown("### Describe Target Anomalies")
            anom_desc = gr.Textbox(label="What type of anomalies or failure patterns are you looking for?", value="", lines=4)

            gr.Markdown("### Configuration Summary")
            sum_main_data = gr.Textbox(label="Maintenance Data Files", value="0 uploaded")
            sum_time_series = gr.Textbox(label="Time Series Connection", value="Not connected")
            sum_build_button = gr.Button("Setup ML Agent")
            



if __name__ == "__main__":
    demo.launch()