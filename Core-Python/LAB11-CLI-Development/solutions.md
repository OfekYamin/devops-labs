# LAB11 - CLI Tool Development Solutions

This file provides a reference solution for the CLI Development lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation

### `main.py`

```python
#!/usr/bin/env python3
"""
LAB11 - CLI Tool Development

This module serves as the entry point for the CLI tool.
It demonstrates how to build professional command-line
applications using Python's argparse module.
"""

import argparse
import sys
from cli_tool.cli import run_cli


def main():
    """Main function to set up and run the CLI tool."""
    # Set up any environment variables or global configuration
    # For a real application, you might load configuration here
    
    try:
        # Call the CLI runner with sys.argv[1:]
        exit_code = run_cli()
        return exit_code
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nOperation cancelled by user")
        return 130  # Standard exit code for SIGINT
    except Exception as e:
        # Handle any uncaught exceptions
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    # This is the entry point when the script is run directly
    # It calls main() and uses the return value as the exit code
    sys.exit(main())
```

### `cli_tool/cli.py`

```python
"""
CLI module for the CLI tool.

This module handles command-line argument parsing and dispatching
to the appropriate command handlers.
"""

import argparse
import sys
from .commands import server, monitor


def create_parser():
    """
    Create the command-line argument parser.
    
    Returns:
        argparse.ArgumentParser: The argument parser
    """
    # Create main parser with program description
    parser = argparse.ArgumentParser(
        prog="devops-cli",
        description="DevOps CLI Tool - A utility for common DevOps tasks",
        epilog="For more information, see the documentation.",
    )
    
    # Add global options
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (can be used multiple times)"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    
    # Create subparsers for different command groups
    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        help="Command to execute"
    )
    subparsers.required = True
    
    # Set up the server commands
    server.setup_server_commands(subparsers)
    
    # Set up the monitor commands
    monitor.setup_monitor_commands(subparsers)
    
    return parser


def parse_args(args=None):
    """
    Parse command-line arguments.
    
    Args:
        args (list, optional): Command-line arguments to parse
            If None, uses sys.argv[1:]
            
    Returns:
        argparse.Namespace: Parsed command-line arguments
    """
    parser = create_parser()
    
    # Parse the arguments
    parsed_args = parser.parse_args(args)
    
    # Special handling for global options
    if parsed_args.verbose >= 3:
        print("Debug mode enabled (verbose level 3)")
    
    return parsed_args


def run_cli(args=None):
    """
    Run the CLI tool with the given arguments.
    
    Args:
        args (list, optional): Command-line arguments
            If None, uses sys.argv[1:]
            
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    try:
        # Parse the command-line arguments
        parsed_args = parse_args(args)
        
        # Call the handler function associated with the command
        # The handler should be stored in the func attribute by setup_*_commands
        if hasattr(parsed_args, 'func'):
            return parsed_args.func(parsed_args)
        else:
            print(f"Error: No handler found for command '{parsed_args.command}'")
            return 1
            
    except argparse.ArgumentError as e:
        print(f"Argument error: {str(e)}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1
```

### `cli_tool/commands/server.py`

