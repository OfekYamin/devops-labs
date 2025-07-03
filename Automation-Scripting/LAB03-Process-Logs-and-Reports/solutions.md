# LAB03 - Process Logs and Generate Reports Solutions

This file provides a reference solution for the Log Processing and Reporting lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `parser.py`

```python
#!/usr/bin/env python3
"""
LAB03 - Process Logs and Generate Reports

This script analyzes log files, extracts meaningful information,
and generates summary reports based on the findings.

Usage:
    python parser.py
"""

import re
import os
import datetime
from collections import defaultdict, Counter


def read_log_file(file_path):
    """
    Read the log file and return its contents as a list of lines.
    
    Args:
        file_path (str): Path to the log file
        
    Returns:
        list: List of log lines
    """
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading log file: {e}")
        return []


def parse_log_line(line):
    """
    Parse a log line into its components.
    
    Args:
        line (str): A single log line
        
    Returns:
        dict: Parsed log entry with timestamp, level, and message
    """
    # Use regex to parse log format: [timestamp] LEVEL: message
    match = re.match(r'\[(.*?)\] (\w+): (.*)', line.strip())
    
    if match:
        timestamp_str, level, message = match.groups()
        try:
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            return {
                "timestamp": timestamp,
                "level": level,
                "message": message
            }
        except ValueError:
            print(f"Warning: Invalid timestamp format in line: {line}")
    
    return None


def analyze_logs(logs):
    """
    Analyze log entries to extract metrics and insights.
    
    Args:
        logs (list): List of log lines
        
    Returns:
        dict: Analysis results including counts, time range, and patterns
    """
    results = {
        "total_entries": 0,
        "level_counts": defaultdict(int),
        "start_time": None,
        "end_time": None,
        "error_types": [],
        "notable_events": []
    }
    
    parsed_logs = []
    
    # Parse each log line
    for line in logs:
        entry = parse_log_line(line)
        if entry:
            parsed_logs.append(entry)
            
            # Count by log level
            results["level_counts"][entry["level"]] += 1
            
            # Track time range
            if results["start_time"] is None or entry["timestamp"] < results["start_time"]:
                results["start_time"] = entry["timestamp"]
            if results["end_time"] is None or entry["timestamp"] > results["end_time"]:
                results["end_time"] = entry["timestamp"]
            
            # Collect error types
            if entry["level"] == "ERROR":
                error_type = categorize_error(entry["message"])
                results["error_types"].append(error_type)
            
            # Identify notable events
            if is_notable_event(entry):
                results["notable_events"].append(entry)
    
    results["total_entries"] = len(parsed_logs)
    
    # Count error types
    results["error_type_counts"] = Counter(results["error_types"])
    
    return results


def categorize_error(message):
    """
    Categorize error messages into types.
    
    Args:
        message (str): Error message
        
    Returns:
        str: Error category
    """
    if any(term in message.lower() for term in ["connect", "timeout", "unreachable"]):
        return "Connection/timeout issues"
    elif any(term in message.lower() for term in ["permission", "access", "denied"]):
        return "Permission problems"
    elif any(term in message.lower() for term in ["deploy", "installation"]):
        return "Deployment failures"
    elif any(term in message.lower() for term in ["memory", "allocation", "overflow"]):
        return "Out of memory errors"
    elif any(term in message.lower() for term in ["service", "unavailable", "responding"]):
        return "Service availability issues"
    else:
        return "Other errors"


def is_notable_event(entry):
    """
    Determine if a log entry represents a notable event.
    
    Args:
        entry (dict): Parsed log entry
        
    Returns:
        bool: True if the entry is a notable event
    """
    level = entry["level"]
    message = entry["message"].lower()
    
    # Consider errors as notable
    if level == "ERROR":
        return True
    
    # Consider certain warnings as notable
    if level == "WARNING" and any(term in message for term in ["failed", "unusual", "high", "limit"]):
        return True
    
    # Consider specific service events as notable
    if "service" in message and any(term in message for term in ["restart", "down", "unavailable"]):
        return True
    
    # Consider deployment or rollback events as notable
    if any(term in message for term in ["deploy", "rollback"]):
        return True
        
    return False


def generate_report(results, output_file="report.txt"):
    """
    Generate a report file from the analysis results.
    
    Args:
        results (dict): Analysis results
        output_file (str): Path to the output report file
        
    Returns:
        bool: True if report was generated successfully
    """
    try:
        with open(output_file, "w") as report:
            # Header
            report.write("LOG ANALYSIS REPORT\n")
            report.write("==================\n")
            report.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Summary statistics
            report.write("SUMMARY STATISTICS\n")
            report.write("-----------------\n")
            report.write(f"Total log entries: {results['total_entries']}\n")
            
            if results["start_time"] and results["end_time"]:
                start_time_str = results["start_time"].strftime("%Y-%m-%d %H:%M:%S")
                end_time_str = results["end_time"].strftime("%Y-%m-%d %H:%M:%S")
                report.write(f"Time range: {start_time_str} to {end_time_str}\n\n")
            
            # Log level breakdown
            report.write("LOG LEVEL BREAKDOWN\n")
            report.write("------------------\n")
            
            total = results["total_entries"]
            for level, count in sorted(results["level_counts"].items()):
                percentage = (count / total) * 100 if total > 0 else 0
                report.write(f"{level:<7} {count:>3} ({percentage:.1f}%)\n")
            
            report.write("\n")
            
            # Top error types
            if results["error_type_counts"]:
                report.write("TOP ERROR TYPES\n")
                report.write("--------------\n")
                
                for error_type, count in results["error_type_counts"].most_common():
                    report.write(f"- {error_type}: {count}\n")
                
                report.write("\n")
            
            # Notable events
            if results["notable_events"]:
                report.write("NOTABLE EVENTS\n")
                report.write("-------------\n")
                
                for event in results["notable_events"]:
                    time_str = event["timestamp"].strftime("%H:%M:%S")
                    report.write(f"- {event['message']} at {time_str}\n")
        
        print(f"Report successfully generated: {os.path.abspath(output_file)}")
        return True
        
    except Exception as e:
        print(f"Error generating report: {e}")
        return False


def main():
    """Main function to execute the log analysis workflow."""
    log_file = "logs.txt"
    output_file = "report.txt"
    
    print("Log Analysis Tool")
    print("================")
    
    # Read the log file
    print(f"Reading log file: {log_file}")
    logs = read_log_file(log_file)
    
    if not logs:
        print("No logs to analyze. Exiting.")
        return
    
    # Analyze the logs
    print(f"Analyzing {len(logs)} log entries...")
    analysis_results = analyze_logs(logs)
    
    # Generate the report
    print("Generating report...")
    generate_report(analysis_results, output_file)
    
    print(f"Analysis complete. Check {output_file} for details.")


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Reading and Parsing Logs**:
   - Open and read text files with proper error handling
   - Use regular expressions to parse structured log lines
   - Convert string timestamps to datetime objects for comparison

2. **Data Analysis and Aggregation**:
   - Count occurrences by category (log levels)
   - Track ranges (first and last timestamps)
   - Group similar items (error types)
   - Identify patterns or notable events

3. **Report Generation**:
   - Format data in a human-readable way
   - Calculate statistics like percentages
   - Organize information in logical sections

4. **Text Processing Techniques**:
   - String manipulation for text extraction
   - Case-insensitive searching with `.lower()`
   - Pattern matching with `in` operator or regex

5. **Error Handling**:
   - Handle file not found errors
   - Manage parsing failures gracefully
   - Validate input data

## Expected Output

The generated `report.txt` would look like:

```
LOG ANALYSIS REPORT
==================
Generated: 2023-05-16 14:30:22

