# Solutions: Azure Virtual Network Setup with Python

## Complete Implementation of `create_vnet.py`

```python
#!/usr/bin/env python3
"""
Azure Virtual Network Setup Lab
This script demonstrates how to create and manage Azure Virtual Networks using the Azure SDK for Python
"""

import os
import time
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError

# Configuration parameters
RESOURCE_GROUP_NAME = "lab-vnet-rg"
LOCATION = "eastus"
VNET_NAME = "lab-vnet"
SUBNET_NAME = "default-subnet"
VNET_ADDRESS_PREFIX = "10.0.0.0/16"
SUBNET_ADDRESS_PREFIX = "10.0.1.0/24"

def get_credentials():
    """
    Get the Azure credentials and subscription ID.
    
    Returns:
        tuple: (credentials, subscription_id)
    """
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        raise ValueError("AZURE_SUBSCRIPTION_ID environment variable not set")
    
    credentials = DefaultAzureCredential()
    return credentials, subscription_id

def create_resource_group(resource_client):
    """
    Create a resource group for the virtual network resources.
    
    Args:
        resource_client: Azure Resource Management client
        
    Returns:
        dict: Resource group properties
    """
    try:
        print(f"Creating resource group '{RESOURCE_GROUP_NAME}' in location '{LOCATION}'...")
        
        # Create resource group parameters
        rg_params = {
            'location': LOCATION
        }
        
        # Create or update resource group
        resource_group = resource_client.resource_groups.create_or_update(
            RESOURCE_GROUP_NAME, 
            rg_params
        )
        
        print(f"Resource group created successfully: {resource_group.name} in {resource_group.location}")
        return {
            'id': resource_group.id,
            'name': resource_group.name,
            'location': resource_group.location
        }
    except HttpResponseError as ex:
        print(f"Error creating resource group: {ex.message}")
        raise

def create_virtual_network(network_client):
    """
    Create a virtual network with address prefix.
    
    Args:
        network_client: Azure Network Management client
        
    Returns:
        dict: Virtual network properties
    """
    try:
        print(f"Creating virtual network '{VNET_NAME}' with address prefix '{VNET_ADDRESS_PREFIX}'...")
        
        # Create VNet parameters
        vnet_params = {
            'location': LOCATION,
            'address_space': {
                'address_prefixes': [VNET_ADDRESS_PREFIX]
            }
        }
        
        # Create or update the virtual network
        poller = network_client.virtual_networks.begin_create_or_update(
            RESOURCE_GROUP_NAME,
            VNET_NAME,
            vnet_params
        )
        
        # Wait for the operation to complete
        vnet_result = poller.result()
        
        print(f"Virtual network created successfully: {vnet_result.name}")
        return {
            'id': vnet_result.id,
            'name': vnet_result.name,
            'location': vnet_result.location,
            'address_space': vnet_result.address_space.address_prefixes
        }
    except HttpResponseError as ex:
        print(f"Error creating virtual network: {ex.message}")
        raise

def create_subnet(network_client):
    """
    Create a subnet within the virtual network.
    
    Args:
        network_client: Azure Network Management client
        
    Returns:
        dict: Subnet properties
    """
    try:
        print(f"Creating subnet '{SUBNET_NAME}' with address prefix '{SUBNET_ADDRESS_PREFIX}'...")
        
        # Create subnet parameters
        subnet_params = {
            'address_prefix': SUBNET_ADDRESS_PREFIX
        }
        
        # Create or update the subnet
        poller = network_client.subnets.begin_create_or_update(
            RESOURCE_GROUP_NAME,
            VNET_NAME,
            SUBNET_NAME,
            subnet_params
        )
        
        # Wait for the operation to complete
        subnet_result = poller.result()
        
        print(f"Subnet created successfully: {subnet_result.name}")
        return {
            'id': subnet_result.id,
            'name': subnet_result.name,
            'address_prefix': subnet_result.address_prefix
        }
    except HttpResponseError as ex:
        print(f"Error creating subnet: {ex.message}")
        raise

def get_virtual_network_details(network_client):
    """
    Get details of a virtual network.
    
    Args:
        network_client: Azure Network Management client
        
    Returns:
        dict: Virtual network details
    """
    try:
        print(f"Getting details for virtual network '{VNET_NAME}'...")
        
        vnet = network_client.virtual_networks.get(
            RESOURCE_GROUP_NAME,
            VNET_NAME
        )
        
        print(f"Virtual network details retrieved:")
        print(f"  Name: {vnet.name}")
        print(f"  ID: {vnet.id}")
        print(f"  Location: {vnet.location}")
        print(f"  Address Space: {vnet.address_space.address_prefixes}")
        
        return {
            'id': vnet.id,
            'name': vnet.name,
            'location': vnet.location,
            'address_space': vnet.address_space.address_prefixes,
            'subnets': [{'name': subnet.name, 'address_prefix': subnet.address_prefix} for subnet in vnet.subnets]
        }
    except ResourceNotFoundError:
        print(f"Virtual network '{VNET_NAME}' not found")
        return None
    except HttpResponseError as ex:
        print(f"Error retrieving virtual network: {ex.message}")
        raise

def list_subnets(network_client):
    """
    List all subnets in the specified virtual network.
    
    Args:
        network_client: Azure Network Management client
        
    Returns:
        list: List of subnets with their properties
    """
    try:
        print(f"Listing subnets in virtual network '{VNET_NAME}'...")
        
        subnets = network_client.subnets.list(
            RESOURCE_GROUP_NAME,
            VNET_NAME
        )
        
        subnet_list = []
        print("Subnets:")
        for subnet in subnets:
            print(f"  Name: {subnet.name}, Address Prefix: {subnet.address_prefix}")
            subnet_list.append({
                'id': subnet.id,
                'name': subnet.name,
                'address_prefix': subnet.address_prefix
            })
        
        return subnet_list
    except ResourceNotFoundError:
        print(f"Virtual network '{VNET_NAME}' not found")
        return []
    except HttpResponseError as ex:
        print(f"Error listing subnets: {ex.message}")
        raise

def delete_vnet_and_resources(network_client, resource_client):
    """
    Delete the virtual network and resource group.
    
    Args:
        network_client: Azure Network Management client
        resource_client: Azure Resource Management client
        
    Returns:
        bool: True if deletion was successful
    """
    try:
        print(f"Starting cleanup of resources...")
        
        # Delete virtual network
        print(f"Deleting virtual network '{VNET_NAME}'...")
        poller = network_client.virtual_networks.begin_delete(
            RESOURCE_GROUP_NAME,
            VNET_NAME
        )
        poller.wait()
        print(f"Virtual network '{VNET_NAME}' deleted successfully")
        
        # Delete resource group
        print(f"Deleting resource group '{RESOURCE_GROUP_NAME}'...")
        poller = resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME)
        poller.wait()
        print(f"Resource group '{RESOURCE_GROUP_NAME}' deleted successfully")
        
        return True
    except ResourceNotFoundError:
        print(f"One or more resources not found (they might have been deleted already)")
        return True
    except HttpResponseError as ex:
        print(f"Error deleting resources: {ex.message}")
        return False

def main():
    """Main function to orchestrate the virtual network operations."""
    try:
        # Get Azure credentials
        credentials, subscription_id = get_credentials()
        
        # Create management clients
        network_client = NetworkManagementClient(credentials, subscription_id)
        resource_client = ResourceManagementClient(credentials, subscription_id)
        
        # Menu system
        operation = input(
            "\nSelect an operation to perform:\n"
            "1. Create resource group, virtual network, and subnet\n"
            "2. Get virtual network details\n"
            "3. List subnets\n"
            "4. Delete all resources\n"
            "5. Exit\n"
            "Enter choice (1-5): "
        )
        
        if operation == "1":
            # Create resources
            create_resource_group(resource_client)
            create_virtual_network(network_client)
            create_subnet(network_client)
        elif operation == "2":
            # Get VNet details
            get_virtual_network_details(network_client)
        elif operation == "3":
            # List subnets
            list_subnets(network_client)
        elif operation == "4":
            # Delete resources
            delete_vnet_and_resources(network_client, resource_client)
        elif operation == "5":
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please select a number from 1 to 5.")
        
        # Allow the user to see the results before returning to the menu
        input("\nPress Enter to continue...")
        
        # Recursive call to show the menu again
        main()
    
    except ValueError as ex:
        print(f"Error: {str(ex)}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")

if __name__ == "__main__":
    main()
```

