# Solutions: Azure Monitor Metrics and Alerts Automation

This document provides the reference solutions for the Azure Monitor Metrics and Alerts lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

Below is the full implementation of the `monitor_alert.py` script:

```python
#!/usr/bin/env python3
"""
Azure Monitor Metrics and Alerts Automation Script

This script demonstrates how to interact with Azure Monitor to fetch metrics and create alerts
using the Azure SDK for Python. It shows how to query resource metrics and set up monitoring alerts.
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
from azure.core.exceptions import HttpResponseError, ResourceNotFoundError

def get_clients():
    """
    Create Azure SDK clients for Monitor and Resource Management.
    
    Returns:
        tuple: (monitor_client, resource_client, subscription_id)
    """
    # Get subscription ID from environment variables
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        sys.exit(1)
    
    # Create credential using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
    except Exception as e:
        print(f"Error creating credential: {e}")
        print("Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set.")
        sys.exit(1)
    
    # Create and return monitor and resource clients
    monitor_client = MonitorManagementClient(credential, subscription_id)
    resource_client = ResourceManagementClient(credential, subscription_id)
    
    return monitor_client, resource_client, subscription_id

def list_resources(resource_client, resource_group=None, resource_type=None):
    """
    List Azure resources that can be monitored.
    
    Args:
        resource_client: Azure Resource Management client
        resource_group (str, optional): Resource group to filter by
        resource_type (str, optional): Resource type to filter by (e.g. "Microsoft.Compute/virtualMachines")
        
    Returns:
        list: Resources with their IDs and types
    """
    print(f"Listing resources in {'resource group ' + resource_group if resource_group else 'all resource groups'}")
    
    resources = []
    
    # Filter by resource group if specified
    if resource_group:
        resource_list = resource_client.resources.list_by_resource_group(resource_group)
    else:
        resource_list = resource_client.resources.list()
    
    # Collect resources with optional filtering by type
    for resource in resource_list:
        if resource_type and resource.type.lower() != resource_type.lower():
            continue
            
        resource_info = {
            'name': resource.name,
            'id': resource.id,
            'type': resource.type,
            'location': resource.location
        }
        resources.append(resource_info)
        print(f"- {resource.name} ({resource.type}): {resource.id}")
    
    if not resources:
        print("No resources found matching the criteria.")
        
    return resources

def get_resource_metrics(monitor_client, resource_uri, metric_names, time_window_minutes=30):
    """
    Get metrics for a specific Azure resource.
    
    Args:
        monitor_client: Azure Monitor Management client
        resource_uri (str): The resource URI to get metrics for
        metric_names (list): List of metric names to retrieve
        time_window_minutes (int): Time window in minutes to look back
        
    Returns:
        dict: Metrics data organized by metric name
    """
    print(f"Getting metrics for resource: {resource_uri}")
    
    # Calculate time range (start_time to now)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=time_window_minutes)
    timespan = f"{start_time.isoformat()}Z/{end_time.isoformat()}Z"
    
    # Join metric names if it's a list
    if isinstance(metric_names, list):
        metric_names_str = ','.join(metric_names)
    else:
        metric_names_str = metric_names
    
    # Query metrics from Azure Monitor
    try:
        metrics_data = monitor_client.metrics.list(
            resource_uri,
            timespan=timespan,
            interval='PT1M',  # 1-minute interval
            metricnames=metric_names_str,
            aggregation='Average,Maximum'
        )
    except HttpResponseError as e:
        print(f"Error fetching metrics: {e}")
        if "ResourceNotFound" in str(e):
            print(f"Resource not found: {resource_uri}")
        elif "MetricNotFound" in str(e):
            print(f"Metric not found: {metric_names_str}")
        return None
    
    # Process and return the metrics data
    result = {}
    
    for metric in metrics_data.value:
        metric_name = metric.name.value
        print(f"\nMetric: {metric_name}")
        print(f"Unit: {metric.unit}")
        
        # Initialize the entry for this metric
        result[metric_name] = {
            'unit': metric.unit,
            'display_name': metric.display_description or metric.name.localized_value,
            'time_series': []
        }
        
        # Process each time series
        for time_series in metric.timeseries:
            time_values = []
            avg_values = []
            max_values = []
            
            # Process each data point
            for data_point in time_series.data:
                time_values.append(data_point.time_stamp)
                
                # Add average and maximum values if available
                avg_value = data_point.average if hasattr(data_point, 'average') else None
                max_value = data_point.maximum if hasattr(data_point, 'maximum') else None
                
                avg_values.append(avg_value)
                max_values.append(max_value)
                
                # Print the data point
                avg_str = f"Avg: {avg_value:.2f}" if avg_value is not None else "Avg: N/A"
                max_str = f"Max: {max_value:.2f}" if max_value is not None else "Max: N/A"
                print(f"Time: {data_point.time_stamp}, {avg_str}, {max_str}")
            
            # Add this time series to the result
            result[metric_name]['time_series'].append({
                'time_values': time_values,
                'avg_values': avg_values,
                'max_values': max_values
            })
    
    return result

def create_metric_alert(monitor_client, resource_group, alert_name, resource_uri, 
                        metric_name, operator, threshold, window_minutes=5):
    """
    Create a metric alert for a resource.
    
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
    
    # Define alert rule parameters
    alert_rule = {
        "location": "global",  # Metric alerts are a global resource
        "description": f"Alert when {metric_name} {operator} {threshold}",
        "severity": 2,  # 0-4 (0=critical, 4=verbose)
        "enabled": True,
        "scopes": [resource_uri],
        "evaluation_frequency": f"PT{window_minutes}M",  # ISO 8601 duration format
        "window_size": f"PT{window_minutes}M",
        "criteria": {
            "odata.type": "Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria",
            "allOf": [
                {
                    "name": "condition1",
                    "metricName": metric_name,
                    "metricNamespace": "",
                    "operator": operator,
                    "threshold": threshold,
                    "timeAggregation": "Average",
                    "criterionType": "StaticThresholdCriterion"
                }
            ]
        },
        "auto_mitigate": True,
        "target_resource_type": resource_uri.split("/providers/")[1].split("/")[0] + "/" + 
                               resource_uri.split("/providers/")[1].split("/")[1],
        "actions": []
    }
    
    try:
        # Create the alert rule
        response = monitor_client.metric_alerts.create_or_update(
            resource_group,
            alert_name,
            alert_rule
        )
        
        # Extract and return the alert rule details
        alert_details = {
            "id": response.id,
            "name": response.name,
            "type": response.type,
            "description": response.description,
            "severity": response.severity,
            "scopes": response.scopes
        }
        
        print(f"Metric alert '{alert_name}' created successfully.")
        print(f"Alert ID: {alert_details['id']}")
        
        return alert_details
    
    except HttpResponseError as e:
        print(f"Error creating alert rule: {e}")
        return None

def delete_metric_alert(monitor_client, resource_group, alert_name):
    """
    Delete a metric alert rule.
    
    Args:
        monitor_client: Azure Monitor Management client
        resource_group (str): Resource group name
        alert_name (str): Name of the alert rule to delete
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting metric alert '{alert_name}' from {resource_group}")
    
    try:
        # Delete the alert rule
        monitor_client.metric_alerts.delete(resource_group, alert_name)
        print(f"Metric alert '{alert_name}' deleted successfully.")
        return True
    
    except ResourceNotFoundError:
        print(f"Alert rule '{alert_name}' not found.")
        return False
    
    except Exception as e:
        print(f"Error deleting alert rule: {e}")
        return False

def plot_metrics(metrics_data, metric_name, resource_name):
    """
    Plot metrics data using matplotlib.
    
    Args:
        metrics_data (dict): Metrics data from get_resource_metrics
        metric_name (str): The name of the metric to plot
        resource_name (str): The name of the resource (for the plot title)
    """
    print(f"Plotting {metric_name} metrics for {resource_name}")
    
    if not metrics_data or metric_name not in metrics_data:
        print(f"No data available for metric: {metric_name}")
        return
    
    # Extract metric data
    metric_data = metrics_data[metric_name]
    unit = metric_data['unit']
    display_name = metric_data['display_name']
    
    # Set up the plot
    plt.figure(figsize=(12, 6))
    
    # Process each time series
    for i, series in enumerate(metric_data['time_series']):
        # Extract timestamps and values
        timestamps = series['time_values']
        avg_values = series['avg_values']
        max_values = series['max_values']
        
        # Plot average values
        if any(v is not None for v in avg_values):
            plt.plot(timestamps, avg_values, label=f'Average', marker='o', linestyle='-')
        
        # Plot maximum values
        if any(v is not None for v in max_values):
            plt.plot(timestamps, max_values, label=f'Maximum', marker='x', linestyle='--')
    
    # Set labels and title
    plt.xlabel('Time (UTC)')
    plt.ylabel(f'{display_name} ({unit})')
    plt.title(f'{display_name} for {resource_name}')
    
    # Format the plot
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to a file
    filename = f"{resource_name}_{metric_name}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.png"
    filename = filename.replace('/', '_').replace('\\', '_')
    plt.savefig(filename)
    print(f"Plot saved as: {filename}")
    
    # Show the plot
    plt.show()

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
        # Get Azure clients
        monitor_client, resource_client, subscription_id = get_clients()
        
        # Process the requested operation
        if args.operation == "list-resources":
            list_resources(resource_client, args.resource_group, args.resource_type)
            
        elif args.operation == "get-metrics":
            if not args.resource_uri:
                print("Error: --resource-uri is required for get-metrics operation.")
                sys.exit(1)
                
            # Get metrics for the resource
            metrics_data = get_resource_metrics(
                monitor_client, 
                args.resource_uri, 
                args.metric,
                args.time_window
            )
            
            # Plot metrics if requested
            if args.plot and metrics_data:
                resource_name = args.resource_uri.split('/')[-1]
                plot_metrics(metrics_data, args.metric, resource_name)
                
        elif args.operation == "create-alert":
            if not args.resource_uri:
                print("Error: --resource-uri is required for create-alert operation.")
                sys.exit(1)
                
            if not args.resource_group:
                print("Error: --resource-group is required for create-alert operation.")
                sys.exit(1)
                
            # Create metric alert
            create_metric_alert(
                monitor_client,
                args.resource_group,
                args.alert_name,
                args.resource_uri,
                args.metric,
                args.operator,
                args.threshold,
                args.window
            )
            
        elif args.operation == "delete-alert":
            if not args.resource_group:
                print("Error: --resource-group is required for delete-alert operation.")
                sys.exit(1)
                
            # Delete metric alert
            delete_metric_alert(
                monitor_client,
                args.resource_group,
                args.alert_name
            )
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Sample Usage

### 1. List Resources
```bash
# List all resources
python monitor_alert.py list-resources

