import gradio as gr
from gradio import ChatMessage
from pathlib import Path
from PIL import Image
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.proc_pipe.gr_handlers import filter_cobble_data_by_date, filter_cobble_data_by_anomaly_id

from src.llms.gemini_wrapper import get_gemini_analysis_response
from tmp_app.jin_shell_demo_prompt import JIN_SHELL_DEMO_PROMPT

global ct_anom_selected_df
global ct_anom_id_list 
ct_anom_id_list = []

global tag_img1
img_path1 = Path(__file__).parent.parent / "src" / "data" / "jin_fm_grp_plots" / "fm_ana_1.png"
img_path2 = Path(__file__).parent.parent / "src" / "data" / "jin_fm_grp_plots" / "fm_ana_2.png"
img_path3 = Path(__file__).parent.parent / "src" / "data" / "jin_fm_grp_plots" / "fm_comp_3.png"
#img_path1 = Path(__file__).parent.parent / "src" / "data" / "jin_init_plots" / "anom_90_plot_one.jpg"
print(img_path1)
tag_img1 = Image.open(img_path1)

global gemini_session_type
gemini_session_type = "New Session"

# context dictrionary
global current_failure_event_dict

def calc_return_list (srch_res_df):
    global ct_anom_id_list
# given the return df from search, calculate button lables to display in the sidebar
    num_rows = srch_res_df.shape[0]
    if num_rows > 5:
        num_rows = 5
    btn_list = []
    for i in range(num_rows):
        row = srch_res_df.iloc[i]
        ct_anom_id_list.append(row['anomaly_event_id'])
        btn_label = f"{row['anomaly_event_id']} - {row['anomaly_start_time']}"
        btn_list.append(btn_label)
    return btn_list

def get_images_from_file (anom_event_id):
    fn_one = f"anom_{anom_event_id}_plot_one.jpg"
    fn_two = f"anom_{anom_event_id}_plot_two.jpg"
    #check if the files exist
    img_path = Path(__file__).parent.parent / "src" / "data" / "jin_init_plots"
    img_path_one = img_path / fn_one
    img_path_two = img_path / fn_two

    if img_path_one.exists():
        img_one = Image.open(img_path_one)
    else:
        img_one = None
    if img_path_two.exists():
        img_two = Image.open(img_path_two)
    else:
        img_two = None
    return img_one, img_two

def handle_search_query (srch_choice, start_date, end_date, search_by_failure_mode, search_by_component, search_by_sub_component, search_anomaly_id):
    
    global ct_anom_selected_df
    global current_failure_event_dict
    if srch_choice == "Date":
        ret_df = filter_cobble_data_by_date(start_date, end_date)
    elif srch_choice == "Anomaly ID":
        ret_df = filter_cobble_data_by_anomaly_id(search_anomaly_id)
    #selected_columns = ['anomaly_event_id','anomaly_date', 'anomaly_start_time', 'anomaly_end_time', 'summary', 'cause', 'component', 'sub_component', 'failure_mode']
    
    ct_anom_selected_df = ret_df

    # send top 5 results. (5 buttons + top data)
    b1_label, b2_label, b3_label, b4_label, b5_label = None, None, None, None, None
    lab_list = calc_return_list(ret_df)
    for i in range(len(lab_list)):
        if i == 0:
            b0_label = gr.Button(value=lab_list[i], variant="primary", visible=True)
        elif i == 1:
            b1_label = gr.Button(value=lab_list[i], visible=True)
        elif i == 2:
            b2_label = gr.Button(value=lab_list[i], visible=True)
        elif i == 3:
            b3_label = gr.Button(value=lab_list[i], visible=True)
        elif i == 4:
            b4_label = gr.Button(value=lab_list[i], visible=True)
    # hide search bar, show sidebar
    hide_srch_bar = gr.Accordion(open=False)
    show_sidebar = gr.Sidebar(open=True)

    # get the first row of the df
    sel_row = ret_df.iloc[0]
    current_failure_event_dict = sel_row.to_dict()
    anom_event_id = sel_row['anomaly_event_id']
    # select images file.
    ret_img_one, ret_img_two = get_images_from_file(anom_event_id)
    

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

    ret_img_one, ret_img_two = get_images_from_file(anom_event_id)

    return hide_srch_bar, show_sidebar, b0_label, b1_label, b2_label, b3_label, b4_label, ret_start_time, ret_end_time, delay_data, ret_equip, ret_summary, ret_cause, ret_reasoning, ret_recommendation, ret_tags_one, ret_tags_one_rationale, ret_img_one, ret_img_two
    




