# LAB03 - Functions and Modules Solutions

This file contains the solutions for the Functions and Modules lab. Please attempt to solve the exercises yourself before consulting this reference solution.

## helper.py Solution

```python
#!/usr/bin/env python3
"""
Helper Module for LAB03

This module contains utility functions that will be imported and used in main.py.
"""

def greet(name):
    """
    Returns a greeting message with the provided name.
    
    Args:
        name (str): The name to include in the greeting
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def add(x, y):
    """
    Adds two numbers together and returns the result.
    
    Args:
        x (int/float): First number
        y (int/float): Second number
        
    Returns:
        int/float: The sum of x and y
    """
    return x + y


def max_of_three(a, b, c):
    """
    Returns the maximum value among three numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        c (int/float): Third number
        
    Returns:
        int/float: The maximum value
    """
    return max(a, b, c)


def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    return length * width


if __name__ == "__main__":
    # This code only runs when helper.py is executed directly (not when imported)
    print("This is the helper module containing utility functions.")
    print("Import these functions in main.py to use them!")
    
    # Test calls to verify functions work correctly
    print(greet("Test User"))
    print(add(10, 20))
    print(max_of_three(5, 12, 8))
    print(f"Area of 4x5 rectangle: {calculate_area(4, 5)}")
```

## main.py Solution

```python
#!/usr/bin/env python3
"""
Main Module for LAB03

This script demonstrates how to import and use functions from another module.
"""

# Import the required functions from helper.py
from helper import greet, add, max_of_three, calculate_area

# Call the greet() function with your name
result = greet("DevOps Learner")
print(result)

# Call the add() function with two numbers
sum_result = add(10, 25)
print(f"Sum of 10 and 25 is: {sum_result}")

# Call the max_of_three() function with three numbers
max_value = max_of_three(15, 23, 7)
print(f"Maximum value of 15, 23, and 7 is: {max_value}")

# Call the custom function you created in helper.py
area = calculate_area(6.5, 3.2)
print(f"Area of rectangle with length 6.5 and width 3.2 is: {area}")

print("\nAll tasks completed successfully! 🎉")
```

## Key Learning Points

1. **Function Definition**
   - Functions are defined using the `def` keyword followed by the function name and parameters
   - The function body is indented and can contain any valid Python code
   - The `return` statement is used to send values back to the caller

2. **Function Parameters**
   - Parameters are variables that receive values when the function is called
   - They are defined in parentheses after the function name
   - Parameters can have default values and can be optional

3. **Docstrings**
   - Good practice to include docstrings that explain what the function does
   - Helps other developers understand your code
   - Can be accessed using the `help()` function

4. **Modules**
   - Python files that contain reusable code
   - Can be imported using the `import` statement
   - Helps organize code and promotes reusability

5. **The `if __name__ == "__main__":` Pattern**
   - Common pattern to include code that runs only when the file is executed directly
   - Useful for testing functions without affecting imports

## Common Issues and Solutions

1. **Import Error**
   - Error: `ModuleNotFoundError: No module named 'helper'`
   - Solution: Ensure that the helper.py file is in the same directory as main.py

2. **Function Not Defined**
   - Error: `NameError: name 'function_name' is not defined`
   - Solution: Make sure you've properly defined the function and imported it if it's in another module

3. **Incorrect Function Usage**
   - Error: `TypeError: function_name() takes X positional arguments but Y were given`
   - Solution: Check the function definition and provide the correct number of arguments 