# LAB10: Azure Container Instance Launch - Solutions

This document provides the complete solution for the Azure Container Instance Launch lab, including implementations for all the TODO sections and important learning points.

## Complete Implementation of `launch_container.py`

```python
#!/usr/bin/env python3
"""
Azure Container Instance Launch Script

This script demonstrates how to deploy a container to Azure Container Instances (ACI)
using the Azure SDK for Python.
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
    
    # Get the subscription ID from environment variable
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        print("Please set this variable with your Azure subscription ID.")
        sys.exit(1)
    
    try:
        # Create and return DefaultAzureCredential
        credential = DefaultAzureCredential()
        return credential, subscription_id
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
        # Create the resource group if it doesn't exist
        rg_params = {'location': LOCATION}
        resource_group = resource_client.resource_groups.create_or_update(
            RESOURCE_GROUP_NAME,
            rg_params
        )
        print(f"Resource group '{RESOURCE_GROUP_NAME}' created or exists already")
        return resource_group
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
            {
                "name": "main",
                "image": IMAGE_NAME,
                "resources": {
                    "requests": {
                        "cpu": CPU_CORES,
                        "memory_in_gb": MEMORY_GB
                    }
                },
                "ports": [{"port": 80}]
            }
        ],
        "os_type": "Linux",
        "ip_address": {
            "type": "Public",
            "ports": [{"protocol": "tcp", "port": 80}]
        }
    }
    
    try:
        # Create or update the container group
        container_group = aci_client.container_groups.begin_create_or_update(
            RESOURCE_GROUP_NAME,
            CONTAINER_GROUP_NAME,
            container_group_definition
        ).result()
        
        print(f"Container instance '{CONTAINER_GROUP_NAME}' created successfully")
        return container_group
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
        # Get the container group details
        container_group = aci_client.container_groups.get(
            RESOURCE_GROUP_NAME,
            CONTAINER_GROUP_NAME
        )
        print(f"Container details retrieved successfully")
        return container_group
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
        # Delete the container group
        aci_client.container_groups.begin_delete(
            RESOURCE_GROUP_NAME,
            CONTAINER_GROUP_NAME
        ).wait()
        
        print(f"Container instance '{CONTAINER_GROUP_NAME}' deleted successfully")
        return True
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
        # Delete the resource group
        poller = resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME)
        poller.wait()
        
        print(f"Resource group '{RESOURCE_GROUP_NAME}' deleted successfully")
        return True
    except HttpResponseError as e:
        print(f"Error deleting resource group: {str(e)}")
        return False

def main():
    """Main function to orchestrate the container instance operations."""
    print("Azure Container Instance Deployment Lab")
    print("--------------------------------------")
    
    # Get Azure credentials and clients
    credentials, subscription_id = get_credentials()
    
    # Create the ACI and Resource Management clients
    aci_client = ContainerInstanceManagementClient(credentials, subscription_id)
    resource_client = ResourceManagementClient(credentials, subscription_id)
    
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
```

## Key Learning Points

### Azure Container Instances (ACI) Concepts

1. **What are Azure Container Instances?**
   - A serverless container platform that allows you to run containers without managing servers
   - Ideal for simple applications, task automation, and build jobs
   - Fast startup with per-second billing
   - Support for both Linux and Windows containers

2. **Core Components**
   - **Container Groups**: A collection of containers that share lifecycle, resources, network, and storage volumes
   - **Containers**: Individual Docker containers with specific configuration
   - **Images**: Container images from Docker Hub, Azure Container Registry, or other registries
   - **Resources**: CPU and memory allocations for containers
   - **Networking**: Public IP addresses and port mappings

3. **Container Group Properties**
   - **OS Type**: Linux or Windows
   - **IP Address Type**: Public or Private
   - **Restart Policy**: Always, OnFailure, or Never
   - **Network Profile**: For integration with Azure Virtual Networks
   - **Volumes**: For persistent storage

