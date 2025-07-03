#!/usr/bin/env python3
"""
Helper Module for LAB03

This module contains utility functions that will be imported and used in main.py.
"""

# TODO: Define a function called greet
# This function should:
# - Accept a parameter called 'name'
# - Return a greeting string like "Hello, {name}!"
# Example: def greet(name):
#              return f"Hello, {name}!"
def greet(name):
    return print(f"Hello, {name}!")

# TODO: Define a function called add
# This function should:
# - Accept two parameters, 'x' and 'y'
# - Return the sum of x and y

def add(x,y):
    return x + y
# TODO: Bonus - Define a function called max_of_three
# This function should:
# - Accept three parameters: 'a', 'b', and 'c'
# - Return the maximum value of the three
# Hint: You can use the built-in max() function
def max_of_three(a,b,c):
    print(max(a,b,c))
# TODO: Extra Challenge - Create your own function
# Define a new function that does something useful (e.g., calculate area, multiply numbers, etc.)
# Make sure to include docstrings explaining what the function does!
def leave(name):
    return f"Cant wait to have you back, {name}!"

if __name__ == "__main__":
    # This code only runs when helper.py is executed directly (not when imported)
    print("This is the helper module containing utility functions.")
    print("Import these functions in main.py to use them!")
    
    # You can also add test calls here to verify your functions work correctly
    # Examples:
    # print(greet("Test User"))
    # print(add(10, 20)) 