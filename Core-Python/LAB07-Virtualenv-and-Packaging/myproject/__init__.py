"""
MyProject Package

This is a simple Python package created for LAB07 on virtual environments and packaging.
It demonstrates how to structure a basic reusable package for DevOps automation tools.

The __init__.py file serves several purposes:
1. It marks the directory as a Python package
2. It can expose specific functions/classes from modules to simplify imports
3. It can run initialization code when the package is imported
4. It can define package-level variables like __version__
"""

# TODO: Import and expose key functions from your modules
# This allows users to import directly from the package
# Uncomment and modify these lines after implementing your functions:
# 
# from .core import say_hello
# from .core import get_timestamp  # Or whatever your second function is called

# Package metadata
__version__ = '0.1.0'
__author__ = 'Your Name'

# You could also initialize package-wide resources here if needed
# For example, setting up logging configuration for the package 