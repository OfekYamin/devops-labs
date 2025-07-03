#!/usr/bin/env python3
"""
GCP LAB05 - Cloud Monitoring Metrics Script
This script fetches and displays metrics from Google Cloud Monitoring.
"""

import os
import argparse
import time
from datetime import datetime, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
from google.cloud import monitoring_v3
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# Common metric types for different GCP services
METRIC_TYPES = {
    'cpu': 'compute.googleapis.com/instance/cpu/utilization',
    'memory': 'agent.googleapis.com/memory/percent_used',
    'disk': 'compute.googleapis.com/instance/disk/read_bytes_count',
    'network': 'compute.googleapis.com/instance/network/received_bytes_count',
    'uptime': 'compute.googleapis.com/instance/uptime',
    'gce_instance_count': 'compute.googleapis.com/instance/reserved_cores',
    'http_requests': 'loadbalancing.googleapis.com/https/request_count',
    'database_connections': 'cloudsql.googleapis.com/database/network/connections'
}

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Fetch metrics from Google Cloud Monitoring'
    )
    parser.add_argument(
        '--project',
        help='GCP Project ID',
        default=os.environ.get('GCP_PROJECT_ID')
    )
    parser.add_argument(
        '--metric',
        help='Metric type to fetch (see --list-metrics for available metrics)',
        default='cpu'
    )
    parser.add_argument(
        '--custom-metric',
        help='Custom metric type (e.g. "compute.googleapis.com/instance/cpu/utilization")',
        default=None
    )
    parser.add_argument(
        '--window',
        help='Time window in minutes to fetch metrics for',
        type=int,
        default=10
    )
    parser.add_argument(
        '--list-metrics',
        action='store_true',
        help='List available metric types'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Plot the metrics data using matplotlib'
    )
    
    return parser.parse_args()

def list_available_metrics(project_id):
    """
    List available metric types for the project.
    
    Args:
        project_id (str): GCP Project ID
    """
    print("Available predefined metrics:")
    for name, metric_type in METRIC_TYPES.items():
        print(f"  --metric={name} : {metric_type}")
    
    print("\nTo use a custom metric, use --custom-metric with the full metric type.")
    print("To discover all available metrics in your project, run:")
    print(f"  gcloud monitoring metrics list --project={project_id}")

def create_time_interval(minutes):
    """
    Create a time interval for the past X minutes.
    
    Args:
        minutes (int): Minutes in the past to start the interval
        
    Returns:
        monitoring_v3.TimeInterval: The time interval object
    """
    # TODO: Create a TimeInterval object
    # - Set end_time to the current timestamp (in seconds)
    # - Set start_time to X minutes in the past
    
    pass

def fetch_metric_data(project_id, metric_type, time_interval):
    """
    Fetch metric data from Cloud Monitoring.
    
    Args:
        project_id (str): GCP Project ID
        metric_type (str): The metric type to fetch
        time_interval (monitoring_v3.TimeInterval): Time interval to fetch metrics for
        
    Returns:
        list: The time series results
    """
    print(f"Fetching {metric_type} metrics for project {project_id}...")
    
    # TODO: Initialize the Cloud Monitoring API client
    
    # Format the project name
    project_name = f"projects/{project_id}"
    
    # TODO: Create the request to list time series
    # - Set the name (project_name)
    # - Set the filter using the metric_type
    # - Set the interval
    # - Set the view to FULL
    
    # TODO: Execute the request and return the results
    pass

def display_metric_data(results, metric_type):
    """
    Display metric data in a readable format.
    
    Args:
        results: The time series results from the API
        metric_type (str): The metric type that was fetched
    """
    print(f"\nMetric: {metric_type}")
    
    # TODO: Check if any results were returned
    
    # TODO: Format the results in a table
    # - Extract resource labels (e.g., instance_id, zone)
    # - Extract metric values and timestamps
    # - Display in a tabular format using tabulate
    
    # TODO: Display summary statistics (min, max, avg)
    
    pass

def plot_metric_data(results, metric_type, window_minutes):
    """
    Plot metric data using matplotlib.
    
    Args:
        results: The time series results from the API
        metric_type (str): The metric type that was fetched
        window_minutes (int): The time window in minutes
    """
    # TODO: Check if any results were returned
    
    # TODO: Create a plot with matplotlib
    # - Extract timestamps and values for each time series
    # - Create a line plot
    # - Add labels and a title
    # - Show the plot
    
    pass

def main():
    """Main function to fetch and display metrics."""
    args = parse_arguments()
    
    # Verify we have the project ID
    if not args.project:
        print("Error: GCP Project ID is required. Provide it with --project flag or set GCP_PROJECT_ID environment variable.")
        return 1
    
    # List available metrics if requested
    if args.list_metrics:
        list_available_metrics(args.project)
        return 0
    
    # Determine which metric type to use
    if args.custom_metric:
        metric_type = args.custom_metric
    else:
        if args.metric not in METRIC_TYPES:
            print(f"Error: Unknown metric type '{args.metric}'. Use --list-metrics to see available metrics.")
            return 1
        metric_type = METRIC_TYPES[args.metric]
    
    try:
        # Create the time interval
        time_interval = create_time_interval(args.window)
        
        # Fetch the metric data
        results = fetch_metric_data(args.project, metric_type, time_interval)
        
        # Display the data
        display_metric_data(results, metric_type)
        
        # Plot the data if requested
        if args.plot:
            plot_metric_data(results, metric_type, args.window)
        
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 