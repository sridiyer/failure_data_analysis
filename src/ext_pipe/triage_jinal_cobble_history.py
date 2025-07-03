"""
analyze the cobble historical data provided by client Jinal

"""

import sys
import os
from pathlib import Path
from typing import Union, Dict, Any, List
import yaml
import pandas as pd
import asyncio
from datetime import datetime
import time
import pickle
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.data.csv_reader import load_csv_data
from src.data.postgres_connector import PostgresConnector
from src.database.postgres_writer import write_triage_data
from src.llms.gemini_wrapper import extract_jinal_cobble_history_triage_tags
from src.llms.gemini_wrapper import extract_jinal_capa_tags
# call LLM to get a prelimary list of tags to analyze.

def read_historical_cobble_data(file_path:  Union[str, Path]) -> pd.DataFrame:
    return pd.read_csv(file_path)






async def get_output_postgres_connection() -> PostgresConnector:
    """Initialize and return a connection to the output postgres database."""
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    db_config = config['databases']['output_postgres']
    connector = PostgresConnector(db_config)
    await connector.connect()
    return connector

async def write_triage_results(
    connector: PostgresConnector,
    ev_date: str,
    ev_start_time: str,
    ev_end_time: str,
    ev_dly_duration: int,
    ev_equipment_details: str,
    ev_summary: str,
    ev_cause: str,
    ev_component: str,
    ev_failure_mode: str,
    ev_reasoning_rationale: str,
    ev_recommendations: str,
    ev_equip_op_status: str,
    ev_user_summary_one: str,
    ev_user_summary_two: str,
    ev_tags_set_one: List[str],
    ev_tags_rationale_one: str,
    ev_tags_set_two: List[str],
    ev_tags_rationale_two: str,
    ev_tags_set_three: List[str],
    ev_tags_rationale_three: str,
    ev_source_name: str,
    ev_source_type: str,
    ev_contributor_tags: List[str],
    ev_search_key_words: List[str],
    ev_facility_zone: str,
    ev_billet_size: str,
    ev_proc_flag: int
) -> int:
    """
    Write triage results to the database.
    
    Args:
        connector: PostgresConnector instance
        All other parameters are the extracted event data
        
    Returns:
        int: The anomaly_event_id of the inserted record
    """
    # Prepare the data dictionary according to the schema
    triage_data = {
        'anomaly_date': ev_date,
        'anomaly_start_time': ev_start_time,
        'anomaly_end_time': ev_end_time,
        'delay_duration': ev_dly_duration,      
        'equipment_details': ev_equipment_details,
        'summary': ev_summary,
        'cause': ev_cause,
        'component': ev_component,
        'failure_mode': ev_failure_mode,
        'reasoning_rationale': ev_reasoning_rationale,
        'recommendations': ev_recommendations,
        'equip_op_status': ev_equip_op_status,
        'user_summary_one': ev_user_summary_one,
        'user_summary_two': ev_user_summary_two,
        'tags_set_one': ev_tags_set_one,
        'tags_rationale_one': ev_tags_rationale_one,
        'tags_set_two': ev_tags_set_two,
        'tags_rationale_two': ev_tags_rationale_two,
        'tags_set_three': ev_tags_set_three,
        'tags_rationale_three': ev_tags_rationale_three,
        'source_name': ev_source_name, #TODO
        'source_type': ev_source_type,
        'contributor_tags': ev_contributor_tags,
        'search_key_words': ev_search_key_words,
        'facility_zone': ev_facility_zone,
        'billet_size': ev_billet_size,
        'proc_flag': ev_proc_flag
    }
    
    return await write_triage_data(connector, triage_data)




