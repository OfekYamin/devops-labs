# Solutions: Azure IAM Role Assignment Automation

This document provides the reference solutions for the Azure IAM Role Assignment lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

Below is the full implementation of the `assign_role.py` script:

```python
#!/usr/bin/env python3
"""
Azure IAM Role Assignment Automation Script

This script demonstrates how to automate role assignments in Azure using 
the Azure SDK for Python. It includes functions for assigning roles,
listing role assignments, and revoking them.

Note: In production environments, always use secure methods to handle credentials.
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
    
    Returns:
        tuple: (auth_client, subscription_id)
    """
    # Get subscription ID from environment variables
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        sys.exit(1)
    
    # Create credential using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
    except Exception as e:
        print(f"Error creating credential: {e}")
        print("Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set.")
        sys.exit(1)
    
    # Create and return auth client
    auth_client = AuthorizationManagementClient(credential, subscription_id)
    return auth_client, subscription_id

def get_role_definition_id(auth_client, subscription_id, role_name):
    """
    Get the role definition ID for a given role name.
    
    Args:
        auth_client: The authorization management client
        subscription_id: The subscription ID
        role_name: The name of the role (e.g., "Reader", "Contributor")
        
    Returns:
        str: The role definition ID
    """
    # Common built-in role IDs - saves API calls for common roles
    common_roles = {
        "owner": "8e3af657-a8ff-443c-a75c-2fe8c4bcb635",
        "contributor": "b24988ac-6180-42a0-ab88-20f7382dd24c",
        "reader": "acdd72a7-3385-48ef-bd42-f606fba81ae7",
        "user access administrator": "18d7d88d-d35e-4fb5-a5c3-7773c20a72d9",
        "storage blob data contributor": "ba92f5b4-2d11-453d-a403-e96b0029c9fe",
        "storage blob data reader": "2a2b9908-6ea1-4ae2-8e65-a410df84e7d1"
    }
    
    # Check if it's a common role (case insensitive)
    role_name_lower = role_name.lower()
    if role_name_lower in common_roles:
        return f"/subscriptions/{subscription_id}/providers/Microsoft.Authorization/roleDefinitions/{common_roles[role_name_lower]}"
    
    # Otherwise, look up the role definition
    print(f"Looking up role definition for '{role_name}'...")
    
    # List role definitions and filter by name
    role_defs = auth_client.role_definitions.list(
        scope=f"/subscriptions/{subscription_id}",
        filter=f"roleName eq '{role_name}'"
    )
    
    # Find the matching role
    matching_roles = list(role_defs)
    if not matching_roles:
        print(f"Error: Role '{role_name}' not found.")
        sys.exit(1)
    
    # Return the first matching role
    return matching_roles[0].id

def assign_role(auth_client, subscription_id, resource_group, role_name, principal_id):
    """
    Assign a role to a principal at resource group scope.
    
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
    
    # Define the scope for the resource group
    scope = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}"
    
    # Get the role definition ID
    role_definition_id = get_role_definition_id(auth_client, subscription_id, role_name)
    
    # Create a new role assignment with a unique UUID
    assignment_id = str(uuid.uuid4())
    
    try:
        # Create the role assignment
        assignment = auth_client.role_assignments.create(
            scope=scope,
            role_assignment_name=assignment_id,
            parameters={
                'role_definition_id': role_definition_id,
                'principal_id': principal_id
            }
        )
        
        print(f"Role '{role_name}' assigned successfully.")
        print(f"Assignment ID: {assignment.id}")
        
        # Return assignment details
        return {
            'id': assignment.id,
            'principal_id': assignment.principal_id,
            'role_definition_id': assignment.role_definition_id,
            'scope': assignment.scope
        }
        
    except HttpResponseError as e:
        if "already exists" in str(e):
            print(f"Note: Principal already has this role assignment.")
            return {'id': f"{scope}/providers/Microsoft.Authorization/roleAssignments/{assignment_id}"}
        else:
            raise

def list_role_assignments(auth_client, subscription_id, resource_group=None, principal_id=None):
    """
    List role assignments, optionally filtered by resource group or principal.
    
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
        scope = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}"
    else:
        print("Listing role assignments at subscription level...")
        scope = f"/subscriptions/{subscription_id}"
    
    # List role assignments
    filter_string = None
    if principal_id:
        filter_string = f"principalId eq '{principal_id}'"
    
    assignments = []
    
    try:
        # Get role assignments at the specified scope
        if resource_group or not principal_id:
            for assignment in auth_client.role_assignments.list_for_scope(
                scope=scope,
                filter=filter_string
            ):
                assignments.append(assignment)
        
        # If principal_id is specified and no resource_group, get all for that principal
        if principal_id and not resource_group:
            for assignment in auth_client.role_assignments.list(
                filter=filter_string
            ):
                assignments.append(assignment)
        
        # Print and format the assignments
        if assignments:
            print(f"Found {len(assignments)} role assignment(s):")
            for i, assignment in enumerate(assignments, 1):
                # Try to get role definition name
                role_name = "Unknown Role"
                try:
                    role_def = auth_client.role_definitions.get_by_id(assignment.role_definition_id)
                    role_name = role_def.role_name
                except:
                    # If we can't get the role name, use the ID
                    role_id = assignment.role_definition_id.split('/')[-1]
                    role_name = f"Role {role_id}"
                
                print(f"{i}. Assignment ID: {assignment.name}")
                print(f"   Principal: {assignment.principal_id}")
                print(f"   Role: {role_name}")
                print(f"   Scope: {assignment.scope}")
                print()
        else:
            print("No role assignments found.")
        
        return assignments
    
    except HttpResponseError as e:
        print(f"Error listing role assignments: {e}")
        return []

def delete_role_assignment(auth_client, role_assignment_id):
    """
    Delete a role assignment.
    
    Args:
        auth_client: The authorization management client
        role_assignment_id: The ID of the role assignment to delete
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting role assignment '{role_assignment_id}'...")
    
    try:
        # Check if it's a full ID or just the name
        if '/' in role_assignment_id:
            # Extract the name from the full ID
            name = role_assignment_id.split('/')[-1]
            
            # Extract the scope from the ID
            scope = '/'.join(role_assignment_id.split('/')[:-3])
            
            # Delete the role assignment
            auth_client.role_assignments.delete(scope=scope, role_assignment_name=name)
        else:
            # Assume it's just the name part
            # For simplicity, we'll delete at subscription level
            subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
            scope = f"/subscriptions/{subscription_id}"
            
            # Delete the role assignment
            auth_client.role_assignments.delete(scope=scope, role_assignment_name=role_assignment_id)
        
        print(f"Role assignment deleted successfully.")
        return True
    
    except ResourceNotFoundError:
        print(f"Role assignment '{role_assignment_id}' not found.")
        return False
    except Exception as e:
        print(f"Error deleting role assignment: {e}")
        return False

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
        # Get auth client
        auth_client, subscription_id = get_auth_client()
        
        # Perform the requested operation
        if args.operation == "assign":
            assign_role(
                auth_client,
                subscription_id,
                args.resource_group,
                args.role,
                args.principal_id
            )
        
        elif args.operation == "list":
            list_role_assignments(
                auth_client,
                subscription_id,
                args.resource_group,
                args.principal_id
            )
        
        elif args.operation == "delete":
            success = delete_role_assignment(
                auth_client,
                args.assignment_id
            )
            if not success:
                sys.exit(1)
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Sample Usage

### 1. Assign a role to a principal
```bash
# Assign Reader role to a user or service principal
python assign_role.py assign --resource-group devops-lab-rg --role Reader --principal-id 00000000-0000-0000-0000-000000000000

