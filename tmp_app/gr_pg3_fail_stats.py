import gradio as gr
from pathlib import Path
from gradio import ChatMessage
import os
import sys
import pandas as pd
import pickle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.proc_pipe.gr_handlers import filter_cobble_data_by_date, filter_cobble_data_by_anomaly_id
from tmp_app.jin_shell_demo_prompt import JIN_SHELL_GROUP_PROMPT
from src.llms.gemini_wrapper import get_gemini_analysis_response


global g1_sub_grps_list, g2_sub_grps_list, g3_sub_grps_list
g1_sub_grps_list = ['Over-Torque', 'Loss of Torque',  'TC Discharge']
g2_sub_grps_list = ['Pneumatic Failure', 'Upstream Failure', 'Drive Coupling']
g3_sub_grps_list = ['Position Control Error', 'Mechanical Obstruction', 'Fatigue / Wear-out']


# 3 group summary, 3 group-sub-groups

# data path
data_path = Path(__file__).parent.parent / "src" / "data" / "jin_fm_grp_data/"
global g1_summary, g2_summary, g3_summary
#g1_summary = gr.Markdown(Path(data_path / "0_sum.txt").read_text())
g1_summary = Path(data_path / "0_sum.txt").read_text()    
g2_summary = Path(data_path / "1_sum.txt").read_text()
g3_summary = Path(data_path / "2_sum.txt").read_text()

global gemini_session_type
gemini_session_type = "New Session"

global current_fail_group_data
current_fail_group_data = g1_summary

global g1_sub_data_df, g2_sub_data_df, g3_sub_data_df
g1_sub_data_df = pd.read_pickle(data_path / "drive_sys_subgroups.pkl")
g2_sub_data_df = pd.read_pickle(data_path / "high_pressure_subgroups.pkl")
g3_sub_data_df = pd.read_pickle(data_path / "position_gap_subgroups.pkl")

def get_selected_group_data (btn_name):
    global ct_anom_selected_df
    global ct_anom_id_list
    global current_fail_group_data
    global g1_summary, g2_summary, g3_summary

    
    btn_index = int(btn_name.split("_")[1].strip())
    
    
    sel_row = ct_anom_selected_df.iloc[btn_index]
    anom_event_id = sel_row['anomaly_event_id']
    # select images file.
    #ret_img_one, ret_img_two = get_images_from_file(anom_event_id)
    # reset all btns
    b0_label = gr.Button(variant="secondary")
    b1_label = gr.Button(variant="secondary") 
    b2_label = gr.Button(variant="secondary")


    
    # need to set sub-group buttons also.
    if btn_index == 0:
        b0_label = gr.Button(variant="primary")
        current_fail_group_data = g1_summary
        #set subgroup buttons
    elif btn_index == 1:
        b1_label = gr.Button(variant="primary")
        current_fail_group_data = g2_summary
    elif btn_index == 2:
        b2_label = gr.Button(variant="primary")
        current_fail_group_data = g3_summary
   

    return b0_label, b1_label, b2_label

def parse_sub_group_dataframe (sub_grp_df, req_row_index):
    sel_row = sub_grp_df.iloc[req_row_index]
    return sel_row['Group_Members'], sel_row['Equipment_Details'],  sel_row['Summary'], sel_row['Causes'], sel_row['reason'], sel_row['Primary_Similarities'], sel_row['Primary_Dissimilarities'], sel_row['component'] + " - " +sel_row['sub_component'], sel_row['tags_set_one'], sel_row['tags_rationale_one']
    
