# LAB05 - API Integration Tool Solutions

This file provides a reference solution for the API Integration Tool lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `config.py`

```python
"""
Configuration settings for the API Integration Tool

This file contains all the configuration parameters for the API client.
Separating configuration from code improves maintainability and security.
"""

# API connection parameters
# Base URL for the API
API_BASE_URL = "https://jsonplaceholder.typicode.com"

# Request timeout in seconds
API_TIMEOUT = 10

# Default headers
DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# API authentication parameters
# Uncomment and populate these if your API requires authentication
# API_KEY = "your_api_key_here"
# API_USERNAME = "your_username"
# API_PASSWORD = "your_password"

# Additional configuration parameters
API_MAX_RETRIES = 3
API_RETRY_BACKOFF = 0.5  # seconds
API_ENDPOINTS = {
    "users": "/users",
    "posts": "/posts",
    "comments": "/comments",
    "albums": "/albums",
    "photos": "/photos",
    "todos": "/todos"
}
```

## Complete Implementation of `api_client.py`

```python
#!/usr/bin/env python3
"""
LAB05 - API Integration Tool

This script demonstrates how to interact with a REST API using Python.
It creates a reusable API client class that handles requests, responses, and errors.

Usage:
    python api_client.py
"""

import json
import requests
import time
from typing import Dict, List, Any, Optional, Union
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout, TooManyRedirects
from config import (
    API_BASE_URL, 
    API_TIMEOUT, 
    DEFAULT_HEADERS, 
    API_MAX_RETRIES, 
    API_RETRY_BACKOFF,
    API_ENDPOINTS
)


class APIClient:
    """
    A reusable client for interacting with REST APIs.
    
    This class provides methods to interact with different API endpoints,
    handles authentication, and processes responses and errors.
    """
    
    def __init__(self, base_url: str = API_BASE_URL, timeout: int = API_TIMEOUT):
        """
        Initialize the API client.
        
        Args:
            base_url (str): The base URL of the API
            timeout (int): Request timeout in seconds
        """
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        
        # Uncomment and add if your API requires authentication
        # if hasattr(config, 'API_KEY'):
        #     self.session.headers.update({"Authorization": f"Bearer {config.API_KEY}"})
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict] = None, 
        data: Optional[Dict] = None, 
        headers: Optional[Dict] = None
    ) -> Any:
        """
        Make an HTTP request to the API with retry logic.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint to call
            params (dict, optional): Query parameters
            data (dict, optional): Request body for POST/PUT
            headers (dict, optional): Additional headers
            
        Returns:
            dict/list: Parsed JSON response
            
        Raises:
            requests.exceptions.RequestException: For request errors
        """
        url = f"{self.base_url}{endpoint}"
        request_headers = headers if headers else {}
        
        # Implement retry logic
        retries = 0
        while retries <= API_MAX_RETRIES:
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data,  # Automatically serializes dict to JSON
                    headers=request_headers,
                    timeout=self.timeout
                )
                
                # Raise an exception for 4XX/5XX responses
                response.raise_for_status()
                
                # Parse and return JSON response
                return response.json()
                
            except (ConnectionError, Timeout) as e:
                # Network or timeout errors - retry
                retries += 1
                if retries > API_MAX_RETRIES:
                    raise
                # Exponential backoff
                time.sleep(API_RETRY_BACKOFF * (2 ** (retries - 1)))
                
            except HTTPError as e:
                # Server returned error status code
                if 500 <= e.response.status_code < 600 and retries < API_MAX_RETRIES:
                    # Retry on 5XX errors
                    retries += 1
                    time.sleep(API_RETRY_BACKOFF * (2 ** (retries - 1)))
                else:
                    # Don't retry on 4XX errors or if max retries reached
                    # Try to get error details from response
                    try:
                        error_data = e.response.json()
                        error_message = error_data.get('message', str(e))
                    except:
                        error_message = str(e)
                    
                    raise HTTPError(f"HTTP Error: {e.response.status_code} - {error_message}", response=e.response)
            
            except Exception as e:
                # Other exceptions - don't retry
                raise
    
    def get_users(self) -> List[Dict]:
        """
        Fetch users from the API.
        
        Returns:
            list: List of user dictionaries
        """
        return self._request("GET", API_ENDPOINTS["users"])
    
    def get_user_by_id(self, user_id: int) -> Dict:
        """
        Fetch a specific user by ID.
        
        Args:
            user_id (int): User ID to fetch
            
        Returns:
            dict: User data
        """
        return self._request("GET", f"{API_ENDPOINTS['users']}/{user_id}")
    
    def get_posts(self, user_id: Optional[int] = None) -> List[Dict]:
        """
        Fetch posts, optionally filtered by user.
        
        Args:
            user_id (int, optional): Filter posts by user ID
            
        Returns:
            list: List of post dictionaries
        """
        params = {"userId": user_id} if user_id else None
        return self._request("GET", API_ENDPOINTS["posts"], params=params)
    
    def get_comments(self, post_id: Optional[int] = None) -> List[Dict]:
        """
        Fetch comments, optionally filtered by post.
        
        Args:
            post_id (int, optional): Filter comments by post ID
            
        Returns:
            list: List of comment dictionaries
        """
        params = {"postId": post_id} if post_id else None
        return self._request("GET", API_ENDPOINTS["comments"], params=params)
    
    def create_post(self, title: str, body: str, user_id: int) -> Dict:
        """
        Create a new post.
        
        Args:
            title (str): Post title
            body (str): Post content
            user_id (int): User ID to associate with the post
            
        Returns:
            dict: Created post data
        """
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self._request("POST", API_ENDPOINTS["posts"], data=data)
    
    def update_post(self, post_id: int, title: str, body: str) -> Dict:
        """
        Update an existing post.
        
        Args:
            post_id (int): ID of the post to update
            title (str): New post title
            body (str): New post content
            
        Returns:
            dict: Updated post data
        """
        data = {
            "title": title,
            "body": body
        }
        return self._request("PUT", f"{API_ENDPOINTS['posts']}/{post_id}", data=data)
    
    def delete_post(self, post_id: int) -> Dict:
        """
        Delete a post.
        
        Args:
            post_id (int): ID of the post to delete
            
        Returns:
            dict: API response (usually empty)
        """
        return self._request("DELETE", f"{API_ENDPOINTS['posts']}/{post_id}")


def display_user_info(user: Dict) -> None:
    """Display formatted user information."""
    print(f"\nUser Information:")
    print(f"  Name: {user['name']}")
    print(f"  Username: {user['username']}")
    print(f"  Email: {user['email']}")
    print(f"  Address: {user['address']['street']}, {user['address']['city']}")
    print(f"  Company: {user['company']['name']}")


def main() -> None:
    """Main function demonstrating API client usage."""
    print("API Integration Tool")
    print("===================")
    
    client = APIClient()
    
    try:
        # Fetch and display users
        print("\nFetching users...")
        users = client.get_users()
        print(f"Found {len(users)} users")
        
        if users:
            # Display first 3 users
            for i, user in enumerate(users[:3], 1):
                print(f"{i}. {user['name']} ({user['email']})")
        
        # Get and display specific user
        user_id = 1
        print(f"\nFetching details for user {user_id}...")
        user = client.get_user_by_id(user_id)
        display_user_info(user)
        
        # Get posts for this user
        print(f"\nFetching posts for user {user_id}...")
        posts = client.get_posts(user_id)
        print(f"Found {len(posts)} posts")
        
        if posts:
            # Display first post
            post = posts[0]
            print(f"\nSample post title: {post['title']}")
            print(f"Sample post body: {post['body'][:100]}...")
            
            # Get comments for this post
            post_id = post['id']
            print(f"\nFetching comments for post {post_id}...")
            comments = client.get_comments(post_id)
            print(f"Found {len(comments)} comments")
            
            if comments:
                # Show first comment
                comment = comments[0]
                print(f"\nSample comment from: {comment['name']} ({comment['email']})")
                print(f"Comment: {comment['body'][:100]}...")
        
        # Create a new post (demo)
        print("\nCreating a new post (demo)...")
        new_post = client.create_post(
            title="New Post from Python API Client",
            body="This is a test post created using the Python API client.",
            user_id=user_id
        )
        print(f"Created new post with ID: {new_post['id']}")
        
        # Update the post (demo)
        print("\nUpdating the post (demo)...")
        updated_post = client.update_post(
            post_id=new_post['id'],
            title="Updated Post Title",
            body="This post has been updated using the Python API client."
        )
        print(f"Updated post title: {updated_post['title']}")
        
        # Delete the post (demo)
        print("\nDeleting the post (demo)...")
        client.delete_post(new_post['id'])
        print("Post deleted successfully")
        
    except RequestException as e:
        print(f"\nAPI Request Error: {e}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **API Client Design Patterns**:
   - Creating a reusable client class
   - Separating configuration from implementation
   - Using request/response abstractions
   - Implementing endpoint-specific methods

2. **HTTP Request Handling**:
   - Making GET, POST, PUT, DELETE requests
   - Setting headers and timeouts
   - Passing query parameters and request bodies
   - Using sessions for connection pooling

3. **Response Processing**:
   - Parsing JSON responses
   - Error detection with `raise_for_status()`
   - Extracting error details from responses
   - Returning structured data to the caller

4. **Error Handling and Resilience**:
   - Catching specific exception types
   - Implementing retry logic with backoff
   - Distinguishing between retriable and non-retriable errors
   - Providing meaningful error messages

5. **API Authentication Techniques**:
   - Bearer token authentication
   - API key authentication
   - Basic HTTP authentication
   - Session management

## Expected Output

```
API Integration Tool
===================

