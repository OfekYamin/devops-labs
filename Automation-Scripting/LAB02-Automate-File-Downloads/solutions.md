# LAB02 - Automate File Downloads Solutions

This file provides a reference solution for the Automate File Downloads lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `downloader.py`

```python
#!/usr/bin/env python3
"""
LAB02 - Automate File Downloads with Python

This script demonstrates how to download files from the internet using the requests library.
It handles HTTP requests, saves the content to disk, and manages errors.

Usage:
    python downloader.py
    python downloader.py --url https://example.com/sample.txt --output sample.txt
"""

import argparse
import os
import requests
import sys
from tqdm import tqdm


def download_file(url, filename, show_progress=True):
    """
    Download a file from a URL and save it to disk.
    
    Args:
        url (str): The URL to download from
        filename (str): The name to save the file as
        show_progress (bool): Whether to display a progress bar
        
    Returns:
        bool: True if download succeeded, False otherwise
    """
    try:
        print(f"Downloading {url}...")
        
        # Send a HEAD request first to get the file size
        head_response = requests.head(url, allow_redirects=True)
        file_size = int(head_response.headers.get('content-length', 0))
        
        # Stream the download
        response = requests.get(url, stream=True, allow_redirects=True)
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to download. Status code: {response.status_code}")
            print(f"Response: {response.text[:100]}...")
            return False
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
        
        # Write the content to a file
        with open(filename, "wb") as f:
            if show_progress and file_size > 0:
                with tqdm(total=file_size, unit='B', unit_scale=True, desc=filename) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:  # filter out keep-alive chunks
                            f.write(chunk)
                            pbar.update(len(chunk))
            else:
                f.write(response.content)
        
        print(f"File saved as: {os.path.abspath(filename)}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except IOError as e:
        print(f"Error saving file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return False


def main():
    """Parse command-line arguments and download the file."""
    parser = argparse.ArgumentParser(description="Download files from the internet")
    
    parser.add_argument(
        "--url", 
        default="https://raw.githubusercontent.com/python/cpython/master/README.rst",
        help="URL to download from"
    )
    
    parser.add_argument(
        "--output", 
        default="downloaded_file.txt",
        help="Name to save the file as"
    )
    
    parser.add_argument(
        "--no-progress", 
        action="store_true",
        help="Disable progress bar"
    )
    
    args = parser.parse_args()
    
    # Download the file
    success = download_file(args.url, args.output, not args.no_progress)
    
    # Set exit code based on success
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Using the Requests Library**:
   - Make HTTP requests with `requests.get(url)`
   - Use streaming for large files with `stream=True`
   - Check response status code to verify success

2. **File Handling**:
   - Open files in binary mode (`"wb"`) for downloads
   - Create directories as needed with `os.makedirs()`
   - Use `with` statements to ensure files are properly closed

3. **Error Handling**:
   - Catch connection errors (`requests.exceptions.RequestException`)
   - Handle file I/O errors (`IOError`)
   - Provide informative error messages

4. **Progress Indication**:
   - Use `tqdm` for visual progress bars
   - Download in chunks to update progress
   - Show file size and download speed

5. **Command-Line Interface**:
   - Use `argparse` to create a user-friendly CLI
   - Provide sensible defaults for arguments
   - Return appropriate exit codes

## Expected Output

```
$ python downloader.py
Downloading https://raw.githubusercontent.com/python/cpython/master/README.rst...
downloaded_file.txt: 100%|██████████| 14.7k/14.7k [00:01<00:00, 13.8kB/s]
File saved as: /path/to/downloaded_file.txt

$ python downloader.py --url https://www.python.org/static/img/python-logo.png --output python-logo.png
Downloading https://www.python.org/static/img/python-logo.png...
python-logo.png: 100%|██████████| 8.93k/8.93k [00:00<00:00, 27.6kB/s]
File saved as: /path/to/python-logo.png
```

## Common Issues and Troubleshooting

1. **Missing Dependencies**: Make sure to install required packages with `pip install requests tqdm`
2. **Connection Errors**: Check your internet connection and URL validity
3. **File Permission Errors**: Ensure you have write permissions in the target directory
4. **Timeout Errors**: Large files might need longer timeouts, consider adding a timeout parameter
5. **Redirects**: Some URLs may redirect, use `allow_redirects=True` to follow them

## Extension Ideas

1. **Parallel Downloads**: Download multiple files concurrently using threads or async
2. **Resume Capability**: Add the ability to resume interrupted downloads
3. **File Type Detection**: Auto-detect file type based on headers or content
4. **MD5/SHA Verification**: Verify downloaded file integrity with hash checking
5. **Retry Mechanism**: Automatically retry failed downloads with exponential backoff

## Best Practices

1. **Stream Large Files**: Always use streaming for large files to avoid memory issues
2. **Handle Redirects**: Enable redirect following for URLs that might redirect
3. **Check File Size First**: Send a HEAD request to get file size before downloading
4. **User-Agent Headers**: Set a proper User-Agent header to identify your script
5. **Timeout Settings**: Set reasonable timeouts to avoid hanging on slow connections 