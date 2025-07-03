#!/usr/bin/env python3
"""
GCP LAB07 - Cloud SQL Instance Automation
This script demonstrates how to create, list, and delete Cloud SQL instances
using the Google Cloud SQL Admin API with Python.
"""

import os
import argparse
import time
import json
from tabulate import tabulate
from googleapiclient import discovery
from google.oauth2 import service_account

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

def build_sql_admin_client(credentials):
    """
    Build and return a Cloud SQL Admin API client.
    
    Args:
        credentials: The authenticated credentials
        
    Returns:
        googleapiclient.discovery.Resource: SQL Admin API client
    """
    # TODO: Build and return a SQL Admin API client
    # - Use the discovery.build method with 'sqladmin' and 'v1beta4'
    
    pass

def create_sql_instance(service, project_id, instance_name, db_version="MYSQL_8_0", 
                        tier="db-f1-micro", region="us-central1"):
    """
    Create a new Cloud SQL instance.
    
    Args:
        service: SQL Admin API client
        project_id (str): GCP Project ID
        instance_name (str): Name for the new SQL instance
        db_version (str): Database version (default: MYSQL_8_0)
        tier (str): Machine tier (default: db-f1-micro)
        region (str): Region for the instance (default: us-central1)
        
    Returns:
        dict: The response from the API
    """
    print(f"Creating Cloud SQL instance '{instance_name}' in {region}...")
    
    # TODO: Define the instance configuration
    # - Set the instance name
    # - Set the database version (e.g., MYSQL_8_0, POSTGRES_14)
    # - Configure settings: tier, region, backup
    
    # TODO: Send the instance creation request
    # - Use service.instances().insert
    # - Execute the request and return the response
    
    pass

def wait_for_operation(service, project_id, operation_name):
    """
    Wait for a SQL Admin operation to complete.
    
    Args:
        service: SQL Admin API client
        project_id (str): GCP Project ID
        operation_name (str): Name of the operation to wait for
        
    Returns:
        dict: The completed operation response
    """
    print(f"Waiting for operation {operation_name} to complete...")
    
    # TODO: Implement waiting for an operation to complete
    # - Poll the operation status periodically
    # - Return once the operation is complete
    # - Handle timeouts and errors appropriately
    
    pass

def list_sql_instances(service, project_id):
    """
    List all Cloud SQL instances in the project.
    
    Args:
        service: SQL Admin API client
        project_id (str): GCP Project ID
        
    Returns:
        list: List of SQL instances
    """
    print(f"Listing Cloud SQL instances in project {project_id}...")
    
    # TODO: List SQL instances in the project
    # - Use service.instances().list
    # - Execute the request
    # - Format and display the results
    
    pass

def delete_sql_instance(service, project_id, instance_name):
    """
    Delete a Cloud SQL instance.
    
    Args:
        service: SQL Admin API client
        project_id (str): GCP Project ID
        instance_name (str): Name of the SQL instance to delete
        
    Returns:
        dict: The operation response
    """
    print(f"Deleting Cloud SQL instance '{instance_name}'...")
    
    # TODO: Delete the SQL instance
    # - Use service.instances().delete
    # - Execute the request
    # - Return the operation response
    
    pass

def display_instance_info(instance):
    """
    Display detailed information about a SQL instance.
    
    Args:
        instance (dict): The SQL instance data
    """
    print("\nInstance Details:")
    
    # Basic information
    info_table = [
        ["Name", instance.get("name")],
        ["Database Version", instance.get("databaseVersion")],
        ["State", instance.get("state")],
        ["Region", instance.get("region")],
        ["Machine Type", instance.get("settings", {}).get("tier")],
        ["IP Address", instance.get("ipAddresses", [{}])[0].get("ipAddress", "None") 
                       if instance.get("ipAddresses") else "None"],
        ["Create Time", instance.get("createTime")]
    ]
    
    print(tabulate(info_table, tablefmt="grid"))
    
    # Connection information
    if instance.get("ipAddresses"):
        print("\nConnection Information:")
        print(f"Connection name: {instance.get('connectionName')}")
        print(f"Public IP: {instance.get('ipAddresses', [{}])[0].get('ipAddress', 'None')}")

def main():
    parser = argparse.ArgumentParser(
        description="Create, list, or delete Cloud SQL instances"
    )
    parser.add_argument("--project_id", required=True, help="Your GCP Project ID")
    parser.add_argument("--credentials_file", help="Path to service account credentials JSON file")
    parser.add_argument("--create", action="store_true", help="Create a new SQL instance")
    parser.add_argument("--list", action="store_true", help="List all SQL instances")
    parser.add_argument("--delete", action="store_true", help="Delete a SQL instance")
    parser.add_argument("--instance_name", help="Name for the SQL instance")
    parser.add_argument("--db_version", default="MYSQL_8_0", help="Database version")
    parser.add_argument("--tier", default="db-f1-micro", help="Machine tier")
    parser.add_argument("--region", default="us-central1", help="Region for the instance")
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.create or args.delete:
        if not args.instance_name:
            print("Error: --instance_name is required when using --create or --delete")
            return 1
    
    if not (args.create or args.list or args.delete):
        print("Error: You must specify at least one action: --create, --list, or --delete")
        return 1
    
    try:
        # Authenticate
        credentials = authenticate(args.credentials_file)
        
        # Build the SQL Admin client
        service = build_sql_admin_client(credentials)
        
        # Perform the requested action
        if args.list:
            instances = list_sql_instances(service, args.project_id)
            
            if not instances:
                print("No SQL instances found in this project.")
            else:
                print(f"Found {len(instances)} SQL instance(s).")
        
        if args.create:
            response = create_sql_instance(
                service, 
                args.project_id,
                args.instance_name,
                args.db_version,
                args.tier,
                args.region
            )
            
            if response and 'name' in response:
                operation = wait_for_operation(service, args.project_id, response['name'])
                
                if operation.get('status') == 'DONE':
                    print(f"SQL instance {args.instance_name} created successfully!")
                    
                    # Get details about the created instance
                    instance_request = service.instances().get(
                        project=args.project_id,
                        instance=args.instance_name
                    )
                    instance = instance_request.execute()
                    display_instance_info(instance)
                else:
                    print(f"Operation failed: {operation}")
        
        if args.delete:
            response = delete_sql_instance(service, args.project_id, args.instance_name)
            
            if response and 'name' in response:
                operation = wait_for_operation(service, args.project_id, response['name'])
                
                if operation.get('status') == 'DONE':
                    print(f"SQL instance {args.instance_name} deleted successfully!")
                else:
                    print(f"Operation failed: {operation}")
        
        return 0
    
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 