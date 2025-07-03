#!/usr/bin/env python3
"""
# LAB03 - Functions and Modules in Python

# Instructions:
# 1. Complete both this file and helper.py
# 2. Import and use the functions from helper.py in this file
# 3. Run the script to test your implementations
# """

# TODO: Import functions from helper.py
# Add your import statement here to bring in the functions you'll create
# TODO: Call the greet() function
# Call the greet() function with your name or "DevOps Learner"

from helper import greet
greet("Ofek")

# TODO: Call the add() function
# Call the add() function with two numbers and print the result
# Example: print("Sum:", add(5, 3))
from helper import add
print("Sum:", add(6, 9))

# TODO: Bonus - Call the max_of_three() function
# Call the max_of_three() function with three different numbers
# Print the result
from helper import max_of_three
print(max_of_three(1,8,9))

# TODO: Extra Challenge - Create and call a new function
# First, add a new function to helper.py (e.g., multiply, calculate_area, etc.)
# Then import and use it here
from helper import leave 
print(leave("Ofek"))

# print("\nGreat job! You've successfully worked with functions and modules.")
# print("Run this script with: python main.py")
# print("Check your implementation against the validation checklist in the README.md") 