Fetching users...
Found 10 users
1. Leanne Graham (Sincere@april.biz)
2. Ervin Howell (Shanna@melissa.tv)
3. Clementine Bauch (Nathan@yesenia.net)

Fetching details for user 1...

User Information:
  Name: Leanne Graham
  Username: Bret
  Email: Sincere@april.biz
  Address: Kulas Light, Gwenborough
  Company: Romaguera-Crona

Fetching posts for user 1...
Found 10 posts

Sample post title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Sample post body: quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut...

Fetching comments for post 1...
Found 5 comments

Sample comment from: id labore ex et quam laborum (Eliseo@gardner.biz)
Comment: laudantium enim quasi est quidem magnam voluptate ipsam eos tempora quo necessitatibus dolor...

Creating a new post (demo)...
Created new post with ID: 101

Updating the post (demo)...
Updated post title: Updated Post Title

Deleting the post (demo)...
Post deleted successfully
```

## Common Issues and Troubleshooting

1. **Connection Errors**:
   - Check internet connectivity
   - Verify the API base URL is correct
   - Ensure no firewall or proxy is blocking requests

2. **Authentication Failures**:
   - Verify API key or credentials are correct
   - Check if token has expired
   - Ensure authentication headers are properly formatted

3. **Rate Limiting**:
   - Implement backoff and retry logic
   - Check API documentation for rate limits
   - Add delays between requests if necessary

4. **Data Parsing Errors**:
   - Validate JSON responses before parsing
   - Handle unexpected response formats
   - Check API documentation for response structure

5. **HTTPS Certificate Errors**:
   - Update your certificate authorities
   - Verify the API is using a valid certificate
   - Use `verify=False` only in development (security risk)

## Extension Ideas

1. **API Documentation Generator**:
   - Auto-generate documentation from API responses
   - Create OpenAPI/Swagger specs

2. **Response Caching**:
   - Implement local caching of API responses
   - Add cache invalidation strategies

3. **Advanced Authentication**:
   - Implement OAuth2 flows
   - Add token refresh capability

4. **Asynchronous Requests**:
   - Use `aiohttp` or `httpx` for async API calls
   - Implement concurrent requests

5. **Response Validation**:
   - Add schema validation for API responses
   - Implement data transformation layers

## Best Practices

1. **Configuration Management**:
   - Keep API keys and credentials out of code
   - Use environment variables or configuration files
   - Consider using a secret manager for production

2. **Error Handling**:
   - Implement comprehensive error handling
   - Provide clear error messages to users
   - Log detailed error information for debugging

3. **Rate Limiting Respect**:
   - Honor API rate limits
   - Implement exponential backoff for retries
   - Consider using rate limiting libraries

4. **Type Hints**:
   - Use type annotations for better code readability
   - Enable static type checking with mypy
   - Document return types and parameters

5. **Testing**:
   - Write unit tests with mocked API responses
   - Create integration tests for API endpoints
   - Test error handling and edge cases 