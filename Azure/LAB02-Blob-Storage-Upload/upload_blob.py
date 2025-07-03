#!/usr/bin/env python3
"""
Azure Blob Storage Upload Automation Script

This script demonstrates how to automate file uploads to Azure Blob Storage using 
the Azure SDK for Python. It includes functions for creating containers, uploading files,
listing blobs, and cleaning up resources.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import argparse
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError

def get_blob_service_client(connection_string=None):
    """
    Create a blob service client using connection string.
    
    TODO: Implement this function to:
    1. Get the connection string (from parameter or environment variable)
    2. Create and return a BlobServiceClient
    
    Args:
        connection_string (str, optional): Azure Storage connection string.
                                          If None, tries to get from environment.
    
    Returns:
        BlobServiceClient: The blob service client object
    """
    # TODO: Try to get connection string from environment if not provided
    
    # TODO: Check if connection string exists and exit if not
    
    # TODO: Create and return the BlobServiceClient
    pass

def create_container(blob_service_client, container_name):
    """
    Create a container in the storage account if it doesn't exist.
    
    TODO: Implement this function to:
    1. Get a container client from the blob service client
    2. Create the container (handle the case when it already exists)
    
    Args:
        blob_service_client (BlobServiceClient): The blob service client
        container_name (str): Name of the container to create
    
    Returns:
        ContainerClient: The container client
    """
    print(f"Creating container '{container_name}' (if it doesn't exist)...")
    
    # TODO: Get container client 
    
    # TODO: Create the container (handle ResourceExistsError)
    
    # TODO: Return the container client
    pass

def upload_blob(container_client, file_path, blob_name=None, overwrite=True):
    """
    Upload a file to the specified container as a blob.
    
    TODO: Implement this function to:
    1. Determine the blob name if not provided
    2. Check if the file exists
    3. Open and upload the file
    
    Args:
        container_client (ContainerClient): The container client
        file_path (str): Path to the file to upload
        blob_name (str, optional): Name to give the blob. If None, uses file name.
        overwrite (bool): Whether to overwrite if blob exists
    
    Returns:
        str: The name of the uploaded blob
    """
    # TODO: If blob_name not provided, use the file name from file_path
    
    # TODO: Check if file exists and exit if not
    
    # TODO: Open the file and upload it as a blob
    
    # TODO: Return the blob name
    pass

def list_blobs(container_client, prefix=None):
    """
    List all blobs in the container with optional prefix filter.
    
    TODO: Implement this function to:
    1. List blobs with optional prefix filter
    2. Print each blob name
    
    Args:
        container_client (ContainerClient): The container client
        prefix (str, optional): Prefix filter for blob names
    
    Returns:
        list: List of blob names
    """
    # TODO: List blobs with optional prefix
    
    # TODO: Print and collect blob names
    
    # TODO: Return the list of blob names
    pass

def delete_blob(container_client, blob_name):
    """
    Delete a blob from the container.
    
    TODO: Implement this function to:
    1. Delete the specified blob
    2. Handle the case when the blob doesn't exist
    
    Args:
        container_client (ContainerClient): The container client
        blob_name (str): Name of the blob to delete
    
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    # TODO: Delete the blob and handle ResourceNotFoundError
    
    # TODO: Return success status
    pass

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
    
    # TODO: Get blob service client
    
    # TODO: Create container
    
    # TODO: Perform the specified operation
    # 1. If args.operation == "upload": call upload_blob()
    # 2. If args.operation == "list": call list_blobs()
    # 3. If args.operation == "delete": call delete_blob()

if __name__ == "__main__":
    main() 