# LAB05 - Error Handling and Logging in Python

Writing robust, production-ready Python code requires effective error handling and logging strategies. In this lab, you'll learn how to catch and manage exceptions and implement a comprehensive logging system - essential skills for creating reliable DevOps tools and automation scripts.

---

## 🎯 Objectives

By the end of this lab, you will:
- Master Python's exception handling with `try`, `except`, `else`, and `finally` blocks
- Create and raise custom exceptions for specific error cases
- Configure and use the built-in `logging` module for effective debugging and monitoring
- Understand and apply appropriate logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Implement file-based logging with formatted output
- Learn best practices for error management in production code
- Create user-friendly error messages while logging technical details

---

## 🧰 Prerequisites

- Completion of LAB04 (File Handling)
- Python 3.8+ installed on your system
- Basic understanding of Python syntax, functions, and file operations
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB05-Error-Handling-and-Logging/
├── main.py                # Python script with TODOs to implement
├── app.log                # Log file that will be created during execution
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB05-Error-Handling-and-Logging/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `main.py` in your code editor and follow the TODO comments.

---

## ✍️ Your Task

Open the `main.py` file and complete all the TODOs to learn about error handling and logging:

1. Set up basic logging:
   - Import the logging module
   - Configure logging to write to "app.log" file
   - Set an appropriate logging level (INFO)
   - Define a format that includes timestamp, log level, and message
   - Log an initial INFO message indicating the program has started

2. Handle division errors:
   - Create a try-except-finally block for division operations
   - Get a number from the user with `input()`
   - Attempt to divide 100 by the user's number
   - Catch `ZeroDivisionError` when the user enters zero
   - Catch `ValueError` when the user enters a non-number
   - Log appropriate error messages
   - Use a finally block to indicate the operation is complete

3. Handle file operations:
   - Create a try-except block to open a non-existent file
   - Attempt to open and read "config.json"
   - Catch and handle `FileNotFoundError`
   - Log detailed error information

4. Create and use a custom exception:
   - Define a custom exception class `InvalidValueError`
   - Create a validation function that raises this exception
   - Use a try-except block to handle the custom exception
   - Log information about validation success or failure

5. Implement different logging levels:
   - Write log messages using all five logging levels
   - Use DEBUG for detailed troubleshooting information
   - Use INFO for general operational events
   - Use WARNING for unexpected events that don't cause errors
   - Use ERROR for problems that prevent functionality
   - Use CRITICAL for serious errors that might crash the program

---

## 🧪 Validation Checklist

✅ Your logging configuration is correctly set up with appropriate format and level  
✅ Division by zero is properly caught and handled  
✅ Invalid input (non-numeric) is properly caught and handled  
✅ File not found errors are properly caught and logged  
✅ Your custom exception works correctly for validation scenarios  
✅ All five logging levels are demonstrated in your code  
✅ The app.log file contains appropriate entries after running your script  
✅ Error messages are user-friendly while log messages contain technical details  
✅ Your script runs without crashing despite encountering errors  

Run your script with:
```bash
python main.py
```

After running, check the contents of `app.log` to verify your logging implementation.

---

## 📚 Error Handling and Logging Concepts

- **Exception Handling**:
  - **`try`**: Block where exceptions might occur
  - **`except`**: Catches and handles specific exceptions
  - **`except Exception as e`**: Captures exception object for inspection
  - **`else`**: Executes when no exception occurs
  - **`finally`**: Always executes, regardless of exceptions
  - **`raise`**: Manually triggers an exception

- **Custom Exceptions**:
  - Inherit from built-in Exception class or its subclasses
  - Provide specific error types for your application
  - Include meaningful error messages
  - Example: `class CustomError(Exception): pass`

- **Logging Levels** (from lowest to highest severity):
  - **DEBUG**: Detailed information for diagnosing problems
  - **INFO**: Confirmation that things are working as expected
  - **WARNING**: Something unexpected, but not necessarily an error
  - **ERROR**: A more serious problem that prevented something from working
  - **CRITICAL**: A very serious error that might cause program failure

- **Logging Configuration**:
  - `logging.basicConfig()`: Sets up the logging system
  - `filename`: Where to save log entries
  - `level`: Minimum severity level to record
  - `format`: How to format log messages
  - Common formatters: `%(asctime)s`, `%(levelname)s`, `%(message)s`

- **Best Practices**:
  - Be specific about which exceptions to catch
  - Don't use bare `except:` statements (too broad)
  - Log both entry and exit of critical code sections
  - Include context in log messages (function name, input values)
  - Use different log levels appropriately

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Implement log rotation to manage log file size
2. Create a context manager using `__enter__` and `__exit__` methods
3. Set up a root logger and child loggers for different modules
4. Implement different handlers for console and file logging
5. Add exception chaining with the `raise ... from ...` syntax
6. Create a decorator for logging function calls and exceptions

---

## 💬 What's Next?

Next: [LAB06 - OOP and Classes](../LAB06-OOP-and-Classes/) to learn about object-oriented programming in Python - a powerful paradigm for creating modular, reusable code through classes and objects.

---

## 🙏 Acknowledgments

Error handling and logging are essential components of production-ready code. The skills you've learned in this lab will help you create more robust, maintainable applications that gracefully handle unexpected situations and provide useful information for debugging and monitoring.

Happy coding! 🛡️🐍

