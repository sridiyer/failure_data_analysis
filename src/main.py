#!/usr/bin/env python3
"""
Main entry point for the failure analysis system.
Orchestrates the full analysis pipeline from data loading to insights storage.
"""

import logging
import argparse
from pathlib import Path

from src.utils.config_loader import load_config
from src.utils.logger import setup_logger
from src.data.csv_reader import load_csv_data
from src.data.postgres_connector import PostgresConnector
from src.data.bigquery_connector import BigQueryConnector
from src.analysis.initial_analysis import perform_initial_analysis
from src.analysis.time_series_analysis import analyze_time_series
from src.llm.gemini_connector import GeminiLLM
from src.database.output_connector import OutputDatabaseConnector

logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Failure Analysis System")
    parser.add_argument("--config", type=str, default="config/config.yaml",
                        help="Path to configuration file")
    parser.add_argument("--credentials", type=str, default="config/credentials.yaml",
                        help="Path to credentials file")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    return parser.parse_args()

def main():
    """Main execution function."""
    # Parse command line arguments and load configuration
    args = parse_args()
    config = load_config(args.config, args.credentials)
    setup_logger(debug=args.debug)
    
    logger.info("Starting failure analysis pipeline")
    
    try:
        # Step 1: Load data from CSV
        logger.info("Loading CSV data")
        csv_path = Path(config["paths"]["csv_data"])
        failure_df = load_csv_data(csv_path)
        
        # Step 2: Connect to input PostgreSQL database
        logger.info("Connecting to input PostgreSQL database")
        input_pg_config = config["databases"]["input_postgres"]
        input_pg = PostgresConnector(
            host=input_pg_config["host"],
            port=input_pg_config["port"],
            database=input_pg_config["database"],
            user=input_pg_config["user"],
            password=input_pg_config["password"]
        )
        
        # Step 3: Get additional failure data from PostgreSQL
        logger.info("Fetching additional failure data")
        additional_failure_data = input_pg.fetch_failure_data()
        
        # Step 4: Merge data sources
        merged_data = failure_df.merge(additional_failure_data, on="failure_id", how="left")
        
        # Step 5: Connect to output PostgreSQL database
        logger.info("Connecting to output PostgreSQL database")
        output_pg_config = config["databases"]["output_postgres"]
        output_db = OutputDatabaseConnector(
            host=output_pg_config["host"],
            port=output_pg_config["port"],
            database=output_pg_config["database"],
            user=output_pg_config["user"],
            password=output_pg_config["password"]
        )
        
        # Step 6: Initialize LLM
        logger.info("Initializing Gemini LLM")
        llm_config = config["llm"]["gemini"]
        llm = GeminiLLM(
            api_key=llm_config["api_key"],
            model=llm_config["model"],
            max_tokens=llm_config["max_tokens"],
            temperature=llm_config["temperature"]
        )
        
        # Step 7: Perform initial analysis with LLM
        logger.info("Performing initial analysis")
        initial_analysis_results = perform_initial_analysis(merged_data, llm)
        
        # Step 8: Save initial analysis to output database
        logger.info("Saving initial analysis results")
        output_db.save_initial_analysis(initial_analysis_results)
        
        # Step 9: Get list of sensors for time-series analysis
        sensors = initial_analysis_results["identified_sensors"]
        
        # Step 10: Connect to BigQuery
        logger.info("Connecting to BigQuery")
        bq_config = config["databases"]["bigquery"]
        bq = BigQueryConnector(
            project_id=bq_config["project_id"],
            dataset=bq_config["dataset"],
            credentials_path=bq_config["credentials_path"]
        )
        
        # Step 11: Get time series data for each failure
        analysis_results = []
        for iteration in range(3):  # Default to max 3 iterations
            logger.info(f"Starting analysis iteration {iteration+1}")
            
            # Get time series data from BigQuery
            time_window = config["analysis"]["time_window"]
            time_series_data = bq.get_sensor_data(
                sensors=sensors,
                failure_times=initial_analysis_results["failure_times"],
                pre_failure_window=time_window["pre_failure"],
                post_failure_window=time_window["post_failure"]
            )
            
            # Analyze time series data
            ts_analysis_config = config["analysis"]["time_series"]
            analysis_result = analyze_time_series(
                time_series_data, 
                config["analysis"]["anomaly_detection"]
            )
            
            # Send analysis results to LLM for interpretation
            llm_interpretation = llm.analyze_time_series_results(analysis_result)
            
            # Save iteration results
            iteration_result = {
                "iteration": iteration + 1,
                "analysis_result": analysis_result,
                "llm_interpretation": llm_interpretation
            }
            analysis_results.append(iteration_result)
            
            # Save to output database
            output_db.save_analysis_iteration(iteration_result)
            
            # Check if further iterations are needed based on LLM response
            if not llm_interpretation.get("continue_analysis", False):
                logger.info(f"LLM suggests stopping after iteration {iteration+1}")
                break
                
            # Update sensors list for next iteration if needed
            sensors = llm_interpretation.get("additional_sensors", sensors)
        
        logger.info("Analysis pipeline completed successfully")
        
    except Exception as e:
        logger.error(f"Analysis pipeline failed: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()