#!/usr/bin/env python3
"""
LAB08 - Unit Testing Basics in Python

This module contains functions that will be tested with the unittest framework.
These functions demonstrate common operations that might be used in DevOps automation
scripts, and will help you learn how to properly test your code.
"""

# TODO: Implement the add function
# The function should:
# - Take two parameters (a and b)
# - Return their sum
# - Include a proper docstring with Args and Returns sections
#
# Example:
# def add(a, b):
#     """
#     Add two numbers and return the result.
#     
#     Args:
#         a: First number
#         b: Second number
#         
#     Returns:
#         The sum of a and b
#     """
#     return a + b


# TODO: Implement the is_even function
# The function should:
# - Take a single parameter (number)
# - Return True if the number is even, False otherwise
# - Include a proper docstring
#
# Example:
# def is_even(number):
#     """
#     Check if a number is even.
#     
#     Args:
#         number: The number to check
#         
#     Returns:
#         True if the number is even, False otherwise
#     """
#     return number % 2 == 0


# TODO: Implement the get_largest function
# The function should:
# - Take a list of numbers as a parameter
# - Return the largest number in the list
# - Raise ValueError if the list is empty
# - Include a proper docstring with Args, Returns, and Raises sections
#
# Example:
# def get_largest(numbers):
#     """
#     Get the largest number from a list.
#     
#     Args:
#         numbers: A list of numbers
#         
#     Returns:
#         The largest number in the list
#         
#     Raises:
#         ValueError: If the list is empty
#     """
#     if not numbers:
#         raise ValueError("Cannot find largest in an empty list")
#     return max(numbers)


# TODO: Implement the reverse_string function
# The function should:
# - Take a string parameter
# - Return the reversed string
# - Include a proper docstring
#
# Example:
# def reverse_string(s):
#     """
#     Reverse a string.
#     
#     Args:
#         s: The string to reverse
#         
#     Returns:
#         The reversed string
#     """
#     return s[::-1]


# This section allows you to manually test your functions
if __name__ == "__main__":
    # This code runs only if the script is executed directly
    # You can use this section to manually test your functions
    print("Testing functions manually:")
    
    # Uncomment these lines after implementing your functions:
    # print(f"add(2, 3) = {add(2, 3)}")
    # print(f"is_even(4) = {is_even(4)}")
    # print(f"get_largest([1, 5, 3]) = {get_largest([1, 5, 3])}")
    # print(f"reverse_string('hello') = {reverse_string('hello')}")
    
    print("Remember that manual testing is no substitute for automated tests!")
    print("Make sure to implement the tests in test_main.py as well.") 