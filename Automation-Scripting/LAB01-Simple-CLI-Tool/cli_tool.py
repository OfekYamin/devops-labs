#!/usr/bin/env python3
"""
LAB01 - Simple CLI Calculator Tool

This script demonstrates how to build a command-line interface (CLI) tool using argparse.
The tool performs basic arithmetic operations based on user input.

Usage:
    python cli_tool.py 10 5 --op add     # Addition
    python cli_tool.py 10 5 --op sub     # Subtraction
    python cli_tool.py 10 5 --op mul     # Multiplication
    python cli_tool.py 10 5 --op div     # Division
"""

# TODO: Import the required modules
# import argparse
# import sys


def main():
    """Main function to set up and run the CLI calculator."""
    # TODO: Create an argument parser with a description
    
    # TODO: Add arguments for the numbers and operation
    # - Add x as first positional argument (number)
    # - Add y as second positional argument (number)
    # - Add --op as optional argument with choices and default value
    
    # TODO: Parse the arguments
    
    # TODO: Perform the calculation based on the operation
    
    # TODO: Display the result to the user
    
    # Optional: Display available commands
    pass


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
    # TODO: Implement the calculation logic for different operations
    # - Addition (add)
    # - Subtraction (sub)
    # - Multiplication (mul)
    # - Division (div)
    # - Handle potential errors (like division by zero)
    pass


if __name__ == "__main__":
    main()