## Key Learning Points

### Azure Virtual Network Concepts

1. **Virtual Networks (VNets)**
   - Virtual networks are the fundamental building block for private networks in Azure
   - They enable many types of Azure resources to securely communicate with each other, the internet, and on-premises networks
   - A VNet is similar to a traditional network that you'd operate in your own data center, but brings additional benefits of Azure's infrastructure

2. **Subnets**
   - Segments of a virtual network that allow you to organize and secure groups of resources
   - Enable you to divide your VNet address space into segments that are appropriate for the organization's internal network
   - Help control network traffic flow using network security groups (NSGs)

3. **CIDR Notation**
   - CIDR (Classless Inter-Domain Routing) is used to define IP address ranges
   - Format: IP address/prefix length (e.g., 10.0.0.0/16)
   - The prefix length defines how many bits are fixed in the address:
     - /16 provides 65,536 addresses (2^16 = 65,536)
     - /24 provides 256 addresses (2^8 = 256)

### Azure Python SDK

1. **Azure SDK for Python Components**
   - `azure-identity`: Authentication libraries for Azure
   - `azure-mgmt-network`: Management libraries for Azure Networking
   - `azure-mgmt-resource`: Management libraries for Azure Resources
   - `azure-core`: Core functionality shared by Azure libraries

