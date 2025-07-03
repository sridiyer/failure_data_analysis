"""
Module for connecting to and querying PostgreSQL databases.
"""

import logging
from typing import Dict, List, Optional, Any, Union

import pandas as pd
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import asyncpg
from asyncpg.pool import Pool
from datetime import datetime

logger = logging.getLogger(__name__)

class PostgresConnector:
    """
    Class for connecting to and querying a PostgreSQL database.
    Uses connection pooling for better performance.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize the PostgreSQL connector with configuration."""
        self.config = config
        self.pool: Optional[Pool] = None
        self._connection = None

    async def connect(self) -> None:
        """Establish connection to the PostgreSQL database."""
        try:
            self.pool = await asyncpg.create_pool(
                host=self.config["host"],
                port=self.config["port"],
                database=self.config["database"],
                user=self.config["user"],
                password=self.config["password"],
                min_size=5,
                max_size=20
            )
            logger.info("Successfully connected to PostgreSQL database")
        except Exception as e:
            logger.error(f"Failed to connect to PostgreSQL database: {str(e)}")
            raise

    async def disconnect(self) -> None:
        """Close the database connection pool."""
        if self.pool:
            await self.pool.close()
            logger.info("Closed PostgreSQL connection pool")

    def is_connected(self) -> bool:
        """Check if the database connection is active."""
        return self.pool is not None

    async def execute_query(
        self, 
        query: str, 
        params: Optional[Union[tuple, dict]] = None
    ) -> List[Dict[str, Any]]:
        """
        Execute a query and return results as a list of dictionaries.
        
        Args:
            query: SQL query string
            params: Query parameters (optional)
            
        Returns:
            List of dictionaries containing query results
        """
        if not self.pool:
            raise ConnectionError("Database connection not established")

        try:
            async with self.pool.acquire() as connection:
                if params:
                    result = await connection.fetch(query, *params)
                else:
                    result = await connection.fetch(query)
                
                return [dict(row) for row in result]
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            raise

    async def execute_transaction(self, queries: List[Dict[str, Any]]) -> None:
        """
        Execute multiple queries in a transaction.
        
        Args:
            queries: List of dictionaries containing queries and their parameters
                    [{"query": "SQL query", "params": (param1, param2)}]
        """
        if not self.pool:
            raise ConnectionError("Database connection not established")

        try:
            async with self.pool.acquire() as connection:
                async with connection.transaction():
                    for query_dict in queries:
                        query = query_dict["query"]
                        params = query_dict.get("params")
                        if params:
                            await connection.execute(query, *params)
                        else:
                            await connection.execute(query)
        except Exception as e:
            logger.error(f"Error executing transaction: {str(e)}")
            raise

    async def execute_batch(
        self, 
        query: str, 
        records: List[tuple]
    ) -> None:
        """
        Execute a batch insert/update operation.
        
        Args:
            query: SQL query string
            records: List of tuples containing values for each record
        """
        if not self.pool:
            raise ConnectionError("Database connection not established")

        try:
            async with self.pool.acquire() as connection:
                await connection.executemany(query, records)
        except Exception as e:
            logger.error(f"Error executing batch operation: {str(e)}")
            raise

    async def execute_query_to_df(self, query: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a pandas DataFrame.
        
        Args:
            query: SQL query to execute
            params: Query parameters
            
        Returns:
            DataFrame with query results
        """
        if not self.pool:
            raise ConnectionError("Database connection not established")

        try:
            async with self.pool.acquire() as connection:
                if params:
                    # Convert params dict to tuple for asyncpg
                    param_values = tuple(params.values())
                    result = await connection.fetch(query, *param_values)
                else:
                    result = await connection.fetch(query)
                
                # Convert asyncpg.Record objects to dictionaries
                records = [dict(row) for row in result]
                
                # Create DataFrame from list of dictionaries
                if records:
                    df = pd.DataFrame(records)
                    logger.info(f"Retrieved {len(df)} records")
                    return df
                else:
                    logger.info("No records found")
                    return pd.DataFrame()
                    
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            raise

    def fetch_failure_data(self) -> pd.DataFrame:
        """
        Fetch failure data from the database.
        
        Returns:
            DataFrame with failure data
        """
        query = """
        SELECT 
            failure_id,
            equipment_id,
            component_id,
            failure_type,
            severity,
            detection_timestamp,
            resolution_timestamp,
            maintenance_notes,
            equipment_type,
            installation_date,
            last_maintenance_date
        FROM failure_records
        JOIN equipment ON failure_records.equipment_id = equipment.id
        ORDER BY detection_timestamp DESC
        """
        
        logger.info("Fetching failure data from PostgreSQL")
        df = self.execute_query_to_df(query)
        logger.info(f"Retrieved {len(df)} failure records")
        return df
    
    def fetch_sensor_mappings(self) -> pd.DataFrame:
        """
        Fetch sensor to equipment mappings from the database.
        
        Returns:
            DataFrame with sensor mappings
        """
        query = """
        SELECT 
            sensor_id,
            equipment_id,
            component_id,
            sensor_type,
            installation_date,
            last_calibration_date,
            measurement_unit,
            normal_min_range,
            normal_max_range
        FROM sensors
        """
        
        logger.info("Fetching sensor mappings from PostgreSQL")
        df = self.execute_query_to_df(query)
        logger.info(f"Retrieved {len(df)} sensor mappings")
        return df
    
    def execute_batch_insert(self, table_name: str, data_list: List[Dict[str, Any]]) -> int:
        """
        Insert multiple rows into a table.
        
        Args:
            table_name: Name of the table
            data_list: List of dictionaries with data to insert
            
        Returns:
            Number of rows inserted
        """
        if not data_list:
            logger.warning("No data provided for batch insert")
            return 0
            
        # Get column names from the first dictionary
        columns = list(data_list[0].keys())
        placeholders = [f"%({col})s" for col in columns]
        
        query = f"""
        INSERT INTO {table_name} 
        ({', '.join(columns)}) 
        VALUES ({', '.join(placeholders)})
        """
        
        conn = None
        try:
            conn = self._get_connection()
            with conn.cursor() as cursor:
                cursor.executemany(query, data_list)
                inserted_rows = cursor.rowcount
                conn.commit()
                
                logger.info(f"Inserted {inserted_rows} rows into {table_name}")
                return inserted_rows
                
        except psycopg2.Error as e:
            logger.error(f"Database batch insert error: {str(e)}")
            if conn:
                conn.rollback()
            raise
            
        finally:
            if conn:
                self._return_connection(conn)