import gradio as gr
import pandas as pd
import json

from sqlalchemy import create_engine, text

engine = create_engine('postgresql://bramhesh:Dev%400119%40%21%40@34.72.177.167:5432/experimental_si')

test_data = {
    "date_time" : ["2024-03-01 10:00:00", "2024-03-01 14:30:00", "2024-03-01 18:00:00"],
    "event" : ["Cobble 1", "Cobble 2", "Cobble 3"],
    "event_description" : ["Cobble 1 description", "Cobble 2 description", "Cobble 3 description"],
}
test_data_df = pd.DataFrame(test_data)

global anom_data_df
def get_data_from_db(cob_date_from, cob_date_to):
    global anom_data_df
    # '2024-01-02'
    cob_date_start = str(cob_date_from).strip()
    cob_date_end = str(cob_date_to).strip()
    print(cob_date_start, cob_date_end)
    query = text("""SELECT * FROM jindal_maintenance_data 
                 WHERE anomaly_date >= :anom_date_start AND anomaly_date <= :anom_date_end
                 AND source_type = 'BK_FILTERED' """ )
    anom_data_df = pd.read_sql_query(query, engine, params={'anom_date_start': cob_date_start, 'anom_date_end': cob_date_end})
    # list of dicts
   
    
    selected_columns = ['anomaly_event_id','anomaly_date', 'anomaly_start_time', 'anomaly_end_time', 'summary', 'cause', 'component', 'sub_component', 'failure_mode']
    ret_df = anom_data_df[selected_columns]
    return ret_df

# load tail_braker_fmea
# load twin_channel_fmea

# filter FMEA by causes and components


def get_selected_fmea_row (in_df, evt: gr.SelectData):
    global anom_data_df
    sel_row = anom_data_df.iloc[evt.index[0]]
    
    delay_data = sel_row['delay_summary']
    capa_data = sel_row['capa_summary']
    ret_date = sel_row['anomaly_date']
    ret_start_time = sel_row['anomaly_start_time']
    ret_end_time = sel_row['anomaly_end_time']
    ret_equip = sel_row['equipment_details']
    ret_summary = sel_row['summary']
    ret_cause = sel_row['cause']
    ret_component = sel_row['component']
    ret_sub_component = sel_row['sub_component']
    ret_fm = sel_row['failure_mode']
    ret_reasoning = sel_row['reason']
    ret_recommendation = sel_row['recommendation']
    ret_op_status = sel_row['equip_op_status']
    ret_tags_one = sel_row['tags_set_one']
    ret_tags_one_rationale = sel_row['tags_rationale_one']
    ret_tags_two = sel_row['tags_set_two']
    ret_tags_two_rationale = sel_row['tags_rationale_two']
    
    return delay_data, capa_data, ret_equip, ret_summary, ret_fm, ret_component, ret_sub_component, ret_cause, ret_reasoning, ret_recommendation, ret_tags_one, ret_tags_one_rationale

    
# ana_equipment, ana_summary, ana_fm, ana_comp, ana_sub_comp, 
# ana_cause, ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale    
    


       



            
def bottom_feedback_bar ():
    gr.Markdown("## SME Review and Feedback")
    with gr.Row():
        rev_text =gr.TextArea(label="SME Review and Feedback", placeholder="This is SME feedback", lines=3)
    with gr.Row():
        rev_name = gr.Textbox(label="SME Name", value="Don, Anand, Clay,...", scale=12)
        gr.Button ("Clear", scale = 4)
        gr.Button("Submit", scale = 4)
    