SUMMARY STATISTICS
-----------------
Total log entries: 35
Time range: 2023-05-15 08:12:34 to 2023-05-15 23:59:59

LOG LEVEL BREAKDOWN
------------------
DEBUG    5 (14.3%)
ERROR    5 (14.3%)
INFO    15 (42.9%)
WARNING  5 (14.3%)

TOP ERROR TYPES
--------------
- Connection/timeout issues: 2
- Permission problems: 1
- Deployment failures: 1
- Out of memory errors: 1
- Service availability issues: 1

NOTABLE EVENTS
-------------
- Failed to connect to database - Connection timeout at 09:05:43
- Permission denied when accessing /etc/restricted/config.json at 12:05:12
- Deployment failed - Missing dependency: libcrypto.so.1.1 at 14:20:41
- Security scan failed on host 192.168.1.45 - Port timeout at 16:25:45
- Out of memory error in worker process #8 at 18:01:55
- Service unavailable - Authentication service not responding at 23:05:42
```

## Common Issues and Troubleshooting

1. **File Path Problems**: Make sure the log file path is correct relative to where the script is run
2. **Parsing Errors**: Log formats may vary; adjust your regex pattern if logs have a different format
3. **Date/Time Parsing**: Ensure timestamp format in the code matches the log file format
4. **Memory Issues**: For very large log files, consider processing them line by line instead of loading all at once
5. **Character Encoding**: Some logs may use special encodings; specify encoding when opening files if needed

## Extension Ideas

1. **Advanced Filtering**: Filter logs by date range, specific services, or keywords
2. **Visualization**: Generate charts or graphs from log analysis (using matplotlib)
3. **Pattern Detection**: Identify sequences of events that indicate problems
4. **Real-time Monitoring**: Process logs as they're written using file watching
5. **Multi-file Analysis**: Compare or consolidate logs from multiple sources

## Best Practices

1. **Modular Code**: Break down tasks into separate functions with specific responsibilities
2. **Robust Error Handling**: Always anticipate and handle potential errors in file operations
3. **Efficient Parsing**: Use regular expressions for structured text but don't over-complicate them
4. **Memory Efficiency**: Process large files in chunks rather than loading entirely into memory
5. **Documentation**: Include clear docstrings and comments, especially for regex patterns 