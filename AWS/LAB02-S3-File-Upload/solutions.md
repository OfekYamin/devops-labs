# LAB02 - S3 File Upload: Solutions

This document contains the complete solution for the S3 File Upload Automation lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for upload_file.py

```python
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
        # Initialize the S3 client with the specified region
        s3_client = boto3.client('s3', region_name=region)
        
        # Set up LocationConstraint parameter for regions other than us-east-1
        location = {'LocationConstraint': region}
        
        # us-east-1 is the default and doesn't accept a LocationConstraint
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
        
        print(f"Created bucket: {bucket_name}")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"Bucket {bucket_name} already exists and is owned by you.")
            return True
        elif e.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f"Bucket {bucket_name} already exists but is owned by another account.")
            return False
        else:
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
    # If object_name is not specified, use the file_path's basename
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    try:
        # Initialize the S3 client
        s3_client = boto3.client('s3')
        
        # Set ACL parameter based on make_public flag
        extra_args = {'ACL': 'public-read'} if make_public else {}
        
        print(f"Uploading file: {file_path} to {bucket_name}/{object_name}")
        
        # Upload the file
        s3_client.upload_file(
            file_path, 
            bucket_name, 
            object_name,
            ExtraArgs=extra_args
        )
        
        print("Upload complete!")
        
        # If the file is public, generate a public URL
        if make_public:
            region = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint'] or 'us-east-1'
            
            # Generate public URL
            url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{object_name}"
            print(f"Public URL: {url}")
        
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
        # Initialize the S3 client
        s3_client = boto3.client('s3')
        
        # Generate the presigned URL
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name
            },
            ExpiresIn=expiration
        )
        
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
        # Initialize the S3 client
        s3_client = boto3.client('s3')
        
        # Get the list of objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            
            print(f"\nFiles in bucket {bucket_name}:")
            for file in files:
                print(f"- {file}")
                
            return files
        else:
            print(f"No files found in bucket {bucket_name}")
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
        # Initialize S3 client
        s3_client = boto3.client('s3')
        
        # Delete all objects if force=True
        if force:
            print(f"Deleting all objects in bucket {bucket_name}...")
            
            # List all objects in the bucket
            response = s3_client.list_objects_v2(Bucket=bucket_name)
            
            if 'Contents' in response:
                # Create a list of objects to delete
                objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]
                
                # Delete the objects
                s3_client.delete_objects(
                    Bucket=bucket_name,
                    Delete={'Objects': objects_to_delete}
                )
                
                # For buckets with more than 1000 objects, we need to paginate
                while response['IsTruncated']:
                    response = s3_client.list_objects_v2(
                        Bucket=bucket_name,
                        ContinuationToken=response['NextContinuationToken']
                    )
                    
                    if 'Contents' in response:
                        objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]
                        s3_client.delete_objects(
                            Bucket=bucket_name,
                            Delete={'Objects': objects_to_delete}
                        )
        
        # Delete the bucket
        print(f"Deleting bucket: {bucket_name}")
        s3_client.delete_bucket(Bucket=bucket_name)
        
        print("Bucket deleted successfully!")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketNotEmpty':
            print(f"Bucket {bucket_name} is not empty. Use force=True to delete all objects first.")
        else:
            print(f"Error deleting bucket: {e}")
        return False

def main():
    """Main function to execute the script"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='S3 File Upload Automation')
    parser.add_argument('--file', required=True, help='Path to the file to upload')
    parser.add_argument('--bucket', help='Name of the S3 bucket (a random name will be generated if not provided)')
    parser.add_argument('--region', default=DEFAULT_REGION, help=f'AWS region (default: {DEFAULT_REGION})')
    parser.add_argument('--public', action='store_true', help='Make the uploaded file publicly accessible')
    parser.add_argument('--cleanup', action='store_true', help='Delete the bucket after upload')
    
    args = parser.parse_args()
    
    # Validate that the file exists
    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' does not exist")
        sys.exit(1)
    
    # Generate a bucket name if not provided
    bucket_name = args.bucket
    if not bucket_name:
        bucket_name = f"{DEFAULT_BUCKET_PREFIX}{uuid.uuid4().hex[:8]}"
    
    print("AWS S3 File Upload Tool")
    print("=====================")
    
    # Create the bucket
    if create_bucket(bucket_name, args.region):
        # Upload the file
        file_path = args.file
        object_name = os.path.basename(file_path)
        
        if upload_file(file_path, bucket_name, object_name, args.public):
            # List files in the bucket
            list_bucket_files(bucket_name)
            
            # Generate a presigned URL (useful if the file is not public)
            if not args.public:
                generate_presigned_url(bucket_name, object_name)
            
            # Cleanup if requested
            if args.cleanup:
                delete_bucket(bucket_name, force=True)
            else:
                print(f"\n⚠️  IMPORTANT: Bucket '{bucket_name}' will incur storage charges until deleted.")
                print(f"To delete the bucket, run: aws s3 rb s3://{bucket_name} --force")

if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **S3 Bucket Management**:
   - Creating buckets with proper region configuration
   - Handling bucket name uniqueness requirements
   - Properly deleting buckets and their contents

2. **File Operations**:
   - Uploading files to S3 buckets
   - Setting object permissions (public vs. private)
   - Listing objects within a bucket

3. **S3 Access Controls**:
   - Using ACL settings to control object visibility
   - Generating presigned URLs for temporary access
   - Understanding public URL formats for S3 objects

4. **Command-Line Interface Design**:
   - Creating a flexible CLI using argparse
   - Providing sensible defaults and auto-generation of resources
   - Supporting cleanup options to prevent unexpected charges

5. **Error Handling**:
   - Handling different error types when working with S3
   - Validating inputs before making API calls
   - Providing clear error messages for common issues

## Common Issues and Troubleshooting

1. **Bucket Naming Constraints**:
   - Bucket names must be globally unique across all AWS accounts
   - Names must be between 3 and 63 characters
   - Names must be lowercase letters, numbers, dots, and hyphens
   - Solution: Use a unique prefix with random suffixes

2. **Permission Issues**:
   - "Access Denied" errors when your IAM user lacks S3 permissions
   - Solution: Attach the AmazonS3FullAccess policy or create a custom policy

3. **Region Considerations**:
   - S3 is a global service, but buckets are created in specific regions
   - File access times can be affected by choosing regions far from your users
   - Solution: Choose a region close to your target users for better performance

4. **Public Access Blocks**:
   - Default account settings may block public access even when requested
   - Solution: Check account-level S3 Block Public Access settings if public access isn't working

5. **Bucket Deletion Issues**:
   - Buckets cannot be deleted if they contain objects
   - Solution: Use the force option to delete all objects first 
