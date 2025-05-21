import pytest
import asyncio
from typing import AsyncGenerator
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test database configuration
TEST_DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "database": os.getenv("POSTGRES_DB", "test_db"),
    "user": os.getenv("POSTGRES_USER", "test_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "test_password")
}

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def db_connection():
    """Create a database connection for testing."""
    from src.data.postgres_connector import PostgresConnector
    
    connector = PostgresConnector(TEST_DB_CONFIG)
    await connector.connect()
    yield connector
    await connector.disconnect()

@pytest.mark.asyncio
async def test_connection(db_connection):
    """Test if we can establish a connection to the database."""
    assert db_connection.is_connected() is True

@pytest.mark.asyncio
async def test_read_failure_data(db_connection):
    """Test reading failure data from the database."""
    query = """
    SELECT * FROM failure_data 
    WHERE timestamp >= NOW() - INTERVAL '1 day'
    LIMIT 10
    """
    result = await db_connection.execute_query(query)
    assert isinstance(result, list)
    if result:
        assert all(isinstance(row, dict) for row in result)

@pytest.mark.asyncio
async def test_read_sensor_data(db_connection):
    """Test reading sensor data from the database."""
    query = """
    SELECT * FROM sensor_data 
    WHERE timestamp >= NOW() - INTERVAL '1 hour'
    LIMIT 100
    """
    result = await db_connection.execute_query(query)
    assert isinstance(result, list)
    if result:
        assert all(isinstance(row, dict) for row in result)

@pytest.mark.asyncio
async def test_read_with_parameters(db_connection):
    """Test reading data with parameterized query."""
    query = """
    SELECT * FROM failure_data 
    WHERE machine_id = $1 
    AND timestamp >= $2
    LIMIT 5
    """
    params = ("MACHINE_001", datetime.now().isoformat())
    result = await db_connection.execute_query(query, params)
    assert isinstance(result, list)

@pytest.mark.asyncio
async def test_error_handling(db_connection):
    """Test error handling for invalid queries."""
    with pytest.raises(Exception):
        await db_connection.execute_query("SELECT * FROM non_existent_table")

@pytest.mark.asyncio
async def test_connection_pool(db_connection):
    """Test connection pool functionality."""
    # Execute multiple queries concurrently
    queries = [
        "SELECT COUNT(*) FROM failure_data",
        "SELECT COUNT(*) FROM sensor_data",
        "SELECT COUNT(*) FROM machine_data"
    ]
    
    tasks = [db_connection.execute_query(query) for query in queries]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    assert all(not isinstance(result, Exception) for result in results) 