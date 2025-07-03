#!/usr/bin/env python3
"""
LAB03 - Process Logs and Generate Reports

This script analyzes log files, extracts meaningful information,
and generates summary reports based on the findings.

Usage:
    python parser.py
"""

# TODO: Define a function to read the log file
# The function should:
# - Open the log file
# - Read all lines
# - Return the content as a list of lines


# TODO: Define a function to analyze the logs
# The function should:
# - Count occurrences of different log levels (ERROR, WARNING, INFO, DEBUG)
# - Identify the time range of the logs (first and last timestamp)
# - Optionally: Extract specific types of events (e.g., failed logins, service errors)


# TODO: Define a function to generate a report
# The function should:
# - Create a new file called "report.txt"
# - Write a summary of the findings
# - Include counts, percentages, and notable events


# TODO: BONUS - Add more advanced analysis
# Some ideas:
# - Group errors by type or service
# - Detect patterns or trends (e.g., increasing error rates)
# - Calculate time between related events
# - Identify peak activity periods


if __name__ == "__main__":
    print("Log Analysis Tool")
    print("================")
    
    # TODO: Implement the main program flow
    # 1. Read the log file
    # 2. Analyze the logs
    # 3. Generate the report
    
    # Example implementation (uncomment and modify after completing the functions):
    # logs = read_log_file("logs.txt")
    # analysis_results = analyze_logs(logs)
    # generate_report(analysis_results)
    
    print("Analysis complete. Check report.txt for details.")


# Sample report output format:
"""
LOG ANALYSIS REPORT
==================
Generated: 2023-05-16 14:30:22

SUMMARY STATISTICS
-----------------
Total log entries: 35
Time range: 2023-05-15 08:12:34 to 2023-05-15 23:59:59

LOG LEVEL BREAKDOWN
------------------
ERROR:   5 (14.3%)
WARNING: 5 (14.3%)
INFO:    15 (42.9%)
DEBUG:   10 (28.6%)

TOP ERROR TYPES
--------------
- Connection/timeout issues: 2
- Permission problems: 1
- Deployment failures: 1
- Out of memory errors: 1

NOTABLE EVENTS
-------------
- System experienced database connectivity issues at 09:05:43
- Deployment of v2.3.4 failed at 14:20:41
- Authentication service downtime for 18 minutes around 23:05:42
""" 