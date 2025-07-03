#!/usr/bin/env python3
"""
LAB04 - System Monitoring Scripts with Python

This script collects and displays real-time system metrics using the psutil library.
It provides an overview of CPU, memory, disk, and network usage.

Usage:
    python monitor.py
"""

# TODO: Import the necessary libraries
# You'll need psutil for system metrics and time for the monitoring loop


# TODO: Define a function to collect system metrics
# The function should gather:
# - CPU usage percentage
# - Memory usage (used, available, percentage)
# - Disk usage (total, used, free, percentage)
# - Network I/O statistics (optional)


# TODO: Define a function to display the metrics in a readable format
# Consider using formatting to make the output clear and easy to read
# Example: print(f"CPU Usage: {cpu_percent:>5.1f}%")


# TODO: Implement a continuous monitoring loop (optional)
# This should:
# - Call your collection and display functions
# - Sleep for a specified interval
# - Allow for clean termination with Ctrl+C


if __name__ == "__main__":
    print("System Monitoring Tool")
    print("=====================")
    
    # TODO: Implement your monitoring logic here
    # Options:
    # 1. Simple single measurement of system stats
    # 2. Continuous monitoring with a loop and interval
    
    # Example for a single measurement:
    # collect_metrics()
    # display_metrics(metrics)
    
    # Example for continuous monitoring:
    # try:
    #     while True:
    #         metrics = collect_metrics()
    #         display_metrics(metrics)
    #         time.sleep(interval)
    # except KeyboardInterrupt:
    #     print("\nMonitoring stopped.")

"""
Sample output:

=== System Metrics (2023-06-01 14:30:22) ===

CPU Usage:    23.5%  [##########...............]

MEMORY:
  Total:     16.0 GB
  Used:       8.2 GB (51.3%)
  Available:  7.8 GB
  
DISK (/):
  Total:    512.0 GB
  Used:     298.5 GB (58.3%)
  Free:     213.5 GB
  
NETWORK:
  Sent:      12.5 MB
  Received:  45.8 MB
  
Press Ctrl+C to stop monitoring.
""" 