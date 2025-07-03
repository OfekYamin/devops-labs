#!/usr/bin/env python3
"""
GCP LAB02 - Google Cloud Storage (GCS) File Upload Script
This script demonstrates how to upload files to Google Cloud Storage
and list the contents of a bucket using the google-cloud-storage Python SDK.
"""

import os
import argparse
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Upload a file to Google Cloud Storage'
    )
    parser.add_argument(
        '--project', 
        help='GCP Project ID',
        default=os.environ.get('GCP_PROJECT_ID')
    )
    parser.add_argument(
        '--bucket', 
        help='GCS Bucket name',
        default=os.environ.get('GCS_BUCKET_NAME')
    )
    parser.add_argument(
        '--file', 
        help='Local file path to upload',
        default=os.environ.get('UPLOAD_FILE_PATH', 'sample.txt')
    )
    parser.add_argument(
        '--destination', 
        help='Destination path in the bucket (including filename)',
        default=os.environ.get('DESTINATION_PATH')
    )
    parser.add_argument(
        '--list', 
        action='store_true',
        help='List all files in the bucket after upload'
    )
    
    return parser.parse_args()

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name=None):
    """
    Upload a file to Google Cloud Storage bucket.
    
    Args:
        bucket_name (str): Name of the GCS bucket
        source_file_path (str): Path to the local file to upload
        destination_blob_name (str, optional): Name to give the file in GCS
            If not specified, uses the basename of the source file
            
    Returns:
        blob: The uploaded blob object
    """
    # If destination not specified, use the source filename
    if not destination_blob_name:
        destination_blob_name = os.path.basename(source_file_path)
    
    # TODO: Initialize the GCS client
    
    # TODO: Get the bucket object
    
    # TODO: Get a blob object
    
    # TODO: Upload the file
    
    # TODO: Print upload confirmation message
    
    # TODO: Return the blob object
    pass

def list_blobs(bucket_name):
    """
    List all blobs in a GCS bucket.
    
    Args:
        bucket_name (str): Name of the GCS bucket
    """
    print(f"\nListing objects in bucket: {bucket_name}")
    print("-" * 50)
    
    # TODO: Initialize the GCS client
    
    # TODO: List all blobs in the bucket and print their names
    # Hint: Use client.list_blobs() and iterate over the results
    
    print("-" * 50)

def main():
    """Main function to upload a file to GCS and optionally list bucket contents."""
    args = parse_arguments()
    
    # Verify we have the required arguments
    if not args.bucket:
        print("Error: GCS Bucket name is required. Provide it with --bucket flag or set GCS_BUCKET_NAME environment variable.")
        return 1
    
    # If destination path wasn't provided, use the source filename
    destination_blob_name = args.destination or os.path.basename(args.file)
    
    print(f"Uploading file: {args.file}")
    print(f"To bucket: {args.bucket}")
    print(f"As: {destination_blob_name}")
    
    try:
        # Upload the file
        blob = upload_to_gcs(args.bucket, args.file, destination_blob_name)
        
        # List files in the bucket if requested
        if args.list:
            list_blobs(args.bucket)
            
        # TODO: Add code to demonstrate blob metadata and generation
        # (Extra credit exercise)
        
        print("\nUpload completed successfully!")
        print(f"Public URL: https://storage.googleapis.com/{args.bucket}/{destination_blob_name}")
        
        # Cleanup reminder
        print("\n🧹 Remember to clean up the uploaded file when done:")
        print(f"   - Use the Google Cloud Console, or")
        print(f"   - Run: 'gsutil rm gs://{args.bucket}/{destination_blob_name}'")
        
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 