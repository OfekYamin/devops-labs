# LAB06 - Task Scheduler Automation Solutions

This file provides a reference solution for the Task Scheduler Automation lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `tasks.py`

```python
#!/usr/bin/env python3
"""
LAB06 - Task Scheduler Automation (Tasks Module)

This module contains the definitions of tasks that will be scheduled.
Each task is implemented as a function that performs a specific job.

These tasks will be imported and scheduled in scheduler.py.
"""

import datetime
import time
import random
import os
import shutil
import psutil
import requests


def log_event(message, log_file="task_log.txt"):
    """
    Log a message with timestamp both to console and file.
    
    Args:
        message (str): The message to log
        log_file (str): The file to write logs to
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    
    # Print to console
    print(log_entry)
    
    # Write to log file
    with open(log_file, "a") as f:
        f.write(log_entry + "\n")


def check_system():
    """
    Simulated system check task.
    
    Checks CPU, memory, and disk usage and logs the status.
    """
    log_event("Performing system check...")
    
    try:
        # Simulate task duration
        time.sleep(2)
        
        # Get system metrics (if psutil is installed)
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            log_event(f"CPU usage: {cpu_percent}%")
            log_event(f"Memory usage: {memory.percent}%")
            log_event(f"Disk usage: {disk.percent}%")
            
            # Determine status based on resource usage
            if cpu_percent > 80 or memory.percent > 80 or disk.percent > 90:
                status = "Warning: High resource usage detected"
            else:
                status = "All systems normal"
                
        except (ImportError, NameError):
            # psutil not installed, use random status
            status = random.choice([
                "All systems normal",
                "Warning: High CPU usage detected",
                "Warning: Low disk space",
                "Warning: Memory usage high"
            ])
        
        log_event(f"System check result: {status}")
        return True
        
    except Exception as e:
        log_event(f"Error in system check: {str(e)}")
        return False


def backup_data(source_dir="./data", backup_dir="./backups"):
    """
    Simulated backup task.
    
    Args:
        source_dir (str): Directory to backup
        backup_dir (str): Where to store the backup
    
    Returns:
        bool: True if successful, False otherwise
    """
    log_event(f"Starting backup process: {source_dir} -> {backup_dir}")
    
    try:
        # Create directories if they don't exist
        os.makedirs(source_dir, exist_ok=True)
        os.makedirs(backup_dir, exist_ok=True)
        
        # Create a timestamped backup directory
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        os.makedirs(backup_path, exist_ok=True)
        
        # Simulate a backup operation
        time.sleep(3)  # Simulate time for copying files
        
        # Create a sample file in the backup directory to simulate backed up content
        with open(os.path.join(backup_path, "backup_info.txt"), "w") as f:
            f.write(f"Backup created at: {timestamp}\n")
            f.write(f"Source directory: {os.path.abspath(source_dir)}\n")
            f.write("This is a simulated backup file.\n")
        
        log_event(f"Backup completed successfully: {backup_path}")
        return True
        
    except Exception as e:
        log_event(f"Error in backup process: {str(e)}")
        return False


def cleanup_old_files(directory="./backups", max_age_days=7):
    """
    Clean up old files in a directory based on age.
    
    Args:
        directory (str): Directory to clean
        max_age_days (int): Maximum age of files to keep in days
    
    Returns:
        bool: True if successful, False otherwise
    """
    log_event(f"Starting cleanup of old files in {directory}")
    
    try:
        if not os.path.exists(directory):
            log_event(f"Directory {directory} does not exist, skipping cleanup")
            return True
            
        # Calculate cutoff time
        cutoff_time = time.time() - (max_age_days * 24 * 60 * 60)
        count_removed = 0
        
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for name in files:
                file_path = os.path.join(root, name)
                # Check file age
                if os.stat(file_path).st_mtime < cutoff_time:
                    os.remove(file_path)
                    count_removed += 1
                    log_event(f"Removed old file: {file_path}")
            
            # Also remove empty directories
            for name in dirs:
                dir_path = os.path.join(root, name)
                if not os.listdir(dir_path):  # Check if directory is empty
                    os.rmdir(dir_path)
                    log_event(f"Removed empty directory: {dir_path}")
        
        log_event(f"Cleanup completed. Removed {count_removed} old files.")
        return True
        
    except Exception as e:
        log_event(f"Error during cleanup: {str(e)}")
        return False


def check_website_status(url="https://www.example.com"):
    """
    Check if a website is available and measure response time.
    
    Args:
        url (str): The URL to check
    
    Returns:
        bool: True if successful, False otherwise
    """
    log_event(f"Checking website status: {url}")
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            log_event(f"Website {url} is UP (Status: {response.status_code}, Response time: {response_time:.2f}s)")
            return True
        else:
            log_event(f"Website {url} returned status code: {response.status_code}")
            return False
            
    except requests.RequestException as e:
        log_event(f"Error checking website {url}: {str(e)}")
        return False


def rotate_logs(log_file="task_log.txt", max_size_kb=1024, backup_count=3):
    """
    Rotate log files when they exceed a certain size.
    
    Args:
        log_file (str): The log file to rotate
        max_size_kb (int): Maximum file size in KB before rotation
        backup_count (int): Number of backup files to keep
    
    Returns:
        bool: True if rotation was performed, False otherwise
    """
    if not os.path.exists(log_file):
        return False
        
    # Check file size
    file_size_kb = os.path.getsize(log_file) / 1024
    
    if file_size_kb <= max_size_kb:
        return False  # No rotation needed
        
    log_event(f"Rotating log file: {log_file} ({file_size_kb:.2f} KB)")
    
    try:
        # Remove the oldest log file if it exists
        oldest_log = f"{log_file}.{backup_count}"
        if os.path.exists(oldest_log):
            os.remove(oldest_log)
            
        # Shift existing log files
        for i in range(backup_count - 1, 0, -1):
            src = f"{log_file}.{i}"
            dst = f"{log_file}.{i+1}"
            if os.path.exists(src):
                shutil.move(src, dst)
                
        # Rename the current log file
        shutil.move(log_file, f"{log_file}.1")
        
        # Create a new empty log file
        with open(log_file, "w") as f:
            f.write(f"Log rotated at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
        log_event("Log rotation completed")
        return True
        
    except Exception as e:
        print(f"Error during log rotation: {str(e)}")  # Use print since logging might fail
        return False


# This allows you to test the tasks directly
if __name__ == "__main__":
    print("Task Definitions Module")
    print("======================")
    print("This module contains tasks to be scheduled.")
    print("It's not meant to be run directly, but you can test tasks here.")
    
    print("\nTesting system_check task:")
    check_system()
    
    print("\nTesting backup_data task:")
    backup_data()
    
    print("\nTesting cleanup_old_files task:")
    cleanup_old_files()
    
    print("\nTesting website status check task:")
    check_website_status()
    
    print("\nTesting log rotation task:")
    rotate_logs()
```

