#!/usr/bin/env python3
"""
GCP LAB04 - Cloud Functions Deployment Script
This script automates the deployment of a Google Cloud Function using the Google APIs.
"""

import os
import sys
import time
import argparse
import subprocess
import tempfile
import zipfile
import base64
from pathlib import Path
from google.cloud import storage
from googleapiclient import discovery
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Deploy a Google Cloud Function'
    )
    parser.add_argument(
        '--project',
        help='GCP Project ID',
        default=os.environ.get('GCP_PROJECT_ID')
    )
    parser.add_argument(
        '--region',
        help='GCP Region for the function',
        default=os.environ.get('GCP_REGION', 'us-central1')
    )
    parser.add_argument(
        '--function_name',
        help='Name of the cloud function',
        default=os.environ.get('FUNCTION_NAME', 'hello-world')
    )
    parser.add_argument(
        '--entry_point',
        help='Entry point (function name in main.py)',
        default=os.environ.get('ENTRY_POINT', 'hello_world')
    )
    parser.add_argument(
        '--runtime',
        help='Python runtime for the function',
        default=os.environ.get('RUNTIME', 'python310')
    )
    parser.add_argument(
        '--source_dir',
        help='Directory containing function source code',
        default=os.environ.get('SOURCE_DIR', '.')
    )
    parser.add_argument(
        '--use_gcloud',
        action='store_true',
        help='Use gcloud CLI instead of API for deployment'
    )
    parser.add_argument(
        '--allow_unauthenticated',
        action='store_true',
        help='Allow unauthenticated invocations'
    )
    
    return parser.parse_args()

def create_source_zip(source_dir, function_name):
    """
    Create a zip file of the source code for deployment.
    
    Args:
        source_dir (str): Directory containing the function source code
        function_name (str): Name of the function
        
    Returns:
        str: Path to the created zip file
    """
    print(f"Packaging source code from '{source_dir}'...")
    
    # Resolve the full path to the source directory
    source_path = Path(source_dir).resolve()
    
    # Create a temporary zip file
    zip_path = os.path.join(tempfile.gettempdir(), f"{function_name}.zip")
    
    # TODO: Create a zip file containing main.py and requirements-function.txt
    # Hint: Use zipfile.ZipFile() to create a zip file and write the source files to it
    
    print(f"Source code packaged to: {zip_path}")
    return zip_path

def upload_source_to_gcs(zip_path, project_id, function_name):
    """
    Upload the source zip file to Google Cloud Storage.
    
    Args:
        zip_path (str): Path to the source zip file
        project_id (str): GCP Project ID
        function_name (str): Name of the function
        
    Returns:
        str: GCS URL of the uploaded zip file
    """
    print(f"Uploading source code to GCS...")
    
    # Bucket name for the function source code
    # Note: This bucket must already exist in your project
    bucket_name = f"{project_id}-cloud-functions"
    
    # TODO: Initialize the Google Cloud Storage client
    
    # TODO: Check if the bucket exists, and create it if it doesn't
    
    # TODO: Upload the zip file to the GCS bucket
    
    # TODO: Return the GCS URL of the uploaded source code
    pass

def deploy_function_with_api(project_id, region, function_name, entry_point, runtime, source_gcs_url, allow_unauthenticated):
    """
    Deploy a Cloud Function using the API.
    
    Args:
        project_id (str): GCP Project ID
        region (str): Region for the function
        function_name (str): Name of the function
        entry_point (str): Function to execute (from main.py)
        runtime (str): Python runtime version
        source_gcs_url (str): GCS URL to the source code
        allow_unauthenticated (bool): Whether to allow unauthenticated invocations
        
    Returns:
        dict: The created function resource
    """
    print(f"Deploying function '{function_name}' to region '{region}'...")
    
    # Full name of the function
    function_path = f"projects/{project_id}/locations/{region}/functions/{function_name}"
    
    # TODO: Initialize the Cloud Functions API client
    
    # TODO: Create the function configuration
    # - Set the entry point
    # - Set the runtime
    # - Configure the HTTP trigger
    # - Set the source code GCS URL
    
    # TODO: Check if the function already exists
    
    # TODO: Create or update the function
    
    # TODO: Wait for the operation to complete
    
    # TODO: If allow_unauthenticated is True, configure IAM policy for public access
    
    # TODO: Return the deployed function details
    pass

def deploy_function_with_gcloud(project_id, region, function_name, entry_point, runtime, source_dir, allow_unauthenticated):
    """
    Deploy a Cloud Function using the gcloud CLI.
    
    Args:
        project_id (str): GCP Project ID
        region (str): Region for the function
        function_name (str): Name of the function
        entry_point (str): Function to execute (from main.py)
        runtime (str): Python runtime version
        source_dir (str): Directory containing the function source code
        allow_unauthenticated (bool): Whether to allow unauthenticated invocations
        
    Returns:
        bool: Whether the deployment was successful
    """
    print(f"Deploying function '{function_name}' using gcloud CLI...")
    
    # Build the gcloud command
    command = [
        "gcloud", "functions", "deploy", function_name,
        "--project", project_id,
        "--region", region,
        "--runtime", runtime,
        "--trigger-http",
        "--entry-point", entry_point,
        "--source", source_dir
    ]
    
    if allow_unauthenticated:
        command.append("--allow-unauthenticated")
    
    # Execute the command
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        
        if result.stderr:
            print(f"Warnings: {result.stderr}")
            
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error deploying function: {e}")
        print(f"stderr: {e.stderr}")
        return False

def main():
    """Main function to deploy a Google Cloud Function."""
    args = parse_arguments()
    
    # Verify we have the project ID
    if not args.project:
        print("Error: GCP Project ID is required. Provide it with --project flag or set GCP_PROJECT_ID environment variable.")
        return 1
        
    try:
        # Check if main.py exists in the source directory
        main_py_path = os.path.join(args.source_dir, "main.py")
        if not os.path.exists(main_py_path):
            print(f"Error: main.py not found in '{args.source_dir}'")
            return 1
            
        # Check if requirements-function.txt exists in the source directory
        req_path = os.path.join(args.source_dir, "requirements-function.txt")
        if not os.path.exists(req_path):
            print(f"Warning: requirements-function.txt not found in '{args.source_dir}'. The function may not have the necessary dependencies.")
            
        if args.use_gcloud:
            # Deploy with gcloud CLI
            success = deploy_function_with_gcloud(
                args.project,
                args.region,
                args.function_name,
                args.entry_point,
                args.runtime,
                args.source_dir,
                args.allow_unauthenticated
            )
            
            if not success:
                return 1
        else:
            # Deploy with API
            # Package the source code
            zip_path = create_source_zip(args.source_dir, args.function_name)
            
            # Upload to GCS
            source_gcs_url = upload_source_to_gcs(zip_path, args.project, args.function_name)
            
            # Deploy the function
            function = deploy_function_with_api(
                args.project,
                args.region,
                args.function_name,
                args.entry_point,
                args.runtime,
                source_gcs_url,
                args.allow_unauthenticated
            )
            
            print("\nFunction deployed successfully!")
            print(f"HTTP Trigger URL: {function.get('httpsTrigger', {}).get('url', 'N/A')}")
        
        # Show the cleanup command
        print("\n🧹 Cleanup:")
        print("To delete this function when you're done, run:")
        print(f"gcloud functions delete {args.function_name} --region={args.region} --project={args.project}")
        
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 