```python
"""
Server management commands.

This module contains commands for managing servers - a common DevOps task.
"""

import os
import sys
import time
import socket
from ..utils import print_success, print_error, print_info, print_warning, confirm_action


def server_status(args):
    """
    Check and display the status of servers.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    print_info(f"Checking status of server(s)...")
    
    # In a real implementation, you would connect to actual servers
    # or use an API to retrieve status information
    
    # Example implementation with simulated server statuses
    servers = {
        "web-server-1": {
            "status": "running",
            "uptime": "7 days, 3 hours",
            "load": "0.75, 0.62, 0.55",
            "ip": "192.168.1.101"
        },
        "db-server-1": {
            "status": "running",
            "uptime": "14 days, 8 hours",
            "load": "0.32, 0.28, 0.27",
            "ip": "192.168.1.102"
        },
        "app-server-1": {
            "status": "stopped",
            "uptime": "0",
            "load": "0.0, 0.0, 0.0",
            "ip": "192.168.1.103"
        }
    }
    
    if hasattr(args, 'name') and args.name:
        # Check a specific server
        server_name = args.name
        if server_name in servers:
            server = servers[server_name]
            print_info(f"Server: {server_name}")
            print_info(f"Status: {server['status']}")
            print_info(f"IP Address: {server['ip']}")
            print_info(f"Uptime: {server['uptime']}")
            print_info(f"Load: {server['load']}")
            
            if server['status'] == 'running':
                print_success(f"Server {server_name} is operational")
                return 0
            else:
                print_warning(f"Server {server_name} is not running")
                return 1
        else:
            print_error(f"Server '{server_name}' not found")
            return 1
    else:
        # Check all servers
        print_info(f"All Servers:")
        
        running_count = 0
        for name, server in servers.items():
            status_marker = "✓" if server['status'] == 'running' else "✗"
            print_info(f"{status_marker} {name} ({server['ip']}): {server['status']}")
            
            if server['status'] == 'running':
                running_count += 1
        
        print_info(f"\nSummary: {running_count} of {len(servers)} servers running")
        
        if running_count == len(servers):
            print_success("All servers are operational")
            return 0
        elif running_count > 0:
            print_warning("Some servers are not running")
            return 0  # Still return success as the command completed
        else:
            print_error("No servers are running")
            return 1
    
    return 0


def server_start(args):
    """
    Start one or more servers.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    server_name = args.name
    
    print_info(f"Starting server: {server_name}")
    
    # In a real implementation, you would execute commands to start the server
    # or use an API to initiate server startup
    
    # Simulate server startup with confirmation
    if not args.force:
        confirmed = confirm_action(f"Are you sure you want to start server '{server_name}'?")
        if not confirmed:
            print_info("Operation cancelled")
            return 0
    
    # Simulate startup process
    print_info("Executing startup sequence...")
    for step in range(5):
        print_info(f"Startup step {step+1}/5 completed")
        time.sleep(0.2)  # Simulate time passing
    
    print_success(f"Server {server_name} started successfully")
    return 0


def server_stop(args):
    """
    Stop one or more servers.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    server_name = args.name
    
    print_info(f"Stopping server: {server_name}")
    
    # In a real implementation, you would execute commands to stop the server
    # or use an API to initiate server shutdown
    
    # Simulate server shutdown with confirmation
    if not args.force:
        confirmed = confirm_action(
            f"Are you sure you want to stop server '{server_name}'? "
            f"This will terminate all connections and services."
        )
        if not confirmed:
            print_info("Operation cancelled")
            return 0
    
    # Check for graceful shutdown option
    if args.graceful:
        print_info("Performing graceful shutdown...")
        print_info("Waiting for active connections to close...")
        timeout_sec = 5
        for i in range(timeout_sec, 0, -1):
            print_info(f"Shutdown in {i} seconds...")
            time.sleep(0.2)  # Simulate time passing
    
    # Simulate shutdown process
    print_info("Executing shutdown sequence...")
    for step in range(3):
        print_info(f"Shutdown step {step+1}/3 completed")
        time.sleep(0.2)  # Simulate time passing
    
    print_success(f"Server {server_name} stopped successfully")
    return 0


def setup_server_commands(subparsers):
    """
    Set up the server commands in the argument parser.
    
    Args:
        subparsers: Subparsers object from argparse
    """
    # Create parser for the "server" command
    server_parser = subparsers.add_parser(
        "server",
        help="Server management commands",
        description="Commands for managing server instances"
    )
    
    # Create subparsers for server commands
    server_subparsers = server_parser.add_subparsers(
        title="server commands",
        dest="server_command",
        help="Server command to execute"
    )
    server_subparsers.required = True
    
    # "status" command
    status_parser = server_subparsers.add_parser(
        "status",
        help="Check server status",
        description="Check and display the status of one or all servers"
    )
    status_parser.add_argument(
        "name",
        nargs="?",
        help="Name of the server to check (omit for all servers)"
    )
    status_parser.set_defaults(func=server_status)
    
    # "start" command
    start_parser = server_subparsers.add_parser(
        "start",
        help="Start a server",
        description="Start a specified server instance"
    )
    start_parser.add_argument(
        "name",
        help="Name of the server to start"
    )
    start_parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force start without confirmation"
    )
    start_parser.set_defaults(func=server_start)
    
    # "stop" command
    stop_parser = server_subparsers.add_parser(
        "stop",
        help="Stop a server",
        description="Stop a specified server instance"
    )
    stop_parser.add_argument(
        "name",
        help="Name of the server to stop"
    )
    stop_parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force stop without confirmation"
    )
    stop_parser.add_argument(
        "-g", "--graceful",
        action="store_true",
        help="Perform a graceful shutdown"
    )
    stop_parser.set_defaults(func=server_stop)
```