async def triage_jindal_delays_data():
    DATA_FILE = "may23_capa_delay_match_189.csv"
    
    # Get the current file's directory
    current_dir = Path(__file__).parent
    
    # Construct full file path
    file_path = current_dir.parent / "data" / DATA_FILE
    
    print("cobble incidents file path: ", file_path)
    
    # Initialize database connection
    connector = await get_output_postgres_connection()

    processed_timestamps_list = []
    
    try:
        # Load cobble incidents data
        cobble_incidents_df = load_csv_data(file_path)
        count = 0
        inserted_ids = []
        
        for index, row in cobble_incidents_df.iterrows():
            if index < 152:
                continue
            print(f"Processing row {index}  ------")
            ev_date = str(row['delay_event_date'])
            ev_start_time = str(row['delay_start_time'])
            ev_end_time = str(row['delay_end_time'])
            ev_dly_duration = int(row['delay_minutes'])
            
            # TODO: compare start-date - skip already processed events.
            if ev_start_time in processed_timestamps_list:
                continue
            else:
                processed_timestamps_list.append(ev_start_time)
            
            # parse equipment details (location)
            ev_dly_area = str(row['area'])
            ev_dly_device = str(row['device'])
            ev_dly_agency = str(row['agency'])
            ev_capa_equip = str(row['equipment'])

            # parse comments
            ev_dly_reason = str(row['reason'])
            ev_dly_description = str(row['description'])
            ev_capa_prob_desc = str(row['problem_description'])
            ev_capa_restart_steps = str(row['restart_steps'])
            ev_capa_1yr = str(row['one_year'])
            ev_capa_2yr = str(row['two_year'])
            ev_capa_3yr = str(row['three_year'])
            ev_capa_4yr = str(row['four_year'])
            ev_capa_5yr = str(row['five_year'])
            ev_capa_corrective_action = str(row['corrective_action'])
            ev_capa_preventive_action = str(row['preventive_action'])
            ev_capa_actual_action_taken = str(row['actual_action_taken'])
            
            # need two observation notes sections
            # sub-sections within each.
            rept_1_notes = "-AREA:" + ev_dly_area + "\n-DEVICE:" + ev_dly_device + "\n-AGENCY:" + ev_dly_agency 
            rept_1_notes += "\n-REASON:" + ev_dly_reason + "\n-DESCRIPTION:" + ev_dly_description 
            
            rept_2_notes = "-EQUIPMENT:" + ev_capa_equip + "\n-PROBLEM DESCRIPTION:" + ev_capa_prob_desc + "\n-RESTART STEPS:" + ev_capa_restart_steps 
            rept_2_notes += "\n-1Y:" + ev_capa_1yr + "\n-2Y:" + ev_capa_2yr + "\n-3Y:" + ev_capa_3yr + "\n-4Y:" + ev_capa_4yr + "\n-5Y:" + ev_capa_5yr 
            rept_2_notes += "\n-CORRECTIVE ACTION:" + ev_capa_corrective_action + "\n-PREVENTIVE ACTION:" + ev_capa_preventive_action + "\n-ACTUAL ACTION TAKEN:" + ev_capa_actual_action_taken
            
            
            gem_response = extract_jinal_cobble_history_triage_tags(rept_1_notes, rept_2_notes)
            #print ("\n______")
            #print (gem_response)
            time.sleep(3)
            # extract data from gem_response
            # TODO: extract data from gem_response
          
            ev_equipment_details = gem_response.get('equipment_details', '')
            ev_summary = gem_response.get('summary', '')
            ev_cause = gem_response.get('cause', '')
            ev_component = gem_response.get('component', '')
            ev_failure_mode = gem_response.get('failure_mode', '')
            ev_reasoning_rationale = gem_response.get('reasoning_rationale', '')
            ev_recommendations = gem_response.get('recommendations', '')
            ev_equip_op_status = gem_response.get('equip_op_status', '')
            ev_user_summary_one = gem_response.get('user_summary_one', '')
            ev_user_summary_two = gem_response.get('user_summary_two', '')
            ev_tags_set_one = gem_response.get('tags_set_one', [])
            ev_tags_rationale_one = gem_response.get('tags_rationale_one', '')
            ev_tags_set_two = gem_response.get('tags_set_two', [])
            ev_tags_rationale_two = gem_response.get('tags_rationale_two', '')
            ev_tags_set_three = gem_response.get('tags_set_three', [])
            ev_tags_rationale_three = gem_response.get('tags_rationale_three', '')
            ev_source_name = "DELAY_AND_CAPA"
            ev_source_type = "HISTORICAL_DATA"
            ev_contributor_tags = []
            ev_search_key_words = []
            ev_proc_flag = 0
            
            # TODO: extract facility_zone and billet_size
            ev_facility_zone = ""
            ev_billet_size = ""
            
            anomaly_event_id = await write_triage_results(
                connector,
                ev_date, ev_start_time, ev_end_time,
                ev_dly_duration,
                ev_equipment_details,
                ev_summary,
                ev_cause,
                ev_component,
                ev_failure_mode,
                ev_reasoning_rationale,
                ev_recommendations,
                ev_equip_op_status,
                ev_user_summary_one,
                ev_user_summary_two,
                ev_tags_set_one,
                ev_tags_rationale_one,
                ev_tags_set_two,
                ev_tags_rationale_two,
                ev_tags_set_three,
                ev_tags_rationale_three,
                ev_source_name,
                ev_source_type,
                ev_contributor_tags,
                ev_search_key_words,
                ev_facility_zone,
                ev_billet_size,
                ev_proc_flag
            )
            inserted_ids.append(anomaly_event_id)
            
            
            count += 1
            #if count > 2:
            #    break
            
        #inserted_ids = [1,2]
        print(f"Successfully inserted : {len(inserted_ids)} records")
        print(f"Successfully processed : {count} records")
        # Save processed timestamps list
        pickle_file_path = current_dir / "processed_ts_list.pkl"
        with open(pickle_file_path, 'wb') as f:
            pickle.dump(processed_timestamps_list, f)
        print(f"Saved processed timestamps list to {pickle_file_path}")
        
        return inserted_ids
        
    finally:
        # Ensure connection is closed
        await connector.disconnect()
        

