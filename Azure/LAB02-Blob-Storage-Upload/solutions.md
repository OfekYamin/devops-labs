# Solutions: Azure Blob Storage Upload Automation

This document provides the reference solutions for the Azure Blob Storage Upload lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

Below is the full implementation of the `upload_blob.py` script:

```python
#!/usr/bin/env python3
"""
Azure Blob Storage Upload Automation Script

This script demonstrates how to automate file uploads to Azure Blob Storage using 
the Azure SDK for Python. It includes functions for creating containers, uploading files,
listing blobs, and cleaning up resources.

Note: In production environments, always use secure methods to handle connection strings.
"""

import os
import sys
import argparse
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError

def get_blob_service_client(connection_string=None):
    """
    Create a blob service client using connection string.
    
    Args:
        connection_string (str, optional): Azure Storage connection string.
                                          If None, tries to get from environment.
    
    Returns:
        BlobServiceClient: The blob service client object
    """
    # Try to get connection string from environment if not provided
    if not connection_string:
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        
    if not connection_string:
        print("Error: No connection string provided or found in environment variables.")
        print("Please set AZURE_STORAGE_CONNECTION_STRING environment variable or provide the connection string.")
        sys.exit(1)
    
    # Create the BlobServiceClient
    try:
        return BlobServiceClient.from_connection_string(connection_string)
    except Exception as e:
        print(f"Error creating blob service client: {e}")
        sys.exit(1)

def create_container(blob_service_client, container_name):
    """
    Create a container in the storage account if it doesn't exist.
    
    Args:
        blob_service_client (BlobServiceClient): The blob service client
        container_name (str): Name of the container to create
    
    Returns:
        ContainerClient: The container client
    """
    print(f"Creating container '{container_name}' (if it doesn't exist)...")
    
    try:
        # Get container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Create the container
        container_client.create_container()
        print(f"Container '{container_name}' created successfully.")
    except ResourceExistsError:
        print(f"Container '{container_name}' already exists.")
    except Exception as e:
        print(f"Error creating container: {e}")
        sys.exit(1)
        
    return container_client

def upload_blob(container_client, file_path, blob_name=None, overwrite=True):
    """
    Upload a file to the specified container as a blob.
    
    Args:
        container_client (ContainerClient): The container client
        file_path (str): Path to the file to upload
        blob_name (str, optional): Name to give the blob. If None, uses file name.
        overwrite (bool): Whether to overwrite if blob exists
    
    Returns:
        str: The name of the uploaded blob
    """
    # If blob_name not provided, use the file name from file_path
    if not blob_name:
        blob_name = os.path.basename(file_path)
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)
        
    print(f"Uploading file '{file_path}' to blob '{blob_name}'...")
    
    try:
        # Open the file
        with open(file_path, "rb") as data:
            # Upload the file
            blob_client = container_client.upload_blob(
                name=blob_name, 
                data=data, 
                overwrite=overwrite
            )
            print(f"File uploaded successfully as blob '{blob_name}'.")
            return blob_name
    except Exception as e:
        print(f"Error uploading file: {e}")
        sys.exit(1)

def list_blobs(container_client, prefix=None):
    """
    List all blobs in the container with optional prefix filter.
    
    Args:
        container_client (ContainerClient): The container client
        prefix (str, optional): Prefix filter for blob names
    
    Returns:
        list: List of blob names
    """
    print(f"Listing blobs in container{' with prefix ' + prefix if prefix else ''}...")
    
    try:
        blob_list = container_client.list_blobs(name_starts_with=prefix)
        
        blobs = []
        print("Blobs:")
        for blob in blob_list:
            print(f"- {blob.name}")
            blobs.append(blob.name)
            
        if not blobs:
            print("No blobs found.")
            
        return blobs
    except Exception as e:
        print(f"Error listing blobs: {e}")
        return []

def delete_blob(container_client, blob_name):
    """
    Delete a blob from the container.
    
    Args:
        container_client (ContainerClient): The container client
        blob_name (str): Name of the blob to delete
    
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    print(f"Deleting blob '{blob_name}'...")
    
    try:
        container_client.delete_blob(blob_name)
        print(f"Blob '{blob_name}' deleted successfully.")
        return True
    except ResourceNotFoundError:
        print(f"Blob '{blob_name}' not found.")
        return False
    except Exception as e:
        print(f"Error deleting blob: {e}")
        return False

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description="Azure Blob Storage Upload Automation")
    
    # Common parameters
    parser.add_argument("--connection-string", help="Azure Storage connection string")
    parser.add_argument("--container", default="devops-container", help="Container name (default: devops-container)")
    
    # Operation groups
    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")
    
    # Upload operation
    upload_parser = subparsers.add_parser("upload", help="Upload a file to blob storage")
    upload_parser.add_argument("--file", required=True, help="Path to the file to upload")
    upload_parser.add_argument("--blob-name", help="Name to give the blob (default: file name)")
    upload_parser.add_argument("--no-overwrite", action="store_true", help="Don't overwrite if blob exists")
    
    # List operation
    list_parser = subparsers.add_parser("list", help="List blobs in a container")
    list_parser.add_argument("--prefix", help="Prefix filter for blob names")
    
    # Delete operation
    delete_parser = subparsers.add_parser("delete", help="Delete a blob")
    delete_parser.add_argument("--blob-name", required=True, help="Name of the blob to delete")
    
    args = parser.parse_args()
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    # Get blob service client
    blob_service_client = get_blob_service_client(args.connection_string)
    
    # Create container
    container_client = create_container(blob_service_client, args.container)
    
    # Perform the specified operation
    if args.operation == "upload":
        upload_blob(
            container_client, 
            args.file, 
            args.blob_name,
            not args.no_overwrite
        )
        
    elif args.operation == "list":
        list_blobs(container_client, args.prefix)
        
    elif args.operation == "delete":
        delete_blob(container_client, args.blob_name)

if __name__ == "__main__":
    main()
```

