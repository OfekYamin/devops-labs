# Solutions: Azure VM Creation with Azure SDK

This document provides the reference solutions for the Azure VM Creation lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

Below is the full implementation of the `create_vm.py` script with all the TODOs completed:

```python
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
    
    Returns:
        tuple: (credential, subscription_id)
    """
    # Check for subscription ID
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        sys.exit(1)
    
    # Create Azure credential object
    credential = DefaultAzureCredential()
    
    return credential, subscription_id

def create_resource_group(resource_client, resource_group_name, location):
    """
    Create a resource group in Azure.
    
    Args:
        resource_client: Azure Resource Management client
        resource_group_name: Name of the resource group
        location: Azure region
        
    Returns:
        The created resource group
    """
    print(f"Creating resource group '{resource_group_name}' in {location}...")
    
    # Check if resource group exists
    if resource_client.resource_groups.check_existence(resource_group_name):
        print(f"Resource group '{resource_group_name}' already exists.")
        return resource_client.resource_groups.get(resource_group_name)
    
    # Create resource group
    return resource_client.resource_groups.create_or_update(
        resource_group_name,
        {"location": location}
    )

def create_virtual_network(network_client, resource_group_name, location):
    """
    Create a virtual network with a subnet.
    
    Args:
        network_client: Azure Network Management client
        resource_group_name: Name of the resource group
        location: Azure region
        
    Returns:
        tuple: (vnet_name, subnet_name, subnet_id)
    """
    vnet_name = "devops-vnet"
    subnet_name = "devops-subnet"
    
    print(f"Creating virtual network '{vnet_name}' with subnet '{subnet_name}'...")
    
    # Create VNet with address space
    vnet_params = {
        'location': location,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        },
        'subnets': [
            {
                'name': subnet_name,
                'address_prefix': '10.0.0.0/24'
            }
        ]
    }
    
    # Create or update the virtual network
    vnet = network_client.virtual_networks.begin_create_or_update(
        resource_group_name,
        vnet_name,
        vnet_params
    ).result()
    
    # Get the subnet ID
    subnet = network_client.subnets.get(
        resource_group_name, 
        vnet_name, 
        subnet_name
    )
    
    print(f"Virtual network '{vnet_name}' and subnet '{subnet_name}' created successfully.")
    return vnet_name, subnet_name, subnet.id

def create_public_ip_address(network_client, resource_group_name, location):
    """
    Create a public IP address.
    
    Args:
        network_client: Azure Network Management client
        resource_group_name: Name of the resource group
        location: Azure region
        
    Returns:
        The created public IP address
    """
    public_ip_name = "devops-ip"
    
    print(f"Creating public IP address '{public_ip_name}'...")
    
    # Create public IP parameters
    public_ip_params = {
        'location': location,
        'sku': {
            'name': 'Standard'
        },
        'public_ip_allocation_method': 'Static',
        'public_ip_address_version': 'IPV4'
    }
    
    # Create or update the public IP
    public_ip = network_client.public_ip_addresses.begin_create_or_update(
        resource_group_name,
        public_ip_name,
        public_ip_params
    ).result()
    
    print(f"Public IP '{public_ip_name}' created successfully.")
    return public_ip

def create_network_interface(network_client, resource_group_name, location, 
                             subnet_id, public_ip_id):
    """
    Create a network interface.
    
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
    
    # Create NIC parameters
    nic_params = {
        'location': location,
        'ip_configurations': [
            {
                'name': 'ipconfig1',
                'subnet': {
                    'id': subnet_id
                },
                'public_ip_address': {
                    'id': public_ip_id
                }
            }
        ]
    }
    
    # Create or update the NIC
    nic = network_client.network_interfaces.begin_create_or_update(
        resource_group_name,
        nic_name,
        nic_params
    ).result()
    
    print(f"Network interface '{nic_name}' created successfully.")
    return nic

def create_virtual_machine(compute_client, resource_group_name, location, vm_name, 
                          vm_size, nic_id, admin_username, admin_password):
    """
    Create a virtual machine.
    
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
    
    # Define VM parameters
    vm_parameters = {
        'location': location,
        'os_profile': {
            'computer_name': vm_name,
            'admin_username': admin_username,
            'admin_password': admin_password
        },
        'hardware_profile': {
            'vm_size': vm_size
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'Canonical',
                'offer': 'UbuntuServer',
                'sku': '18.04-LTS',
                'version': 'latest'
            },
            'os_disk': {
                'name': f"{vm_name}-osdisk",
                'caching': 'ReadWrite',
                'create_option': 'FromImage',
                'managed_disk': {
                    'storage_account_type': 'Standard_LRS'
                }
            }
        },
        'network_profile': {
            'network_interfaces': [
                {
                    'id': nic_id,
                    'primary': True
                }
            ]
        }
    }
    
    # Create or update the VM
    vm_operation = compute_client.virtual_machines.begin_create_or_update(
        resource_group_name,
        vm_name,
        vm_parameters
    )
    
    # Wait for the operation to complete
    print("Waiting for VM creation to complete...")
    vm_result = vm_operation.result()
    
    print(f"Virtual machine '{vm_name}' created successfully.")
    return vm_result

def delete_resource_group(resource_client, resource_group_name):
    """
    Delete a resource group and all resources within it.
    
    Args:
        resource_client: Azure Resource Management client
        resource_group_name: Name of the resource group
    """
    print(f"Cleaning up: Deleting resource group '{resource_group_name}'...")
    
    # Delete the resource group
    delete_operation = resource_client.resource_groups.begin_delete(resource_group_name)
    
    print("Waiting for resource group deletion to complete...")
    delete_operation.wait()
    
    print(f"Resource group '{resource_group_name}' deleted successfully.")

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
        credential, subscription_id = authenticate_to_azure()
        
        # Initialize clients
        resource_client = ResourceManagementClient(credential, subscription_id)
        network_client = NetworkManagementClient(credential, subscription_id)
        compute_client = ComputeManagementClient(credential, subscription_id)
        
        # Create resource group
        resource_group = create_resource_group(resource_client, resource_group_name, location)
        
        # Create networking components
        vnet_name, subnet_name, subnet_id = create_virtual_network(network_client, resource_group_name, location)
        public_ip = create_public_ip_address(network_client, resource_group_name, location)
        nic = create_network_interface(
            network_client, 
            resource_group_name, 
            location, 
            subnet_id, 
            public_ip.id
        )
        
        # Create VM
        vm = create_virtual_machine(
            compute_client,
            resource_group_name,
            location,
            vm_name,
            vm_size,
            nic.id,
            admin_username,
            admin_password
        )
        
        print(f"\nVM '{vm_name}' created successfully in resource group '{resource_group_name}'.")
        print("You can connect to the VM using the Azure portal or SSH client.")
        
        # Clean up if specified
        if args.cleanup:
            delete_resource_group(resource_client, resource_group_name)
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
```

