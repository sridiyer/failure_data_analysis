from typing import List, Dict, Any, Optional
import pandas as pd
from src.data.postgres_connector import PostgresConnector

async def triage_data_reader(
    db_connector: PostgresConnector,
    table_name: str = "triage_data",
    filter_conditions: Optional[List[Dict[str, Any]]] = None
) -> pd.DataFrame:
    """
    Read triage data from PostgreSQL database with optional filtering conditions.
    
    Args:
        db_connector: PostgresConnector instance for database connection
        table_name: Name of the table to query (default: "triage_data")
        filter_conditions: List of dictionaries containing column_name: value pairs for WHERE clause
        
    Returns:
        pd.DataFrame: Query results as a pandas DataFrame
        
    Raises:
        ConnectionError: If database connection is not established
        Exception: If there's an error executing the query
    """
    if not db_connector.is_connected():
        raise ConnectionError("Database connection not established")

    try:
        # Base query
        query = f"SELECT * FROM {table_name}"
        
        # Add WHERE clause if filter conditions are provided
        params = {}
        if filter_conditions and len(filter_conditions) > 0:
            where_clauses = []
            param_index = 1
            
            for condition in filter_conditions:
                for column, value in condition.items():
                    param_name = f"param_{param_index}"
                    where_clauses.append(f"{column} = ${param_index}")
                    params[param_name] = value
                    param_index += 1
            
            if where_clauses:
                query += " WHERE " + " AND ".join(where_clauses)
        
        # Execute query using PostgresConnector's execute_query_to_df method
        df = await db_connector.execute_query_to_df(query, params)
        return df
        
    except Exception as e:
        raise Exception(f"Error processing query: {str(e)}")