### `cli_tool/commands/monitor.py`

```python
"""
System monitoring commands.

This module contains commands for monitoring system resources,
a common DevOps task for observability.
"""

import os
import sys
import time
import platform
import psutil
from ..utils import print_success, print_error, print_info, format_bytes


def monitor_cpu(args):
    """
    Monitor CPU usage and display information.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    print_info("CPU Monitoring")
    print_info("-------------")
    
    try:
        # Get CPU information
        cpu_count_logical = psutil.cpu_count(logical=True)
        cpu_count_physical = psutil.cpu_count(logical=False)
        cpu_freq = psutil.cpu_freq()
        
        # Display CPU information
        print_info(f"Physical cores: {cpu_count_physical}")
        print_info(f"Logical cores: {cpu_count_logical}")
        
        if cpu_freq:
            print_info(f"Current frequency: {cpu_freq.current:.2f} MHz")
            if hasattr(cpu_freq, 'min') and cpu_freq.min:
                print_info(f"Min frequency: {cpu_freq.min:.2f} MHz")
            if hasattr(cpu_freq, 'max') and cpu_freq.max:
                print_info(f"Max frequency: {cpu_freq.max:.2f} MHz")
        
        # Get and display CPU usage
        print_info("\nCPU Usage:")
        
        if args.per_cpu:
            # Show per-CPU usage
            per_cpu = psutil.cpu_percent(interval=1, percpu=True)
            for i, usage in enumerate(per_cpu):
                print_info(f"  Core {i}: {usage:.1f}%")
        
        # Show overall CPU usage
        overall_usage = psutil.cpu_percent(interval=1 if not args.per_cpu else 0)
        print_info(f"\nOverall CPU usage: {overall_usage:.1f}%")
        
        # Get and display CPU load
        try:
            load_avg = psutil.getloadavg()
            print_info(f"Load average: {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")
        except (AttributeError, OSError):
            # Not available on all platforms
            pass
        
        print_success("CPU monitoring completed")
        return 0
        
    except Exception as e:
        print_error(f"Error monitoring CPU: {str(e)}")
        return 1


def monitor_memory(args):
    """
    Monitor memory usage and display information.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    print_info("Memory Monitoring")
    print_info("----------------")
    
    try:
        # Get virtual memory information
        virtual_mem = psutil.virtual_memory()
        
        # Display memory information
        print_info(f"Total memory: {format_bytes(virtual_mem.total)}")
        print_info(f"Available memory: {format_bytes(virtual_mem.available)}")
        print_info(f"Used memory: {format_bytes(virtual_mem.used)} ({virtual_mem.percent:.1f}%)")
        print_info(f"Free memory: {format_bytes(virtual_mem.free)}")
        
        # Get and display swap information
        swap = psutil.swap_memory()
        print_info("\nSwap Information:")
        print_info(f"Total swap: {format_bytes(swap.total)}")
        print_info(f"Used swap: {format_bytes(swap.used)} ({swap.percent:.1f}%)")
        print_info(f"Free swap: {format_bytes(swap.free)}")
        
        print_success("Memory monitoring completed")
        return 0
        
    except Exception as e:
        print_error(f"Error monitoring memory: {str(e)}")
        return 1


def monitor_disk(args):
    """
    Monitor disk usage and display information.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    print_info("Disk Monitoring")
    print_info("--------------")
    
    try:
        # Determine the path to monitor
        path = args.path if hasattr(args, 'path') and args.path else "/"
        
        # Get disk usage for the specified path
        disk_usage = psutil.disk_usage(path)
        
        # Display disk usage information
        print_info(f"Path: {path}")
        print_info(f"Total space: {format_bytes(disk_usage.total)}")
        print_info(f"Used space: {format_bytes(disk_usage.used)} ({disk_usage.percent:.1f}%)")
        print_info(f"Free space: {format_bytes(disk_usage.free)}")
        
        # Show all disk partitions if requested
        if args.all:
            print_info("\nAll Disk Partitions:")
            partitions = psutil.disk_partitions(all=True)
            for i, partition in enumerate(partitions):
                print_info(f"\nPartition {i+1}:")
                print_info(f"  Device: {partition.device}")
                print_info(f"  Mountpoint: {partition.mountpoint}")
                print_info(f"  File system: {partition.fstype}")
                print_info(f"  Options: {partition.opts}")
                
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    print_info(f"  Total: {format_bytes(usage.total)}")
                    print_info(f"  Used: {format_bytes(usage.used)} ({usage.percent:.1f}%)")
                    print_info(f"  Free: {format_bytes(usage.free)}")
                except (PermissionError, OSError):
                    print_info("  Usage: Not accessible")
        
        print_success("Disk monitoring completed")
        return 0
        
    except Exception as e:
        print_error(f"Error monitoring disk: {str(e)}")
        return 1


def monitor_all(args):
    """
    Monitor all system resources and display information.
    
    Args:
        args: Command-line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    print_info("System Monitoring")
    print_info("----------------")
    
    try:
        # Display system information
        print_info(f"System: {platform.system()} {platform.release()}")
        print_info(f"Version: {platform.version()}")
        print_info(f"Machine: {platform.machine()}")
        print_info(f"Processor: {platform.processor()}")
        print_info(f"Node: {platform.node()}")
        print_info("")
        
        # Call individual monitoring functions
        cpu_result = monitor_cpu(args)
        print_info("")
        
        memory_result = monitor_memory(args)
        print_info("")
        
        disk_result = monitor_disk(args)
        
        # Monitor network if requested
        if args.network:
            print_info("")
            print_info("Network Monitoring")
            print_info("-----------------")
            
            # Get network IO statistics
            net_io = psutil.net_io_counters()
            
            print_info(f"Bytes sent: {format_bytes(net_io.bytes_sent)}")
            print_info(f"Bytes received: {format_bytes(net_io.bytes_recv)}")
            print_info(f"Packets sent: {net_io.packets_sent}")
            print_info(f"Packets received: {net_io.packets_recv}")
            print_info(f"Error in: {net_io.errin}")
            print_info(f"Error out: {net_io.errout}")
            print_info(f"Drop in: {net_io.dropin}")
            print_info(f"Drop out: {net_io.dropout}")
        
        # Return success if all monitoring functions succeeded
        if cpu_result == 0 and memory_result == 0 and disk_result == 0:
            print_success("\nSystem monitoring completed successfully")
            return 0
        else:
            print_warning("\nSystem monitoring completed with some errors")
            return 1
        
    except Exception as e:
        print_error(f"Error monitoring system: {str(e)}")
        return 1


def setup_monitor_commands(subparsers):
    """
    Set up the monitoring commands in the argument parser.
    
    Args:
        subparsers: Subparsers object from argparse
    """
    # Create parser for the "monitor" command
    monitor_parser = subparsers.add_parser(
        "monitor",
        help="System monitoring commands",
        description="Commands for monitoring system resources"
    )
    
    # Create subparsers for monitor commands
    monitor_subparsers = monitor_parser.add_subparsers(
        title="monitor commands",
        dest="monitor_command",
        help="Resource to monitor"
    )
    monitor_subparsers.required = True
    
    # "cpu" command
    cpu_parser = monitor_subparsers.add_parser(
        "cpu",
        help="Monitor CPU usage",
        description="Monitor and display CPU usage information"
    )
    cpu_parser.add_argument(
        "--per-cpu",
        action="store_true",
        help="Show usage per CPU core"
    )
    cpu_parser.set_defaults(func=monitor_cpu)
    
    # "memory" command
    memory_parser = monitor_subparsers.add_parser(
        "memory",
        help="Monitor memory usage",
        description="Monitor and display memory usage information"
    )
    memory_parser.set_defaults(func=monitor_memory)
    
    # "disk" command
    disk_parser = monitor_subparsers.add_parser(
        "disk",
        help="Monitor disk usage",
        description="Monitor and display disk usage information"
    )
    disk_parser.add_argument(
        "path",
        nargs="?",
        help="Path to check disk usage (default: root directory)"
    )
    disk_parser.add_argument(
        "--all",
        action="store_true",
        help="Show all disk partitions"
    )
    disk_parser.set_defaults(func=monitor_disk)
    
    # "all" command
    all_parser = monitor_subparsers.add_parser(
        "all",
        help="Monitor all system resources",
        description="Monitor and display all system resource information"
    )
    all_parser.add_argument(
        "--network",
        action="store_true",
        help="Include network statistics"
    )
    all_parser.add_argument(
        "--per-cpu",
        action="store_true",
        help="Show usage per CPU core"
    )
    all_parser.add_argument(
        "--all",
        action="store_true",
        help="Show all disk partitions"
    )
    all_parser.set_defaults(func=monitor_all)
```

