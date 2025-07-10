import gradio as gr 
from PIL import Image
import pandas as pd

import plotly.express as px

"""
theme = gr.themes.Soft(
    #primary_hue="amber",
    primary_hue="lime",
    text_size="lg",
)
"""
theme = gr.themes.Monochrome(
    primary_hue="lime",
    text_size="lg",
)

## DATA
comp_data = {
        'system': ['Compressor', 'Compressor','Dry Gas Seal', 'Lubrication', 'Cooling', 'Cooling'],
        'component': ['Impeller', 'Rotor', 'Valve', 'Oil Pump', 'Water Filter', 'Radiator'],
        'value': [3, 2, 1, 4, 5, 6]
    }
comp_data_df = pd.DataFrame(comp_data)

img_net = Image.open("/Users/sridhariyer/spector/sp_dev/failure_data_analysis/tests/gr_imgs/img_network.png")
img_pid = Image.open("/Users/sridhariyer/spector/sp_dev/failure_data_analysis/tests/gr_imgs/cent_pid.png")

def test_spider_chart_hl():
    df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3, 4],
    theta=['General Knowledge & Reference','Standards','Troubleshooting & Diagnostics',
           'Case Studies', 'Performance', 'Tutorial Papers']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    return fig

ext_text = """
The primary operational zones of the mill are:

- **1. Re-Heating Furnace Exit Area:** This zone receives hot billets from the furnace, removes surface scale with a high-pressure water descaler, and transfers them onto the main rolling line.
- **2. Roughing Mill Area:** Performs the initial, heavy rolling of the billet using robust SHS-type stands to achieve a significant reduction in the bar's cross-sectional area.
- **3. Finishing Mill:** Conducts subsequent rolling passes to further refine the bar's shape and achieve tighter dimensional tolerances, utilizing interstand loopers to control tension.
- **4. High Speed Bar & Small Rounds Lines:** These parallel production paths contain specialized Fast Finishing Blocks (FFB) and shears designed for the high-speed production and cutting of smaller diameter bars and wire rod.
- **5. Big Rounds Line:** A separate, dedicated path for larger diameter products that bypass the FFB and are cut to length by a heavy-duty dividing shear.
- **6. Twin Channel and Cooling Bed:** The final handling area that receives the cut-to-length bars from all production lines, brakes their momentum, and discharges them onto a large cooling bed.
"""

img_text = """
The image shows the PID for the 1st Stage Compressor. The safety margins are specified.
"""

res_text = """
Research Agent searching the web for additional information regarding troubleshooting of cobble events due to mechanical issues 
in the Twin Channel and  Tail Braker Areas.
"""

with gr.Blocks(theme=theme) as demo:

    with gr.Tab("Spector Customer Onboarding"):
        with gr.TabItem("Plant Information"):
            with gr.Accordion("Info Display (only for testing / demo) - in prod, what gets displayed will be driven by the Doc Agent"):
                with gr.Row():
                    sel_display = gr.Radio(label="Display Demo", choices=["Dashboard", "Text", "Image", "Spreadsheet", "Plot", "Research"], value="Dashboard")
            
            # demo accordion
            with gr.Row():
                with gr.Column():
                    """"
                    gr.Image(label="Plant Dashobard")
                    gr.File(label="upload additional information")
                    """
                    # return n0t needed
                    @gr.render(inputs=sel_display)
                    def render_display(sel_display):
                        if sel_display == "Dashboard":
                            gr.Plot(value=test_spider_chart_hl(), label="Plant Documents")
                            gr.Image(label="Upload Additional Information")
                        elif sel_display == "Text":
                            gr.Markdown(ext_text)
                        elif sel_display == "Image":
                            gr.Image(label="Plant Image", value=img_pid)
                            gr.TextArea(label="Image Summary", value=img_text, lines=10)
                        elif sel_display == "Spreadsheet":
                            gr.Dataframe(label="Plant Equipment", value=comp_data_df)
                        elif sel_display == "Plot":
                            gr.Image(label="Plant Equipment", value=img_net)
                            gr.Dataframe(label="Components", value=comp_data_df)
                        else:
                            gr.TextArea(label="Research Results", value=res_text, lines=10)
                with gr.Column():
                    doc_chat = gr.Chatbot(label="Doc Agent", type="messages")
                    doc_input = gr.MultimodalTextbox( sources=["upload", "microphone"], placeholder="Ask me anything about the document", show_label=False,  interactive=True )
        with gr.TabItem("Maintenance Information"):
            gr.Textbox(label="Maintenance Information")

        with gr.TabItem("Timeseries Data"):
            gr.Textbox(label="Timeseries Data")


demo.queue()
demo.launch(server_name="0.0.0.0", server_port=8080)