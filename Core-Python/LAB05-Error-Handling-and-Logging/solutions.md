# LAB05 - Error Handling and Logging Solutions

This document contains the complete solution for the Error Handling and Logging lab exercises. Use this as a reference after attempting the lab on your own.

## Complete Implementation of `main.py`

```python
#!/usr/bin/env python3
"""
LAB05 - Error Handling and Logging in Python

Instructions:
1. Complete the code blocks below to implement error handling and logging
2. Run the script to see how exceptions are managed
3. Check the app.log file to view your log entries
"""

# TODO: 1. Import the logging module
import logging

# TODO: 2. Configure basic logging
# Set up logging to write to "app.log" with a level of INFO and appropriate format
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# TODO: 3. Write some initial log messages
# Log an INFO message that the program is starting
logging.info("Program started")

# TODO: 4. Handle division by zero exception
print("Division Operation")
print("-----------------")
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print(f"Result: 100 / {num} = {result}")
    logging.info(f"Successfully divided 100 by {num}, result: {result}")
except ZeroDivisionError:
    error_msg = "Error: Division by zero attempted"
    print(error_msg)
    logging.error(error_msg)
except ValueError:
    error_msg = "Error: Invalid input! Please enter a valid number"
    print(error_msg)
    logging.error(error_msg)
finally:
    print("Division operation completed")
    logging.info("Division operation completed")

# TODO: 5. Handle file operations with exceptions
print("\nFile Operation")
print("-------------")
try:
    with open("config.json", "r") as file:
        content = file.read()
        print(f"Successfully read config.json: {content[:50]}...")
        logging.info("Successfully read config.json file")
except FileNotFoundError as e:
    error_msg = f"Error: Config file not found - {e}"
    print(error_msg)
    logging.error(error_msg)

# TODO: 6. Create and raise a custom exception
print("\nCustom Exception")
print("----------------")

class InvalidValueError(Exception):
    """Custom exception for invalid values in our application"""
    pass

def validate_age(age):
    """Validate that an age is reasonable for a working professional"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 18:
        raise InvalidValueError("Age must be at least 18 for a working professional")
    if age > 100:
        raise InvalidValueError("Age must be realistic (<=100)")
    return True

# Test the custom exception
try:
    # Try different values: 25, 15, 150, "thirty"
    test_age = 25
    print(f"Validating age: {test_age}")
    validate_age(test_age)
    print(f"Age {test_age} is valid")
    logging.info(f"Age validation passed for {test_age}")
except InvalidValueError as e:
    print(f"Validation Error: {e}")
    logging.error(f"Age validation failed: {e}")
except TypeError as e:
    print(f"Type Error: {e}")
    logging.error(f"Age validation failed: {e}")

# TODO: 7. Bonus: Different logging levels
print("\nDemonstrating Logging Levels")
print("--------------------------")

# Temporarily change logging level to DEBUG to show all levels
logging.getLogger().setLevel(logging.DEBUG)

logging.debug("This is a DEBUG message - detailed information for troubleshooting")
logging.info("This is an INFO message - confirmation that things are working")
logging.warning("This is a WARNING message - something unexpected, but not an error")
logging.error("This is an ERROR message - something failed, but the program continues")
logging.critical("This is a CRITICAL message - a serious error that might stop the program")

# Reset to INFO level
logging.getLogger().setLevel(logging.INFO)

print("\nGreat job! You've successfully practiced error handling and logging.")
print("Check the app.log file to see your logged messages.")
```

## Key Learning Points

1. **Exception Handling**: 
   - The `try-except-finally` structure for handling exceptions
   - Catching specific exception types (`ZeroDivisionError`, `ValueError`, etc.)
   - Using the `finally` block for cleanup code that always executes

2. **Logging Setup**:
   - Configuring logging with `logging.basicConfig()`
   - Setting appropriate log levels and formats
   - Writing logs to a file

3. **Log Levels**:
   - DEBUG: Detailed information for troubleshooting
   - INFO: Confirmation that things are working as expected
   - WARNING: Something unexpected happened, but not an error
   - ERROR: A more serious problem, some functionality may be affected
   - CRITICAL: A very serious error that might cause the program to fail

4. **Custom Exceptions**:
   - Creating custom exception classes
   - Raising exceptions with meaningful messages
   - Handling different exception types appropriately

## Best Practices

1. **Exception Handling**:
   - Catch specific exceptions rather than using bare `except` statements
   - Keep exception handling blocks small and focused
   - Include helpful error messages that describe what went wrong

2. **Logging**:
   - Use appropriate log levels based on the severity of the message
   - Include relevant context in log messages
   - Structure log formats to include timestamp, severity, and message

3. **Error Messages**:
   - Make error messages user-friendly and actionable
   - Log technical details for debugging, but show simplified messages to users
   - Include remediation steps when possible

## Common Issues and Troubleshooting

1. **Log File Access**:
   - Problem: Permission errors when writing to log files
   - Solution: Ensure the application has write permissions to the directory

2. **Excessive Logging**:
   - Problem: Log files grow too large too quickly
   - Solution: Use appropriate log levels and implement log rotation

3. **Silent Failures**:
   - Problem: Exceptions are caught but not logged or reported
   - Solution: Always log exceptions, even if they're handled silently

4. **Exception Handling Scope**:
   - Problem: Try blocks that are too large make it hard to identify error sources
   - Solution: Keep try blocks as small as possible while still being functional

## Cleanup Procedures

After running the script, you may want to clean up the log file if it's no longer needed:

```python
import os

# Remove the log file
if os.path.exists("app.log"):
    os.remove("app.log")
    print("Removed app.log")
```

This cleanup is optional, as you might want to keep the logs for future reference. 