### `cli_tool/commands/utils.py`

```python
"""
Utility functions for CLI commands.

This module contains utility functions used by various CLI commands.
"""

import sys
import os
from datetime import datetime

# Try to import colorama for cross-platform colored output
try:
    from colorama import init, Fore, Back, Style
    init()  # Initialize colorama
    HAS_COLORS = True
except ImportError:
    HAS_COLORS = False


def print_success(message):
    """
    Print a success message with formatting.
    
    Args:
        message (str): The message to print
    """
    if HAS_COLORS:
        print(f"{Fore.GREEN}✓ SUCCESS: {message}{Style.RESET_ALL}")
    else:
        print(f"✓ SUCCESS: {message}")


def print_error(message):
    """
    Print an error message with formatting.
    
    Args:
        message (str): The message to print
    """
    if HAS_COLORS:
        print(f"{Fore.RED}✗ ERROR: {message}{Style.RESET_ALL}", file=sys.stderr)
    else:
        print(f"✗ ERROR: {message}", file=sys.stderr)


def print_info(message):
    """
    Print an informational message with formatting.
    
    Args:
        message (str): The message to print
    """
    if HAS_COLORS:
        print(f"{Fore.BLUE}ℹ INFO: {message}{Style.RESET_ALL}")
    else:
        print(f"ℹ INFO: {message}")


def print_warning(message):
    """
    Print a warning message with formatting.
    
    Args:
        message (str): The message to print
    """
    if HAS_COLORS:
        print(f"{Fore.YELLOW}⚠ WARNING: {message}{Style.RESET_ALL}")
    else:
        print(f"⚠ WARNING: {message}")


def format_bytes(bytes_value, precision=2):
    """
    Format a byte value into a human-readable string.
    
    Args:
        bytes_value (int): The value in bytes
        precision (int): The number of decimal places to show
        
    Returns:
        str: Formatted string (e.g. "4.52 MB")
    """
    if bytes_value is None or bytes_value < 0:
        return "0 bytes"
    
    # Define unit suffixes
    suffixes = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    
    # Determine the appropriate suffix
    suffix_index = 0
    value = float(bytes_value)
    
    while value >= 1024 and suffix_index < len(suffixes) - 1:
        value /= 1024
        suffix_index += 1
    
    # Format the value with the appropriate precision
    if suffix_index == 0:
        # For bytes, show as an integer
        return f"{int(value)} {suffixes[suffix_index]}"
    else:
        # For KB and above, show with decimal places
        return f"{value:.{precision}f} {suffixes[suffix_index]}"


def confirm_action(prompt="Are you sure you want to continue?"):
    """
    Prompt the user for confirmation.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        bool: True if the user confirmed, False otherwise
    """
    while True:
        if HAS_COLORS:
            user_input = input(f"{Fore.YELLOW}{prompt} [y/N]: {Style.RESET_ALL}").strip().lower()
        else:
            user_input = input(f"{prompt} [y/N]: ").strip().lower()
        
        if user_input in ('y', 'yes'):
            return True
        elif user_input in ('', 'n', 'no'):
            return False
        else:
            print("Please answer with 'y' (yes) or 'n' (no).")


def get_timestamp():
    """
    Get a formatted timestamp for the current time.
    
    Returns:
        str: Formatted timestamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_terminal_size():
    """
    Get the size of the terminal window.
    
    Returns:
        tuple: (width, height) of the terminal in characters
    """
    try:
        return os.get_terminal_size()
    except (AttributeError, OSError):
        # Default fallback values
        return (80, 24)
```

