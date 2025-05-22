import asyncio
import sys
from pathlib import Path
import yaml
from dotenv import load_dotenv

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from src.data.big_query_connector import BigQueryConnector

def load_config() -> dict:
    """Load configuration from YAML file."""
    config_path = Path(__file__).parent.parent / "src" / "config" / "config.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

async def main():
    # Load configuration
    config = load_config()
    bigquery_config = config["databases"]["bigquery"]
    

    # Initialize BigQuery connector
    print("\nInitializing BigQuery connector...")
    credentials_path = Path(__file__).parent.parent / "src" / "config" / bigquery_config["credentials_file"]
    connector = BigQueryConnector(
        project_id=bigquery_config["project_id"],
        dataset=bigquery_config["dataset"],
        table=bigquery_config["table"],
        credentials_path=credentials_path
    )
    
    # Test connection by executing a simple query
    print("\nTesting connection with a simple query...")
    try:
        # Simple query to test connection
        query = f"""
        SELECT COUNT(*) as count
        FROM `{bigquery_config['project_id']}.{bigquery_config['dataset']}.{bigquery_config['table']}`
        LIMIT 1
        """
        
        # Execute query
        query_job = connector.client.query(query)
        results = query_job.result()
        
        # Print results
        for row in results:
            print(f"\nQuery successful! Found {row.count} rows in the table.")
            print("Connection test passed!")
            
    except Exception as e:
        print(f"\nError testing connection: {str(e)}")
        print("Connection test failed!")

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Run the async main function
    asyncio.run(main()) 