import gradio as gr
import pandas as pd
import json


test_data = {
    "date_time" : ["2024-03-01 10:00:00", "2024-03-01 14:30:00", "2024-03-01 18:00:00"],
    "event" : ["Cobble 1", "Cobble 2", "Cobble 3"],
    "event_description" : ["Cobble 1 description", "Cobble 2 description", "Cobble 3 description"],
}
test_data_df = pd.DataFrame(test_data)


def display_maintenance_fmea_corr_tab():
    pass

def tab_search_results():
    with gr.Tab("Search Results"):
        gr.Markdown("Search Results")
        test1 = gr.DataFrame(test_data_df)
       

def tab_analysis ():
    with gr.Tab("Analysis"):
        gr.Markdown("Analysis")
        with gr.Row():
            b_cause = gr.Textbox(label="Failure Mode", value="FM")
            c_cause = gr.Textbox(label="Component", value="Component")
            a_cause = gr.Textbox(label="Cause", value="Cause")
        with gr.Row():
            ana_summary = gr.TextArea(label="Analysis Summary", value="Analysis Summary")
        with gr.Row():
            ana_tags_list = gr.Textbox(label="Additional Tags", value="Tag1, Tag2, Tag3")
        with gr.Row():
            ana_tags_rationale = gr.TextArea(label="Ration ale for Additional Tags", value="Tag1, Tag2, Tag3")
            
def additional_analysis ():
    with gr.Tab("Additional Analysis"):
        gr.Markdown("Additional Analysis")
        with gr.Row():
            add_ana_graph = gr.Image()
        with gr.Row():
            add_ana_summary = gr.TextArea(label="Additional Analysis Summary", value="Additional Analysis Summary")
        with gr.Row():
            add_ana_tags_list = gr.Textbox(label="Additional Tags", value="Tag1, Tag2, Tag3")
        with gr.Row():
            gr.Button("Add Additional Analysis")

def analyze_alerts_tab ():
    with gr.Tab("Analyze Alerts"):
        gr.Markdown("""Analyze Alerts : Enter an Alert ID from Spector Platform and
                    brain storm with the diagnostic agent.""")
        with gr.Row():
            alert_id = gr.Textbox(label="Alert ID", value=1163)
            analyze_alert_button = gr.Button("Analyze Alert")
        with gr.Row():
            alert_summary = gr.TextArea(label="Alert Summary", value="Alert Summary")

def tab_maintenance_data ():
    with gr.Tab("Maintenance Data"):
        gr.Markdown("Maintenance Data")
        with gr.Row():
            delay_data = gr.TextArea (label="Delay Data", value="Delay Data Summary")
            capa_data = gr.TextArea (label="Capa Data", value="Capa Data Summary")

def tab_maintenance_fmea ():
    with gr.Tab("FMEA"):
        gr.Markdown("FMEA")
        with gr.Row():
            fm_df = gr.DataFrame()

def top_search_bar ():
    with gr.Row():
            start_date = gr.DateTime(label="Start Date", value="2024-03-01", include_time = False)
            end_date = gr.DateTime(label="End Date", value="2024-03-31", include_time = False )
            search_button = gr.Button("Search")
    with gr.Row():
            search_results = gr.Textbox(label="Search Response Message", value="Multiple results found")


def bottom_feedback_bar ():
    with gr.Row():
        rev_text =gr.TextArea(label="SME Review and Feedback", placeholder="This is SME feedback")
    with gr.Row():
        rev_name = gr.Textbox(label="Don, Anand, Clay,...", value="SME Name")
        gr.Button ("Clear")
        gr.Button("Submit")

with gr.Blocks() as demo:
    top_search_bar()
    tab_search_results()
    tab_analysis()
    tab_maintenance_data()
    tab_maintenance_fmea()
    bottom_feedback_bar()

if __name__ == "__main__":
    demo.queue()
    demo.launch(server_name="0.0.0.0", server_port=8080)