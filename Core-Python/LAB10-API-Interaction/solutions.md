# LAB10 - API Interaction and REST Solutions

This file provides a reference solution for the API Interaction lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `main.py`

```python
#!/usr/bin/env python3
"""
LAB10 - API Interaction and REST

This module demonstrates how to interact with RESTful APIs
using Python, which is essential for DevOps automation.
"""

import json
import os
import time
import requests
from urllib.parse import urljoin


def load_config(config_file="config.json"):
    """
    Load API configuration from a JSON file.
    
    Args:
        config_file (str): Path to the configuration file
        
    Returns:
        dict: Configuration settings
    """
    try:
        # Check if the file exists
        if not os.path.exists(config_file):
            print(f"Warning: Configuration file {config_file} not found.")
            # Return default configuration
            return {
                "api_base_url": "https://jsonplaceholder.typicode.com",
                "timeout": 30,
                "headers": {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
            }
        
        # Open and read the JSON file
        with open(config_file, 'r') as file:
            config = json.load(file)
            print(f"Configuration loaded from {config_file}")
            return config
            
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in configuration file: {str(e)}")
        raise
    except Exception as e:
        print(f"Error loading configuration: {str(e)}")
        raise


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
    # Create a session for connection pooling and reuse
    session = requests.Session()
    
    # Set default headers
    if headers:
        session.headers.update(headers)
    
    # Create a client object
    client = {
        "base_url": base_url,
        "session": session,
        "timeout": timeout
    }
    
    print(f"API client created for {base_url}")
    return client


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
    # Construct full URL
    url = urljoin(client["base_url"], endpoint)
    
    try:
        # Make the GET request
        response = client["session"].get(
            url,
            params=params,
            timeout=client["timeout"]
        )
        
        # Check for errors
        handle_api_error(response)
        
        # Parse and return JSON response
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Request error for GET {url}: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response from {url}: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error for GET {url}: {str(e)}")
        raise


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
    # Construct full URL
    url = urljoin(client["base_url"], endpoint)
    
    try:
        # Make the POST request
        if json_data:
            response = client["session"].post(
                url,
                json=data,  # Automatically serializes dict to JSON
                timeout=client["timeout"]
            )
        else:
            response = client["session"].post(
                url,
                data=data,  # Send as form data
                timeout=client["timeout"]
            )
        
        # Check for errors
        handle_api_error(response)
        
        # Parse and return JSON response
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Request error for POST {url}: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response from {url}: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error for POST {url}: {str(e)}")
        raise


def put_data(client, endpoint, data, json_data=True):
    """
    Perform a PUT request to update data in an API.
    
    Args:
        client (dict): API client object
        endpoint (str): API endpoint to call
        data (dict): Data to send
        json_data (bool): Whether to send as JSON
        
    Returns:
        dict: Response data
    """
    # Construct full URL
    url = urljoin(client["base_url"], endpoint)
    
    try:
        # Make the PUT request
        if json_data:
            response = client["session"].put(
                url,
                json=data,  # Automatically serializes dict to JSON
                timeout=client["timeout"]
            )
        else:
            response = client["session"].put(
                url,
                data=data,  # Send as form data
                timeout=client["timeout"]
            )
        
        # Check for errors
        handle_api_error(response)
        
        # Parse and return JSON response
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Request error for PUT {url}: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response from {url}: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error for PUT {url}: {str(e)}")
        raise


def delete_data(client, endpoint):
    """
    Perform a DELETE request to remove data from an API.
    
    Args:
        client (dict): API client object
        endpoint (str): API endpoint to call
        
    Returns:
        dict or bool: Response data or success indicator
    """
    # Construct full URL
    url = urljoin(client["base_url"], endpoint)
    
    try:
        # Make the DELETE request
        response = client["session"].delete(
            url,
            timeout=client["timeout"]
        )
        
        # Check for errors
        handle_api_error(response)
        
        # Some APIs return an empty response for DELETE
        if response.text:
            return response.json()
        else:
            return response.status_code == 200 or response.status_code == 204
        
    except requests.exceptions.RequestException as e:
        print(f"Request error for DELETE {url}: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response from {url}: {str(e)}")
        # Return success status if we can't parse JSON but request was successful
        if response.status_code in [200, 204]:
            return True
        raise
    except Exception as e:
        print(f"Unexpected error for DELETE {url}: {str(e)}")
        raise


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
    # Check if the response status code indicates an error
    if 400 <= response.status_code < 600:
        # Try to extract error details from JSON response
        error_message = f"HTTP Error: {response.status_code}"
        
        try:
            error_data = response.json()
            if isinstance(error_data, dict):
                # Look for common error fields
                message = error_data.get('message') or error_data.get('error') or error_data.get('detail')
                if message:
                    error_message = f"HTTP Error {response.status_code}: {message}"
        except:
            # If we can't parse JSON, use text content
            if response.text:
                error_message = f"HTTP Error {response.status_code}: {response.text[:100]}"
        
        # Raise specific exceptions based on status code
        if response.status_code == 400:
            raise ValueError(f"Bad Request - {error_message}")
        elif response.status_code == 401:
            raise PermissionError(f"Unauthorized - {error_message}")
        elif response.status_code == 403:
            raise PermissionError(f"Forbidden - {error_message}")
        elif response.status_code == 404:
            raise FileNotFoundError(f"Not Found - {error_message}")
        elif response.status_code == 429:
            raise TimeoutError(f"Rate Limited - {error_message}")
        elif 500 <= response.status_code < 600:
            raise ConnectionError(f"Server Error - {error_message}")
        else:
            raise Exception(error_message)


def retry_request(func, max_retries=3, backoff_factor=0.5, retry_status_codes=None):
    """
    Retry a request function with exponential backoff.
    
    Args:
        func: Function to retry (should be a lambda or partial)
        max_retries (int): Maximum number of retry attempts
        backoff_factor (float): Backoff factor for delay calculation
        retry_status_codes (list): Status codes to retry on
        
    Returns:
        The result of the function call
    """
    if retry_status_codes is None:
        retry_status_codes = [429, 500, 502, 503, 504]
    
    retries = 0
    while True:
        try:
            return func()
        except (requests.exceptions.RequestException, ConnectionError) as e:
            retries += 1
            if retries > max_retries:
                print(f"Maximum retries ({max_retries}) reached. Giving up.")
                raise
            
            # Check if we should retry based on status code
            if hasattr(e, 'response') and e.response and e.response.status_code not in retry_status_codes:
                raise
            
            # Calculate delay with exponential backoff
            delay = backoff_factor * (2 ** (retries - 1))
            print(f"Request failed. Retrying in {delay:.2f} seconds...")
            time.sleep(delay)


def display_user_info(user):
    """Display user information in a readable format."""
    print(f"User: {user['name']} (@{user['username']})")
    print(f"  Email: {user['email']}")
    print(f"  Company: {user['company']['name']}")
    print(f"  Website: {user['website']}")


def display_post_info(post):
    """Display post information in a readable format."""
    print(f"Post #{post['id']}: {post['title']}")
    print(f"  {post['body'][:60]}..." if len(post['body']) > 60 else f"  {post['body']}")
    print(f"  By User: {post['userId']}")


def main():
    """Main function to demonstrate API interaction."""
    print("LAB10 - API Interaction and REST")
    print("================================\n")
    
    try:
        # Load configuration
        config = load_config()
        
        # Create API client
        client = create_api_client(
            base_url=config.get("api_base_url", "https://jsonplaceholder.typicode.com"),
            headers=config.get("headers", {}),
            timeout=config.get("timeout", 30)
        )
        
        # Perform GET request to retrieve data
        print("\n1. Getting users from API:")
        print("-------------------------")
        users = get_data(client, "/users")
        print(f"Retrieved {len(users)} users\n")
        
        # Display first 3 users
        for user in users[:3]:
            display_user_info(user)
            print()
        
        # Perform GET request with parameters
        print("\n2. Getting posts for a specific user:")
        print("-----------------------------------")
        user_id = 1  # Example user ID
        posts = get_data(client, "/posts", params={"userId": user_id})
        print(f"Retrieved {len(posts)} posts for user {user_id}\n")
        
        # Display first 3 posts
        for post in posts[:3]:
            display_post_info(post)
            print()
        
        # Perform POST request to create data
        print("\n3. Creating a new post:")
        print("---------------------")
        new_post = {
            "title": "New Post",
            "body": "This is a new post created via the API",
            "userId": user_id
        }
        created_post = post_data(client, "/posts", new_post)
        print("Created new post:")
        display_post_info(created_post)
        
        # Demonstrate PUT request (update data)
        print("\n4. Updating a post:")
        print("------------------")
        post_id = 1  # Example post ID
        updated_post_data = {
            "id": post_id,
            "title": "Updated Post Title",
            "body": "This post has been updated via the API",
            "userId": user_id
        }
        updated_post = put_data(client, f"/posts/{post_id}", updated_post_data)
        print("Updated post:")
        display_post_info(updated_post)
        
        # Demonstrate DELETE request
        print("\n5. Deleting a post:")
        print("------------------")
        post_id = 2  # Example post ID
        result = delete_data(client, f"/posts/{post_id}")
        print(f"Delete operation successful: {result}")
        
        # Demonstrate retry logic with a simulated error
        print("\n6. Demonstrating retry logic:")
        print("--------------------------")
        try:
            # Using a non-existent endpoint to trigger 404
            retry_request(
                lambda: get_data(client, "/nonexistent"),
                max_retries=2,
                backoff_factor=0.1,
                retry_status_codes=[404]  # Including 404 just for demonstration
            )
        except FileNotFoundError as e:
            print(f"Expected error after retries: {str(e)}")
        
        print("\nAPI interaction completed successfully!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Working with the Requests Library**:
   - Using `requests.get()`, `requests.post()`, etc. for HTTP operations
   - Setting headers, parameters, and timeouts
   - Using sessions for connection pooling and common settings

2. **Handling API Responses**:
   - Checking status codes to detect errors
   - Parsing JSON responses with proper error handling
   - Extracting meaningful information from responses

3. **Error Handling Techniques**:
   - Identifying different types of errors (client vs. server)
   - Creating specific exceptions based on status codes
   - Providing informative error messages

4. **URL Construction**:
   - Using `urljoin()` to properly build URLs
   - Working with query parameters
   - Handling different endpoint formats

5. **Configuration Management**:
   - Loading settings from external files
   - Providing sensible defaults
   - Validating configuration values

6. **Retry Logic**:
   - Implementing exponential backoff
   - Identifying retryable status codes
   - Limiting retry attempts

## Common Issues and Troubleshooting

1. **Connection Problems**:
   - Check your network connection
   - Verify the base URL is correct
   - Ensure firewall/proxy settings allow access

2. **Authentication Issues**:
   - Verify API keys or credentials are correct
   - Check that authentication headers are properly formatted
   - Ensure tokens have not expired

3. **Request Format Errors**:
   - Double-check content types match the data format
   - Ensure required fields are included in requests
   - Validate parameter names and values

4. **Response Parsing Errors**:
   - Check if the API is returning valid JSON
   - Handle empty responses appropriately
   - Be prepared for unexpected response structures

5. **Rate Limiting**:
   - Implement proper retry logic with backoff
   - Track rate limits and respect them
   - Consider adding delays between consecutive requests

## Extension Ideas

1. Implement a class-based API client for better organization
2. Add authentication support (API key, OAuth, etc.)
3. Create a command-line interface for interacting with the API
4. Implement caching to reduce unnecessary API calls
5. Add comprehensive logging for debugging and auditing
6. Create a more advanced retry mechanism with circuit breaking

## RESTful API Best Practices

1. **Endpoint Organization**:
   - Use nouns, not verbs, for resource endpoints (e.g., `/users`, not `/getUsers`)
   - Use HTTP methods to indicate operations (GET, POST, PUT, DELETE)
   - Structure collections as plural nouns (e.g., `/users` not `/user`)

2. **Status Codes**:
   - Use appropriate status codes to indicate outcomes
   - 2xx for success, 4xx for client errors, 5xx for server errors
   - Be consistent in status code usage

3. **Error Handling**:
   - Return meaningful error messages
   - Include error codes or types
   - Provide guidance on how to fix issues

4. **Authentication**:
   - Use standard authentication methods (API keys, OAuth, JWT)
   - Send credentials securely (HTTPS, Authorization header)
   - Implement token expiration and refresh

5. **Response Formatting**:
   - Use consistent response structures
   - Include metadata (pagination, counts, etc.)
   - Format dates and times according to standards (ISO 8601) 