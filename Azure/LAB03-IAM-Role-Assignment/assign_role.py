#!/usr/bin/env python3
"""
Azure IAM Role Assignment Automation Script

This script demonstrates how to automate role assignments in Azure using 
the Azure SDK for Python. It includes functions for assigning roles,
listing role assignments, and revoking them.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import uuid
import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.core.exceptions import HttpResponseError, ResourceNotFoundError

def get_auth_client():
    """
    Create an authorization management client using DefaultAzureCredential.
    
    TODO: Implement this function to:
    1. Get the subscription ID from environment variables
    2. Create DefaultAzureCredential
    3. Create and return AuthorizationManagementClient
    
    Returns:
        tuple: (auth_client, subscription_id)
    """
    # TODO: Get subscription ID from environment variables
    
    # TODO: Create credential using DefaultAzureCredential
    
    # TODO: Create and return auth client and subscription_id
    pass

def assign_role(auth_client, subscription_id, resource_group, role_name, principal_id):
    """
    Assign a role to a principal at resource group scope.
    
    TODO: Implement this function to:
    1. Determine the scope based on resource group
    2. Find the role definition ID for the given role name
    3. Create a role assignment
    
    Args:
        auth_client: The authorization management client
        subscription_id: The subscription ID
        resource_group: The resource group name
        role_name: The role name (e.g., "Reader", "Contributor")
        principal_id: The principal's object ID (user, group, or service principal)
        
    Returns:
        dict: The role assignment details
    """
    print(f"Assigning role '{role_name}' to principal '{principal_id}' on resource group '{resource_group}'...")
    
    # TODO: Define the scope for the resource group
    
    # TODO: Define role definition ID mapping or lookup mechanism
    
    # TODO: Create a new role assignment with a unique UUID
    
    # TODO: Return assignment details
    pass

def list_role_assignments(auth_client, subscription_id, resource_group=None, principal_id=None):
    """
    List role assignments, optionally filtered by resource group or principal.
    
    TODO: Implement this function to:
    1. List role assignments with optional filtering
    2. Format and return the results
    
    Args:
        auth_client: The authorization management client
        subscription_id: The subscription ID
        resource_group: Optional resource group to filter by
        principal_id: Optional principal ID to filter by
        
    Returns:
        list: The list of role assignments
    """
    if resource_group:
        print(f"Listing role assignments for resource group '{resource_group}'...")
    elif principal_id:
        print(f"Listing role assignments for principal '{principal_id}'...")
    else:
        print("Listing all role assignments...")
    
    # TODO: List role assignments with optional filtering
    
    # TODO: Format and return the results
    pass

def delete_role_assignment(auth_client, role_assignment_id):
    """
    Delete a role assignment.
    
    TODO: Implement this function to:
    1. Delete the specified role assignment
    2. Handle errors appropriately
    
    Args:
        auth_client: The authorization management client
        role_assignment_id: The ID of the role assignment to delete
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting role assignment '{role_assignment_id}'...")
    
    # TODO: Delete the role assignment
    
    # TODO: Return success status
    pass

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description="Azure IAM Role Assignment Tool")
    
    # Operation subparsers
    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")
    
    # Assign role operation
    assign_parser = subparsers.add_parser("assign", help="Assign a role to a principal")
    assign_parser.add_argument("--resource-group", required=True, help="Resource group name")
    assign_parser.add_argument("--role", required=True, help="Role name (e.g., Reader, Contributor)")
    assign_parser.add_argument("--principal-id", required=True, help="Object ID of the principal")
    
    # List role assignments operation
    list_parser = subparsers.add_parser("list", help="List role assignments")
    list_parser.add_argument("--resource-group", help="Filter by resource group name")
    list_parser.add_argument("--principal-id", help="Filter by principal object ID")
    
    # Delete role assignment operation
    delete_parser = subparsers.add_parser("delete", help="Delete a role assignment")
    delete_parser.add_argument("--assignment-id", required=True, help="ID of the role assignment to delete")
    
    args = parser.parse_args()
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    try:
        # TODO: Get auth client
        
        # TODO: Perform the requested operation
        # 1. If args.operation == "assign": call assign_role()
        # 2. If args.operation == "list": call list_role_assignments()
        # 3. If args.operation == "delete": call delete_role_assignment()
        pass
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 