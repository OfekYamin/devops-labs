#!/usr/bin/env python3
"""
AWS LAB02 - S3 File Upload Automation

This script demonstrates how to use boto3 to automate S3 bucket operations,
including creating buckets, uploading files, setting permissions, and generating presigned URLs.

Usage:
    python upload_file.py --file <file_path> [--bucket <bucket_name>] [--region <region>] [--public]
"""

import boto3
import argparse
import os
import uuid
import sys
from botocore.exceptions import ClientError

# Default configuration
DEFAULT_REGION = 'eu-west-1'
DEFAULT_BUCKET_PREFIX = 'devops-lab-bucket-'


def create_bucket(bucket_name, region=DEFAULT_REGION):
    """
    Create an S3 bucket in the specified region

    Args:
        bucket_name (str): Name of the bucket to create
        region (str): AWS region to create the bucket in

    Returns:
        bool: True if bucket was created or already exists, False on error
    """
    try:
        # TODO: Initialize the S3 client with the specified region
        
        # TODO: Set up LocationConstraint parameter for regions other than us-east-1
        # location = {'LocationConstraint': region}
        
        # TODO: Create the bucket
        # Remember that us-east-1 is the default and doesn't accept a LocationConstraint
        # For other regions, you need to provide a CreateBucketConfiguration
        
        print(f"Created bucket: {bucket_name}")
        return True
    except ClientError as e:
        # TODO: Handle different error codes appropriately
        # - BucketAlreadyOwnedByYou
        # - BucketAlreadyExists
        # - Other errors
        print(f"Error creating bucket: {e}")
        return False


def upload_file(file_path, bucket_name, object_name=None, make_public=False):
    """
    Upload a file to an S3 bucket

    Args:
        file_path (str): Path to the file to upload
        bucket_name (str): Name of the bucket to upload to
        object_name (str): S3 object name (if None, file_path's basename is used)
        make_public (bool): Whether to make the file publicly accessible

    Returns:
        bool: True if file was uploaded, False on error
    """
    # TODO: If object_name is not specified, use the file_path's basename
    
    try:
        # TODO: Initialize the S3 client
        
        # TODO: Set ACL parameter based on make_public flag
        # extra_args = {'ACL': 'public-read'} if make_public else {}
        
        print(f"Uploading file: {file_path} to {bucket_name}/{object_name}")
        
        # TODO: Upload the file using s3_client.upload_file
        # Don't forget to include ExtraArgs if make_public is True
        
        print("Upload complete!")
        
        # TODO: If the file is public, generate and print a public URL
        # You'll need to get the bucket region first
        
        return True
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False


def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """
    Generate a presigned URL for an S3 object

    Args:
        bucket_name (str): Name of the bucket
        object_name (str): Name of the S3 object
        expiration (int): Time in seconds the URL will be valid for

    Returns:
        str: Presigned URL or None if error
    """
    try:
        # TODO: Initialize the S3 client
        
        # TODO: Generate the presigned URL using s3_client.generate_presigned_url
        # You'll need to specify:
        # - The operation ('get_object')
        # - The parameters (bucket and key)
        # - The expiration time in seconds
        
        url = None  # Replace with your implementation
        
        print(f"\nGenerated presigned URL (valid for {expiration} seconds):")
        print(url)
        
        return url
    except ClientError as e:
        print(f"Error generating presigned URL: {e}")
        return None


def list_bucket_files(bucket_name):
    """
    List all files in an S3 bucket

    Args:
        bucket_name (str): Name of the bucket

    Returns:
        list: List of file names in the bucket
    """
    try:
        # TODO: Initialize the S3 client
        
        # TODO: Get the list of objects in the bucket using list_objects_v2
        
        # TODO: Extract and print the Key (filename) from each object
        # Example:
        # print(f"\nFiles in bucket {bucket_name}:")
        # for file in files:
        #     print(f"- {file}")
        
        # Return a list of filenames or an empty list if none found
        return []
    except ClientError as e:
        print(f"Error listing bucket files: {e}")
        return []


def delete_bucket(bucket_name, force=False):
    """
    Delete an S3 bucket

    Args:
        bucket_name (str): Name of the bucket to delete
        force (bool): If True, delete all objects in the bucket first

    Returns:
        bool: True if bucket was deleted, False on error
    """
    try:
        # TODO: Initialize S3 client
        
        # TODO: If force is True, delete all objects in the bucket first
        # This will require:
        # 1. Listing all objects in the bucket
        # 2. Deleting each object
        
        # TODO: Delete the bucket once it's empty
        
        print(f"Deleted bucket: {bucket_name}")
        return True
    except ClientError as e:
        print(f"Error deleting bucket: {e}")
        return False


def main():
    """
    Main function to parse arguments and execute S3 operations
    """
    parser = argparse.ArgumentParser(description="S3 File Upload Tool")
    
    # TODO: Add arguments to the parser:
    # --file: Path to the file to upload
    # --bucket: Bucket name (optional)
    # --region: AWS region (optional, default to DEFAULT_REGION)
    # --public: Flag to make the file publicly accessible
    # --url: Flag to generate a presigned URL
    # --list: Flag to list files in the bucket
    # --delete: Flag to delete the bucket after operations
    # --force: Flag to force deletion of non-empty buckets
    
    # TODO: Parse the arguments
    args = None  # Replace with parser.parse_args()
    
    # TODO: Generate a unique bucket name if none is provided
    # Example: bucket_name = args.bucket or f"{DEFAULT_BUCKET_PREFIX}{uuid.uuid4().hex[:8]}"
    
    # TODO: Implement the main workflow:
    # 1. Create bucket if it doesn't exist
    # 2. Upload file if --file is provided
    # 3. Generate presigned URL if --url is specified
    # 4. List files if --list is specified
    # 5. Delete bucket if --delete is specified
    
    print("\nS3 operations completed successfully!")


if __name__ == "__main__":
    main()