2. **Authentication**
   - `DefaultAzureCredential` provides a default authentication flow for applications deployed to Azure
   - It attempts multiple authentication methods in sequence, including:
     - Environment variables
     - Managed Identity
     - Visual Studio Code credentials
     - Azure CLI credentials
     - Interactive browser authentication

3. **LRO Pattern (Long-Running Operations)**
   - Azure operations that take time to complete use the LRO pattern
   - Methods like `begin_create_or_update` return a poller object
   - You can use `poller.result()` to wait for the operation to complete and get the result

## Common Issues and Troubleshooting

### Authentication Issues
- **Problem**: `DefaultAzureCredential authentication failed`
- **Solution**: Run `az login` to authenticate with Azure CLI or set the required environment variables

### Permission Issues
- **Problem**: `The client does not have authorization to perform action`
- **Solution**: Ensure your account has the proper RBAC roles assigned (e.g., Network Contributor)

### Resource Not Found
- **Problem**: `ResourceNotFoundError` when trying to access a resource
- **Solution**: Verify the resource name and resource group name are correct, and that the resource exists in your subscription

### Address Space Conflicts
- **Problem**: `The address prefix 10.0.0.0/16 overlaps with the existing VNet`
- **Solution**: Choose a different address prefix that doesn't overlap with existing VNets

### Subnet Deletion Failures
- **Problem**: `Cannot delete subnet because it has resources using it`
- **Solution**: Identify and delete or disassociate any resources (e.g., NICs, Application Gateways) attached to the subnet

## Best Practices

### Resource Naming
- Use a consistent naming convention for resources
- Include purpose, environment, and region in resource names
- Example: `prod-eastus-vnet-web`

### IP Address Planning
- Plan your address space carefully to allow for future growth
- Use non-overlapping address ranges to enable VNet peering
- Reserve address space for specialized subnets (e.g., gateway subnet)

### Network Security
- Use Network Security Groups (NSGs) to control traffic flow
- Follow the principle of least privilege when configuring NSGs
- Consider using Application Security Groups (ASGs) for application-centric security

### Resource Cleanup
- Always clean up resources when they're no longer needed
- Delete resources in the correct order to avoid dependency issues
- Consider using Azure Resource Manager templates for reproducible deployments

## Advanced Concepts

### VNet Peering
- Connects two VNets, allowing resources to communicate across VNets
- Can be configured within the same region or across regions
- Requires non-overlapping IP address spaces

### Service Endpoints
- Extend your VNet private address space to Azure services
- Improve security by allowing Azure services to be accessed only from your VNet
- Available for services like Azure Storage, SQL Database, and Cosmos DB

### Network Security Groups (NSGs)
- Filter network traffic to and from Azure resources in a VNet
- Control east-west and north-south traffic
- Can be associated with subnets or network interfaces

### Private Link and Private Endpoints
- Access Azure PaaS services over a private endpoint in your VNet
- Eliminates exposure of service traffic to the public internet
- Enhances security and reduces risk of data exfiltration

## Cleanup Instructions

Always remember to clean up your Azure resources when you're done experimenting:

1. **Delete the Virtual Network**: This will automatically delete all subnets
2. **Delete the Resource Group**: This will delete all resources in the group

The `delete_vnet_and_resources()` function implements this cleanup process:
- First deletes the virtual network using `begin_delete()`
- Then deletes the resource group using `begin_delete()`
- Uses the LRO pattern with `poller.wait()` to ensure operations complete before proceeding

Remember: Keeping unused Azure resources running can result in unexpected charges to your Azure account. 