async def triage_jindal_capa_data():
    DATA_FILE = "may23_capa_dates_fixed.csv"
    
    # Get the current file's directory
    current_dir = Path(__file__).parent
    
    # Construct full file path
    file_path = current_dir.parent / "data" / DATA_FILE
    
    print("cobble incidents file path: ", file_path)
    
    # Initialize database connection
    connector = await get_output_postgres_connection()

    processed_timestamps_list = []
    
    try:
        # Load cobble incidents data
        cobble_incidents_df = load_csv_data(file_path)
        count = 0
        inserted_ids = []
        
        for index, row in cobble_incidents_df.iterrows():
            # 518 had min text in number field temp fix
            if index < 622: #or index > 518:
                continue
            print(f"Processing row {index}  ------")
            ev_date = str(row['date'].split(" ")[0])
            ev_start_time = str(row['capa_start_time'])
            ev_end_time = str(row['capa_end_time'])
            ev_dly_duration = int(row['delay_minutes'])
            ev_billet_size = str(row['section'])
            
            
            
            
            ev_capa_equip = str(row['equipment'])

            ev_capa_prob_desc = str(row['problem_description'])
            ev_capa_restart_steps = str(row['restart_steps'])
            ev_capa_1yr = str(row['one_year'])
            ev_capa_2yr = str(row['two_year'])
            ev_capa_3yr = str(row['three_year'])
            ev_capa_4yr = str(row['four_year'])
            ev_capa_5yr = str(row['five_year'])
            ev_capa_corrective_action = str(row['corrective_action'])
            ev_capa_preventive_action = str(row['preventive_action'])
            ev_capa_actual_action_taken = str(row['actual_action_taken'])
            
            # need two observation notes sections
            # sub-sections within each.
            rept_1_notes = "" # no delay notes
            
            rept_2_notes = "-EQUIPMENT:" + ev_capa_equip + "\n-PROBLEM DESCRIPTION:" + ev_capa_prob_desc + "\n-RESTART STEPS:" + ev_capa_restart_steps 
            rept_2_notes += "\n-1Y:" + ev_capa_1yr + "\n-2Y:" + ev_capa_2yr + "\n-3Y:" + ev_capa_3yr + "\n-4Y:" + ev_capa_4yr + "\n-5Y:" + ev_capa_5yr 
            rept_2_notes += "\n-CORRECTIVE ACTION:" + ev_capa_corrective_action + "\n-PREVENTIVE ACTION:" + ev_capa_preventive_action + "\n-ACTUAL ACTION TAKEN:" + ev_capa_actual_action_taken
            
            
            gem_response = extract_jinal_capa_tags(rept_2_notes)
            #print ("\n______")
            #print (gem_response)
            time.sleep(2)
            # extract data from gem_response
            # TODO: extract data from gem_response
          
            ev_equipment_details = gem_response.get('equipment_details', '')
            ev_summary = gem_response.get('summary', '')
            ev_cause = gem_response.get('cause', '')
            ev_component = gem_response.get('component', '')
            ev_failure_mode = gem_response.get('failure_mode', '')
            ev_reasoning_rationale = gem_response.get('reasoning_rationale', '')
            ev_recommendations = gem_response.get('recommendations', '')
            ev_equip_op_status = gem_response.get('equip_op_status', '')
            ev_user_summary_one = ''
            ev_user_summary_two = gem_response.get('user_summary_two', '')
            ev_tags_set_one = gem_response.get('tags_set_one', [])
            ev_tags_rationale_one = gem_response.get('tags_rationale_one', '')
            ev_tags_set_two = gem_response.get('tags_set_two', [])
            ev_tags_rationale_two = gem_response.get('tags_rationale_two', '')
            ev_tags_set_three = gem_response.get('tags_set_three', [])
            ev_tags_rationale_three = gem_response.get('tags_rationale_three', '')
            ev_source_name = "CAPA"
            ev_source_type = "HISTORICAL_DATA"
            ev_contributor_tags = []
            ev_search_key_words = []
            ev_facility_zone = gem_response.get('facility_zone', '')
            ev_proc_flag = 0
            
            anomaly_event_id = await write_triage_results(
                connector,
                ev_date, ev_start_time, ev_end_time,
                ev_dly_duration,
                ev_equipment_details,
                ev_summary,
                ev_cause,
                ev_component,
                ev_failure_mode,
                ev_reasoning_rationale,
                ev_recommendations,
                ev_equip_op_status,
                ev_user_summary_one,
                ev_user_summary_two,
                ev_tags_set_one,
                ev_tags_rationale_one,
                ev_tags_set_two,
                ev_tags_rationale_two,
                ev_tags_set_three,
                ev_tags_rationale_three,
                ev_source_name,
                ev_source_type,
                ev_contributor_tags,
                ev_search_key_words,
                ev_facility_zone,
                ev_billet_size,
                ev_proc_flag
            )
            inserted_ids.append(anomaly_event_id)
            
            
            count += 1
            #if count > 1:
            #    break
            
        #inserted_ids = [1,2]
        print(f"Successfully inserted : {len(inserted_ids)} records")
        print(f"Successfully processed : {count} records")
        # Save processed timestamps list
        """
        pickle_file_path = current_dir / "processed_ts_list.pkl"
        with open(pickle_file_path, 'wb') as f:
            pickle.dump(processed_timestamps_list, f)
        print(f"Saved processed timestamps list to {pickle_file_path}")
        """
        return inserted_ids
        
    finally:
        # Ensure connection is closed
        await connector.disconnect()
if __name__ == "__main__":
    #asyncio.run(triage_jindal_delays_data())
    asyncio.run(triage_jindal_capa_data())