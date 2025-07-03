import gradio as gr
import pandas as pd
import json

from sqlalchemy import create_engine, text

engine = create_engine('postgresql://bramhesh:Dev%400119%40%21%40@34.72.177.167:5432/experimental_si')



def get_data_from_db(cob_date_from, cob_date_to):

    # '2024-01-02'
    cob_date_start = cob_date_from.strip()
    cob_date_end = cob_date_to.strip()
    query = text("""SELECT * FROM triage_data 
                 WHERE triage_data.anomaly_date >= :anom_date_start AND triage_data.anomaly_date <= :anom_date_end
                 AND triage_data.facility_zone = 'TCTB' """ )
    data_df = pd.read_sql_query(query, engine, params={'anom_date_start': cob_date_start, 'anom_date_end': cob_date_end})
    # list of dicts
    data_df = data_df.drop(columns=['created_at'])
    dict_list = data_df.to_dict(orient='records')
    #row_data = data_df.iloc[0].to_dict()
    json_data = json.dumps(dict_list, indent=4)

    return json_data


with gr.Blocks() as demo:
    gr.Markdown("Analysis of Historical Cobble Data (from capa data - between 2024-01-02 and 2024-12-31)")
    with gr.Row():
        cob_date_from = gr.Textbox(label="Cobble Events Start Date (yyyy-mm-dd)", value="2024-01-02")
        cob_date_to = gr.Textbox(label="Cobble Events End Date (yyyy-mm-dd)", value="2024-01-03")
        sql_btn =gr.Button("Get Cobble Analysis Data")
    #db_data = gr.Textbox(label="Cobble Events Analysis", lines=25)
    db_data = gr.JSON(label="Cobble Events Analysis")
    sql_btn.click(get_data_from_db, inputs=[cob_date_from, cob_date_to], outputs=db_data)

if __name__ == "__main__":
    demo.queue()
    demo.launch(server_name="0.0.0.0", server_port=8080)