# need similar to above for sub-groups
global main_grp_btn_name
def grp_btn_click_handler(btn_name):
    global main_grp_btn_name
    main_grp_btn_name = btn_name
    if btn_name == "Drive System Failure":
        g0_label = gr.Button(variant="primary")
        g1_label = gr.Button(variant="secondary")
        g2_label = gr.Button(variant="secondary")
        sg_0 = gr.Button(value=g1_sub_grps_list[0])
        sg_1 = gr.Button(value=g1_sub_grps_list[1])
        sg_2 = gr.Button(value=g1_sub_grps_list[2])
        rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10 = parse_sub_group_dataframe(g1_sub_data_df, 0)
        return gr.Markdown(g1_summary), g0_label, g1_label, g2_label, sg_0, sg_1, sg_2, rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10
    elif btn_name == "High Pressure Braking":
        g0_label = gr.Button(variant="secondary")
        g1_label = gr.Button(variant="primary")
        g2_label = gr.Button(variant="secondary")
        sg_0 = gr.Button(value=g2_sub_grps_list[0])
        sg_1 = gr.Button(value=g2_sub_grps_list[1])
        sg_2 = gr.Button(value=g2_sub_grps_list[2])
        rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10 = parse_sub_group_dataframe(g2_sub_data_df, 0)
        return gr.Markdown(g2_summary), g0_label, g1_label, g2_label, sg_0, sg_1, sg_2, rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10
    elif btn_name == "Incor. Pos. / Gap Insufficiency":
        g0_label = gr.Button(variant="secondary")
        g1_label = gr.Button(variant="secondary")
        g2_label = gr.Button(variant="primary")
        sg_0 = gr.Button(value=g3_sub_grps_list[0])
        sg_1 = gr.Button(value=g3_sub_grps_list[1])
        sg_2 = gr.Button(value=g3_sub_grps_list[2])
        rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10 = parse_sub_group_dataframe(g3_sub_data_df, 0)
        return gr.Markdown(g3_summary), g0_label, g1_label, g2_label, sg_0, sg_1, sg_2, rt1, rt2, rt3, rt4, rt5, rt6, rt7, rt8, rt9, rt10
    else:
        return gr.Markdown("No summary available"), gr.Button(variant="secondary"), gr.Button(variant="secondary"), gr.Button(variant="secondary")

def sg_btn_click_handler(btn_name):
    global main_grp_btn_name
    
    if main_grp_btn_name == "Drive System Failure":
        sg_data_df = g1_sub_data_df
        btn_index = g1_sub_grps_list.index(btn_name)
    elif main_grp_btn_name == "High Pressure Braking":
        sg_data_df = g2_sub_data_df
        btn_index = g2_sub_grps_list.index(btn_name)
    elif main_grp_btn_name == "Incor. Pos. / Gap Insufficiency":
        sg_data_df = g3_sub_data_df
        btn_index = g3_sub_grps_list.index(btn_name)
    
    sg_0_label = gr.Button(variant="secondary")
    sg_1_label = gr.Button(variant="secondary") 
    sg_2_label = gr.Button(variant="secondary")

    # need to set sub-group buttons also.
    if btn_index == 0:
        sg_0_label = gr.Button(variant="primary")
        #set subgroup buttons
    elif btn_index == 1:
        sg_1_label = gr.Button(variant="primary")
    elif btn_index == 2:
        sg2_label = gr.Button(variant="primary")
    
    sel_row = sg_data_df.iloc[btn_index]
    return sg_0_label, sg_1_label, sg_2_label, sel_row['Group_Members'], sel_row['Equipment_Details'],  sel_row['Summary'], sel_row['Causes'], sel_row['reason'], sel_row['Primary_Similarities'], sel_row['Primary_Dissimilarities'], sel_row['component'] + " - " +sel_row['sub_component'], sel_row['tags_set_one'], sel_row['tags_rationale_one']


def get_gemini_analysis_handler (query_text, history):
    global gemini_session_type
    global current_fail_group_data
    
    if gemini_session_type == "New Session":
        gemini_session_type = "Old"
        req_prompt = JIN_SHELL_GROUP_PROMPT.replace("xxx_failure_group_notes_xxx", str(current_fail_group_data))
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

    # baaed on main button (or another gloabl variable) get the name of the data file.

    # based on button click index - (from the list of sub-groups)

    # get the data from dataframe file- send index info.

    # each field from the dataframe.
    pass
