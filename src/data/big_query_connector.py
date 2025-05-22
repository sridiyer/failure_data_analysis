"""
Module for connecting to and querying Google BigQuery for IoT sensor data.
"""

import logging
from typing import Dict, List, Any, Union, Optional
from pathlib import Path
from datetime import datetime, timedelta
import re

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

logger = logging.getLogger(__name__)

class BigQueryConnector:
    """
    Class to connect to and query Google BigQuery for sensor data.
    """
    
    def __init__(
        self,
        project_id: str = "sp-prod-mlops",
        dataset: str = "jindal_raw_data",
        table: str = "tb_twc_data",
        credentials_path: Optional[str] = "config/bigquery_service_account.json"
    ):
        """
        Initialize the BigQuery connector.
        
        Args:
            project_id: Google Cloud project ID
            dataset: BigQuery dataset ID
            credentials_path: Path to the service account credentials JSON file
        """
        self.project_id = project_id
        self.dataset = dataset
        self.table = table
        logger.info(f"Initializing BigQuery connector for {dataset} in {project_id}")
       
        try:
            # Set up credentials and client
            print (credentials_path)
            if credentials_path:
                credentials = service_account.Credentials.from_service_account_file(
                    credentials_path,
                    scopes=["https://www.googleapis.com/auth/bigquery"]
                )
                self.client = bigquery.Client(
                    project=project_id,
                    credentials=credentials
                )
            else:
                # Use application default credentials
                self.client = bigquery.Client(project=project_id)
                
            logger.info("BigQuery client initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize BigQuery client: {str(e)}")
            raise
    
    def parse_time_window(self, time_window: str) -> timedelta:
        """
        Parse a time window string (e.g., '24h', '30m') into a timedelta object.
        
        Args:
            time_window: String representing time window (e.g., '24h', '30m')
            
        Returns:
            timedelta object
        """
        pattern = r'(\d+)([hms])'
        match = re.match(pattern, time_window)
        
        if not match:
            raise ValueError(f"Invalid time window format: {time_window}. Expected format like '24h', '30m', '60s'")
            
        value, unit = match.groups()
        value = int(value)
        
        if unit == 'h':
            return timedelta(hours=value)
        elif unit == 'm':
            return timedelta(minutes=value)
        elif unit == 's':
            return timedelta(seconds=value)
        else:
            raise ValueError(f"Invalid time unit: {unit}")
    
    def get_sensor_data(
        self,
        sensors: List[str],
        failure_times: Dict[str, datetime],
        pre_failure_window: str = "24h",
        post_failure_window: str = "2h"
    ) -> pd.DataFrame:
        """
        Get time series data for specified sensors around failure times.
        
        Args:
            sensors: List of sensor IDs
            failure_times: Dict mapping failure IDs to failure timestamps
            pre_failure_window: Time window before failure (format: '24h', '30m', etc.)
            post_failure_window: Time window after failure (format: '2h', '15m', etc.)
            
        Returns:
            DataFrame with sensor time series data
        """
        # Parse time windows
        pre_window = self.parse_time_window(pre_failure_window)
        post_window = self.parse_time_window(post_failure_window)
        
        logger.info(f"Fetching sensor data for {len(sensors)} sensors around {len(failure_times)} failure events")
        
        # Format sensors list for SQL query
        sensors_str = ', '.join([f"'{s}'" for s in sensors])
        
        all_data = []
        
        # Query data for each failure event
        for failure_id, failure_time in failure_times.items():
            start_time = failure_time - pre_window
            end_time = failure_time + post_window
            
            # Format timestamps for BigQuery
            start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
            end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
            
            query = f"""
            SELECT
                sensor_id,
                timestamp,
                value,
                quality,
                '{failure_id}' AS failure_id,
                TIMESTAMP_DIFF(timestamp, TIMESTAMP('{failure_time.strftime('%Y-%m-%d %H:%M:%S')}'), SECOND) AS seconds_from_failure
            FROM
                `{self.project_id}.{self.dataset}.{self.table}`
            WHERE
                sensor_id IN ({sensors_str})
                AND timestamp BETWEEN TIMESTAMP('{start_time_str}') AND TIMESTAMP('{end_time_str}')
            ORDER BY
                sensor_id, timestamp
            """
            
            logger.debug(f"Executing BigQuery for failure {failure_id}")
            
            try:
                # Execute query
                query_job = self.client.query(query)
                results = query_job.result()
                
                # Convert to DataFrame
                df = results.to_dataframe()
                
                if not df.empty:
                    all_data.append(df)
                    logger.debug(f"Retrieved {len(df)} data points for failure {failure_id}")
                else:
                    logger.warning(f"No data found for failure {failure_id}")
                    
            except Exception as e:
                logger.error(f"Error querying BigQuery for failure {failure_id}: {str(e)}")
                continue
                
        # Combine all results
        if all_data:
            combined_df = pd.concat(all_data, ignore_index=True)
            logger.info(f"Retrieved total of {len(combined_df)} sensor readings")
            return combined_df
        else:
            logger.warning("No sensor data retrieved")
            return pd.DataFrame()
            
    def get_sensor_metadata(self, sensors: List[str]) -> pd.DataFrame:
        """
        Get metadata for the specified sensors.
        
        Args:
            sensors: List of sensor IDs
            
        Returns:
            DataFrame with sensor metadata
        """
        # Format sensors list for SQL query
        sensors_str = ', '.join([f"'{s}'" for s in sensors])
        
        query = f"""
        SELECT
            sensor_id,
            equipment_id,
            sensor_type,
            unit,
            min_normal_range,
            max_normal_range,
            calibration_date,
            installation_date,
            location_x,
            location_y,
            location_z
        FROM
            `{self.project_id}.{self.dataset}.sensor_metadata`
        WHERE
            sensor_id IN ({sensors_str})
        """
        
        logger.info(f"Fetching metadata for {len(sensors)} sensors")
        
        try:
            # Execute query
            query_job = self.client.query(query)
            results = query_job.result()
            
            # Convert to DataFrame
            df = results.to_dataframe()
            
            logger.info(f"Retrieved metadata for {len(df)} sensors")
            return df
            
        except Exception as e:
            logger.error(f"Error querying sensor metadata: {str(e)}")
            return pd.DataFrame()