def get_selected_btn_data (btn_name):
    global ct_anom_selected_df
    global ct_anom_id_list
    global current_failure_event_dict
    
    anom_id = int(btn_name.split("-")[0].strip())
    btn_index = ct_anom_id_list.index(anom_id)
    
    sel_row = ct_anom_selected_df.iloc[btn_index]
    current_failure_event_dict = sel_row.to_dict()
    anom_event_id = sel_row['anomaly_event_id']
    # select images file.
    ret_img_one, ret_img_two = get_images_from_file(anom_event_id)
    # reset all btns
    b0_label = gr.Button(variant="secondary")
    b1_label = gr.Button(variant="secondary") 
    b2_label = gr.Button(variant="secondary")
    b3_label = gr.Button(variant="secondary")
    b4_label = gr.Button(variant="secondary") 
    if btn_index == 0:
        b0_label = gr.Button(variant="primary")
    elif btn_index == 1:
        b1_label = gr.Button(variant="primary")
    elif btn_index == 2:
        b2_label = gr.Button(variant="primary")
    elif btn_index == 3:
        b3_label = gr.Button(variant="primary")
    elif btn_index == 4:
        b4_label = gr.Button(variant="primary")

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
    
    
    
    return b0_label, b1_label, b2_label, b3_label, b4_label, ret_start_time, ret_end_time, delay_data, ret_equip, ret_summary, ret_cause, ret_reasoning, ret_recommendation, ret_tags_one, ret_tags_one_rationale, ret_img_one, ret_img_two, ret_fm, ret_component, ret_sub_component
    
    #return ret_start_time, ret_end_time, delay_data, capa_data, ret_equip, ret_summary, ret_fm, ret_component, ret_sub_component, ret_cause, ret_reasoning, ret_recommendation, ret_tags_one, ret_tags_one_rationale, ret_tags_two, ret_tags_two_rationale, ret_img_one, ret_img_two

