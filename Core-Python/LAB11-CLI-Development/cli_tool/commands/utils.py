"""
Utility functions for CLI commands.

This module contains utility functions used by various CLI commands.
"""

# TODO: Import required libraries
# import sys
# import os
# from datetime import datetime


def print_success(message):
    """
    Print a success message with formatting.
    
    Args:
        message (str): The message to print
    """
    # TODO: Implement success message formatting
    # Use green color if available
    print(f"✓ SUCCESS: {message}")


def print_error(message):
    """
    Print an error message with formatting.
    
    Args:
        message (str): The message to print
    """
    # TODO: Implement error message formatting
    # Use red color if available
    print(f"✗ ERROR: {message}", file=sys.stderr)


def print_info(message):
    """
    Print an informational message with formatting.
    
    Args:
        message (str): The message to print
    """
    # TODO: Implement info message formatting
    # Use blue color if available
    print(f"ℹ INFO: {message}")


def print_warning(message):
    """
    Print a warning message with formatting.
    
    Args:
        message (str): The message to print
    """
    # TODO: Implement warning message formatting
    # Use yellow color if available
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
    # TODO: Implement byte formatting
    # Convert bytes to KB, MB, GB, etc. as appropriate
    return f"{bytes_value} bytes"


def confirm_action(prompt="Are you sure you want to continue?"):
    """
    Prompt the user for confirmation.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        bool: True if the user confirmed, False otherwise
    """
    # TODO: Implement user confirmation
    # Ask for y/n response and return appropriate boolean
    return True 