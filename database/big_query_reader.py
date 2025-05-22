# Python module to read data from BigQuery

from .big_query_connector import BigQueryConnector
from datetime import datetime, timezone 

# Define a placeholder for the table name and dataset/project details
DEFAULT_PROJECT_ID = "your-gcp-project-id" 
DEFAULT_DATASET_ID = "your_dataset_id"
# This table_id would be the actual table name, e.g., 'my_sensor_data_table'
DEFAULT_TABLE_ID = "your_table_id" 

class BigQueryReader:
    def __init__(self, project_id: str = DEFAULT_PROJECT_ID, dataset_id: str = DEFAULT_DATASET_ID, table_id: str = DEFAULT_TABLE_ID):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.connector = BigQueryConnector(project_id=self.project_id, dataset_id=self.dataset_id)
        self.table_name = f"`{self.project_id}.{self.dataset_id}.{table_id}`"
        print(f"BigQueryReader: Initialized for table {self.table_name}")

    def set_table(self, table_id: str):
        '''Allows setting a specific table if different from default'''
        self.table_name = f"`{self.project_id}.{self.dataset_id}.{table_id}`"
        print(f"BigQueryReader: Target table set to {self.table_name}")

    def read_data(self, 
                  column_names: list[str], 
                  start_timestamp: datetime, 
                  end_timestamp: datetime,
                  aggregate_100ms: bool = True):
        """
        Reads data from BigQuery, with an option to aggregate to 100ms intervals.

        Args:
            column_names: A list of column names to select. 
                          The first column in this list MUST be the timestamp column.
                          Subsequent columns are treated as values to be potentially averaged
                          if they are numeric, or selected with ANY_VALUE if they are not,
                          during aggregation.
            start_timestamp: The start of the time range (inclusive).
            end_timestamp: The end of the time range (exclusive).
            aggregate_100ms: If True, attempts to aggregate data to 100ms intervals.
                             If False, raw 5ms data will be fetched.

        Returns:
            A list of dictionaries, where each dictionary represents a row of data,
            or None if an error occurs.
        """
        if not column_names or not isinstance(column_names, list) or len(column_names) == 0:
            print("BigQueryReader: Error - No column names provided.")
            return None
        
        # Ensure timestamps are timezone-aware (UTC is typical for BQ)
        if start_timestamp.tzinfo is None:
            start_timestamp = start_timestamp.replace(tzinfo=timezone.utc)
        if end_timestamp.tzinfo is None:
            end_timestamp = end_timestamp.replace(tzinfo=timezone.utc)

        if not self.connector.connect(): # This is a simulated connection
            print("BigQueryReader: Error - Could not establish connection (simulated).")
            return None

        try:
            query = self._build_query(column_names, start_timestamp, end_timestamp, aggregate_100ms)
            print(f"BigQueryReader: Constructed query:\n{query}")

            results = self.connector.execute_query(query)

        except ValueError as ve:
            print(f"BigQueryReader: Error building query: {ve}")
            return None
        except Exception as e:
            print(f"BigQueryReader: An unexpected error occurred: {e}")
            return None
        finally:
            self.connector.disconnect() # Simulated disconnect

        if results is None:
            print("BigQueryReader: Query execution failed or returned no results (simulated).")
            return None
        
        return results

    def _build_query(self, 
                     column_names: list[str], 
                     start_timestamp: datetime, 
                     end_timestamp: datetime, 
                     aggregate_100ms: bool) -> str:
        """
        Constructs the BigQuery SQL query.
        Assumes the first column in column_names is the timestamp column.
        Other columns are value columns. During aggregation, numeric value columns
        are averaged. Non-numeric value columns are selected using ANY_VALUE.
        """
        if not column_names or not isinstance(column_names, list) or len(column_names) < 1:
            raise ValueError("column_names must be a list with at least the timestamp column.")

        timestamp_col = column_names[0]
        value_cols = column_names[1:]

        start_ts_str = start_timestamp.isoformat() 
        end_ts_str = end_timestamp.isoformat()

        select_expressions = []

        if aggregate_100ms:
            aggregated_ts_alias = "aggregated_timestamp"
            select_expressions.append(
                f"TIMESTAMP_ADD(TIMESTAMP_BUCKET({timestamp_col}, INTERVAL 100 MILLISECOND), INTERVAL 50 MILLISECOND) AS {aggregated_ts_alias}"
            )
            
            for val_col in value_cols:
                # Heuristic to determine if a column is likely non-numeric
                # In a real-world scenario, this might come from schema introspection
                # or more explicit column type information.
                if 'id' in val_col.lower() or \
                   'name' in val_col.lower() or \
                   'string' in val_col.lower() or \
                   'code' in val_col.lower() or \
                   'type' in val_col.lower() or \
                   'category' in val_col.lower() or \
                   'description' in val_col.lower():
                    select_expressions.append(f"ANY_VALUE({val_col}) AS {val_col}")
                else: # Assume numeric and average it
                    select_expressions.append(f"AVG({val_col}) AS avg_{val_col}")
            
            group_by_clause = f"GROUP BY 1" # Group by the aggregated_timestamp alias
            order_by_clause = f"ORDER BY {aggregated_ts_alias}"
            
        else: # No aggregation
            select_expressions.append(timestamp_col)
            select_expressions.extend(value_cols) # Select all provided value columns as is
            group_by_clause = "" 
            order_by_clause = f"ORDER BY {timestamp_col}"

        select_clause = "SELECT " + ", ".join(select_expressions)
        
        # Note: The f-string interpolation for table_name, timestamp_col, and value_cols is safe
        # as these are derived from developer-controlled inputs (column_names list, class attributes).
        # start_ts_str and end_ts_str are also safe as they are ISO formatted dates.
        # In a scenario where any part of this query structure could come from direct external
        # input without sanitization, SQL injection would be a risk.
        # BigQuery client libraries typically offer parameterization for values, not identifiers.
        query = f"""
{select_clause}
FROM {self.table_name}
WHERE {timestamp_col} >= TIMESTAMP('{start_ts_str}') 
  AND {timestamp_col} < TIMESTAMP('{end_ts_str}')
{group_by_clause}
{order_by_clause};"""
        return query.strip()


