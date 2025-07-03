#!/usr/bin/env python3
"""
GCP LAB10 - Cloud Run Deployment
This script automates the deployment of a containerized application to Google Cloud Run.
It handles building Docker images, pushing to Container Registry, and deploying to Cloud Run.
"""

import os
import argparse
import subprocess
import time
from google.oauth2 import service_account
from googleapiclient import discovery
from googleapiclient.errors import HttpError

def authenticate(credentials_file=None):
    """
    Authenticate with Google Cloud using service account credentials.
    
    Args:
        credentials_file (str, optional): Path to service account JSON file.
            If None, uses the GOOGLE_APPLICATION_CREDENTIALS environment variable.
            
    Returns:
        google.oauth2.service_account.Credentials: Authenticated credentials
    """
    # TODO: Implement authentication
    # - If credentials_file is provided, use it directly
    # - Otherwise, use the GOOGLE_APPLICATION_CREDENTIALS environment variable
    # - Return the credentials object
    
    pass

def build_cloud_run_client(credentials):
    """
    Build and return a Cloud Run API client.
    
    Args:
        credentials: The authenticated credentials
        
    Returns:
        googleapiclient.discovery.Resource: Cloud Run API client
    """
    # TODO: Build and return a Cloud Run API client
    # - Use the discovery.build method with 'run' and 'v1'
    
    pass

def build_and_push_image(project_id, image_name, dockerfile_dir="."):
    """
    Build a Docker image and push it to Google Container Registry.
    
    Args:
        project_id (str): GCP Project ID
        image_name (str): Name for the container image
        dockerfile_dir (str): Directory containing the Dockerfile
        
    Returns:
        str: The full image path in GCR
    """
    print(f"Building and pushing Docker image to Google Container Registry...")
    
    # TODO: Implement Docker build and push
    # - Build the Docker image using subprocess
    # - Tag the image for Google Container Registry (gcr.io)
    # - Push the image to GCR
    # - Return the full image path
    
    pass

def deploy_to_cloud_run(service, project_id, service_name, image_path, region="us-central1"):
    """
    Deploy a container image to Cloud Run.
    
    Args:
        service: Cloud Run API client
        project_id (str): GCP Project ID
        service_name (str): Name for the Cloud Run service
        image_path (str): Full path to the container image
        region (str): Region for deployment
        
    Returns:
        dict: The deployment response
    """
    print(f"Deploying {image_path} to Cloud Run as '{service_name}'...")
    
    # TODO: Implement Cloud Run deployment
    # - Create a Cloud Run service configuration
    # - Set container image, scaling, memory, CPU, etc.
    # - Deploy using the Cloud Run API
    # - Return the deployment response
    
    pass

def wait_for_deployment(service, name):
    """
    Wait for a Cloud Run deployment to complete.
    
    Args:
        service: Cloud Run API client
        name (str): Full name of the Cloud Run service
        
    Returns:
        dict: The completed service
    """
    print(f"Waiting for deployment of {name} to complete...")
    
    # TODO: Implement waiting for deployment completion
    # - Poll the service status periodically
    # - Return once the deployment is complete
    # - Handle timeouts and errors
    
    pass

def get_service_url(service, name):
    """
    Get the URL of a deployed Cloud Run service.
    
    Args:
        service: Cloud Run API client
        name (str): Full name of the Cloud Run service
        
    Returns:
        str: The service URL
    """
    # TODO: Implement getting the service URL
    # - Get the service details
    # - Extract and return the URL
    
    pass

def main():
    parser = argparse.ArgumentParser(
        description="Deploy a containerized application to Google Cloud Run"
    )
    parser.add_argument("--project_id", required=True, help="Your GCP Project ID")
    parser.add_argument("--credentials_file", help="Path to service account credentials JSON file")
    parser.add_argument("--service_name", default="devops-cloudrun", help="Name for the Cloud Run service")
    parser.add_argument("--image_name", default="devops-cloudrun", help="Name for the container image")
    parser.add_argument("--region", default="us-central1", help="Region for deployment")
    parser.add_argument("--dockerfile_dir", default=".", help="Directory containing Dockerfile")
    parser.add_argument("--public", action="store_true", help="Make the service publicly accessible")
    
    args = parser.parse_args()
    
    try:
        # Authenticate with Google Cloud
        credentials = authenticate(args.credentials_file)
        
        # Build the Cloud Run client
        run_service = build_cloud_run_client(credentials)
        
        # Build and push the Docker image
        image_path = build_and_push_image(
            args.project_id,
            args.image_name,
            args.dockerfile_dir
        )
        
        # Deploy to Cloud Run
        parent = f"projects/{args.project_id}/locations/{args.region}"
        service_name = f"{parent}/services/{args.service_name}"
        
        response = deploy_to_cloud_run(
            run_service,
            args.project_id,
            args.service_name,
            image_path,
            args.region
        )
        
        if response:
            # Wait for deployment to complete
            service_details = wait_for_deployment(run_service, service_name)
            
            # Get and display the service URL
            service_url = get_service_url(run_service, service_name)
            
            print("\n" + "=" * 50)
            print(f"Cloud Run deployment successful!")
            print(f"Service URL: {service_url}")
            print("=" * 50 + "\n")
            
            print("To clean up this deployment, run:")
            print(f"gcloud run services delete {args.service_name} --region={args.region} --quiet")
        
        return 0
    
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    main() 