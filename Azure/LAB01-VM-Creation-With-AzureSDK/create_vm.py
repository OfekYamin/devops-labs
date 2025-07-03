#!/usr/bin/env python3
"""
Azure VM Creation Automation Script

This script automates the creation of a Virtual Machine in Azure using the Azure SDK for Python.
The script demonstrates how to authenticate to Azure, create a resource group, set up networking,
and provision a virtual machine.

Note: This is a lab exercise. In production, never hardcode credentials in your scripts.
"""

import os
import sys
import argparse
import time
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Azure VM Creation Script')
    parser.add_argument('--resource-group', default="devops-lab-rg", 
                        help='Name of the resource group (default: devops-lab-rg)')
    parser.add_argument('--location', default="eastus", 
                        help='Azure region to deploy resources (default: eastus)')
    parser.add_argument('--vm-name', default="devops-vm", 
                        help='Name of the virtual machine (default: devops-vm)')
    parser.add_argument('--vm-size', default="Standard_B1s", 
                        help='Size of the VM (default: Standard_B1s)')
    parser.add_argument('--admin-username', default="azureuser", 
                        help='Admin username for the VM (default: azureuser)')
    parser.add_argument('--admin-password', default="P@ssw0rd1234", 
                        help='Admin password for the VM (default: P@ssw0rd1234)')
    parser.add_argument('--cleanup', action='store_true', 
                        help='Clean up resources after creation')
    
    return parser.parse_args()

def authenticate_to_azure():
    """
    Authenticate to Azure using DefaultAzureCredential.
    
    TODO: Implement this function to return credentials and subscription_id
    1. Get subscription_id from environment variables
    2. Create and return DefaultAzureCredential() object
    
    Returns:
        tuple: (credential, subscription_id)
    """
    # Check for subscription ID
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        sys.exit(1)
    
    # TODO: Create Azure credential object
    
    # TODO: Return the credential and subscription_id

def create_resource_group(resource_client, resource_group_name, location):
    """
    Create a resource group in Azure.
    
    TODO: Implement this function to create or update a resource group
    
    Args:
        resource_client: Azure Resource Management client
        resource_group_name: Name of the resource group
        location: Azure region
        
    Returns:
        The created resource group
    """
    print(f"Creating resource group '{resource_group_name}' in {location}...")
    
    # TODO: Create or update resource group and return the result

def create_virtual_network(network_client, resource_group_name, location):
    """
    Create a virtual network with a subnet.
    
    TODO: Implement this function to create a VNet and subnet
    
    Args:
        network_client: Azure Network Management client
        resource_group_name: Name of the resource group
        location: Azure region
        
    Returns:
        tuple: (vnet_name, subnet_name)
    """
    vnet_name = "devops-vnet"
    subnet_name = "devops-subnet"
    
    print(f"Creating virtual network '{vnet_name}' with subnet '{subnet_name}'...")
    
    # TODO: Create VNet with address space
    
    # TODO: Create subnet with address prefix
    
    print(f"Virtual network '{vnet_name}' and subnet '{subnet_name}' created successfully.")
    return vnet_name, subnet_name

def create_public_ip_address(network_client, resource_group_name, location):
    """
    Create a public IP address.
    
    TODO: Implement this function to create a public IP
    
    Args:
        network_client: Azure Network Management client
        resource_group_name: Name of the resource group
        location: Azure region
        
    Returns:
        The created public IP address
    """
    public_ip_name = "devops-ip"
    
    print(f"Creating public IP address '{public_ip_name}'...")
    
    # TODO: Create and return public IP address

def create_network_interface(network_client, resource_group_name, location, 
                             subnet_id, public_ip_id):
    """
    Create a network interface.
    
    TODO: Implement this function to create a network interface
    
    Args:
        network_client: Azure Network Management client
        resource_group_name: Name of the resource group
        location: Azure region
        subnet_id: ID of the subnet
        public_ip_id: ID of the public IP
        
    Returns:
        The created network interface
    """
    nic_name = "devops-nic"
    
    print(f"Creating network interface '{nic_name}'...")
    
    # TODO: Create and return network interface

def create_virtual_machine(compute_client, resource_group_name, location, vm_name, 
                          vm_size, nic_id, admin_username, admin_password):
    """
    Create a virtual machine.
    
    TODO: Implement this function to create a VM
    
    Args:
        compute_client: Azure Compute Management client
        resource_group_name: Name of the resource group
        location: Azure region
        vm_name: Name of the VM
        vm_size: Size of the VM
        nic_id: ID of the network interface
        admin_username: Admin username
        admin_password: Admin password
        
    Returns:
        The created VM operation
    """
    print(f"Creating virtual machine '{vm_name}'...")
    
    # TODO: Define VM parameters (os_profile, hardware_profile, storage_profile, network_profile)
    
    # TODO: Create and return the VM

def delete_resource_group(resource_client, resource_group_name):
    """
    Delete a resource group and all resources within it.
    
    Args:
        resource_client: Azure Resource Management client
        resource_group_name: Name of the resource group
    """
    print(f"Cleaning up: Deleting resource group '{resource_group_name}'...")
    
    # TODO: Delete the resource group

def main():
    """Main function to create a VM in Azure."""
    # Parse arguments
    args = parse_arguments()
    
    # Set up parameters
    resource_group_name = args.resource_group
    location = args.location
    vm_name = args.vm_name
    vm_size = args.vm_size
    admin_username = args.admin_username
    admin_password = args.admin_password
    
    try:
        # Authenticate to Azure
        print("Authenticating to Azure...")
        # TODO: Call authenticate_to_azure() and store results
        
        # TODO: Initialize clients (resource_client, network_client, compute_client)
        
        # Create resource group
        # TODO: Call create_resource_group()
        
        # Create networking components
        # TODO: Call create_virtual_network()
        # TODO: Call create_public_ip_address()
        # TODO: Call create_network_interface()
        
        # Create VM
        # TODO: Call create_virtual_machine()
        
        print(f"\nVM '{vm_name}' created successfully in resource group '{resource_group_name}'.")
        print("You can connect to the VM using the Azure portal or SSH client.")
        
        # Clean up if specified
        if args.cleanup:
            # TODO: Call delete_resource_group()
            print("Resources cleaned up successfully.")
        else:
            print("\nDon't forget to clean up resources when you're done to avoid unnecessary charges:")
            print(f"az group delete --name {resource_group_name} --yes --no-wait")
            
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error creating VM: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 