from src.data.postgres_connector import PostgresConnector
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd
from datetime import datetime
from src.database.postgres_reader import triage_data_reader
from src.database.postgres_writer import update_triage_data

async def get_output_postgres_connection() -> PostgresConnector:
    """Initialize and return a connection to the output postgres database."""
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    db_config = config['databases']['output_postgres']
    connector = PostgresConnector(db_config)
    await connector.connect()
    return connector

async def analyze_triage_data(
    where_conditions: Optional[List[Dict[str, Any]]] = None
) -> pd.DataFrame:
    """
    Analyze triage data based on provided conditions.
    
    Args:
        where_conditions: List of dictionaries containing column_name: value pairs for filtering
        
    Returns:
        pd.DataFrame: Filtered triage data
    """
    try:
        # Get database connection
        db_connector = await get_output_postgres_connection()
        
        # Read triage data with conditions
        df = await triage_data_reader(
            db_connector=db_connector,
            table_name="triage_data",
            filter_conditions=where_conditions
        )
        
        return df
        
    except Exception as e:
        raise Exception(f"Error analyzing triage data: {str(e)}")
    finally:
        if 'db_connector' in locals():
            await db_connector.disconnect()

async def update_triage_records(
    where_data: Dict[str, Any],
    update_data: Dict[str, Any]
) -> int:
    """
    Update triage records based on where conditions and update values.
    
    Args:
        where_data: Dictionary containing column_name: value pairs for WHERE clause
        update_data: Dictionary containing column_name: value pairs to update
        
    Returns:
        int: Number of records updated
    """
    try:
        # Get database connection
        db_connector = await get_output_postgres_connection()
        
        # Update triage data
        num_updated = await update_triage_data(
            connector=db_connector,
            where_data=where_data,
            update_data=update_data
        )
        
        return num_updated
        
    except Exception as e:
        raise Exception(f"Error updating triage records: {str(e)}")
    finally:
        if 'db_connector' in locals():
            await db_connector.disconnect()

async def process_triage_data(
    where_conditions: List[Dict[str, Any]],
    update_values: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Process triage data by reading and updating records.
    
    Args:
        where_conditions: List of dictionaries containing column_name: value pairs for filtering
        update_values: Dictionary containing column_name: value pairs to update
        
    Returns:
        Dict[str, Any]: Processing results including data and update status
    """
    try:
        # First read the data
        df = await analyze_triage_data(where_conditions)
        
        if df.empty:
            return {
                "status": "no_data",
                "message": "No records found matching the conditions",
                "data": None,
                "updated_count": 0
            }
        
        # Create where_data from the first record's conditions
        where_data = {}
        for condition in where_conditions:
            where_data.update(condition)
        
        # Update the records
        num_updated = await update_triage_records(where_data, update_values)
        
        return {
            "status": "success",
            "message": f"Successfully processed {len(df)} records and updated {num_updated} records",
            "data": df,
            "updated_count": num_updated
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "data": None,
            "updated_count": 0
        }