# List resources in a specific resource group
python monitor_alert.py --resource-group devops-lab-rg list-resources

# List only virtual machines
python monitor_alert.py --resource-type Microsoft.Compute/virtualMachines list-resources
```

### 2. Get Metrics
```bash
# Get CPU metrics for a VM
python monitor_alert.py --resource-uri "/subscriptions/<subscription-id>/resourceGroups/devops-lab-rg/providers/Microsoft.Compute/virtualMachines/devops-vm" --metric "Percentage CPU" get-metrics

# Get metrics with a larger time window and plot them
python monitor_alert.py --resource-uri "/subscriptions/<subscription-id>/resourceGroups/devops-lab-rg/providers/Microsoft.Compute/virtualMachines/devops-vm" --metric "Percentage CPU" --time-window 60 --plot get-metrics
```

### 3. Create Alert
```bash
# Create an alert for high CPU usage
python monitor_alert.py --resource-group devops-lab-rg --resource-uri "/subscriptions/<subscription-id>/resourceGroups/devops-lab-rg/providers/Microsoft.Compute/virtualMachines/devops-vm" --alert-name high-cpu-alert --metric "Percentage CPU" --operator GreaterThan --threshold 80 create-alert
```

### 4. Delete Alert
```bash
# Delete an alert
python monitor_alert.py --resource-group devops-lab-rg --alert-name high-cpu-alert delete-alert
```

## Key Learning Points

1. **Azure Monitor Concepts**
   - Azure Monitor is the unified monitoring service for all Azure resources
   - Metrics are lightweight time-series data points collected at regular intervals
   - Metric alerts allow you to be notified when metric values meet certain conditions

2. **Working with Metrics**
   - Metrics are identified by name (e.g., "Percentage CPU" for VMs)
   - Different resource types expose different metrics
   - Metrics can be aggregated over time using different methods (Average, Maximum, etc.)
   - Time windows and intervals control the granularity of metrics data

3. **Alert Rule Components**
   - Scope: The resource(s) being monitored
   - Condition: The metric, operator, and threshold that trigger the alert
   - Action Group: The actions to take when the alert fires (e.g., email, SMS)
   - Evaluation frequency: How often to check the condition
   - Window size: The time period over which to aggregate the metric

4. **Azure SDK for Python**
   - MonitorManagementClient provides access to Azure Monitor APIs
   - ResourceManagementClient helps with resource discovery
   - DefaultAzureCredential simplifies authentication
   - Understanding Azure resource IDs and URIs is essential

5. **Data Visualization**
   - Matplotlib can be used to create visualizations of metrics data
   - Time series plots help identify trends and anomalies
   - Saving plots allows for offline analysis and sharing

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "DefaultAzureCredential failed to retrieve a token"
   - **Solution**: Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set correctly

2. **Resource Discovery**
   - **Problem**: Can't find resources to monitor
   - **Solution**: Use the list-resources operation to discover available resources and their correct URIs

3. **Metrics Availability**
   - **Problem**: "MetricNotFound" error when retrieving metrics
   - **Solution**: Check that the metric name is correct for the resource type. Different resources expose different metrics.

4. **Metric Alert Creation**
   - **Problem**: "BadRequest" error when creating an alert
   - **Solution**: Verify that all parameters are valid. The metric must be available for the resource, and the threshold must be appropriate.

5. **Permission Issues**
   - **Problem**: "AuthorizationFailed" when creating or deleting alerts
   - **Solution**: Ensure the service principal has appropriate permissions (e.g., Monitoring Contributor role)

## Azure Monitor Best Practices

1. **Choose the Right Metrics**
   - Focus on metrics that indicate service health and user experience
   - Combine multiple metrics for more comprehensive monitoring
   - Consider business impact when setting thresholds

2. **Set Appropriate Alert Thresholds**
   - Too sensitive: Leads to alert fatigue
   - Too lax: Misses important issues
   - Use historical data to determine normal ranges

3. **Configure Proper Time Windows**
   - Shorter windows: Detect issues faster but may cause false alarms
   - Longer windows: More stable but may delay detection
   - Match window size to the metric's natural variability

4. **Implement a Gradual Alert Strategy**
   - Warning alerts for early detection
   - Critical alerts for immediate action
   - Use different notification channels based on severity

5. **Use Action Groups Effectively**
   - Route alerts to appropriate teams
   - Include context in notifications
   - Consider automated remediation for common issues

## Common Metrics by Resource Type

### Virtual Machines
- **Percentage CPU**: CPU utilization
- **Available Memory Bytes**: Available memory
- **Disk Read/Write Operations/Sec**: Disk I/O
- **Network In/Out Total**: Network traffic

### App Service
- **Http2xx/4xx/5xx**: HTTP status codes
- **Response Time**: Request latency
- **CPU Time**: CPU usage
- **Memory Working Set**: Memory usage

### SQL Database
- **DTU/CPU percentage**: Database load
- **Storage**: Database size
- **Deadlocks**: Concurrency issues
- **Blocked by Firewall**: Connection issues

### Storage Accounts
- **Transactions**: Request count
- **Ingress/Egress**: Data transfer
- **SuccessE2ELatency**: End-to-end latency
- **Availability**: Service availability

## Extending This Lab

1. **Create Action Groups**: Configure notifications for alerts
2. **Multi-Resource Monitoring**: Monitor multiple resources with a single script
3. **Custom Metrics**: Send and retrieve custom metrics
4. **Log Analytics**: Integrate with Log Analytics for more advanced monitoring
5. **Automated Remediation**: Trigger Azure Automation runbooks or Azure Functions in response to alerts 