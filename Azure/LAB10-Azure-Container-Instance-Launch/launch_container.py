#!/usr/bin/env python3
"""
Azure Container Instance Launch Script

This script demonstrates how to deploy a container to Azure Container Instances (ACI)
using the Azure SDK for Python. Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import time
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import HttpResponseError

# Configuration parameters
RESOURCE_GROUP_NAME = "devops-lab-rg"
CONTAINER_GROUP_NAME = "devops-container"
LOCATION = "eastus"
IMAGE_NAME = "mcr.microsoft.com/azuredocs/aci-helloworld"
CPU_CORES = 1.0
MEMORY_GB = 1.5

def get_credentials():
    """
    Get Azure credentials and subscription ID.
    
    Returns:
        tuple: (credentials, subscription_id)
    """
    print("Authenticating with Azure...")
    
    # TODO: Get the subscription ID from environment variable
    # Hint: Use os.environ.get("AZURE_SUBSCRIPTION_ID")
    # If not set, print an error message and exit
    
    try:
        # TODO: Create and return DefaultAzureCredential
        # Return the tuple (credential, subscription_id)
        pass
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        sys.exit(1)

def create_resource_group(resource_client):
    """
    Create a resource group if it doesn't exist.
    
    Args:
        resource_client: Azure Resource Management client
    
    Returns:
        dict: Resource group properties
    """
    print(f"Creating resource group '{RESOURCE_GROUP_NAME}' if it doesn't exist...")
    
    try:
        # TODO: Create the resource group if it doesn't exist
        # Hint: Use resource_client.resource_groups.create_or_update with parameters:
        #   - RESOURCE_GROUP_NAME
        #   - {'location': LOCATION}
        # Return the resource group
        pass
    except HttpResponseError as e:
        print(f"Error creating resource group: {str(e)}")
        sys.exit(1)

def create_container_instance(aci_client):
    """
    Create an Azure Container Instance.
    
    Args:
        aci_client: Azure Container Instance Management client
        
    Returns:
        dict: Container group properties
    """
    print(f"Creating container instance '{CONTAINER_GROUP_NAME}'...")
    
    # Container group definition
    container_group_definition = {
        "location": LOCATION,
        "containers": [
            # TODO: Define the container configuration with:
            # - name: "main"
            # - image: IMAGE_NAME
            # - resources.requests.cpu: CPU_CORES
            # - resources.requests.memory_in_gb: MEMORY_GB
            # - ports: [{"port": 80}]
        ],
        # TODO: Configure the OS type (Linux) and IP address settings
        # - os_type: "Linux"
        # - ip_address.type: "Public"
        # - ip_address.ports: [{"protocol": "tcp", "port": 80}]
    }
    
    try:
        # TODO: Create or update the container group
        # Hint: Use aci_client.container_groups.begin_create_or_update with:
        #   - RESOURCE_GROUP_NAME
        #   - CONTAINER_GROUP_NAME
        #   - container_group_definition
        # Wait for the operation to complete with .result()
        # Return the container group
        pass
    except HttpResponseError as e:
        print(f"Error creating container instance: {str(e)}")
        return None

def get_container_details(aci_client):
    """
    Get details of the deployed container instance.
    
    Args:
        aci_client: Azure Container Instance Management client
        
    Returns:
        dict: Container instance details
    """
    print(f"Getting details for container instance '{CONTAINER_GROUP_NAME}'...")
    
    try:
        # TODO: Get the container group details
        # Hint: Use aci_client.container_groups.get with parameters:
        #   - RESOURCE_GROUP_NAME
        #   - CONTAINER_GROUP_NAME
        # Return the container group
        pass
    except HttpResponseError as e:
        print(f"Error getting container details: {str(e)}")
        return None

def delete_container_instance(aci_client):
    """
    Delete the container instance.
    
    Args:
        aci_client: Azure Container Instance Management client
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting container instance '{CONTAINER_GROUP_NAME}'...")
    
    try:
        # TODO: Delete the container group
        # Hint: Use aci_client.container_groups.begin_delete with parameters:
        #   - RESOURCE_GROUP_NAME
        #   - CONTAINER_GROUP_NAME
        # Wait for the operation to complete
        # Return True
        pass
    except HttpResponseError as e:
        print(f"Error deleting container instance: {str(e)}")
        return False

def delete_resource_group(resource_client):
    """
    Delete the resource group.
    
    Args:
        resource_client: Azure Resource Management client
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting resource group '{RESOURCE_GROUP_NAME}'...")
    
    try:
        # TODO: Delete the resource group
        # Hint: Use resource_client.resource_groups.begin_delete with parameter:
        #   - RESOURCE_GROUP_NAME
        # Wait for the operation to complete
        # Return True
        pass
    except HttpResponseError as e:
        print(f"Error deleting resource group: {str(e)}")
        return False

def main():
    """Main function to orchestrate the container instance operations."""
    print("Azure Container Instance Deployment Lab")
    print("--------------------------------------")
    
    # Get Azure credentials and clients
    credentials, subscription_id = get_credentials()
    
    # TODO: Create the ACI and Resource Management clients
    # Hint: Use ContainerInstanceManagementClient and ResourceManagementClient
    aci_client = None
    resource_client = None
    
    # Create resource group
    rg = create_resource_group(resource_client)
    if not rg:
        print("Failed to create resource group. Exiting.")
        sys.exit(1)
    
    # Create container instance
    container = create_container_instance(aci_client)
    if not container:
        print("Failed to create container instance. Exiting.")
        sys.exit(1)
    
    print(f"Container instance '{CONTAINER_GROUP_NAME}' created successfully!")
    
    # Get container details
    details = get_container_details(aci_client)
    if details and details.ip_address and details.ip_address.ip:
        print(f"Container IP address: {details.ip_address.ip}")
        print(f"You can access the container at: http://{details.ip_address.ip}")
        print(f"State: {details.provisioning_state}")
    
    # Cleanup instructions
    print("\nIMPORTANT: To avoid charges, delete these resources when done:")
    print(f"- Container Group: {CONTAINER_GROUP_NAME}")
    print(f"- Resource Group: {RESOURCE_GROUP_NAME}")
    print("\nYou can delete them by uncommenting the cleanup code below,")
    print("or by using the Azure Portal or Azure CLI (az container delete).")
    
    # Clean up - Delete container instance and resource group (commented out for safety)
    # Uncomment these lines to test deletion
    """
    # Delete container instance
    if delete_container_instance(aci_client):
        print(f"Container instance {CONTAINER_GROUP_NAME} deleted successfully.")
    
    # Delete resource group
    if delete_resource_group(resource_client):
        print(f"Resource group {RESOURCE_GROUP_NAME} deleted successfully.")
    """

if __name__ == "__main__":
    main() 