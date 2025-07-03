"""
Test module for jin_iter1_analysis functionality.
This module demonstrates the usage of process_triage_data function.
"""

import asyncio
from datetime import datetime
from src.analysis.jin_iter1_analysis import process_triage_data, analyze_triage_data

async def test_process_triage_data():
    """
    Test the process_triage_data function with specific conditions.
    """
    # Define where conditions
    where_conditions = [
        {"source_name": "CAPA"},
        {"anomaly_date": "2024-03-16"}
    ]
    
    # Define update values
    update_values = {
        "anomaly_event_id": 522,
        "proc_flag": 1
    }
    
    try:
        # Process the data
        result = await process_triage_data(where_conditions, update_values)
        
        # Print results
        print("\nProcessing Results:")
        print("-" * 50)
        print(f"Status: {result['status']}")
        print(f"Message: {result['message']}")
        
        if result['data'] is not None:
            print("\nData Summary:")
            print(f"Number of records: {len(result['data'])}")
            print("\nFirst few records:")
            print(result['data'].head())
        
        print(f"\nNumber of records updated: {result['updated_count']}")
        print("-" * 50)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

async def main():
    """
    Main function to run the analysis.
    """
    print("Starting analysis of triage data...")
    
    # Define where conditions
    where_conditions = [
        {
            "source_name": "CAPA",
            "anomaly_date": "2024-03-16"
        }
    ]
    
    try:
        # Analyze the data
        df = await analyze_triage_data(where_conditions)
        
        # Print results
        print("\nAnalysis Results:")
        print("-" * 50)
        print(f"Number of records found: {len(df)}")
        
        if not df.empty:
            print("\nFirst few records:")
            print(df.head())
            
            # Print column names
            print("\nAvailable columns:")
            print(df.columns.tolist())
            
            # Print basic statistics
            print("\nBasic statistics:")
            print(df.describe())
        
        print("-" * 50)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 