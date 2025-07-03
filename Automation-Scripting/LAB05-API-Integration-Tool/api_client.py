#!/usr/bin/env python3
"""
LAB05 - API Integration Tool

This script demonstrates how to interact with a REST API using Python.
It creates a reusable API client class that handles requests, responses, and errors.

Usage:
    python api_client.py
"""

# TODO: Import necessary modules
# You'll need the requests library and your config settings


# TODO: Create an APIClient class
# This class should:
# - Initialize with the base URL and timeout from config
# - Include methods to interact with different API endpoints
# - Handle authentication (if needed)
# - Process responses and handle errors


# TODO: Implement API endpoint methods
# For example:
# - get_users(): Fetch users from the API
# - get_posts(): Fetch posts from the API
# - get_user_by_id(user_id): Fetch a specific user


# TODO: Add error handling
# Consider handling these common scenarios:
# - Connection errors
# - Timeout errors
# - HTTP error codes (4xx, 5xx)
# - JSON parsing errors


if __name__ == "__main__":
    print("API Integration Tool")
    print("===================")
    
    # TODO: Create an instance of your API client and use it
    # Example:
    # client = APIClient()
    
    # TODO: Call methods and display results
    # Example:
    # try:
    #     users = client.get_users()
    #     print(f"Found {len(users)} users:")
    #     for user in users[:5]:  # Show first 5 users
    #         print(f"  - {user['name']} ({user['email']})")
    # except Exception as e:
    #     print(f"Error: {e}")
    
    # Add more API interactions as needed
    
    print("\nRemember to install dependencies:")
    print("pip install requests") 