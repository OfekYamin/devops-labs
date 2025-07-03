# LAB04 - System Monitoring Scripts Solutions

This file provides a reference solution for the System Monitoring Scripts lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `monitor.py`

```python
#!/usr/bin/env python3
"""
LAB04 - System Monitoring Scripts with Python

This script collects and displays real-time system metrics using the psutil library.
It provides an overview of CPU, memory, disk, and network usage.

Usage:
    python monitor.py                    # Run with default settings
    python monitor.py --interval 2       # Update every 2 seconds
    python monitor.py --no-loop          # Single measurement, no continuous updates
    python monitor.py --advanced         # Show additional metrics
"""

import argparse
import datetime
import os
import platform
import psutil
import time
from collections import namedtuple


def get_size(bytes_value, suffix="B"):
    """
    Scale bytes to a human-readable format.
    
    Args:
        bytes_value (int): Size in bytes
        suffix (str): Unit suffix to use
        
    Returns:
        str: Formatted size string with unit
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_value < factor:
            return f"{bytes_value:.2f} {unit}{suffix}"
        bytes_value /= factor


def collect_metrics(advanced=False):
    """
    Collect system metrics using psutil.
    
    Args:
        advanced (bool): Whether to collect additional metrics
        
    Returns:
        dict: Dictionary containing system metrics
    """
    metrics = {}
    
    # System information
    metrics['timestamp'] = datetime.datetime.now()
    metrics['system'] = {
        'platform': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'hostname': platform.node(),
        'uptime': datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))
    }
    
    # CPU metrics
    metrics['cpu'] = {
        'percent': psutil.cpu_percent(interval=1),
        'count_physical': psutil.cpu_count(logical=False),
        'count_logical': psutil.cpu_count(logical=True)
    }
    
    if advanced:
        metrics['cpu']['per_cpu'] = psutil.cpu_percent(interval=0, percpu=True)
        metrics['cpu']['stats'] = dict(psutil.cpu_stats()._asdict())
        metrics['cpu']['freq'] = dict(psutil.cpu_freq()._asdict()) if psutil.cpu_freq() else None
    
    # Memory metrics
    vm = psutil.virtual_memory()
    metrics['memory'] = {
        'total': vm.total,
        'available': vm.available,
        'used': vm.used,
        'percent': vm.percent
    }
    
    # Swap metrics
    swap = psutil.swap_memory()
    metrics['swap'] = {
        'total': swap.total,
        'used': swap.used,
        'free': swap.free,
        'percent': swap.percent
    }
    
    # Disk metrics
    disk = psutil.disk_usage('/')
    metrics['disk'] = {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }
    
    if advanced:
        metrics['disk']['io'] = dict(psutil.disk_io_counters()._asdict()) if psutil.disk_io_counters() else None
        metrics['disk']['partitions'] = []
        for partition in psutil.disk_partitions():
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                metrics['disk']['partitions'].append({
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'opts': partition.opts,
                    'total': partition_usage.total,
                    'used': partition_usage.used,
                    'free': partition_usage.free,
                    'percent': partition_usage.percent
                })
            except PermissionError:
                # This can happen when accessing certain mountpoints
                continue
    
    # Network metrics
    net_io = psutil.net_io_counters()
    metrics['network'] = {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv,
        'errin': net_io.errin,
        'errout': net_io.errout,
        'dropin': net_io.dropin,
        'dropout': net_io.dropout
    }
    
    if advanced:
        metrics['network']['connections'] = len(psutil.net_connections())
        metrics['network']['interfaces'] = {name: addresses for name, addresses in 
                                           psutil.net_if_addrs().items()}
    
    # Process information (simple count by default)
    metrics['processes'] = {
        'count': len(psutil.pids())
    }
    
    if advanced:
        # Get top 5 processes by memory usage
        processes = []
        for proc in sorted(psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']), 
                          key=lambda p: p.info['memory_percent'] if p.info['memory_percent'] is not None else 0, 
                          reverse=True)[:5]:
            try:
                if proc.info['memory_percent'] is not None:
                    processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        metrics['processes']['top_by_memory'] = processes
    
    return metrics


def display_metrics(metrics, advanced=False):
    """
    Display system metrics in a readable format.
    
    Args:
        metrics (dict): Dictionary containing system metrics
        advanced (bool): Whether to display additional metrics
    """
    # Clear screen for better visibility (works on Windows and Unix)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Header
    print(f"=== System Metrics ({metrics['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}) ===\n")
    
    # System information
    if advanced:
        print(f"SYSTEM INFORMATION:")
        print(f"  Platform:  {metrics['system']['platform']} {metrics['system']['release']}")
        print(f"  Computer:  {metrics['system']['hostname']}")
        print(f"  Processor: {metrics['system']['processor']}")
        print(f"  Uptime:    {metrics['system']['uptime']}\n")
    
    # CPU metrics
    cpu_percent = metrics['cpu']['percent']
    cpu_bar = "#" * int(cpu_percent / 2.5) + "." * (40 - int(cpu_percent / 2.5))
    print(f"CPU Usage:    {cpu_percent:>5.1f}%  [{cpu_bar}]")
    
    if advanced:
        print(f"  Physical:   {metrics['cpu']['count_physical']} cores")
        print(f"  Logical:    {metrics['cpu']['count_logical']} cores")
        if metrics['cpu'].get('per_cpu'):
            print("  Per CPU:    " + " ".join(f"{p:5.1f}%" for p in metrics['cpu']['per_cpu']))
    
    print("")
    
    # Memory metrics
    print("MEMORY:")
    print(f"  Total:      {get_size(metrics['memory']['total']):>9}")
    print(f"  Used:       {get_size(metrics['memory']['used']):>9} ({metrics['memory']['percent']}%)")
    print(f"  Available:  {get_size(metrics['memory']['available']):>9}")
    
    if advanced:
        print("\nSWAP:")
        print(f"  Total:      {get_size(metrics['swap']['total']):>9}")
        print(f"  Used:       {get_size(metrics['swap']['used']):>9} ({metrics['swap']['percent']}%)")
        print(f"  Free:       {get_size(metrics['swap']['free']):>9}")
    
    print("")
    
    # Disk metrics
    print("DISK (/):")
    print(f"  Total:      {get_size(metrics['disk']['total']):>9}")
    print(f"  Used:       {get_size(metrics['disk']['used']):>9} ({metrics['disk']['percent']}%)")
    print(f"  Free:       {get_size(metrics['disk']['free']):>9}")
    
    if advanced and metrics['disk'].get('partitions'):
        print("\n  PARTITIONS:")
        for partition in metrics['disk']['partitions'][:3]:  # Show only the first 3 partitions
            print(f"  - {partition['mountpoint']}:")
            print(f"    {get_size(partition['used']):>9} / {get_size(partition['total']):>9} ({partition['percent']}%)")
    
    print("")
    
    # Network metrics
    print("NETWORK:")
    print(f"  Sent:       {get_size(metrics['network']['bytes_sent']):>9}")
    print(f"  Received:   {get_size(metrics['network']['bytes_recv']):>9}")
    
    if advanced:
        print(f"  Connections: {metrics['network']['connections']}")
        print(f"  Interfaces:  {', '.join(list(metrics['network']['interfaces'].keys())[:3])}" + 
              (", ..." if len(metrics['network']['interfaces']) > 3 else ""))
    
    # Process information
    print(f"\nPROCESSES:    {metrics['processes']['count']}")
    
    if advanced and metrics['processes'].get('top_by_memory'):
        print("\n  TOP PROCESSES (by memory):")
        for proc in metrics['processes']['top_by_memory']:
            print(f"  - {proc['name'][:20]:20} (PID: {proc['pid']:>5}) {proc['memory_percent']:>5.1f}%")
    
    print("\nPress Ctrl+C to stop monitoring.")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Monitor system metrics")
    parser.add_argument("--interval", type=int, default=5, help="Update interval in seconds")
    parser.add_argument("--no-loop", action="store_true", help="Single measurement, no loop")
    parser.add_argument("--advanced", action="store_true", help="Show additional metrics")
    return parser.parse_args()


def main():
    """Main function to collect and display system metrics."""
    args = parse_arguments()
    
    print("System Monitoring Tool")
    print("=====================")
    print("Initializing...\n")
    
    try:
        if args.no_loop:
            # Single measurement
            metrics = collect_metrics(args.advanced)
            display_metrics(metrics, args.advanced)
        else:
            # Continuous monitoring
            previous_net_io = {"bytes_sent": 0, "bytes_recv": 0}
            
            while True:
                metrics = collect_metrics(args.advanced)
                
                # Update network metrics to show per-interval values
                current_net_io = metrics["network"]
                metrics["network"]["bytes_sent"] = current_net_io["bytes_sent"] - previous_net_io["bytes_sent"]
                metrics["network"]["bytes_recv"] = current_net_io["bytes_recv"] - previous_net_io["bytes_recv"]
                
                display_metrics(metrics, args.advanced)
                
                # Save current values for next interval
                previous_net_io = {
                    "bytes_sent": current_net_io["bytes_sent"],
                    "bytes_recv": current_net_io["bytes_recv"]
                }
                
                time.sleep(args.interval)
    
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Using psutil for System Metrics**:
   - Retrieving CPU usage with `psutil.cpu_percent()`
   - Getting memory information with `psutil.virtual_memory()`
   - Finding disk usage with `psutil.disk_usage()`
   - Gathering network I/O with `psutil.net_io_counters()`

2. **Data Presentation**:
   - Formatting bytes into human-readable sizes
   - Creating visual indicators (like bar charts using ASCII characters)
   - Clearing the screen for real-time updates
   - Structuring output for readability

3. **Continuous Monitoring**:
   - Using loops with sleep intervals
   - Handling keyboard interrupts gracefully
   - Computing delta values between measurements

4. **Command-Line Interface**:
   - Parsing arguments with argparse
   - Providing optional flags for different behaviors
   - Setting sensible defaults

5. **Cross-Platform Compatibility**:
   - Using platform module to detect system information
   - Handling OS-specific behaviors (like screen clearing)
   - Managing permissions and access issues

## Expected Output

Basic output:
```
=== System Metrics (2023-06-01 14:30:22) ===

