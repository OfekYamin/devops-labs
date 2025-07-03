#!/usr/bin/env python3
"""
LAB06 - Task Scheduler Automation

This script implements a Python-based task scheduler that can run
recurring tasks at specified intervals without external scheduling tools.

Usage:
    python scheduler.py
"""

# TODO: Import necessary modules
# You'll need the 'schedule' library and your tasks module


# TODO: Define the setup_schedule function
# This function should:
# - Set up all the tasks with their schedules
# - Use schedule.every().interval.do(task) syntax
# - Log the initialization


# TODO: Add any helper functions needed
# For example, a function to clear old logs or display the schedule


if __name__ == "__main__":
    print("Task Scheduler Automation")
    print("========================")
    
    # TODO: Set up the task schedule
    
    # TODO: Implement the main loop
    # The loop should:
    # - Run pending tasks
    # - Sleep for a short interval
    # - Handle clean termination (Ctrl+C)
    
    # Example:
    # try:
    #     setup_schedule()
    #     print("Scheduler started. Press Ctrl+C to exit.")
    #     
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     print("\nScheduler stopped by user.")
    
    print("\nRemember to install dependencies:")
    print("pip install schedule") 