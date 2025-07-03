# LAB05 - Cloud Monitoring Metrics - Solutions

This document provides solutions to the TODOs in the `fetch_metrics.py` script.

## Solution: Create a TimeInterval object

```python
# Create a TimeInterval object
interval = monitoring_v3.TimeInterval()
interval.end_time.seconds = int(datetime.utcnow().timestamp())
interval.end_time.nanos = 0
interval.start_time.seconds = int((datetime.utcnow() - timedelta(minutes=minutes)).timestamp())
interval.start_time.nanos = 0
return interval
```

## Solution: Initialize the Cloud Monitoring API client

```python
# Initialize the Cloud Monitoring API client
client = monitoring_v3.MetricServiceClient()
```

## Solution: Create the request to list time series

```python
# Create the request to list time series
request = {
    "name": project_name,
    "filter": f'metric.type="{metric_type}"',
    "interval": time_interval,
    "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
}

# Execute the request and return the results
results = client.list_time_series(request=request)
return results
```

## Solution: Check if any results were returned in display_metric_data

```python
# Check if any results were returned
count = 0
for time_series in results:
    count += 1
    
if count == 0:
    print("No metric data found for the specified time window.")
    print("This could be because:")
    print("  - No resources of this type exist in the project")
    print("  - The resources exist but haven't reported metrics in the specified time window")
    print("  - The service account doesn't have permission to access these metrics")
    return
```

## Solution: Format the results in a table

```python
# Format the results in a table
table_data = []
headers = ["Resource", "Labels", "Timestamp", "Value"]

for time_series in results:
    # Extract resource info
    resource_type = time_series.resource.type
    resource_labels = ", ".join([f"{k}:{v}" for k, v in time_series.resource.labels.items()])
    
    # Extract metric labels if present
    metric_labels = ", ".join([f"{k}:{v}" for k, v in time_series.metric.labels.items()]) if time_series.metric.labels else "None"
    
    # Get the most recent data point (first in the list)
    if time_series.points:
        point = time_series.points[0]
        timestamp = datetime.fromtimestamp(point.interval.end_time.seconds).strftime('%Y-%m-%d %H:%M:%S')
        
        # Get the value (could be different types)
        if hasattr(point.value, 'double_value') and point.value.double_value is not None:
            value = f"{point.value.double_value:.4f}"
        elif hasattr(point.value, 'int64_value') and point.value.int64_value is not None:
            value = str(point.value.int64_value)
        elif hasattr(point.value, 'bool_value') and point.value.bool_value is not None:
            value = str(point.value.bool_value)
        elif hasattr(point.value, 'string_value') and point.value.string_value:
            value = point.value.string_value
        else:
            value = "Unknown value type"
        
        table_data.append([resource_type, resource_labels, timestamp, value])

# Display the table
print(tabulate(table_data, headers=headers, tablefmt="grid"))
```

## Solution: Display summary statistics

```python
# Display summary statistics (min, max, avg)
if table_data:
    print("\nSummary Statistics:")
    numeric_values = []
    
    for row in table_data:
        try:
            value = float(row[3])
            numeric_values.append(value)
        except ValueError:
            continue
    
    if numeric_values:
        print(f"  Min: {min(numeric_values):.4f}")
        print(f"  Max: {max(numeric_values):.4f}")
        print(f"  Avg: {sum(numeric_values) / len(numeric_values):.4f}")
        print(f"  Count: {len(numeric_values)}")
    else:
        print("  No numeric values found for statistics")
```

## Solution: Check if any results were returned in plot_metric_data

```python
# Check if any results were returned
count = 0
for time_series in results:
    count += 1
    
if count == 0:
    print("No data to plot.")
    return
```

## Solution: Create a plot with matplotlib

```python
# Create a plot with matplotlib
plt.figure(figsize=(12, 6))

# Track if we were able to plot any data
plotted_data = False

# Plot each time series
for time_series in results:
    # Extract resource info for the label
    resource_id = time_series.resource.labels.get('instance_id', 
                                              time_series.resource.labels.get('zone', 
                                                                          'unknown'))
    
    # Extract timestamps and values
    timestamps = []
    values = []
    
    for point in reversed(time_series.points):  # Points are in reverse chronological order
        dt = datetime.fromtimestamp(point.interval.end_time.seconds)
        timestamps.append(dt)
        
        # Get the value based on its type
        if hasattr(point.value, 'double_value') and point.value.double_value is not None:
            values.append(point.value.double_value)
        elif hasattr(point.value, 'int64_value') and point.value.int64_value is not None:
            values.append(point.value.int64_value)
        else:
            # Skip non-numeric values
            continue
    
    if timestamps and values:
        plt.plot(timestamps, values, marker='o', linestyle='-', label=f"{resource_id}")
        plotted_data = True

if not plotted_data:
    print("No numeric data available to plot.")
    return

# Add labels and title
plt.title(f"{metric_type} - Last {window_minutes} minutes")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.legend()

# Format the x-axis to show times nicely
plt.gcf().autofmt_xdate()

# Show the plot
plt.tight_layout()
plt.show()
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. List available metric types:
```bash
python fetch_metrics.py --project=your-gcp-project-id --list-metrics
```

3. Fetch CPU utilization metrics:
```bash
python fetch_metrics.py --project=your-gcp-project-id --metric=cpu
```

4. Fetch metrics with a custom time window:
```bash
python fetch_metrics.py --project=your-gcp-project-id --metric=memory --window=30
```

5. Plot the metrics data:
```bash
python fetch_metrics.py --project=your-gcp-project-id --metric=network --plot
```

6. Use a custom metric:
```bash
python fetch_metrics.py --project=your-gcp-project-id --custom-metric="logging.googleapis.com/log_entry_count"
```

## Notes

To discover all available metrics specific to your GCP project, you can run:

```bash
gcloud monitoring metrics list --project=your-gcp-project-id
```

For complex monitoring scenarios, consider exploring the Cloud Monitoring dashboard in the GCP Console, which offers advanced visualization and alerting features. 