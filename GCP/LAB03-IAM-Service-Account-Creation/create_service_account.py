#!/usr/bin/env python3
"""
GCP LAB03 - IAM Service Account Creation Script
This script demonstrates how to create, manage, and assign roles to 
service accounts in Google Cloud Platform using the IAM API.
"""

import os
import argparse
import time
from googleapiclient import discovery
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Create and manage IAM service accounts in GCP'
    )
    parser.add_argument(
        '--project', 
        help='GCP Project ID',
        default=os.environ.get('GCP_PROJECT_ID')
    )
    parser.add_argument(
        '--account_id', 
        help='Service account ID (must be between 6 and 30 characters)',
        default=os.environ.get('SERVICE_ACCOUNT_ID', 'devops-service-account')
    )
    parser.add_argument(
        '--display_name', 
        help='Display name for the service account',
        default=os.environ.get('SERVICE_ACCOUNT_NAME', 'DevOps Service Account')
    )
    parser.add_argument(
        '--description', 
        help='Description for the service account',
        default=os.environ.get('SERVICE_ACCOUNT_DESCRIPTION', 'Service account for DevOps automation')
    )
    parser.add_argument(
        '--roles', 
        help='Comma-separated list of roles to assign to the service account',
        default=os.environ.get('SERVICE_ACCOUNT_ROLES', 'roles/viewer')
    )
    parser.add_argument(
        '--list', 
        action='store_true',
        help='List all service accounts in the project'
    )
    
    return parser.parse_args()

def create_service_account(project_id, account_id, display_name, description):
    """
    Create a new service account in the specified GCP project.
    
    Args:
        project_id (str): GCP Project ID
        account_id (str): Service account ID (must be between 6 and 30 characters)
        display_name (str): Display name for the service account
        description (str): Description for the service account
        
    Returns:
        dict: The created service account resource
    """
    print(f"Creating service account '{account_id}' in project '{project_id}'...")
    
    # TODO: Initialize the IAM service API client
    
    # TODO: Create the service account request body
    
    # TODO: Submit the create service account request
    
    # TODO: Return the service account resource
    pass

def assign_role_to_service_account(project_id, service_account_email, role):
    """
    Assign a role to a service account at the project level.
    
    Args:
        project_id (str): GCP Project ID
        service_account_email (str): Full email of the service account
        role (str): Role to assign (e.g., 'roles/storage.admin')
        
    Returns:
        dict: The policy binding response
    """
    print(f"Assigning role '{role}' to service account '{service_account_email}'...")
    
    # TODO: Initialize the Resource Manager API client
    
    # TODO: Get the current IAM policy for the project
    
    # TODO: Create the binding for the service account and role
    
    # TODO: Add the new binding to the policy
    
    # TODO: Set the updated IAM policy
    
    print(f"Successfully assigned role '{role}' to '{service_account_email}'")
    
def list_service_accounts(project_id):
    """
    List all service accounts in the specified GCP project.
    
    Args:
        project_id (str): GCP Project ID
    """
    print(f"Listing service accounts in project '{project_id}':")
    print("-" * 60)
    
    # TODO: Initialize the IAM service API client
    
    # TODO: List all service accounts in the project
    
    print("-" * 60)

def main():
    """Main function to create and manage a service account."""
    args = parse_arguments()
    
    # Verify we have the project ID
    if not args.project:
        print("Error: GCP Project ID is required. Provide it with --project flag or set GCP_PROJECT_ID environment variable.")
        return 1
    
    try:
        # List service accounts if requested
        if args.list:
            list_service_accounts(args.project)
            return 0
        
        # Create the service account
        service_account = create_service_account(
            args.project,
            args.account_id,
            args.display_name,
            args.description
        )
        
        # Wait a moment for the service account to be fully created
        print("Waiting for service account to be fully provisioned...")
        time.sleep(2)
        
        # Assign roles if specified
        if service_account and args.roles:
            roles_list = [role.strip() for role in args.roles.split(',')]
            for role in roles_list:
                assign_role_to_service_account(
                    args.project,
                    service_account['email'],
                    role
                )
        
        # Show the cleanup command
        print("\n🧹 Cleanup:")
        print("To delete this service account when you're done, run:")
        print(f"gcloud iam service-accounts delete {service_account['email']} --project={args.project}")
        
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 