## Sample Usage

### 1. Upload a file
```bash
# Upload a file with default name
python upload_blob.py upload --file sample.txt

# Upload a file with custom blob name
python upload_blob.py upload --file sample.txt --blob-name uploads/myfile.txt
```

### 2. List blobs
```bash
# List all blobs
python upload_blob.py list

# List blobs with specific prefix
python upload_blob.py list --prefix uploads/
```

### 3. Delete a blob
```bash
python upload_blob.py delete --blob-name uploads/myfile.txt
```

## Key Learning Points

1. **Azure Blob Storage Fundamentals**
   - A storage account can contain multiple containers
   - Containers hold collections of blobs (files)
   - Blob names can include path-like structures with forward slashes (e.g., `uploads/sample.txt`)

2. **Authentication Methods**
   - Connection strings provide quick access for development
   - In production, prefer Azure AD authentication or Managed Identities
   - Always secure connection strings and keys

3. **Blob Storage Operations**
   - Creating containers if they don't exist
   - Uploading blobs with customizable names
   - Listing blobs with optional filtering
   - Cleaning up by deleting blobs

4. **Error Handling**
   - ResourceExistsError when container already exists
   - ResourceNotFoundError when blob doesn't exist
   - Proper error reporting for user-friendly feedback

5. **Command-Line Interface Best Practices**
   - Subparsers for different operations
   - Required and optional arguments
   - Default values for common parameters

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "No connection string provided" error
   - **Solution**: Set the AZURE_STORAGE_CONNECTION_STRING environment variable or provide it as a parameter

2. **Permission Issues**
   - **Problem**: "AuthorizationPermissionMismatch" error
   - **Solution**: Ensure your connection string has the right permissions (read, write, etc.)

3. **Container Name Constraints**
   - **Problem**: Invalid container name error
   - **Solution**: Container names must be lowercase, alphanumeric with hyphens, 3-63 characters

4. **Large File Upload Issues**
   - **Problem**: Timeout when uploading large files
   - **Solution**: For files >100MB, consider using the upload_blob_from_path method

5. **Blob Name Conflicts**
   - **Problem**: Existing blobs not overwritten
   - **Solution**: Set overwrite=True (default in our script) or handle version conflicts manually

## Best Practices

1. **Organize Blobs with Virtual Directories**
   - Use forward slashes in blob names to create logical hierarchies
   - Example: `logs/2023/01/server-log.txt`

2. **Use Metadata for Better Organization**
   - Add metadata to blobs for searching and filtering
   - Include timestamps, content types, and other relevant data

3. **Consider Performance Optimizations**
   - For large files, use chunked uploads
   - For many small files, consider parallel uploads

4. **Implement Retry Logic**
   - Network issues can interrupt uploads
   - Add retry logic for improved reliability

5. **Secure Your Connection Information**
   - Never hardcode connection strings in code
   - Use environment variables or Azure Key Vault

## Cleanup Importance

Always clean up unused blobs to avoid unnecessary storage costs:
1. Delete test blobs after experiments
2. Implement lifecycle policies for production data
3. Consider automated cleanup for temporary data

The provided script includes a delete function that helps with this cleanup process. Use the `delete` operation to remove blobs when they're no longer needed. 