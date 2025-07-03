# LAB07 - Virtual Environments and Python Packaging - Solutions

This document provides reference solutions for LAB07. Remember to try solving the lab on your own first!

## Virtual Environment Setup

### Creating and Activating a Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

When activated, you should see the virtual environment name in your prompt.

### Installing Dependencies

```bash
pip install requests
```

### Freezing Dependencies to requirements.txt

```bash
pip freeze > requirements.txt
```

The `requirements.txt` file should contain something like:

```
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
requests==2.31.0
urllib3==2.0.4
```

## Package Implementation

### myproject/core.py

```python
#!/usr/bin/env python3
"""
Core module for the myproject package.

This module contains the main functionality for the myproject package.
"""

def say_hello(name):
    """
    Return a greeting message with the given name.
    
    Args:
        name (str): The name to greet.
        
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def calculate_square(number):
    """
    Calculate the square of a number.
    
    Args:
        number (int or float): The number to square.
        
    Returns:
        int or float: The square of the input number.
    """
    return number ** 2

# Test the module if run directly
if __name__ == "__main__":
    print(say_hello("Tester"))
    print(f"Square of 5 is {calculate_square(5)}")
```

### myproject/__init__.py

```python
"""
MyProject Package

A simple demonstration package for learning Python packaging.
You can import key functions directly from the package.
"""

from .core import say_hello, calculate_square

__version__ = '0.1.0'
```

### main.py

```python
#!/usr/bin/env python3
"""
LAB07 - Virtual Environments and Python Packaging

Instructions:
1. Create and activate a virtual environment
2. Install required dependencies
3. Import and use your custom module
"""

# Import the say_hello function from your myproject package
from myproject.core import say_hello
from myproject import calculate_square

# Call the say_hello function with your name or "DevOps"
message = say_hello("DevOps")
print(message)

# Display the result of the calculate_square function
number = 7
square_result = calculate_square(number)
print(f"The square of {number} is {square_result}")

# Import and use a function from the requests library (after installing it)
import requests

response = requests.get("https://api.github.com")
print(f"GitHub API Status Code: {response.status_code}")

print("\nGreat job! You've successfully worked with virtual environments and packages.")
print("You've created a reusable module and managed dependencies.")
print("Run this script with: python main.py")
```

## Key Learning Points

1. **Virtual Environments**:
   - Isolate dependencies for different projects
   - Prevent conflicts between package versions
   - Make projects more portable and reproducible

2. **Package Management**:
   - Using `pip` to install and manage dependencies
   - Creating `requirements.txt` for dependency documentation
   - Importing from packages and modules

3. **Python Package Structure**:
   - The importance of `__init__.py` files
   - Organizing code into modules
   - Importing between modules
   - Package-level imports and exposed functionality

4. **Best Practices**:
   - Always use virtual environments for projects
   - Document dependencies in requirements.txt
   - Add docstrings to functions and modules
   - Structure packages for reusability

## Common Issues and Troubleshooting

1. **Virtual Environment Not Activating**:
   - Make sure you're using the correct activation command for your OS
   - Check if the virtual environment directory was created properly

2. **Import Errors**:
   - Ensure package structure is correct (proper `__init__.py` files)
   - Check that you're running Python from the correct directory
   - Verify modules are named correctly in import statements

3. **Package Installation Issues**:
   - Make sure your virtual environment is activated
   - Check internet connection for downloading packages
   - Verify you have necessary permissions

4. **requirements.txt Issues**:
   - Ensure the file is in the correct format
   - Make sure you have frozen all dependencies (`pip freeze`)
   - Check for version conflicts or compatibility issues 