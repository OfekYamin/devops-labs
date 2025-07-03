# LAB04 - CloudWatch Metrics and Alerts: Solutions

This document contains the complete solution for the CloudWatch Metrics and Alerts lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for monitor.py

```python
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
        # Initialize CloudWatch client
        cw_client = boto3.client('cloudwatch', region_name=region)
        
        # Set default time range if not provided
        if not start_time:
            start_time = datetime.utcnow() - timedelta(hours=1)
        if not end_time:
            end_time = datetime.utcnow()
        
        # Get metrics
        response = cw_client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                },
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=period,
            Statistics=['Average']
        )
        
        # Extract and sort datapoints
        datapoints = sorted(response['Datapoints'], key=lambda x: x['Timestamp'])
        
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
        # Initialize CloudWatch client
        cw_client = boto3.client('cloudwatch', region_name=region)
        
        # Create the alarm
        cw_client.put_metric_alarm(
            AlarmName=alarm_name,
            AlarmDescription=f'Alarm when CPU exceeds {threshold}% for {evaluation_periods} periods of {period} seconds',
            ActionsEnabled=True,
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistic='Average',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                },
            ],
            Period=period,
            EvaluationPeriods=evaluation_periods,
            Threshold=threshold,
            ComparisonOperator='GreaterThanThreshold',
            TreatMissingData='missing'
        )
        
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
        # Initialize CloudWatch client
        cw_client = boto3.client('cloudwatch', region_name=region)
        
        # Get alarms
        if alarm_name:
            response = cw_client.describe_alarms(AlarmNames=[alarm_name])
        else:
            response = cw_client.describe_alarms(AlarmTypes=['MetricAlarm'])
        
        alarms = response['MetricAlarms']
        
        # Print alarm information
        if alarms:
            print("\nCurrent CloudWatch Alarms:")
            for alarm in alarms:
                name = alarm['AlarmName']
                state = alarm['StateValue']
                print(f"- {name} ({state})")
                
                # Optional: Print more details
                print(f"  Metric: {alarm['MetricName']}")
                print(f"  Threshold: {alarm['Threshold']}")
                print(f"  Evaluation Periods: {alarm['EvaluationPeriods']}")
                print("")
        else:
            print("No CloudWatch alarms found")
        
        return alarms
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
        # Initialize CloudWatch client
        cw_client = boto3.client('cloudwatch', region_name=region)
        
        # Delete the alarm
        cw_client.delete_alarms(
            AlarmNames=[alarm_name]
        )
        
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
        # Initialize EC2 client
        ec2_client = boto3.client('ec2', region_name=region)
        
        # Describe instance
        response = ec2_client.describe_instances(
            InstanceIds=[instance_id]
        )
        
        # Check if instance exists and is running
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                state = instance['State']['Name']
                if state == 'running':
                    print(f"Instance {instance_id} is running")
                    return True
                else:
                    print(f"Instance {instance_id} exists but is in state: {state}")
                    return False
        
        # If we get here, instance wasn't found
        print(f"Instance {instance_id} not found")
        return False
    except ClientError as e:
        if 'InvalidInstanceID.NotFound' in str(e):
            print(f"Instance {instance_id} does not exist")
        else:
            print(f"Error checking instance: {e}")
        return False

def main():
    """Main function to parse arguments and execute operations"""
    parser = argparse.ArgumentParser(description='CloudWatch Metrics and Alarm Tool')
    
    parser.add_argument('--instance-id', required=True, help='EC2 instance ID to monitor')
    parser.add_argument('--region', default=DEFAULT_REGION, help=f'AWS region (default: {DEFAULT_REGION})')
    parser.add_argument('--create-alarm', action='store_true', help='Create a CPU utilization alarm')
    parser.add_argument('--list-alarms', action='store_true', help='List existing CloudWatch alarms')
    parser.add_argument('--delete-alarm', metavar='NAME', help='Delete a specific alarm by name')
    parser.add_argument('--threshold', type=float, default=DEFAULT_THRESHOLD, 
                        help=f'CPU percentage threshold for alarm (default: {DEFAULT_THRESHOLD})')
    
    args = parser.parse_args()
    
    print("AWS CloudWatch Monitoring Tool")
    print("=============================")
    
    # Check if instance exists and is running
    if not check_instance_exists(args.instance_id, args.region):
        print("Please provide a valid running instance ID")
        sys.exit(1)
    
    # Get and display metrics
    print(f"\nRetrieving CPU metrics for instance: {args.instance_id}")
    metrics = get_cpu_metrics(args.instance_id, region=args.region)
    
    if metrics:
        print("\nCPU Utilization (last hour):")
        for point in metrics:
            timestamp = point['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"  {timestamp}: {point['Average']:.2f}%")
    else:
        print("No metrics found for this instance")
    
    # Create an alarm if requested
    if args.create_alarm:
        print(f"\nCreating CPU utilization alarm with threshold of {args.threshold}%...")
        create_cpu_alarm(
            args.instance_id, 
            threshold=args.threshold,
            region=args.region
        )
    
    # List alarms if requested
    if args.list_alarms:
        list_alarms(region=args.region)
    
    # Delete alarm if requested
    if args.delete_alarm:
        delete_alarm(args.delete_alarm, args.region)
    
    # Print cleanup instructions
    print("\n⚠️  IMPORTANT: Remember to delete test alarms when you're done!")
    print("To delete an alarm via Python, use:")
    print("python monitor.py --delete-alarm HighCPUAlert")

if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **CloudWatch Metrics API**:
   - How to query metrics using `get_metric_statistics` with the appropriate namespace and dimensions
   - Understanding the metrics data structure returned by CloudWatch
   - Working with time ranges and periods for metric granularity

2. **CloudWatch Alarms**:
   - Creating alarms based on metric thresholds
   - Setting evaluation periods and alarm actions
   - Configuring comparison operators and missing data treatment

3. **Error Handling with boto3**:
   - Using try/except blocks to handle AWS API exceptions
   - Common error patterns when working with CloudWatch
   - Proper error reporting and user feedback

4. **Time Series Data Handling**:
   - Working with timestamps and datetime objects in Python
   - Sorting and processing time-based data points
   - Calculating time ranges for metric queries

5. **Instance Validation**:
   - Verifying EC2 instance existence before attempting to monitor
   - Checking instance state to ensure it's running
   - Error handling for invalid or non-existent instances

## Common Issues and Troubleshooting

1. **Permissions Issues**:
   - "Access Denied" errors when your IAM user lacks CloudWatch or EC2 permissions
   - Solution: Ensure your user has `CloudWatchFullAccess` and `AmazonEC2ReadOnlyAccess` policies at minimum

2. **No Metrics Available**:
   - Empty datapoints returned when querying metrics
   - Solution: Verify the instance is running and generating metrics; some metrics may have a delay

3. **Invalid Instance ID**:
   - Errors when trying to monitor non-existent instances
   - Solution: Implement the `check_instance_exists` function to validate instances before monitoring

4. **Time Range Issues**:
   - Incorrect time ranges leading to no data or too much data
   - Solution: Use appropriate datetime objects and timedelta for time ranges

5. **Alarm Configuration**:
   - Alarms not triggering as expected
   - Solution: Check threshold values, evaluation periods, and comparison operators

## Best Practices

1. **Use Descriptive Alarm Names**: Include the resource type and condition in the alarm name
2. **Set Appropriate Thresholds**: Understand normal behavior before setting alarm thresholds
3. **Use Multiple Evaluation Periods**: Avoid false alarms by requiring multiple periods over threshold
4. **Add Alarm Actions**: Connect alarms to SNS topics for email/SMS notifications (not covered in basic lab)
5. **Implement Missing Data Handling**: Configure how the alarm should behave when data is missing

## Extended Applications

This lab focuses on EC2 CPU monitoring, but the same principles apply to:

1. **Monitoring Other EC2 Metrics**:
   - Memory utilization (requires CloudWatch agent)
   - Disk space utilization
   - Network traffic

2. **Monitoring Other AWS Services**:
   - RDS database metrics
   - ELB/ALB request counts and latency
   - Lambda function invocations and errors

3. **Creating Composite Metrics**:
   - Calculating derived metrics from multiple raw metrics
   - Setting alarms on metric math expressions

4. **Integration with Other AWS Services**:
   - Triggering Auto Scaling actions
   - Invoking Lambda functions for remediation
   - Sending notifications via SNS

## Cleanup Importance

Always remember to clean up CloudWatch alarms after your lab to avoid confusion and potential costs:

1. List all alarms to identify what needs to be cleaned up
2. Delete alarms that are no longer needed
3. Verify in the AWS Management Console that alarms are removed 