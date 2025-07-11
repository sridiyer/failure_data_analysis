"""
Module for writing data to PostgreSQL database tables.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

from src.data.postgres_connector import PostgresConnector

logger = logging.getLogger(__name__)

async def write_triage_data(
    connector: PostgresConnector,
    data: Dict[str, Any]
) -> int:
    """
    Write data to the triage_data table.
    
    Args:
        connector: PostgresConnector instance
        data: Dictionary containing triage data fields
        
    Returns:
        int: Number of rows inserted
    """
    required_fields = {
        'anomaly_date', 'anomaly_start_time', 'anomaly_end_time',
        'delay_duration',  'equipment_details',
        'summary', 'cause', 'component', 'failure_mode',
        'reasoning_rationale', 'recommendations', 'equip_op_status',
        'user_summary_one', 'user_summary_two', 'tags_set_one',
        'tags_rationale_one', 'tags_set_two', 'tags_rationale_two',
        'tags_set_three', 'tags_rationale_three','source_name', 'source_type',
        'contributor_tags', 'search_key_words', 'facility_zone', 'billet_size', 'proc_flag'
    }
    
    # Validate required fields
    missing_fields = required_fields - set(data.keys())
    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")
    
    # Prepare the query
    columns = list(data.keys())
    placeholders = [f"${i+1}" for i in range(len(columns))]
    
    query = f"""
    INSERT INTO triage_data 
    ({', '.join(columns)})
    VALUES ({', '.join(placeholders)})
    RETURNING anomaly_event_id
    """
    
    try:
        # Execute the query
        result = await connector.execute_query(
            query,
            tuple(data[col] for col in columns)
        )
        
        if result:
            anomaly_event_id = result[0]['anomaly_event_id']
            logger.info(f"Successfully inserted triage data with ID: {anomaly_event_id}")
            return anomaly_event_id
        else:
            raise Exception("Failed to insert triage data - no ID returned")
            
    except Exception as e:
        logger.error(f"Error writing triage data: {str(e)}")
        raise

async def write_jindal_maintenance_data(
    connector: PostgresConnector,
    data: Dict[str, Any]
) -> int:
    """
    Write data to the jindal_maintenance_data table.
    
    Args:
        connector: PostgresConnector instance
        data: Dictionary containing jindal maintenance data fields
        
    Returns:
        int: Number of rows inserted
    """
    required_fields = {
        'anomaly_date', 'anomaly_start_time', 'anomaly_end_time',
        'delay_duration', 'equipment_details', 'summary', 'cause', 
        'component', 'sub_component', 'failure_mode', 'reason', 
        'recommendation', 'equip_op_status', 'capa_summary', 'delay_summary', 
        'tags_set_one', 'tags_rationale_one', 'tags_set_two', 'tags_rationale_two', 
        'source_name', 'source_type', 'contributor_tags', 'search_key_words', 
        'facility_zone', 'billet_size', 'proc_flag'
    }
    
    # Validate required fields
    missing_fields = required_fields - set(data.keys())
    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")
    
    # Prepare the query
    columns = list(data.keys())
    placeholders = [f"${i+1}" for i in range(len(columns))]
    
    query = f"""
    INSERT INTO jindal_maintenance_data 
    ({', '.join(columns)})
    VALUES ({', '.join(placeholders)})
    RETURNING anomaly_event_id
    """
    
    try:
        # Execute the query
        result = await connector.execute_query(
            query,
            tuple(data[col] for col in columns)
        )
        
        if result:
            anomaly_event_id = result[0]['anomaly_event_id']
            logger.info(f"Successfully inserted jindal maintenance data with ID: {anomaly_event_id}")
            return anomaly_event_id
        else:
            raise Exception("Failed to insert jindal maintenance data - no ID returned")
            
    except Exception as e:
        logger.error(f"Error writing jindal maintenance data: {str(e)}")
        raise

async def write_analysis_data(
    connector: PostgresConnector,
    data: Dict[str, Any]
) -> int:
    """
    Write data to the analysis_data table.
    
    Args:
        connector: PostgresConnector instance
        data: Dictionary containing analysis data fields
        
    Returns:
        int: Number of rows inserted
    """
    required_fields = {
        'iteration_num', 'anomaly_event_id', 'analysis_summary',
        'tags_data_summary', 'cause', 'component', 'failure_mode',
        'reasoning_rationale', 'equip_op_status_summary',
        'false_positive_flag', 'fp_confidence_score', 'tags_trends',
        'tags_set_one', 'tags_rationale_one', 'tags_set_two',
        'tags_rationale_two', 'tags_set_three', 'tags_rationale_three',
        'images_locations', 'search_key_words'
    }
    
    # Validate required fields
    missing_fields = required_fields - set(data.keys())
    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")
    
    # Prepare the query
    columns = list(data.keys())
    placeholders = [f"${i+1}" for i in range(len(columns))]
    
    query = f"""
    INSERT INTO analysis_data 
    ({', '.join(columns)})
    VALUES ({', '.join(placeholders)})
    RETURNING analysis_id
    """
    
    try:
        # Execute the query
        result = await connector.execute_query(
            query,
            tuple(data[col] for col in columns)
        )
        
        if result:
            analysis_id = result[0]['analysis_id']
            logger.info(f"Successfully inserted analysis data with ID: {analysis_id}")
            return analysis_id
        else:
            raise Exception("Failed to insert analysis data - no ID returned")
            
    except Exception as e:
        logger.error(f"Error writing analysis data: {str(e)}")
        raise

async def write_batch_triage_data(
    connector: PostgresConnector,
    data_list: List[Dict[str, Any]]
) -> List[int]:
    """
    Write multiple records to the triage_data table in a single transaction.
    
    Args:
        connector: PostgresConnector instance
        data_list: List of dictionaries containing triage data
        
    Returns:
        List[int]: List of inserted anomaly_event_ids
    """
    if not data_list:
        logger.warning("No data provided for batch insert")
        return []
    
    # Prepare the query
    columns = list(data_list[0].keys())
    placeholders = [f"${i+1}" for i in range(len(columns))]
    
    query = f"""
    INSERT INTO triage_data 
    ({', '.join(columns)})
    VALUES ({', '.join(placeholders)})
    RETURNING anomaly_event_id
    """
    
    try:
        # Execute batch insert
        results = await connector.execute_batch(
            query,
            [tuple(data[col] for col in columns) for data in data_list]
        )
        
        inserted_ids = [row['anomaly_event_id'] for row in results]
        logger.info(f"Successfully inserted {len(inserted_ids)} triage records")
        return inserted_ids
        
    except Exception as e:
        logger.error(f"Error in batch triage data insert: {str(e)}")
        raise

async def write_batch_analysis_data(
    connector: PostgresConnector,
    data_list: List[Dict[str, Any]]
) -> List[int]:
    """
    Write multiple records to the analysis_data table in a single transaction.
    
    Args:
        connector: PostgresConnector instance
        data_list: List of dictionaries containing analysis data
        
    Returns:
        List[int]: List of inserted analysis_ids
    """
    if not data_list:
        logger.warning("No data provided for batch insert")
        return []
    
    # Prepare the query
    columns = list(data_list[0].keys())
    placeholders = [f"${i+1}" for i in range(len(columns))]
    
    query = f"""
    INSERT INTO analysis_data 
    ({', '.join(columns)})
    VALUES ({', '.join(placeholders)})
    RETURNING analysis_id
    """
    
    try:
        # Execute batch insert
        results = await connector.execute_batch(
            query,
            [tuple(data[col] for col in columns) for data in data_list]
        )
        
        inserted_ids = [row['analysis_id'] for row in results]
        logger.info(f"Successfully inserted {len(inserted_ids)} analysis records")
        return inserted_ids
        
    except Exception as e:
        logger.error(f"Error in batch analysis data insert: {str(e)}")
        raise

async def update_triage_data(
    connector: PostgresConnector,
    where_data: Dict[str, Any],
    update_data: Dict[str, Any],
    table_name: str = "triage_data"
) -> int:
    """
    Update records in the triage_data table based on where conditions.
    
    Args:
        connector: PostgresConnector instance
        where_data: Dictionary containing column_name: value pairs for WHERE clause
        update_data: Dictionary containing column_name: value pairs to update
        table_name: Name of the table to update (default: "triage_data")
        
    Returns:
        int: Number of rows updated
        
    Raises:
        ValueError: If where_data or update_data is empty
        Exception: If there's an error executing the update
    """
    if not where_data:
        raise ValueError("where_data cannot be empty")
    if not update_data:
        raise ValueError("update_data cannot be empty")
        
    try:
        # Construct the SET clause
        set_clauses = []
        param_index = 1
        params = []
        
        for column, value in update_data.items():
            set_clauses.append(f"{column} = ${param_index}")
            params.append(value)
            param_index += 1
            
        # Construct the WHERE clause
        where_clauses = []
        for column, value in where_data.items():
            where_clauses.append(f"{column} = ${param_index}")
            params.append(value)
            param_index += 1
            
        # Construct the full query
        query = f"""
        UPDATE {table_name}
        SET {', '.join(set_clauses)}
        WHERE {' AND '.join(where_clauses)}
        RETURNING *
        """
        
        # Execute the update
        result = await connector.execute_query(query, tuple(params))
        
        if result:
            num_updated = len(result)
            logger.info(f"Successfully updated {num_updated} records in {table_name}")
            return num_updated
        else:
            logger.warning(f"No records were updated in {table_name}")
            return 0
            
    except Exception as e:
        logger.error(f"Error updating {table_name}: {str(e)}")
        raise 