## Key Learning Points

1. **Azure Authentication**
   - Using environment variables for secure authentication
   - Working with DefaultAzureCredential to simplify the authentication process
   - Properly handling credentials and avoiding hardcoded secrets

2. **Resource Management**
   - Creating and managing Azure resource groups
   - Understanding how resources are organized in Azure
   - Efficient cleanup to avoid unnecessary charges

3. **Networking Configuration**
   - Creating virtual networks and subnets
   - Configuring public IP addresses
   - Setting up network interfaces for VMs

4. **Virtual Machine Deployment**
   - Specifying VM parameters (size, image, credentials)
   - Configuring disks and OS properties
   - Connecting VMs to networking components

5. **Azure SDK Patterns**
   - Using begin_* methods for long-running operations
   - Waiting for operation completion with .result()
   - Error handling with Azure-specific exceptions

## Common Issues and Solutions

### Authentication Failures
- **Issue**: "AZURE_SUBSCRIPTION_ID environment variable not set"
  - **Solution**: Set the environment variable with `export AZURE_SUBSCRIPTION_ID=your-subscription-id`
- **Issue**: Azure credential authentication fails
  - **Solution**: Ensure you're logged in with `az login` or have set all required environment variables (AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET)

### Resource Creation Errors
- **Issue**: "Resource group with the same name already exists"
  - **Solution**: Use a different resource group name or check if the group exists before creation
- **Issue**: VM size not available in the selected region
  - **Solution**: Choose a different VM size or region; use `az vm list-sizes --location <location>` to see available sizes

### Network Configuration Problems
- **Issue**: IP allocation failures
  - **Solution**: Ensure the subnet address space is correctly configured and not overlapping
- **Issue**: "The resource <X> is not found"
  - **Solution**: Check if resources exist and their IDs are correctly specified

### VM Creation Timeouts
- **Issue**: VM creation times out
  - **Solution**: Increase timeout or check resource quotas in your subscription
- **Issue**: "Disk creation conflict"
  - **Solution**: Use unique disk names or check for existing disks with the same name

## Best Practices

1. Always clean up resources when they're no longer needed
2. Use parameter defaults wisely to simplify command-line usage
3. Implement proper error handling for API calls
4. Use manageable resource naming conventions
5. Validate parameters before making API calls
6. Structure your code in modular functions for better maintainability

Remember that Azure services evolve over time, so it's important to keep your SDK versions updated and be aware of any API changes that might affect your automation scripts. 