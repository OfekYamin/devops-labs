"""
Core module for myproject package

This module contains the main functionality for the myproject package.
It demonstrates how to create reusable functions in a Python package
that can be imported and used in other scripts.
"""

# TODO: Define a function called say_hello
# The function should:
# - Accept a parameter called 'name'
# - Return a formatted greeting string (e.g., "Hello, DevOps!")
# - Include a proper docstring describing what the function does
#
# Example:
# def say_hello(name):
#     """
#     Generate a personalized greeting message.
#     
#     Args:
#         name (str): The name to include in the greeting
#         
#     Returns:
#         str: A formatted greeting message
#     """
#     return f"Hello, {name}!"


# TODO: Define another useful function for DevOps tasks
# Create a function that would be useful in a DevOps context
# Some ideas:
# - A function to format timestamps for logs
# - A function to parse configuration files
# - A function to validate IP addresses
# - A function to generate unique IDs for resources
#
# Example:
# def get_timestamp():
#     """
#     Get the current timestamp in ISO format.
#     
#     Returns:
#         str: Current timestamp in ISO format
#     """
#     from datetime import datetime
#     return datetime.now().isoformat()


# This conditional block only runs when the file is executed directly
# It's useful for testing your functions without importing them elsewhere
if __name__ == "__main__":
    # Test your functions here
    print("Testing the core module directly:")
    # Uncomment these lines once you've implemented your functions:
    # print(say_hello("DevOps Engineer"))
    # print("Second function test:", get_timestamp())  # Or your custom function 