if __name__ == '__main__':
    print("Running BigQueryReader example...")
    
    # Example: Initialize reader with specific project, dataset, and table
    reader = BigQueryReader(project_id="my-gcp-project", 
                            dataset_id="my_sensor_data", 
                            table_id="raw_events")

    # Define columns to fetch: timestamp column first, then value columns
    cols_to_fetch = ["event_timestamp", "temperature", "humidity", "sensor_id", "status_code"]
    
    # Define time range (ensure timezone-aware datetimes, UTC is common for BQ)
    start_dt = datetime(2023, 11, 1, 10, 0, 0, tzinfo=timezone.utc)
    end_dt = datetime(2023, 11, 1, 10, 5, 0, tzinfo=timezone.utc)

    print(f"\nFetching aggregated data for columns: {cols_to_fetch} from {reader.table_name}")
    # Call read_data with aggregate_100ms=True
    aggregated_data = reader.read_data(cols_to_fetch, start_dt, end_dt, aggregate_100ms=True)
    if aggregated_data:
        print(f"Received {len(aggregated_data)} aggregated_data rows (simulated).")
        # Print the first few rows as an example
        for i, row in enumerate(aggregated_data[:2]): # Print first 2 rows
            print(f"Row {i}: {row}")
    else:
        print("No aggregated data returned or an error occurred.")

    print(f"\nFetching raw data (5ms resolution) for columns: {cols_to_fetch} from {reader.table_name}")
    # Call read_data with aggregate_100ms=False
    raw_data = reader.read_data(cols_to_fetch, start_dt, end_dt, aggregate_100ms=False)
    if raw_data:
        print(f"Received {len(raw_data)} raw_data rows (simulated).")
        for i, row in enumerate(raw_data[:2]): # Print first 2 rows
            print(f"Row {i}: {row}")
    else:
        print("No raw data returned or an error occurred.")

    # Example of changing the table and fetching data
    reader.set_table("another_sensor_feed") # Change to a different table
    cols_to_fetch_2 = ["capture_time", "voltage", "event_type"]
    start_dt_2 = datetime(2023, 11, 2, 0, 0, 0, tzinfo=timezone.utc)
    end_dt_2 = datetime(2023, 11, 2, 0, 1, 0, tzinfo=timezone.utc) # 1 minute of data
    
    print(f"\nFetching aggregated data for columns: {cols_to_fetch_2} from {reader.table_name}")
    agg_data_2 = reader.read_data(cols_to_fetch_2, start_dt_2, end_dt_2, aggregate_100ms=True)
    if agg_data_2:
        print(f"Received {len(agg_data_2)} rows (simulated). First row: {agg_data_2[0] if agg_data_2 else 'N/A'}")
    else:
        print("No aggregated data returned for the second call or an error occurred.")

    # Example: Test with only timestamp column (should still work)
    cols_just_timestamp = ["event_timestamp"]
    print(f"\nFetching aggregated data for only timestamp column: {cols_just_timestamp} from {reader.table_name}")
    timestamp_only_data = reader.read_data(cols_just_timestamp, start_dt, end_dt, aggregate_100ms=True)
    if timestamp_only_data:
        print(f"Received {len(timestamp_only_data)} timestamp_only_data rows (simulated).")
        for i, row in enumerate(timestamp_only_data[:2]):
            print(f"Row {i}: {row}")
    else:
        print("No timestamp-only data returned or an error occurred.")

    # Example: Test with no columns (should be handled gracefully)
    print(f"\nFetching data with no columns specified:")
    no_cols_data = reader.read_data([], start_dt, end_dt)
    if no_cols_data is None:
        print("Correctly handled: No data returned as no columns were specified.")
    else:
        print(f"Unexpectedly received data when no columns were specified: {no_cols_data}")