### `cli_tool/commands/__init__.py`

```python
"""
CLI Tool Commands Package

This package contains the command implementations for the CLI tool.
"""

# Import command modules for setup
from . import server
from . import monitor
```

### `requirements.txt`

```
# LAB11 - CLI Tool Development
# Required dependencies

# Colored terminal output
colorama>=0.4.4

# System information
psutil>=5.9.0
```

## Key Learning Points

1. **Command-Line Interface Design**:
   - Using subparsers for complex command hierarchies
   - Adding help text and examples for user guidance
   - Implementing consistent command naming conventions
   - Providing appropriate default values

2. **Argument Parsing with `argparse`**:
   - Creating parsers and subparsers for command groups
   - Adding different types of arguments (positional, optional)
   - Using action types for flag arguments
   - Setting default values and help text

3. **Command Organization**:
   - Separating commands into logical groups
   - Using a modular approach with separate files
   - Implementing a consistent command structure
   - Creating setup functions for registering commands

4. **User Interaction**:
   - Adding colorful output for readability
   - Implementing confirmation prompts for destructive actions
   - Providing progress feedback during operations
   - Creating helpful error messages

5. **Resource Monitoring**:
   - Using `psutil` to gather system information
   - Formatting resource usage for easy reading
   - Implementing different monitoring scopes (all, specific)
   - Handling platform-specific features

