import pytest
import asyncio
from typing import AsyncGenerator, Any
from datetime import datetime
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

import sys

sys.path.append(str(Path(__file__).parent.parent))

from src.data.postgres_connector import PostgresConnector
# Load environment variables
load_dotenv()

def load_config() -> dict:
    """Load configuration from YAML file."""
    print(Path(__file__).parent.parent)
    config_path = Path(__file__).parent.parent / "src" / "config" / "config.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

# Load database configuration from config file
config = load_config()
TEST_DB_CONFIG = config["databases"]["input_postgres"]
print("Database Configuration:")
print("-" * 80)
for key, value in TEST_DB_CONFIG.items():
    print(f"{key}: {value}")
print("-" * 80)

test_connector = PostgresConnector(TEST_DB_CONFIG)

async def main():
    global test_connector
    
    # First, ensure we're disconnected and pool is closed
    print("\nClosing existing connections and pool...")
    await test_connector.disconnect()
    print("Existing connections closed")
    
    # Wait a moment to ensure connections are fully closed
    await asyncio.sleep(1)
    
    print("\nAttempting to connect to database...")
    connection_result = await test_connector.connect()
    print(f"Connection result: {connection_result}")
    print(f"Connection status: {test_connector.is_connected()}")
    
    if test_connector.is_connected():
        print("Connected to database")
        
        # Execute the query
        query = """
        SELECT sr, section, last_occurrence_date, date, datetime_from, datetime_to, delay_minutes, equipment, problem_description, restart_steps, one_year, two_year, three_year, four_year, five_year, corrective_action, preventive_action, responsibility, target_date, status, actual_action_taken
        FROM public."CAPA_2023_2024" WHERE date = '2024-05-21 00:00:00';
        """
        
        try:
            results = await test_connector.execute_query(query)
            print("\nQuery Results:")
            print("-" * 80)
            for row in results:
                print(f"SR: {row.get('sr')}")
                print(f"Section: {row.get('section')}")
                print(f"Equipment: {row.get('equipment')}")
                print(f"Problem Description: {row.get('problem_description')}")
                print(f"Status: {row.get('status')}")
                print("-" * 80)
            
            print(f"\nTotal records found: {len(results)}")
            
        except Exception as e:
            print(f"Error executing query: {str(e)}")
        finally:
            print("\nClosing connection and pool...")
            await test_connector.disconnect()
            print("Disconnected from database")
    else:
        print("Failed to connect to database")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())