## Complete Implementation of `scheduler.py`

```python
#!/usr/bin/env python3
"""
LAB06 - Task Scheduler Automation

This script implements a Python-based task scheduler that can run
recurring tasks at specified intervals without external scheduling tools.

Usage:
    python scheduler.py
"""

import time
import datetime
import threading
import schedule
import argparse
import signal
import sys
from tasks import (
    log_event,
    check_system,
    backup_data,
    cleanup_old_files,
    check_website_status,
    rotate_logs
)


def run_threaded(job_func, *args, **kwargs):
    """
    Run a scheduled job in its own thread.
    
    Args:
        job_func: The function to run in a thread
        *args, **kwargs: Arguments to pass to the function
    """
    job_thread = threading.Thread(target=job_func, args=args, kwargs=kwargs)
    job_thread.start()
    return job_thread


def setup_schedule(quick_demo=False):
    """
    Set up the task schedule.
    
    Args:
        quick_demo (bool): If True, schedule tasks more frequently for demo purposes
    """
    log_event("Setting up task scheduler...")
    
    # Schedule system checks
    if quick_demo:
        schedule.every(20).seconds.do(run_threaded, check_system)
    else:
        schedule.every(15).minutes.do(run_threaded, check_system)
    
    # Schedule data backups
    if quick_demo:
        schedule.every(1).minutes.do(run_threaded, backup_data)
    else:
        schedule.every().day.at("02:00").do(run_threaded, backup_data)
    
    # Schedule cleanup of old files
    if quick_demo:
        schedule.every(2).minutes.do(run_threaded, cleanup_old_files, max_age_days=0)
    else:
        schedule.every().week.do(run_threaded, cleanup_old_files)
    
    # Schedule website checks
    if quick_demo:
        schedule.every(30).seconds.do(run_threaded, check_website_status)
    else:
        schedule.every(1).hours.do(run_threaded, check_website_status)
    
    # Schedule log rotation
    if quick_demo:
        schedule.every(45).seconds.do(run_threaded, rotate_logs, max_size_kb=1)
    else:
        schedule.every().day.at("00:00").do(run_threaded, rotate_logs)
    
    # Add a heartbeat job
    if quick_demo:
        schedule.every(10).seconds.do(lambda: log_event("Scheduler heartbeat"))
    else:
        schedule.every(1).hours.do(lambda: log_event("Scheduler heartbeat"))
    
    log_event("Task scheduler initialized successfully")


def display_schedule():
    """Display all scheduled jobs."""
    log_event("Current schedule:")
    for job in schedule.get_jobs():
        log_event(f"  - {job}")


def handle_signal(signum, frame):
    """Handle termination signals gracefully."""
    log_event("Received signal to terminate")
    log_event("Shutting down scheduler...")
    sys.exit(0)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Task Scheduler Automation")
    parser.add_argument("--demo", action="store_true", help="Run in quick demo mode with shorter intervals")
    parser.add_argument("--display-only", action="store_true", help="Display schedule and exit")
    return parser.parse_args()


def main():
    """Main function to run the scheduler."""
    args = parse_arguments()
    
    print("Task Scheduler Automation")
    print("========================")
    
    # Set up signal handlers for graceful termination
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    
    try:
        # Set up the task schedule
        setup_schedule(quick_demo=args.demo)
        
        # Display the schedule
        display_schedule()
        
        if args.display_only:
            log_event("Display-only mode. Exiting.")
            return
        
        log_event("Scheduler started. Press Ctrl+C to exit.")
        
        # Run the scheduler in an infinite loop
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    except KeyboardInterrupt:
        log_event("Scheduler stopped by keyboard interrupt.")
    except Exception as e:
        log_event(f"Error in scheduler: {str(e)}")
    finally:
        log_event("Scheduler shutdown complete.")


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Task Scheduling Fundamentals**:
   - Using the `schedule` library to create recurring tasks
   - Setting up different scheduling patterns (interval, daily, weekly)
   - Understanding the main scheduler loop

2. **Task Management**:
   - Defining reusable task functions
   - Ensuring tasks are idempotent (can run multiple times safely)
   - Implementing proper error handling

3. **Concurrency with Threads**:
   - Running tasks in separate threads
   - Preventing the scheduler from being blocked by long-running tasks
   - Managing thread safety

4. **Logging and Monitoring**:
   - Creating structured logs with timestamps
   - Rotating log files
   - Implementing heartbeat tasks for monitoring

5. **Graceful Termination**:
   - Handling interrupt signals (Ctrl+C)
   - Cleaning up resources when shutting down
   - Using signal handlers

## Expected Output

```
Task Scheduler Automation
========================
[2023-06-10 14:30:00] Setting up task scheduler...
[2023-06-10 14:30:00] Task scheduler initialized successfully
[2023-06-10 14:30:00] Current schedule:
[2023-06-10 14:30:00]   - Every 20 seconds do run_threaded(check_system)
[2023-06-10 14:30:00]   - Every 1 minute do run_threaded(backup_data)
[2023-06-10 14:30:00]   - Every 2 minutes do run_threaded(cleanup_old_files, max_age_days=0)
[2023-06-10 14:30:00]   - Every 30 seconds do run_threaded(check_website_status)
[2023-06-10 14:30:00]   - Every 45 seconds do run_threaded(rotate_logs, max_size_kb=1)
[2023-06-10 14:30:00]   - Every 10 seconds do <lambda>()
[2023-06-10 14:30:00] Scheduler started. Press Ctrl+C to exit.
[2023-06-10 14:30:10] Scheduler heartbeat
[2023-06-10 14:30:20] Performing system check...
[2023-06-10 14:30:22] CPU usage: 15.2%
[2023-06-10 14:30:22] Memory usage: 68.4%
[2023-06-10 14:30:22] Disk usage: 54.9%
[2023-06-10 14:30:22] System check result: All systems normal
[2023-06-10 14:30:30] Checking website status: https://www.example.com
[2023-06-10 14:30:31] Website https://www.example.com is UP (Status: 200, Response time: 0.75s)
[2023-06-10 14:30:45] Rotating log file: task_log.txt (2.34 KB)
[2023-06-10 14:30:45] Log rotation completed
[2023-06-10 14:31:00] Starting backup process: ./data -> ./backups
[2023-06-10 14:31:03] Backup completed successfully: ./backups/backup_20230610_143100
```

## Common Issues and Troubleshooting

1. **Missed Schedule Events**:
   - The scheduler only runs tasks when `.run_pending()` is called
   - If the main thread is blocked, tasks will be delayed
   - Use threading to prevent long-running tasks from blocking the scheduler

2. **Thread Safety**:
   - Be careful with shared resources accessed from multiple threads
   - Use thread synchronization mechanisms if needed (locks, queues)
   - Avoid modifying the schedule from within tasks

3. **Resource Usage**:
   - Many threads can consume significant system resources
   - Monitor CPU and memory usage
   - Consider using a thread pool or limiting concurrent tasks

4. **Exception Handling**:
   - Unhandled exceptions in tasks can crash the scheduler
   - Wrap task code in try/except blocks
   - Log exceptions properly for debugging

5. **Time Zone Issues**:
   - Schedule uses the system's local time zone by default
   - Be explicit about time zones for international deployments
   - Test scheduled tasks that run at specific times thoroughly

## Extension Ideas

1. **Task Prioritization**:
   - Implement priority levels for tasks
   - Allow high-priority tasks to preempt lower-priority ones

2. **Persistent Schedule**:
   - Save the schedule to a database or file
   - Restore scheduled tasks after a restart

3. **Web-based Dashboard**:
   - Create a simple web interface to monitor tasks
   - Allow adding/removing tasks through the interface

4. **Task Dependencies**:
   - Implement a dependency system where tasks can depend on others
   - Skip dependent tasks if prerequisites fail

5. **Distributed Tasks**:
   - Extend to run tasks across multiple machines
   - Implement a work-stealing algorithm for load balancing

## Best Practices

1. **Idempotency**:
   - Design tasks to be idempotent (safe to run multiple times)
   - Handle partial execution and recovery

2. **Monitoring**:
   - Implement comprehensive logging
   - Add heartbeat or status checks
   - Set up alerting for task failures

3. **Resource Management**:
   - Clean up resources properly in tasks
   - Use context managers (`with` statements) for resource acquisition
   - Implement timeouts for long-running operations

4. **Configuration**:
   - Externalize schedule configuration
   - Allow dynamic schedule updates
   - Support different configurations for development/production

5. **Testing**:
   - Write unit tests for individual tasks
   - Test the scheduler with mocked time
   - Include integration tests for end-to-end verification
</rewritten_file> 