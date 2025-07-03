#!/usr/bin/env python3
"""
LAB10 - API Interaction and REST

This module demonstrates how to interact with RESTful APIs
using Python, which is essential for DevOps automation.
"""

# TODO: Import required libraries
# import requests
# import json
# import os
# from urllib.parse import urljoin


def load_config(config_file="config.json"):
    """
    Load API configuration from a JSON file.
    
    Args:
        config_file (str): Path to the configuration file
        
    Returns:
        dict: Configuration settings
    """
    # TODO: Implement configuration loading
    # 1. Open the config file and load JSON data
    # 2. Return the configuration dictionary
    # 3. Handle potential errors (file not found, invalid JSON)
    
    print(f"Loading configuration from {config_file}")
    return {}


def create_api_client(base_url, headers=None, timeout=30):
    """
    Create an API client with the given configuration.
    
    Args:
        base_url (str): Base URL for the API
        headers (dict, optional): Default headers to include in requests
        timeout (int, optional): Request timeout in seconds
        
    Returns:
        dict: API client object with methods for interacting with the API
    """
    # TODO: Create a client object with methods for different API operations
    # This can be a class or a dictionary of functions
    
    print(f"Creating API client for {base_url}")
    return {
        "base_url": base_url,
        "headers": headers or {},
        "timeout": timeout,
    }


def get_data(client, endpoint, params=None):
    """
    Perform a GET request to retrieve data from an API.
    
    Args:
        client (dict): API client object
        endpoint (str): API endpoint to call
        params (dict, optional): Query parameters
        
    Returns:
        dict: Response data
    """
    # TODO: Implement GET request function
    # 1. Construct the full URL from base_url and endpoint
    # 2. Make the GET request with appropriate parameters
    # 3. Handle the response (check status, parse JSON)
    # 4. Implement error handling
    
    print(f"GET request to {endpoint}")
    return {}


def post_data(client, endpoint, data, json_data=True):
    """
    Perform a POST request to send data to an API.
    
    Args:
        client (dict): API client object
        endpoint (str): API endpoint to call
        data (dict): Data to send
        json_data (bool): Whether to send as JSON
        
    Returns:
        dict: Response data
    """
    # TODO: Implement POST request function
    # 1. Construct the full URL from base_url and endpoint
    # 2. Make the POST request with the provided data
    # 3. Handle the response (check status, parse JSON)
    # 4. Implement error handling
    
    print(f"POST request to {endpoint}")
    return {}


def handle_api_error(response):
    """
    Handle API errors based on status codes.
    
    Args:
        response: Response object from requests
        
    Returns:
        None
        
    Raises:
        Exception: If the response indicates an error
    """
    # TODO: Implement error handling for different status codes
    # 1. Check if status code indicates an error (4xx or 5xx)
    # 2. Extract error details from the response
    # 3. Raise appropriate exceptions with informative messages
    
    print("Handling API response")
    pass


def main():
    """Main function to demonstrate API interaction."""
    print("LAB10 - API Interaction and REST")
    print("================================\n")
    
    try:
        # TODO: Load configuration
        config = load_config()
        
        # TODO: Create API client
        client = create_api_client(
            base_url=config.get("api_base_url", "https://jsonplaceholder.typicode.com"),
            headers=config.get("headers", {}),
        )
        
        # TODO: Perform GET request to retrieve data
        # Example: Get users from the API
        print("\n1. Getting users from API:")
        print("-------------------------")
        users = get_data(client, "/users")
        # Display some user information
        
        # TODO: Perform GET request with parameters
        # Example: Get posts for a specific user
        print("\n2. Getting posts for a specific user:")
        print("-----------------------------------")
        user_id = 1  # Example user ID
        posts = get_data(client, "/posts", params={"userId": user_id})
        # Display some post information
        
        # TODO: Perform POST request to create data
        # Example: Create a new post
        print("\n3. Creating a new post:")
        print("---------------------")
        new_post = {
            "title": "New Post",
            "body": "This is a new post created via the API",
            "userId": user_id
        }
        created_post = post_data(client, "/posts", new_post)
        # Display the created post information
        
        # TODO: (Bonus) Implement other HTTP methods (PUT, DELETE)
        
        print("\nAPI interaction completed successfully!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main() 