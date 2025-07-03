#!/usr/bin/env python3
"""
AWS LAB04 - CloudWatch Metrics and Alerts

This script demonstrates how to use boto3 to monitor EC2 instances using CloudWatch,
retrieve metrics, and set up alarms based on resource utilization thresholds.

Usage:
    python monitor.py [--instance-id <id>] [--region <region>] [--create-alarm] [--list-alarms] [--delete-alarm <name>]
"""

import boto3
import argparse
import sys
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

# Default configuration
DEFAULT_REGION = 'eu-west-1'
DEFAULT_ALARM_NAME = 'HighCPUAlert'
DEFAULT_THRESHOLD = 70.0
DEFAULT_EVALUATION_PERIODS = 2
DEFAULT_PERIOD = 300  # 5 minutes in seconds

def get_cpu_metrics(instance_id, period=300, start_time=None, end_time=None, region=DEFAULT_REGION):
    """
    Retrieve CPU utilization metrics for an EC2 instance
    
    Args:
        instance_id (str): EC2 instance ID
        period (int): Time period in seconds for each datapoint
        start_time (datetime): Starting time for metrics query
        end_time (datetime): Ending time for metrics query
        region (str): AWS region name
        
    Returns:
        list: List of datapoints with timestamp and CPU utilization
    """
    try:
        # TODO: Initialize CloudWatch client with the specified region
        
        # TODO: Set default time range if not provided
        # If start_time is None, set it to 1 hour ago
        # If end_time is None, set it to current time
        
        # TODO: Get metrics using get_metric_statistics method
        # Parameters:
        # - Namespace: 'AWS/EC2'
        # - MetricName: 'CPUUtilization'
        # - Dimensions: instance_id
        # - StartTime: start_time
        # - EndTime: end_time
        # - Period: period
        # - Statistics: ['Average']
        
        # TODO: Extract and sort datapoints by timestamp
        datapoints = []
        
        return datapoints
    except ClientError as e:
        print(f"Error retrieving CloudWatch metrics: {e}")
        return []

def create_cpu_alarm(instance_id, alarm_name=DEFAULT_ALARM_NAME, threshold=DEFAULT_THRESHOLD, 
                    evaluation_periods=DEFAULT_EVALUATION_PERIODS, period=DEFAULT_PERIOD, region=DEFAULT_REGION):
    """
    Create a CloudWatch alarm for high CPU utilization
    
    Args:
        instance_id (str): EC2 instance ID
        alarm_name (str): Name for the CloudWatch alarm
        threshold (float): CPU utilization percentage to trigger alarm
        evaluation_periods (int): Number of periods to evaluate
        period (int): Time period in seconds
        region (str): AWS region name
        
    Returns:
        bool: True if alarm created successfully, False otherwise
    """
    try:
        # TODO: Initialize CloudWatch client with the specified region
        
        # TODO: Create the alarm using put_metric_alarm method
        # Parameters to include:
        # - AlarmName
        # - AlarmDescription
        # - ActionsEnabled (True)
        # - MetricName ('CPUUtilization')
        # - Namespace ('AWS/EC2')
        # - Statistic ('Average')
        # - Dimensions (InstanceId)
        # - Period
        # - EvaluationPeriods
        # - Threshold
        # - ComparisonOperator ('GreaterThanThreshold')
        # - TreatMissingData ('missing')
        
        print(f"Alarm '{alarm_name}' created successfully!")
        return True
    except ClientError as e:
        print(f"Error creating CloudWatch alarm: {e}")
        return False

def list_alarms(alarm_name=None, region=DEFAULT_REGION):
    """
    List CloudWatch alarms and their status
    
    Args:
        alarm_name (str, optional): Specific alarm name to query
        region (str): AWS region name
        
    Returns:
        list: List of alarm details
    """
    try:
        # TODO: Initialize CloudWatch client with the specified region
        
        # TODO: Get alarms using describe_alarms method
        # If alarm_name is provided, filter by that name
        # Otherwise, get all metric alarms
        
        # TODO: Print alarm information
        # For each alarm, display:
        # - Alarm name
        # - State value
        # - Metric name
        # - Threshold
        # - Evaluation periods
        
        return []  # Return the list of alarms
    except ClientError as e:
        print(f"Error listing CloudWatch alarms: {e}")
        return []

def delete_alarm(alarm_name, region=DEFAULT_REGION):
    """
    Delete a CloudWatch alarm
    
    Args:
        alarm_name (str): Name of the alarm to delete
        region (str): AWS region name
        
    Returns:
        bool: True if deleted successfully, False otherwise
    """
    try:
        # TODO: Initialize CloudWatch client with the specified region
        
        # TODO: Delete the alarm using delete_alarms method
        # Parameter: AlarmNames (list containing the alarm_name)
        
        print(f"Alarm '{alarm_name}' deleted successfully")
        return True
    except ClientError as e:
        print(f"Error deleting CloudWatch alarm: {e}")
        return False

def check_instance_exists(instance_id, region=DEFAULT_REGION):
    """
    Check if an EC2 instance exists and is running
    
    Args:
        instance_id (str): EC2 instance ID to check
        region (str): AWS region name
        
    Returns:
        bool: True if instance exists and is running, False otherwise
    """
    try:
        # TODO: Initialize EC2 client with the specified region
        
        # TODO: Describe the instance to check if it exists
        # Use describe_instances with InstanceIds filter
        
        # TODO: Check if the instance exists and is in a running state
        # 1. Check if 'Reservations' list is not empty
        # 2. Check if 'Instances' list is not empty
        # 3. Check if the state is 'running'
        
        return False  # Replace with your implementation
    except ClientError as e:
        print(f"Error checking instance: {e}")
        return False

def print_metrics(metrics):
    """
    Print CPU utilization metrics in a readable format
    
    Args:
        metrics (list): List of metric datapoints
    """
    # TODO: Print CPU utilization metrics
    # 1. Check if metrics list is empty
    # 2. Print a header for the metrics table
    # 3. For each datapoint, print:
    #    - Timestamp (formatted as a readable date/time)
    #    - CPU utilization percentage (Average value)
    # 4. If no metrics, print a message indicating that
    pass

def main():
    """
    Main function to parse arguments and execute CloudWatch operations
    """
    # TODO: Set up argument parser
    # Add arguments for:
    # - instance-id: EC2 instance ID to monitor
    # - region: AWS region
    # - metric: Flag to get metrics
    # - create-alarm: Flag to create an alarm
    # - threshold: CPU threshold for alarm
    # - list-alarms: Flag to list alarms
    # - delete-alarm: Name of alarm to delete
    
    # TODO: Parse arguments
    args = None  # Replace with parser.parse_args()
    
    # TODO: Implement the main workflow based on arguments
    # 1. If instance-id is provided, check if it exists
    # 2. If metric flag is set, get and print CPU metrics
    # 3. If create-alarm flag is set, create a CPU alarm
    # 4. If list-alarms flag is set, list CloudWatch alarms
    # 5. If delete-alarm is provided, delete the specified alarm
    
    print("\nCloudWatch operations completed successfully!")

if __name__ == "__main__":
    main()