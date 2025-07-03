# LAB01 - Simple CLI Tool Solutions

This file provides a reference solution for the Simple CLI Calculator Tool lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `cli_tool.py`

```python
#!/usr/bin/env python3
"""
LAB01 - Simple CLI Calculator Tool

This script demonstrates how to build a command-line interface (CLI) tool using argparse.
The tool performs basic arithmetic operations based on user input.

Usage:
    python cli_tool.py 10 5 --op add     # Result: 15
    python cli_tool.py 10 5 --op sub     # Result: 5
    python cli_tool.py 10 5 --op mul     # Result: 50
    python cli_tool.py 10 5 --op div     # Result: 2.0
    python cli_tool.py 10 5 --op pow     # Result: 100000
    python cli_tool.py 10 5 --op mod     # Result: 0
"""

import argparse
import sys


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="A simple command-line calculator tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Add arguments to the parser
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    parser.add_argument(
        "--op", 
        choices=["add", "sub", "mul", "div", "pow", "mod"], 
        default="add", 
        help="Operation to perform"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Perform calculation based on the operation
    result = calculate(args.x, args.y, args.op)
    
    # Display result to user
    if result is not None:
        print(f"Result: {result}")
    
    # Display available commands
    print("\nAvailable Operations:")
    print("  python cli_tool.py <x> <y> --op add  # Addition")
    print("  python cli_tool.py <x> <y> --op sub  # Subtraction")
    print("  python cli_tool.py <x> <y> --op mul  # Multiplication")
    print("  python cli_tool.py <x> <y> --op div  # Division")
    print("  python cli_tool.py <x> <y> --op pow  # Exponentiation")
    print("  python cli_tool.py <x> <y> --op mod  # Modulo")


def calculate(x, y, operation):
    """
    Perform calculation based on the specified operation.
    
    Args:
        x (float): First number
        y (float): Second number
        operation (str): Operation to perform
        
    Returns:
        float: Result of the calculation
    """
    if operation == "add":
        return x + y
    elif operation == "sub":
        return x - y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        try:
            return x / y
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None
    elif operation == "pow":
        return x ** y
    elif operation == "mod":
        try:
            return x % y
        except ZeroDivisionError:
            print("Error: Modulo by zero is not allowed.")
            return None
    else:
        print(f"Error: Unknown operation '{operation}'.")
        return None


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Setting Up argparse**:
   - Import the module (`import argparse`)
   - Create an argument parser (`parser = argparse.ArgumentParser()`)
   - Define positional and optional arguments
   - Parse the command-line arguments with `parser.parse_args()`

2. **Argument Types**:
   - **Positional arguments**: Required inputs in a specific order (e.g., `x` and `y`)
   - **Optional arguments**: Preceded by flags like `--op` and may have default values

3. **Control Flow**:
   - Use if/elif/else or match/case (Python 3.10+) to handle different operations
   - Organize code with functions for better readability and maintainability

4. **Error Handling**:
   - Handle potential errors like division by zero
   - Provide meaningful error messages to users

## Expected Output

```
$ python cli_tool.py 10 5 --op add
Result: 15.0

Available Operations:
  python cli_tool.py <x> <y> --op add  # Addition
  python cli_tool.py <x> <y> --op sub  # Subtraction
  python cli_tool.py <x> <y> --op mul  # Multiplication
  python cli_tool.py <x> <y> --op div  # Division
  python cli_tool.py <x> <y> --op pow  # Exponentiation
  python cli_tool.py <x> <y> --op mod  # Modulo

$ python cli_tool.py 10 5 --op div
Result: 2.0

Available Operations:
  python cli_tool.py <x> <y> --op add  # Addition
  python cli_tool.py <x> <y> --op sub  # Subtraction
  python cli_tool.py <x> <y> --op mul  # Multiplication
  python cli_tool.py <x> <y> --op div  # Division
  python cli_tool.py <x> <y> --op pow  # Exponentiation
  python cli_tool.py <x> <y> --op mod  # Modulo
```

## Common Issues and Troubleshooting

1. **TypeError**: Make sure to convert input strings to appropriate types (e.g., `type=float` in argparse)
2. **ZeroDivisionError**: Handle division or modulo by zero with try/except blocks
3. **Command not found**: Ensure you're running the script from the correct directory
4. **Invalid operation**: Make sure to use one of the operations specified in the `choices` parameter

## Extension Ideas

1. Add more operations like square root, factorial, etc.
2. Support multiple operations in a single command
3. Add a verbose mode that shows the equation before the result
4. Create a REPL (Read-Eval-Print Loop) mode for continuous calculations
5. Save calculation history to a file

## Best Practices

1. Use docstrings to document your code
2. Organize code into functions with single responsibilities
3. Handle errors gracefully with informative messages
4. Provide helpful usage examples
5. Use type hints for better code readability (Python 3.6+) 