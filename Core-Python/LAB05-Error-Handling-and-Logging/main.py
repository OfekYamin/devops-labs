#!/usr/bin/env python3
"""
LAB05 - Error Handling and Logging in Python

Instructions:
1. Complete the code blocks below to implement error handling and logging
2. Run the script to see how exceptions are managed
3. Check the app.log file to view your log entries
"""

# TODO: 1. Import the logging module
# Import the necessary module for logging


# TODO: 2. Configure basic logging
# Set up logging to write to "app.log" with a level of INFO and appropriate format
# Format should include timestamp, log level, and message


# TODO: 3. Write some initial log messages
# Log an INFO message that the program is starting


# TODO: 4. Handle division by zero exception
# Create a try-except-finally block that:
# - Asks the user for a number (use input())
# - Divides 100 by that number
# - Handles both ZeroDivisionError and ValueError with appropriate messages
# - Logs any errors that occur
# - Uses a finally block to indicate execution is complete


# TODO: 5. Handle file operations with exceptions
# Create a try-except block that:
# - Attempts to open and read a file called "config.json"
# - Catches FileNotFoundError and logs the error
# - Logs a success message if the file opens correctly


# TODO: 6. Create and raise a custom exception
# Define a custom exception class called "InvalidValueError"
# Create a function that checks a value and raises this exception if the value is invalid
# Call this function in a try-except block and handle the custom exception


# TODO: 7. Bonus: Different logging levels
# Log messages with different severity levels:
# - DEBUG (detailed information for debugging)
# - INFO (confirmation that things are working)
# - WARNING (something unexpected, but the program still works)
# - ERROR (a more serious problem, some functionality is unavailable)
# - CRITICAL (a very serious error, the program might stop running)


print("\nGreat job! You've successfully practiced error handling and logging.")
print("Check the app.log file to see your logged messages.")
print("Run this script with: python main.py") 