with gr.Blocks() as demo:
    
    with gr.Accordion("Search Options : By Date, Anomaly ID, Failure Mode, Component, Sub-Component"):
        with gr.Row():
            with gr.Column(scale=8):
                with gr.Row():
                    start_date = gr.DateTime(label="Start Date", value="2024-03-01", include_time = False, type="string")
                    end_date = gr.DateTime(label="End Date", value="2024-03-31", include_time = False, type="string")
                    search_anomaly_id = gr.Textbox(label="Anomaly ID (88-165)", value="88")
                with gr.Row():
                    search_by_failure_mode = gr.Textbox(label="Failure Mode", value="Drive Failure")
                    search_by_component = gr.Textbox(label="Component", value="Twin Channel")
                    search_by_sub_component = gr.Textbox(label="Sub-Component", value="Brake Disc")
            with gr.Column(scale=2):
                search_button = gr.Button("Search Maintenance Data")
                



    #TODO -a tab for COMPONENTS. (current, new - two PD dataframe + chatbot)

    gr.Markdown("## Search Resuls, Analysis, Data Mining, FMEA Refinement, and much more...")
    with gr.Tabs() as tabs:
        with gr.TabItem("Search Results", id=0):
            gr.Markdown("Search Results")
            sr_res_df = gr.DataFrame()
        search_button.click(get_data_from_db, inputs=[start_date, end_date], outputs=sr_res_df)
       

        with gr.TabItem("Maintenance Data", id=1):
            gr.Markdown("Maintenance Data")
            with gr.Row():
                mnt_start_time = gr.Textbox(label="Event Start Time", value="2024-03-01 10:00:00")
                mnt_end_time = gr.Textbox(label="Event End Time", value="2024-03-01 10:20:00")
            with gr.Row():
                delay_data = gr.TextArea (label="Delay Data", value="Delay Data Summary", lines=15)
                capa_data = gr.TextArea (label="Capa Data", value="Capa Data Summary", lines=15)

        with gr.TabItem("Analysis", id=2):
            gr.Markdown("Analysis")
            with gr.Row():
                ana_equipment = gr.TextArea(label="Equipment Details", value="Equipment")
                ana_summary = gr.TextArea(label="Analysis Summary", value="Analysis Summary")
            with gr.Row():
                ana_fm = gr.Textbox(label="Failure Mode", value="FM")
                ana_comp = gr.Textbox(label="Component", value="Component")
                ana_sub_comp = gr.Textbox(label="Sub-Component", value="Sub-Component")
            
            with gr.Row():
                ana_cause = gr.TextArea(label="Cause", value="Cause")
            with gr.Row():
                ana_reason = gr.TextArea(label="Reasoning", value="Analysis Reasoning")
            with gr.Row():
                ana_recommendations = gr.TextArea(label="Recommendations", value="Recommendations") 
            with gr.Row():
                ana_tags_list = gr.TextArea(label="Tags of Interest", value="Tag1, Tag2, Tag3")
            with gr.Row():
                ana_tags_rationale = gr.TextArea(label="Tags Rationale", value="Tag1, Tag2, Tag3")
            with gr.Row():
                ana_sec_tags_list = gr.TextArea(label="Secondary Tags of Interest", value="Tag1, Tag2, Tag3")
            with gr.Row():
                ana_sec_tags_rationale = gr.TextArea(label="Secondary Tags Rationale", value="Tag1, Tag2, Tag3")
        sr_res_df.select(get_selected_fmea_row, inputs=[sr_res_df], outputs=[delay_data, capa_data, ana_equipment, ana_summary, ana_fm, ana_comp, ana_sub_comp, ana_cause, ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale])

        with gr.TabItem("Data Mining", id=3):
            gr.Markdown("Mine the data for failure modes, associated sensor signatures, trendsand other insights.")
            with gr.Row():
                add_ana_graph = gr.Image()
            with gr.Row():
                add_ana_summary = gr.TextArea(label="Data Mining Analysis Summary", value="Additional Analysis Summary")
            with gr.Row():
                add_ana_tags_list = gr.Textbox(label="Additional Tags", value="Tag1, Tag2, Tag3")
            with gr.Row():
                add_ana_chat   = gr.Chatbot(type="messages")
                add_ana_textBox = gr.Textbox(label="Additional Analysis", value="Additional Analysis")
                add_ana_button = gr.Button("Add Additional Analysis")
        
        with gr.TabItem("FMEA Refinement", id=4):
            gr.Markdown("""Refine the FMEA based on actual failure data - re-evaluate criticality, risk, and other parameters.""")
            with gr.Row():
                fmea_df = gr.DataFrame()
            with gr.Row():
                fmea_text_area = gr.Textbox(label="Edits to FMEA", value = "old data \n new data", lines = 3)
            with gr.Row():
                fmea_micro_chat = gr.Chatbot(type="messages")
            with gr.Row():
                fmea_ma_textBox = gr.Textbox(label="FMEA Micro-Agent", value="FMEA Micro-Agent")

        with gr.TabItem("Analyze Alerts", id=5):
            gr.Markdown("""Analyze Alerts : Enter an Alert ID from Spector Platform and
                    brain storm with the diagnostic agent. Hei, bring your alerts data from Aveva, C3 and GE. We will fix those!
                        Here is the perfect antidote to your alerts fatigue!""")
            with gr.Row():
                alert_id = gr.Textbox(label="Alert ID", value=1163)
                analyze_alert_button = gr.Button("Analyze Alert")
            #TODO - add primary contributors, factors, etc.
            with gr.Row():
                alert_summary = gr.TextArea(label="Alert Summary", value="Alert Summary")
            with gr.Row():
                alert_chat = gr.Chatbot(type="messages")
        
        with gr.TabItem("General QnA", id=6):
            gr.Markdown("General QnA about the ROlling Mill Facility")
            with gr.Row():
                gen_info_chat = gr.Chatbot(type="messages")
        
        with gr.TabItem("HELP", id=7):
            gr.Markdown("## Helpful Information")
            gr.Markdown("""
                        78 cobble events occurred in the Tail Braker / Twin Channel zone during the year 2024. 
                        <br> <b> Review Background Maintenance Data </b>
                        <br>Search by date range or anomaly ID (not both). Anomaly ids are beteen 88 and 165. (both inclusive).
                        <br>Search by date range may bring up multiple results. Click on the row of interest (one row) to see the details.
                        <br>Once you select a row, you can see data from Delay and CAPA files under the Maintenance Data tab.
                        <br> <b>Analysis and Data Mining</b>
                        <br>Initial (automated) analysis of the cobble events is availableunder the Analysis tab.
                        <br>You can also carry out additional analysis under the Data Mining tab.
                        <br>You can also refine the FMEA under the FMEA Refinement tab. Try to match the events in the maintenance data to parameters in the FMEA.
                        <br>You can also analyze alerts (displayed on Spector Platform) under the Analyze Alerts tab. You need to copy the alert ID from Spector Platform.
                        <br>You can also get general information about the Rolling Mill Facility under the General QnA tab.
                        """)

    
    bottom_feedback_bar()

if __name__ == "__main__":
    demo.queue()
    demo.launch(server_name="0.0.0.0", server_port=8080)