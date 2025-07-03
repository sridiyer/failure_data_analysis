

"""
SELECT
  TIMESTAMP_BUCKET(timestamp, INTERVAL 100 MILLISECOND) AS bucket,
  AVG(TB2_1A_ActualSpeed) AS avg_speed,
  AVG(TB2_1A_TailPos) AS avg_tail_pos
FROM
  `sp-prod-mlops`.`jindal_raw_data`.`tb_twc_data`
GROUP BY
  bucket
ORDER BY bucket;


"""

"""
BigQuery Data Query Module

This module provides functionality to query data from BigQuery database
with dynamic column selection and time-based aggregation.

Requirements:
- google-cloud-bigquery
- pandas
- Authenticated BigQuery client (bq_client)
"""

import pandas as pd
from typing import List, Optional
from google.cloud import bigquery


def get_data_from_bq(
    bq_client: bigquery.Client,
    input_column_names: str,
    project_id: str,
    dataset: str,
    table: str,
    interval_time: int = 100
) -> pd.DataFrame:
    """
    Query data from BigQuery with dynamic column selection and time bucketing.
    
    Args:
        bq_client: Authenticated BigQuery client
        input_column_names: Space-separated string of column names to query
        project_id: BigQuery project ID
        dataset: BigQuery dataset name
        table: BigQuery table name
        interval_time: Duration of interval in milliseconds (default: 100)
    
    Returns:
        pandas.DataFrame: Query results with bucketed timestamps and averaged values
    
    Example:
        df = get_data_from_bq(
            bq_client=client,
            input_column_names="TB2_1A_ActualSpeed TB2_1A_TailPos",
            project_id="my-project",
            dataset="my_dataset",
            table="my_table",
            interval_time=200
        )
    """
    
    # Step 1: Split the input column names string
    column_names = input_column_names.split()
    
    if not column_names:
        raise ValueError("No column names provided")
    
    # Step 2: Build the SELECT clause with dynamic columns
    select_columns = ["TIMESTAMP_BUCKET(timestamp, INTERVAL {} MILLISECOND) AS bucket".format(interval_time)]
    
    # Add AVG aggregation for each column
    for col in column_names:
        # Create aggregation string like "AVG(TB2_1A_ActualSpeed) AS avg_TB2_1A_ActualSpeed"
        agg_col = f"AVG({col}) AS avg_{col}"
        select_columns.append(agg_col)
    
    # Join all SELECT columns
    select_clause = ",\n  ".join(select_columns)
    
    # Step 3: Build the complete query
    query = f"""
SELECT
  {select_clause}
FROM
  `{project_id}`.`{dataset}`.`{table}`
GROUP BY
  bucket
ORDER BY bucket;
"""
    
    # Step 4: Execute the query
    try:
        bq_out = bq_client.query(query)
        out_df = bq_out.to_dataframe()
        return out_df
    except Exception as e:
        raise Exception(f"Error executing BigQuery: {str(e)}")


def get_data_from_bq_advanced(
    bq_client: bigquery.Client,
    column_names: List[str],
    project_id: str,
    dataset: str,
    table: str,
    interval_time: int = 100,
    aggregation_func: str = "AVG",
    timestamp_column: str = "timestamp",
    where_clause: Optional[str] = None,
    limit: Optional[int] = None
) -> pd.DataFrame:
    """
    Advanced version with more configuration options.
    
    Args:
        bq_client: Authenticated BigQuery client
        column_names: List of column names to query
        project_id: BigQuery project ID
        dataset: BigQuery dataset name
        table: BigQuery table name
        interval_time: Duration of interval in milliseconds
        aggregation_func: Aggregation function to use (AVG, SUM, MAX, MIN, etc.)
        timestamp_column: Name of the timestamp column
        where_clause: Optional WHERE clause (without WHERE keyword)
        limit: Optional LIMIT for number of rows
    
    Returns:
        pandas.DataFrame: Query results
    """
    
    if not column_names:
        raise ValueError("No column names provided")
    
    # Build SELECT clause
    select_columns = [f"TIMESTAMP_BUCKET({timestamp_column}, INTERVAL {interval_time} MILLISECOND) AS bucket"]
    
    for col in column_names:
        agg_col = f"{aggregation_func}({col}) AS {aggregation_func.lower()}_{col}"
        select_columns.append(agg_col)
    
    select_clause = ",\n  ".join(select_columns)
    
    # Build query components
    from_clause = f"`{project_id}`.`{dataset}`.`{table}`"
    group_by_clause = "bucket"
    order_by_clause = "bucket"
    
    # Build complete query
    query_parts = [
        f"SELECT\n  {select_clause}",
        f"FROM\n  {from_clause}"
    ]
    
    if where_clause:
        query_parts.append(f"WHERE\n  {where_clause}")
    
    query_parts.extend([
        f"GROUP BY\n  {group_by_clause}",
        f"ORDER BY {order_by_clause}"
    ])
    
    if limit:
        query_parts.append(f"LIMIT {limit}")
    
    query = "\n".join(query_parts) + ";"
    
    # Execute query
    try:
        bq_out = bq_client.query(query)
        out_df = bq_out.to_dataframe()
        return out_df
    except Exception as e:
        raise Exception(f"Error executing BigQuery: {str(e)}")


def validate_bq_connection(bq_client: bigquery.Client) -> bool:
    """
    Validate BigQuery client connection.
    
    Args:
        bq_client: BigQuery client to validate
    
    Returns:
        bool: True if connection is valid, False otherwise
    """
    try:
        # Simple query to test connection
        query = "SELECT 1 as test"
        result = bq_client.query(query)
        list(result)  # Force execution
        return True
    except Exception:
        return False


# Example usage and testing
if __name__ == "__main__":
    # This section would be used for testing with an actual BigQuery client
    """
    from google.cloud import bigquery
    
    # Initialize client (assumes authentication is set up)
    client = bigquery.Client()
    
    # Example usage
    df = get_data_from_bq(
        bq_client=client,
        input_column_names="TB2_1A_ActualSpeed TB2_1A_TailPos",
        project_id="your-project-id",
        dataset="your_dataset",
        table="your_table",
        interval_time=200
    )
    
    print(df.head())
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    """
    pass