6. **Error Handling**:
   - Using appropriate exit codes for different scenarios
   - Catching and handling exceptions gracefully
   - Providing context-specific error messages
   - Implementing proper cleanup on failure

## Common Issues and Troubleshooting

1. **Argument Parsing Errors**:
   - Ensure subparser 'dest' parameters are unique
   - Make sure required subparsers have the 'required=True' attribute
   - Handle the case when no command is provided
   - Check for missing function references in set_defaults()

2. **Cross-Platform Compatibility**:
   - Use colorama for cross-platform colored output
   - Handle platform-specific functionality gracefully
   - Use os.path for cross-platform path handling
   - Check for feature availability before use

3. **User Input Handling**:
   - Handle keyboard interrupts gracefully
   - Validate user input before processing
   - Provide clear error messages for invalid input
   - Implement safe defaults when input is missing

4. **Display Formatting**:
   - Adjust output based on terminal width
   - Use consistent formatting styles
   - Handle Unicode characters properly
   - Implement fallbacks for environments without color support

5. **Dependency Management**:
   - Handle missing optional dependencies gracefully
   - Check for required minimum versions
   - Provide clear error messages when dependencies are missing
   - Implement fallbacks for core functionality

## Extension Ideas

1. Implement a configuration file system to store settings
2. Add logging capabilities with different verbosity levels
3. Create a progress bar for long-running operations
4. Implement tab completion for command and argument names
5. Add support for environment variables for configuration
6. Create a plugin system for extending functionality
7. Implement command aliases for common operations
8. Add support for different output formats (JSON, YAML, Table)

## CLI Design Best Practices

1. **Command Structure**:
   - Use a consistent verb-noun structure (e.g., "get users", "create file")
   - Group related commands under a common namespace
   - Use subcommands for complex functionality
   - Maintain backward compatibility when adding new commands

2. **Argument Design**:
   - Use short and long options for common flags (-v, --verbose)
   - Make positional arguments intuitive and ordered by importance
   - Provide sensible default values
   - Use consistent naming across commands

3. **Help and Documentation**:
   - Include comprehensive help text for all commands and options
   - Provide examples in help text
   - Include version information
   - Implement a dedicated "help" command or option

4. **Error Handling**:
   - Return appropriate exit codes (0 for success, non-zero for failure)
   - Provide clear error messages
   - Include suggestions for fixing common errors
   - Implement verbose error modes for debugging

5. **User Experience**:
   - Provide feedback for long-running operations
   - Implement confirmation for destructive actions
   - Use color to highlight important information
   - Make output machine-parsable when needed 