# Assign Contributor role to a user or service principal
python assign_role.py assign --resource-group devops-lab-rg --role Contributor --principal-id 00000000-0000-0000-0000-000000000000
```

### 2. List role assignments
```bash
# List all role assignments in a subscription
python assign_role.py list

# List role assignments for a specific resource group
python assign_role.py list --resource-group devops-lab-rg

# List role assignments for a specific principal
python assign_role.py list --principal-id 00000000-0000-0000-0000-000000000000
```

### 3. Delete a role assignment
```bash
# Delete a role assignment by ID
python assign_role.py delete --assignment-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/devops-lab-rg/providers/Microsoft.Authorization/roleAssignments/00000000-0000-0000-0000-000000000000
```

## Key Learning Points

1. **Azure Role-Based Access Control (RBAC)**
   - RBAC is Azure's authorization system for managing access to resources
   - Roles define collections of permissions like Reader, Contributor, and Owner
   - Role assignments connect security principals to roles at a specific scope

2. **Authentication with Azure SDK**
   - DefaultAzureCredential provides a simplified authentication experience
   - Environment variables store credential information securely
   - Service principals are commonly used for automation scenarios

3. **Working with Role Definitions**
   - Built-in roles have fixed IDs across all Azure subscriptions
   - Custom roles are specific to a tenant or subscription
   - Role definitions contain permissions, actions, and other metadata

4. **Role Assignment Scopes**
   - Management group scope: applies to multiple subscriptions
   - Subscription scope: applies to all resources in a subscription
   - Resource group scope: applies to all resources in a group
   - Resource scope: applies to a specific resource

5. **Error Handling and Idempotency**
   - Duplicate role assignments are automatically handled
   - ResourceNotFoundError helps identify when assignments don't exist
   - Proper error messages improve debugging experience

## Common Issues and Troubleshooting

1. **Authentication Errors**
   - **Problem**: "DefaultAzureCredential failed to retrieve a token"
   - **Solution**: Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set correctly

2. **Permission Issues**
   - **Problem**: "The client does not have authorization to perform action"
   - **Solution**: Ensure the service principal has appropriate permissions (e.g., User Access Administrator role)

3. **Role Definition Lookup Failures**
   - **Problem**: "Role not found" error when assigning a role
   - **Solution**: Double-check role name spelling or use the pre-defined role IDs

4. **Principal ID Errors**
   - **Problem**: Invalid principal ID format
   - **Solution**: Ensure the principal ID is a valid GUID/UUID format

5. **Duplicate Role Assignments**
   - **Problem**: Attempting to create a duplicate role assignment
   - **Solution**: The script handles this gracefully, but consider checking if the assignment exists first

## Azure RBAC Best Practices

1. **Follow Least Privilege Principle**
   - Assign the minimum permissions needed
   - Use custom roles when built-in roles grant too many permissions

2. **Use Resource Groups for Access Control**
   - Group related resources and apply permissions at the resource group level
   - Reduces the number of role assignments needed

3. **Implement Regular Access Reviews**
   - Periodically review and clean up unnecessary assignments
   - Use automated scripts to generate role assignment reports

4. **Leverage Azure AD Groups**
   - Assign roles to groups instead of individual users
   - Simplifies management as users join or leave the organization

5. **Document Role Assignments**
   - Maintain documentation of who has access to what
   - Consider tagging resources with ownership information

## Cleanup Importance

Always remember to clean up role assignments that are no longer needed:

1. Orphaned role assignments can lead to security risks
2. Too many role assignments can make it difficult to audit and manage access
3. For testing and development, remove temporary role assignments promptly

The provided script includes the `delete` operation to help with this cleanup process. 