### Azure Python SDK for Container Instances

1. **Authentication Methods**
   - `DefaultAzureCredential`: Simplifies authentication across different environments
   - Environment variables: `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID`
   - System-assigned managed identity when running in Azure

2. **Key Classes**
   - `ContainerInstanceManagementClient`: Main client for ACI operations
   - `ResourceManagementClient`: Client for resource group operations
   - Azure Identity libraries for authentication

3. **Container Operations**
   - **Create**: `container_groups.begin_create_or_update()` for deploying containers
   - **Read**: `container_groups.get()` for retrieving container details
   - **Delete**: `container_groups.begin_delete()` for removing containers
   - **List**: `container_groups.list()` for listing all container groups

4. **Long-Running Operations**
   - Methods with `begin_` prefix return a poller object
   - Use `.result()` to wait for completion and get the result
   - Use `.wait()` when you don't need the result

### Best Practices

1. **Resource Allocation**
   - Allocate appropriate CPU and memory based on container needs
   - Start with minimal resources and scale as needed
   - Remember that ACI billing is based on allocated resources, not actual usage

2. **Container Configuration**
   - Use specific image tags instead of `latest` for reproducibility
   - Set environment variables for configuration
   - Use startup commands when necessary
   - Consider setting a restart policy based on your application's needs

3. **Networking**
   - Expose only necessary ports
   - Use DNS name label for friendly URLs
   - Consider private networking for sensitive applications

4. **Monitoring and Logging**
   - Configure container logs to stream to Azure Log Analytics
   - Set up Azure Monitor alerts for container health
   - Use container diagnostics for troubleshooting

5. **Security**
   - Use private container registries for sensitive images
   - Consider using managed identities for authentication
   - Follow the principle of least privilege for all credentials

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "Failed to authenticate with Azure" error
   - **Solution**: Verify environment variables are set correctly and credentials have proper permissions

2. **Image Pull Failures**
   - **Problem**: "Failed to pull image" error
   - **Solution**: Check image name, tag, and registry accessibility; verify credentials for private registries

3. **Resource Constraints**
   - **Problem**: "Quota exceeded" or "Insufficient resources" errors
   - **Solution**: Check subscription limits, reduce resource requests, or try a different region

4. **Network Configuration Issues**
   - **Problem**: Container is running but not accessible
   - **Solution**: Verify port configuration, check network security groups, and ensure IP address is configured

5. **Container Crashes**
   - **Problem**: Container starts but stops immediately
   - **Solution**: Check container logs, verify command and environment variables, and ensure the container image is compatible with ACI

## Advanced Concepts

1. **Container Groups**
   - Deploy multiple containers that work together
   - Share network namespace and can communicate via localhost
   - Support for sidecar patterns and multi-container applications

2. **Custom Init Containers**
   - Run initialization containers before your main application
   - Useful for setup, migrations, or downloading dependencies

3. **Volume Mounting**
   - Azure Files shares for persistent storage
   - Empty directories for temporary storage
   - GitRepo volumes for code deployment

4. **Virtual Network Integration**
   - Deploy containers in your VNet
   - Secure access to private resources
   - Network security group rules for container groups

5. **GPU-Enabled Containers**
   - Support for GPU-accelerated workloads
   - Useful for machine learning inference, rendering, and compute-intensive tasks

## Cleanup Instructions

Always remember to clean up your Azure resources when you're done experimenting:

1. **Delete the Container Group**: This releases all compute resources
   ```python
   aci_client.container_groups.begin_delete(RESOURCE_GROUP_NAME, CONTAINER_GROUP_NAME).wait()
   ```

2. **Delete the Resource Group**: This removes all associated resources
   ```python
   resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME).wait()
   ```

You can also use the Azure CLI for cleanup:
```bash
az container delete --name devops-container --resource-group devops-lab-rg --yes
az group delete --name devops-lab-rg --yes
```

Remember: ACI resources incur charges while running, even if the container is idle. 