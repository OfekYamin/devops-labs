#!/usr/bin/env python3
"""
Azure Monitor Metrics and Alerts Automation Script

This script demonstrates how to interact with Azure Monitor to fetch metrics and create alerts
using the Azure SDK for Python. It shows how to query resource metrics and set up monitoring alerts.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import argparse
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import HttpResponseError

def get_clients():
    """
    Create Azure SDK clients for Monitor and Resource Management.
    
    TODO: Implement this function to:
    1. Get subscription ID from environment variables
    2. Create DefaultAzureCredential
    3. Create and return MonitorManagementClient and ResourceManagementClient
    
    Returns:
        tuple: (monitor_client, resource_client, subscription_id)
    """
    # TODO: Get subscription ID from environment variables
    
    # TODO: Create credential using DefaultAzureCredential
    
    # TODO: Create and return monitor and resource clients
    pass

def list_resources(resource_client, resource_group=None, resource_type=None):
    """
    List Azure resources that can be monitored.
    
    TODO: Implement this function to:
    1. List resources filtered by resource group and/or type
    2. Return the resources with their IDs
    
    Args:
        resource_client: Azure Resource Management client
        resource_group (str, optional): Resource group to filter by
        resource_type (str, optional): Resource type to filter by (e.g. "Microsoft.Compute/virtualMachines")
        
    Returns:
        list: Resources with their IDs and types
    """
    print(f"Listing resources in {'resource group ' + resource_group if resource_group else 'all resource groups'}")
    
    # TODO: List resources with optional filtering
    
    # TODO: Format and return resource details
    pass

def get_resource_metrics(monitor_client, resource_uri, metric_names, time_window_minutes=30):
    """
    Get metrics for a specific Azure resource.
    
    TODO: Implement this function to:
    1. Query metrics for the specified resource
    2. Handle the time window and interval
    3. Return the metrics data
    
    Args:
        monitor_client: Azure Monitor Management client
        resource_uri (str): The resource URI to get metrics for
        metric_names (list): List of metric names to retrieve
        time_window_minutes (int): Time window in minutes to look back
        
    Returns:
        dict: Metrics data organized by metric name
    """
    print(f"Getting metrics for resource: {resource_uri}")
    
    # TODO: Calculate time range (start_time to now)
    
    # TODO: Query metrics from Azure Monitor
    
    # TODO: Process and return the metrics data
    pass

def create_metric_alert(monitor_client, resource_group, alert_name, resource_uri, 
                        metric_name, operator, threshold, window_minutes=5):
    """
    Create a metric alert for a resource.
    
    TODO: Implement this function to:
    1. Define the alert criteria
    2. Create the alert rule
    3. Return the alert details
    
    Args:
        monitor_client: Azure Monitor Management client
        resource_group (str): Resource group name
        alert_name (str): Name for the alert rule
        resource_uri (str): The resource URI to monitor
        metric_name (str): Metric name to alert on
        operator (str): Comparison operator (e.g., "GreaterThan")
        threshold (float): Threshold value to trigger the alert
        window_minutes (int): Time window for the alert in minutes
        
    Returns:
        dict: Alert rule details
    """
    print(f"Creating metric alert '{alert_name}' in {resource_group}")
    
    # TODO: Define alert rule parameters
    
    # TODO: Create the alert rule
    
    # TODO: Return the alert rule details
    pass

def delete_metric_alert(monitor_client, resource_group, alert_name):
    """
    Delete a metric alert rule.
    
    TODO: Implement this function to:
    1. Delete the specified alert rule
    2. Handle errors if the alert doesn't exist
    
    Args:
        monitor_client: Azure Monitor Management client
        resource_group (str): Resource group name
        alert_name (str): Name of the alert rule to delete
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting metric alert '{alert_name}' from {resource_group}")
    
    # TODO: Delete the alert rule
    
    # TODO: Return success status
    pass

def plot_metrics(metrics_data, metric_name, resource_name):
    """
    Plot metrics data using matplotlib.
    
    TODO: Implement this function to:
    1. Extract timestamps and values from metrics data
    2. Create a time series plot
    3. Display or save the plot
    
    Args:
        metrics_data (dict): Metrics data from get_resource_metrics
        metric_name (str): The name of the metric to plot
        resource_name (str): The name of the resource (for the plot title)
    """
    print(f"Plotting {metric_name} metrics for {resource_name}")
    
    # TODO: Extract timestamps and values
    
    # TODO: Create the plot
    
    # TODO: Show or save the plot
    pass

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description='Azure Monitor Metrics and Alerts Tool')
    
    # Resource group and resource arguments
    parser.add_argument('--resource-group', help='Resource group name')
    parser.add_argument('--resource-type', help='Resource type (e.g. Microsoft.Compute/virtualMachines)')
    parser.add_argument('--resource-uri', help='Full resource URI')
    
    # Operations
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')
    
    # List resources operation
    list_parser = subparsers.add_parser('list-resources', help='List resources that can be monitored')
    
    # Get metrics operation
    metrics_parser = subparsers.add_parser('get-metrics', help='Get metrics for a resource')
    metrics_parser.add_argument('--metric', required=True, help='Metric name to retrieve')
    metrics_parser.add_argument('--time-window', type=int, default=30, help='Time window in minutes (default: 30)')
    metrics_parser.add_argument('--plot', action='store_true', help='Plot the metrics data')
    
    # Create alert operation
    alert_parser = subparsers.add_parser('create-alert', help='Create a metric alert')
    alert_parser.add_argument('--alert-name', required=True, help='Name for the alert')
    alert_parser.add_argument('--metric', required=True, help='Metric name to alert on')
    alert_parser.add_argument('--operator', default='GreaterThan', 
                             choices=['Equals', 'GreaterThan', 'GreaterThanOrEqual', 'LessThan', 'LessThanOrEqual'],
                             help='Comparison operator')
    alert_parser.add_argument('--threshold', type=float, required=True, help='Threshold value')
    alert_parser.add_argument('--window', type=int, default=5, help='Time window in minutes (default: 5)')
    
    # Delete alert operation
    delete_parser = subparsers.add_parser('delete-alert', help='Delete a metric alert')
    delete_parser.add_argument('--alert-name', required=True, help='Name of the alert to delete')
    
    args = parser.parse_args()
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    try:
        # TODO: Get Azure clients
        
        # TODO: Process the requested operation
        # 1. If args.operation == "list-resources": call list_resources()
        # 2. If args.operation == "get-metrics": call get_resource_metrics()
        # 3. If args.operation == "create-alert": call create_metric_alert()
        # 4. If args.operation == "delete-alert": call delete_metric_alert()
        
        pass
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 