def get_gemini_analysis_handler (query_text, history):
    global gemini_session_type
    global current_failure_event_dict
    
    if gemini_session_type == "New Session":
        gemini_session_type = "Old"
        req_prompt = JIN_SHELL_DEMO_PROMPT.replace("xxx_failure_events_notes_xxx", str(current_failure_event_dict))
        req_prompt = req_prompt + "\n\n <USER_QUERY>" + query_text + "</USER_QUERY>"
        goog_response = get_gemini_analysis_response(req_prompt, "New Session")
        #print (goog_response)
        #print ("New session and flipped")
    else:
        nxt_prompt = "<USER_QUERY>" + query_text + "</USER_QUERY>"
        goog_response = get_gemini_analysis_response(nxt_prompt, "old")
        #print ("Old session")
    #print (history)
    usr_qry = ChatMessage(role="user", content=query_text)
    response = ChatMessage(role="assistant", content=goog_response)
    history.append(usr_qry)
    history.append(response)
    return history, None
    

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Accordion("Search : By Anomaly Date, Anomaly ID, or Failure Mode") as srch_bar:
            with gr.Row():
                    srch_choice = gr.Radio(label="Search by", choices=["Date", "Anomaly ID", "Failure Mode", "Component", "Sub-Component"], value="Date", interactive=True)
            with gr.Row():           
                with gr.Column(scale=8):
                    with gr.Row():
                        start_date = gr.DateTime(label="Start Date", value="2024-03-01", include_time = False, type="string")
                        end_date = gr.DateTime(label="End Date", value="2024-03-31", include_time = False, type="string")
                        search_anomaly_id = gr.Textbox(label="Anomaly ID (88-165)", value="88")
                    with gr.Row():
                        search_by_failure_mode = gr.Dropdown(
                            choices = [
                                        "Drive System Failure",
                                        "Incorrect Positioning / Gap Insufficiency",
                                        "High-Pressure Braking Failure",
                                        "Incorrect Positioning / Gap Insufficiency High-Pressure Braking Failure",
                                        "Drive System Failure Roll Closing Failure",
                                        "Incorrect Positioning / Gap Insufficiency Drive System Failure",
                                        "Roll Closing Failure Drive System Failure",
                                        "Roll Closing Failure",
                                        "High-Pressure Braking Failure Roll Closing Failure",
                                        "Roll Closing Failure High-Pressure Braking Failure",
                                        "Pinch Roller Physical Damage",
                                        "Lubrication System Failure",
                                        "Drive System Failure Bearing failure",
                                        "Drive System Failure / Roll Closing Failure",
                                        "Rotational Mechanism Jam Drive System Failure",
                                        "High-Pressure Braking Failure Pinch Roller Physical Damage",
                                        "Guide Roller Misalignment",
                                        "Rotational Mechanism Jam",
                                        "High-Pressure Braking Failure, Roll Closing Failure, Incorrect Positioning / Gap Insufficiency",
                                        "Rotational Mechanism Jam High-Pressure Braking Failure",
                                        "Rotational Mechanism Jam Roll Closing Failure"
                                        "Drive System Failure Guide Roller Misalignment"
                                        ],
                            value="Drive System Failure",
                            label="Failure Mode", interactive=True)
                        search_by_component = gr.Textbox(label="Component", value="Twin Channel")
                        search_by_sub_component = gr.Textbox(label="Sub-Component", value="Brake Disc")
                        search_button = gr.Button("Search")
    with gr.Row():
        with gr.Sidebar(open=False) as side_bar_btns:
            b_0 = gr.Button(value=123)
            b_1 = gr.Button(value=None, visible=False)
            b_2 = gr.Button(value=None, visible=False)
            b_3 = gr.Button(value=None, visible=False)
            b_4 = gr.Button(value=None, visible=False)
            b_5 = gr.Button(value=None, visible=False)
            b_6 = gr.Button(value=None, visible=False)
            b_7 = gr.Button(value=None, visible=False)
            b_8 = gr.Button(value=None, visible=False)
            b_9 = gr.Button(value=None, visible=False)
    
            
        with gr.Column(scale=2):
            with gr.Tabs():
                with gr.TabItem("Details"):
                    with gr.Column():
                        with gr.Row():
                            mnt_start_time = gr.Textbox(label="Anomaly Start Time", value="2024-03-01 10:00:00")
                            mnt_end_time = gr.Textbox(label="Anomaly End Time", value="2024-03-01 10:20:00")
                        delay_data = gr.TextArea (label="Maintenance Data", value="Delay Data Summary", lines=3, interactive=True)
                        ana_tags_list = gr.TextArea(label="Tags of Interest", value="Tag1, Tag2, Tag3", lines=3,  interactive=True)
                    
                        ana_tags_rationale = gr.TextArea(label="Tags Rationale", value="Tag1, Tag2, Tag3", lines=5, interactive=True)
                        gr.Markdown(f'### Additional Information')
                        ana_equip = gr.TextArea(label="Equipment", value="Cause", lines=3, interactive=True)
                        ana_summary = gr.TextArea(label="Summary", value="Cause", lines=3, interactive=True)
                        ana_cause = gr.TextArea(label="Cause", value="Cause", lines=3, interactive=True)
                    
                        ana_reason = gr.TextArea(label="Reasoning", value="Analysis Reasoning", lines=3, interactive=True)
                    
                        ana_recommendations = gr.TextArea(label="Recommendations", value="Recommendations", lines=3, interactive=True) 
                    
                        
                
                with gr.TabItem("Tags"):
                    tag_img1 = gr.Image(label="Tag 1")
                    tag_img2 = gr.Image(label="Tag 2")
                    
                with gr.TabItem("FMEA Alignment"):
                    x_fm = gr.Textbox(label="Failure Mode", value="Failure Mode")
                    x_f_comp = gr.Textbox(label="Component", value="Component")
                    x_f_sub_comp = gr.Textbox(label="Sub-Component", value="Sub-Component")
                    gr.Markdown(f'### Number of Actual Failures by Failure Modes')
                    
                    x_tag_img1 = gr.Image(label="Failure Modes", type="filepath", value=img_path1)
                    x_tag_img2 = gr.Image(label="Failure Modes", type="filepath", value=img_path2)
                    x_tag_img3 = gr.Image(label="Components Failure", type="filepath", value=img_path3)
                    t13 = gr.Textbox(label=None, container=False, value="Hello from tag signature")
                
                # event handlers
                search_button.click(handle_search_query, inputs=[srch_choice, start_date, end_date, search_by_failure_mode, 
                                                         search_by_component, search_by_sub_component, search_anomaly_id], 
                                                         outputs=[srch_bar, side_bar_btns, b_0, b_1, b_2, b_3, b_4, mnt_start_time, 
                                                                  mnt_end_time, delay_data, ana_equip, ana_summary, ana_cause, ana_reason, 
                                                                  ana_recommendations, ana_tags_list, ana_tags_rationale, tag_img1, tag_img2])
                b_0.click(get_selected_btn_data, inputs=[b_0], outputs=[b_0, b_1, b_2, b_3, b_4, mnt_start_time, mnt_end_time, delay_data, 
                                                                        ana_equip, ana_summary, ana_cause, 
                                                                        ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale, tag_img1, tag_img2,
                                                                        x_fm, x_f_comp, x_f_sub_comp])
                b_1.click(get_selected_btn_data, inputs=[b_1], outputs=[b_0, b_1, b_2, b_3, b_4, mnt_start_time, mnt_end_time, delay_data, 
                                                                        ana_equip, ana_summary, ana_cause, 
                                                                        ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale, tag_img1, tag_img2,
                                                                        x_fm, x_f_comp, x_f_sub_comp])
                b_2.click(get_selected_btn_data, inputs=[b_2], outputs=[b_0, b_1, b_2, b_3, b_4, mnt_start_time, mnt_end_time, delay_data, 
                                                                        ana_equip, ana_summary, ana_cause, 
                                                                        ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale, tag_img1, tag_img2,
                                                                        x_fm, x_f_comp, x_f_sub_comp])
                b_3.click(get_selected_btn_data, inputs=[b_3], outputs=[b_0, b_1, b_2, b_3, b_4, mnt_start_time, mnt_end_time, delay_data, 
                                                                        ana_equip, ana_summary, ana_cause, 
                                                                        ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale, tag_img1, tag_img2,
                                                                        x_fm, x_f_comp, x_f_sub_comp])
                b_4.click(get_selected_btn_data, inputs=[b_4], outputs=[b_0, b_1, b_2, b_3, b_4, mnt_start_time, mnt_end_time, delay_data, 
                                                                        ana_equip, ana_summary, ana_cause, 
                                                                        ana_reason, ana_recommendations, ana_tags_list, ana_tags_rationale, tag_img1, tag_img2,
                                                                        x_fm, x_f_comp, x_f_sub_comp])
                    
            
        with gr.Column(scale=2):
            cb1 = gr.Chatbot(label="Reliability Agent", type="messages")
            cb2_query = gr.Textbox(show_label=False, placeholder="Type your message here...", submit_btn="Send")
            cb2_query.submit(get_gemini_analysis_handler, inputs=[cb2_query, cb1], outputs=[cb1, cb2_query])
            

    demo.load()






if __name__ == "__main__":
    demo.launch()