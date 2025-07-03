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

from src.data.pickle_file_reader import read_pickle_file
from src.data.postgres_connector import PostgresConnector
from src.llms.gemini_wrapper import extract_jinal_cobble_history_triage_tags
from src.database.postgres_writer import write_jindal_maintenance_data


def read_processed_cobble_data(file_path:  Union[str, Path]) -> pd.DataFrame:
    return read_pickle_file (file_path)


async def get_output_postgres_connection() -> PostgresConnector:
    """Initialize and return a connection to the output postgres database."""
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    db_config = config['databases']['output_postgres']
    connector = PostgresConnector(db_config)
    await connector.connect()
    return connector


async def write_llm_results(
    connector: PostgresConnector,
    ev_date: str,
    ev_start_time: str,
    ev_end_time: str,
    ev_equipment_details: str,
    ev_summary: str,
    ev_cause: str,
    ev_component: str,
    ev_sub_component: str,
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
    ev_source_name: str,
    ev_source_type: str,
    ev_contributor_tags: List[str],
    ev_search_key_words: List[str],
    ev_facility_zone: str,
    ev_billet_size: str,
    ev_proc_flag: int
) -> int:
    """
    Write LLM processing results to the jindal_maintenance_data table.
    
    Args:
        connector: PostgresConnector instance
        ev_date: Event date
        ev_start_time: Event start time
        ev_end_time: Event end time
        ev_equipment_details: Equipment details
        ev_summary: Summary of the event
        ev_cause: Cause of the event
        ev_component: Component involved
        ev_sub_component: Sub-component involved
        ev_failure_mode: Failure mode
        ev_reasoning_rationale: Reasoning and rationale
        ev_recommendations: Recommendations
        ev_equip_op_status: Equipment operational status
        ev_user_summary_one: First user summary
        ev_user_summary_two: Second user summary
        ev_tags_set_one: First set of tags
        ev_tags_rationale_one: Rationale for first tag set
        ev_tags_set_two: Second set of tags
        ev_tags_rationale_two: Rationale for second tag set
        ev_source_name: Source name
        ev_source_type: Source type
        ev_contributor_tags: Contributor tags
        ev_search_key_words: Search keywords
        ev_facility_zone: Facility zone
        ev_billet_size: Billet size
        ev_proc_flag: Processing flag
        
    Returns:
        int: The anomaly_event_id of the inserted record
    """
    # Calculate delay duration from start and end times
    try:
        start_dt = datetime.strptime(ev_start_time, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(ev_end_time, "%Y-%m-%d %H:%M:%S")
        delay_duration = int((end_dt - start_dt).total_seconds() / 60)  # Convert to minutes
    except (ValueError, TypeError):
        delay_duration = 0
    
    # Prepare data dictionary for database insertion
    data = {
        'anomaly_date': ev_date,
        'anomaly_start_time': ev_start_time,
        'anomaly_end_time': ev_end_time,
        'delay_duration': delay_duration,
        'equipment_details': ev_equipment_details,
        'summary': ev_summary,
        'cause': ev_cause,
        'component': ev_component,
        'sub_component': ev_sub_component,
        'failure_mode': ev_failure_mode,
        'reason': ev_reasoning_rationale,  # Map to 'reason' field in schema
        'recommendation': ev_recommendations,  # Map to 'recommendation' field in schema
        'equip_op_status': ev_equip_op_status,
        'capa_summary': ev_user_summary_two,  # Use second user summary as CAPA summary
        'delay_summary': ev_user_summary_one,  # Use first user summary as delay summary
        'tags_set_one': ev_tags_set_one,
        'tags_rationale_one': ev_tags_rationale_one,
        'tags_set_two': ev_tags_set_two,
        'tags_rationale_two': ev_tags_rationale_two,
        'source_name': ev_source_name,
        'source_type': ev_source_type,
        'contributor_tags': ev_contributor_tags,
        'search_key_words': ev_search_key_words,
        'facility_zone': ev_facility_zone,
        'billet_size': ev_billet_size,
        'proc_flag': ev_proc_flag
    }
    
    # Write to database using the existing function
    anomaly_event_id = await write_jindal_maintenance_data(connector, data)
    return anomaly_event_id


async def process_filterd_cobble_data():
    DATA_FILE = "bk_delay_capa_merged_summary_data.pkl"
    
    # Get the current file's directory
    current_dir = Path(__file__).parent
    
    # Construct full file path
    file_path = current_dir.parent / "data" / DATA_FILE
    
    print("cobble incidents file path: ", file_path)

    connector = await get_output_postgres_connection()

    try:
        # Load cobble incidents data
        cobble_incidents_df = read_processed_cobble_data(file_path)
        count = 0
        inserted_ids = []
        
        for index, row in cobble_incidents_df.iterrows():
            # filter events
            # if index < 152:
            #     continue
            print(f"Processing row {index}  ------")
            ev_date = str(row['event_date'])
            ev_start_time = str(row['event_start_time'])
            ev_end_time = str(row['event_end_time'])
            ev_delay_data = row['delay_data']
            ev_capa_data = row['capa_data']

            gem_response = extract_jinal_cobble_history_triage_tags(ev_delay_data, ev_capa_data)
            #print ("\n______")
            #print (gem_response)
            time.sleep(3)
            # extract data from gem_response
            # TODO: extract data from gem_response
          
            ev_equipment_details = gem_response.get('equipment_details', '')
            ev_summary = gem_response.get('summary', '')
            ev_cause = gem_response.get('cause', '')
            ev_component = gem_response.get('component', '')
            ev_sub_component = gem_response.get('sub_component', '')
            ev_failure_mode = gem_response.get('failure_mode', '')
            ev_reasoning_rationale = gem_response.get('reasoning_rationale', '')
            ev_recommendations = gem_response.get('recommendations', '')
            ev_equip_op_status = gem_response.get('equip_op_status', '')
            
            ev_tags_set_one = gem_response.get('tags_set_one', [])
            ev_tags_rationale_one = gem_response.get('tags_rationale_one', '')
            ev_tags_set_two = gem_response.get('tags_set_two', [])
            ev_tags_rationale_two = gem_response.get('tags_rationale_two', '')
            ev_user_summary_one = ev_delay_data
            ev_user_summary_two = ev_capa_data
            ev_source_name = "DELAY_AND_CAPA"
            ev_source_type = "BK_FILTERED_DATA"
            ev_contributor_tags = []
            ev_search_key_words = []
            ev_proc_flag = 0
            
            # TODO: extract facility_zone and billet_size
            ev_facility_zone = ""
            ev_billet_size = ""
            ev_proc_flag = 0

            ## CALL LLM HERE
            
            anomaly_event_id = await write_llm_results(
                connector,
                ev_date, ev_start_time, ev_end_time,
                ev_equipment_details,
                ev_summary,
                ev_cause,
                ev_component,
                ev_sub_component,
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
        
        
        return inserted_ids
        
    finally:
        # Ensure connection is closed
        await connector.disconnect()
    

if __name__ == "__main__":
    asyncio.run(process_filterd_cobble_data())