CPU Usage:    23.5%  [#########.................................]

MEMORY:
  Total:      16.00 GB
  Used:        8.21 GB (51.3%)
  Available:   7.79 GB

DISK (/):
  Total:     512.00 GB
  Used:      298.54 GB (58.3%)
  Free:      213.46 GB

NETWORK:
  Sent:        2.34 MB
  Received:    5.67 MB

PROCESSES:    142

Press Ctrl+C to stop monitoring.
```

## Advanced Mode Features

1. **Detailed System Information**:
   - Platform details (OS, version)
   - Host name and processor information
   - System uptime

2. **Expanded CPU Metrics**:
   - Per-CPU utilization percentages
   - CPU frequency information
   - Physical vs. logical core counts

3. **Comprehensive Disk Information**:
   - Partition details and mount points
   - Filesystem types
   - I/O statistics

4. **Enhanced Network Statistics**:
   - Active connection count
   - Network interface details
   - Error and packet statistics

5. **Process Insights**:
   - Top processes by memory usage
   - PID and owner information
   - CPU utilization per process

## Common Issues and Troubleshooting

1. **Permission Errors**: Some metrics require administrator/root access; run with elevated privileges if needed
2. **Cross-Platform Differences**: Some metrics may be unavailable on certain platforms
3. **Performance Impact**: Frequent polling may affect system performance; adjust interval accordingly
4. **Display Issues**: Terminal size limitations may affect output formatting
5. **Network Values**: Network byte counts are cumulative; subtract previous values to show per-interval rates

## Extension Ideas

1. **Data Logging**: Save metrics to a CSV file for historical analysis
2. **Alert Thresholds**: Notify when metrics exceed defined thresholds
3. **Web Dashboard**: Create a simple web server to view metrics in a browser
4. **Remote Monitoring**: Collect metrics from remote machines via SSH or an agent
5. **Resource Graphs**: Generate visual graphs using matplotlib or similar libraries

## Best Practices

1. **Efficient Polling**: Use appropriate intervals to avoid excessive resource usage
2. **Error Handling**: Gracefully handle exceptions for unavailable metrics
3. **User Experience**: Provide clear, readable output with units and context
4. **Configuration Options**: Allow customization through command-line arguments
5. **Documentation**: Include helpful usage information and examples 