with gr.Blocks() as demo:
    # add tabs - groups and subgroups
    gr.Markdown("""
        ### Spector.AI ML Model Development Assistant
        """)
    
    with gr.Row():
        with gr.Column():
            with gr.Tabs():
                with gr.TabItem("Failure Groups"):
                    
                    with gr.Row():
                        with gr.Column(scale=1, min_width=50):
                            g_0 = gr.Button(value='Drive System Failure')
                            g_1 = gr.Button(value='High Pressure Braking')
                            g_2 = gr.Button(value='Incor. Pos. / Gap Insufficiency')
                        with gr.Column(scale=4, min_width=200):
                            gr.Markdown("### Failure Groups Overview")
                            g_equip = gr.Markdown(label="Equipment", value=g1_summary)
                            
                with gr.TabItem("Failure Sub-Groups"):
                    
                    with gr.Row():
                        with gr.Column(scale=1, min_width=50):
                            sg_0 = gr.Button(value='Over-Torque')
                            sg_1 = gr.Button(value='Loss of Torque')
                            sg_2 = gr.Button(value='TC Discharge')
                        with gr.Column(scale=4, min_width=200):
                            gr.Markdown("### Failure Sub Groups")
                            sg_anom_ids = gr.Textbox(label="Anomaly Event IDs", value="", interactive=False)
                            sg_component = gr.Textbox(label="Components", value="Comp + Sub-Comp",  interactive=False)
                            sg_tags_list = gr.TextArea(label="Tags of Interest", value="Tag1, Tag2, Tag3", lines=3, interactive=False)
                            sg_tags_rationale = gr.TextArea(label="Tags Rationale", value="Tag1, Tag2, Tag3", lines=3, interactive=False)
                            
                            sg_similarity = gr.TextArea(label="Similarity", value="Similarity Analysis", lines=3, interactive=False) 
                            sg_dissimilarity = gr.TextArea(label="Dissimilarity", value="Similarity Analysis", lines=3, interactive=False) 
                            sg_equip = gr.TextArea(label="Equipment", value="Cause", lines=3, interactive=True)
                            sg_summary = gr.TextArea(label="Summary", value="Cause", lines=3, interactive=True)
                            sg_cause = gr.TextArea(label="Cause", value="Cause", lines=3, interactive=False)
                    
                            sg_reason = gr.TextArea(label="Reasoning", value="Analysis Reasoning", lines=3, interactive=False)
                            
                            
                    
                            
    # add event handler
            g_0.click(grp_btn_click_handler, inputs=[g_0], outputs=[g_equip, g_0, g_1, g_2, sg_0, sg_1, sg_2, sg_anom_ids, sg_equip, sg_summary, sg_cause, sg_reason, sg_similarity, sg_dissimilarity, sg_component, sg_tags_list, sg_tags_rationale])
            g_1.click(grp_btn_click_handler, inputs=[g_1], outputs=[g_equip, g_0, g_1, g_2, sg_0, sg_1, sg_2, sg_anom_ids, sg_equip, sg_summary, sg_cause, sg_reason, sg_similarity, sg_dissimilarity, sg_component, sg_tags_list, sg_tags_rationale])
            g_2.click(grp_btn_click_handler, inputs=[g_2], outputs=[g_equip, g_0, g_1, g_2, sg_0, sg_1, sg_2, sg_anom_ids, sg_equip, sg_summary, sg_cause, sg_reason, sg_similarity, sg_dissimilarity, sg_component, sg_tags_list, sg_tags_rationale])
            sg_0.click(sg_btn_click_handler, inputs=[sg_0], outputs=[sg_0, sg_1, sg_2, sg_anom_ids, sg_equip, sg_summary, sg_cause, sg_reason, sg_similarity, sg_dissimilarity, sg_component, sg_tags_list, sg_tags_rationale])
            sg_1.click(sg_btn_click_handler, inputs=[sg_1], outputs=[sg_0, sg_1, sg_2, sg_anom_ids, sg_equip, sg_summary, sg_cause, sg_reason, sg_similarity, sg_dissimilarity, sg_component, sg_tags_list, sg_tags_rationale])
            sg_2.click(sg_btn_click_handler, inputs=[sg_2], outputs=[sg_0, sg_1, sg_2, sg_anom_ids, sg_equip, sg_summary, sg_cause, sg_reason, sg_similarity, sg_dissimilarity, sg_component, sg_tags_list, sg_tags_rationale])
        with gr.Column():
            cb1 = gr.Chatbot(label="Reliability Agent", type="messages")
            cb2_query = gr.Textbox(show_label=False, placeholder="Type your message here...", submit_btn="Send")
            cb2_query.submit(get_gemini_analysis_handler, inputs=[cb2_query, cb1], outputs=[cb1, cb2_query])
    
    demo.load()





if __name__ == "__main__":
    demo.launch()