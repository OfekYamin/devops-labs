#!/usr/bin/env python3
"""
LAB02 - Automate File Downloads with Python

This script demonstrates how to download files from the internet using the requests library.
It handles HTTP requests, saves the content to disk, and manages errors.

Usage:
    python downloader.py
"""

# TODO: Import the requests library
# You'll need to install this first with: pip install requests


# TODO: Create a function to download a file from a URL
# The function should:
# - Accept a URL and a filename as parameters
# - Make an HTTP GET request to the URL
# - Check if the response status code is 200 (OK)
# - If successful, save the content to a file
# - Print a success or failure message


# TODO: Add error handling
# What if the connection fails?
# What if the file can't be written?
# Use try-except blocks to handle potential errors


# TODO: BONUS - Add command-line arguments
# Use argparse to accept a URL and filename from the command line
# Example: python downloader.py --url https://example.com/file.txt --output file.txt


# TODO: BONUS - Add a progress indicator
# For larger files, it's nice to show download progress
# You could use the tqdm library or implement a simple percentage display


if __name__ == "__main__":
    # TODO: Call your download function with an example URL
    # Some example URLs you can use:
    # - https://raw.githubusercontent.com/python/cpython/master/README.rst (Text file)
    # - https://www.python.org/static/img/python-logo.png (Small image)
    
    print("File Download Script")
    print("====================")
    
    # Example usage (uncomment and modify after implementing the function):
    # download_file("https://www.example.com/sample.txt", "sample.txt")
    
    print("\nRemember to install the required dependencies:")
    print("pip install requests") 