#!/usr/bin/env python3
"""
Azure Virtual Network Automation Script

This script demonstrates how to create, configure, and manage virtual networks and subnets
in Azure using the Azure SDK for Python.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import argparse
import time
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceExistsError, HttpResponseError, ResourceNotFoundError

# Configuration Parameters
RESOURCE_GROUP_NAME = "vnet-lab-rg"
LOCATION = "westeurope"
VNET_NAME = "lab-vnet"
SUBNET_NAME = "lab-subnet"
VNET_ADDRESS_PREFIX = "10.0.0.0/16"
SUBNET_ADDRESS_PREFIX = "10.0.1.0/24"

def get_credentials():
    """
    Get Azure credentials using DefaultAzureCredential.
    Returns:
        DefaultAzureCredential object
    """
    try:
        credentials = DefaultAzureCredential()
        return credentials
    except Exception as e:
        print(f"Error obtaining credentials: {str(e)}")
        sys.exit(1)

def create_resource_group(resource_client):
    """
    Create a resource group if it doesn't exist.
    
    Args:
        resource_client: Azure Resource Management client
    
    Returns:
        Resource group object
    """
    print(f"Creating Resource Group '{RESOURCE_GROUP_NAME}'...")
    
    # TODO: Create a resource group in the specified location
    # Hint: Use resource_client.resource_groups.create_or_update with parameters RESOURCE_GROUP_NAME and {'location': LOCATION}
    
    print(f"Resource group '{RESOURCE_GROUP_NAME}' created or exists already")
    return None  # Replace None with the created resource group

def create_virtual_network(network_client):
    """
    Create an Azure Virtual Network.
    
    Args:
        network_client: Azure Network Management client
    
    Returns:
        Virtual network operation poller
    """
    print(f"Creating Virtual Network '{VNET_NAME}'...")
    
    # TODO: Create a virtual network with the specified address space
    # Hint: Use network_client.virtual_networks.begin_create_or_update
    # Define the parameters to create a VNet with the address prefix VNET_ADDRESS_PREFIX
    
    print(f"Virtual Network '{VNET_NAME}' creation initiated.")
    return None  # Replace None with the vnet_poller

def create_subnet(network_client):
    """
    Create a subnet in the virtual network.
    
    Args:
        network_client: Azure Network Management client
    
    Returns:
        Subnet operation poller
    """
    print(f"Creating Subnet '{SUBNET_NAME}'...")
    
    # TODO: Create a subnet with the specified address prefix
    # Hint: Use network_client.subnets.begin_create_or_update
    # Define the parameters to create a subnet with the address prefix SUBNET_ADDRESS_PREFIX
    
    print(f"Subnet '{SUBNET_NAME}' creation initiated.")
    return None  # Replace None with the subnet_poller

def get_virtual_network_details(network_client):
    """
    Get details of the created virtual network.
    
    Args:
        network_client: Azure Network Management client
    
    Returns:
        Virtual network object
    """
    print(f"Retrieving details for Virtual Network '{VNET_NAME}'...")
    
    # TODO: Get the VNet details 
    # Hint: Use network_client.virtual_networks.get to retrieve the created network
    # Print the VNet's name, ID, and address space
    
    return None  # Replace None with the retrieved vnet

def list_subnets(network_client):
    """
    List all subnets in the virtual network.
    
    Args:
        network_client: Azure Network Management client
    """
    print(f"Listing subnets in Virtual Network '{VNET_NAME}'...")
    
    # TODO: List all subnets in the virtual network
    # Hint: Use network_client.subnets.list to get all subnets
    # Print each subnet's name and address prefix
    
    pass

def delete_vnet_and_resources(resource_client, network_client):
    """
    Delete the virtual network and resource group.
    
    Args:
        resource_client: Azure Resource Management client
        network_client: Azure Network Management client
    """
    print("Cleaning up resources...")
    
    # TODO: Implement the cleanup process
    # 1. Attempt to delete the virtual network first
    # 2. Then delete the resource group
    # Hint: Use network_client.virtual_networks.begin_delete and resource_client.resource_groups.begin_delete
    
    print("Cleanup completed. All resources have been deleted.")

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description='Azure Virtual Network Automation Tool')
    
    # Resource group and vnet arguments
    parser.add_argument('--resource-group', required=True, help='Resource group name')
    parser.add_argument('--vnet-name', required=True, help='Virtual network name')
    parser.add_argument('--location', default='eastus', help='Azure region (default: eastus)')
    
    # Operations
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')
    
    # Create VNet operation
    create_vnet_parser = subparsers.add_parser('create-vnet', help='Create a virtual network')
    create_vnet_parser.add_argument('--address-space', default=['10.1.0.0/16'], 
                                  nargs='+', help='Address space for the VNet (default: 10.1.0.0/16)')
    
    # Create Subnet operation
    create_subnet_parser = subparsers.add_parser('create-subnet', help='Create a subnet in a VNet')
    create_subnet_parser.add_argument('--subnet-name', required=True, help='Subnet name')
    create_subnet_parser.add_argument('--address-prefix', default='10.1.0.0/24', 
                                    help='Address prefix for the subnet (default: 10.1.0.0/24)')
    
    # Get VNet operation
    get_vnet_parser = subparsers.add_parser('get-vnet', help='Get details of a virtual network')
    
    # List Subnets operation
    list_subnets_parser = subparsers.add_parser('list-subnets', help='List subnets in a VNet')
    
    # Delete Subnet operation
    delete_subnet_parser = subparsers.add_parser('delete-subnet', help='Delete a subnet from a VNet')
    delete_subnet_parser.add_argument('--subnet-name', required=True, help='Subnet name')
    
    # Delete VNet operation
    delete_vnet_parser = subparsers.add_parser('delete-vnet', help='Delete a virtual network')
    
    args = parser.parse_args()
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    try:
        # Get Azure clients
        credentials = get_credentials()
        resource_client = ResourceManagementClient(credentials, os.environ.get("AZURE_SUBSCRIPTION_ID"))
        network_client = NetworkManagementClient(credentials, os.environ.get("AZURE_SUBSCRIPTION_ID"))
        
        # Process the requested operation
        if args.operation == "create-vnet":
            create_virtual_network(network_client)
            
        elif args.operation == "create-subnet":
            create_subnet(network_client)
            
        elif args.operation == "get-vnet":
            get_virtual_network_details(network_client)
            
        elif args.operation == "list-subnets":
            list_subnets(network_client)
            
        elif args.operation == "delete-subnet":
            # Implementation for deleting a subnet
            pass
            
        elif args.operation == "delete-vnet":
            delete_vnet_and_resources(resource_client, network_client)
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 