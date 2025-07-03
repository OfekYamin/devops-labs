#!/usr/bin/env python3
"""
GCP LAB08 - VPC Network Creation Automation
This script demonstrates how to create, list, and delete VPC networks and subnets
using the Google Cloud Compute Engine API with Python.
"""

import os
import argparse
import time
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

def build_compute_client(credentials):
    """
    Build and return a Compute Engine API client.
    
    Args:
        credentials: The authenticated credentials
        
    Returns:
        googleapiclient.discovery.Resource: Compute Engine API client
    """
    # TODO: Build and return a Compute API client
    # - Use the discovery.build method with 'compute' and 'v1'
    
    pass

def create_vpc_network(service, project_id, network_name):
    """
    Create a new custom VPC network.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        network_name (str): Name for the new VPC network
        
    Returns:
        dict: The operation response
    """
    print(f"Creating VPC network '{network_name}'...")
    
    # TODO: Define the network configuration
    # - Set the name and autoCreateSubnetworks to False (for custom subnets)
    
    # TODO: Send the network creation request
    # - Use service.networks().insert
    # - Execute the request and return the response
    
    pass

def create_subnet(service, project_id, region, subnet_name, network_name, ip_cidr_range="10.0.0.0/24"):
    """
    Create a new subnet in a VPC network.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        region (str): GCP region for the subnet
        subnet_name (str): Name for the new subnet
        network_name (str): Name of the VPC network
        ip_cidr_range (str): CIDR range for the subnet
        
    Returns:
        dict: The operation response
    """
    print(f"Creating subnet '{subnet_name}' in region '{region}' with CIDR range '{ip_cidr_range}'...")
    
    # TODO: Define the subnet configuration
    # - Set name, region, network (full URL path), and ipCidrRange
    
    # TODO: Send the subnet creation request
    # - Use service.subnetworks().insert
    # - Execute the request and return the response
    
    pass

def create_firewall_rule(service, project_id, network_name, rule_name=None):
    """
    Create a basic firewall rule to allow SSH access.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        network_name (str): Name of the VPC network
        rule_name (str, optional): Name for the firewall rule
        
    Returns:
        dict: The operation response
    """
    if rule_name is None:
        rule_name = f"{network_name}-allow-ssh"
    
    print(f"Creating firewall rule '{rule_name}' for network '{network_name}'...")
    
    # TODO: Define the firewall rule configuration
    # - Allow TCP port 22 (SSH)
    # - Set appropriate source ranges (e.g., "0.0.0.0/0" for public access)
    # - Associate with the specified network
    
    # TODO: Send the firewall rule creation request
    # - Use service.firewalls().insert
    # - Execute the request and return the response
    
    pass

def wait_for_global_operation(service, project_id, operation_name):
    """
    Wait for a global operation to complete.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        operation_name (str): Name of the operation
        
    Returns:
        dict: The completed operation
    """
    print(f"Waiting for operation {operation_name} to complete...")
    
    # TODO: Implement waiting for a global operation to complete
    # - Poll the operation status periodically
    # - Return once the operation is complete
    # - Handle timeouts and errors
    
    pass

def wait_for_region_operation(service, project_id, region, operation_name):
    """
    Wait for a regional operation to complete.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        region (str): GCP region
        operation_name (str): Name of the operation
        
    Returns:
        dict: The completed operation
    """
    print(f"Waiting for operation {operation_name} in region {region} to complete...")
    
    # TODO: Implement waiting for a regional operation to complete
    # - Poll the operation status periodically
    # - Return once the operation is complete
    # - Handle timeouts and errors
    
    pass

def list_networks(service, project_id):
    """
    List all VPC networks in the project.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        
    Returns:
        list: List of networks
    """
    print(f"Listing VPC networks in project {project_id}...")
    
    # TODO: List all networks in the project
    # - Use service.networks().list
    # - Execute the request and extract the items
    # - Display the networks in a tabular format
    
    pass

def list_subnets(service, project_id, region="all"):
    """
    List all subnets in the project, optionally filtered by region.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        region (str): GCP region or 'all' for all regions
        
    Returns:
        list: List of subnets
    """
    print(f"Listing subnets in project {project_id}{' in region ' + region if region != 'all' else ''}...")
    
    # TODO: List all subnets in the project
    # - If region is specified (not 'all'), use service.subnetworks().list with region parameter
    # - Otherwise, call service.subnetworks().aggregatedList to get subnets across all regions
    # - Execute the request and extract the items
    # - Display the subnets in a tabular format
    
    pass

def delete_subnet(service, project_id, region, subnet_name):
    """
    Delete a subnet.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        region (str): GCP region
        subnet_name (str): Name of the subnet to delete
        
    Returns:
        dict: The operation response
    """
    print(f"Deleting subnet '{subnet_name}' in region '{region}'...")
    
    # TODO: Delete the subnet
    # - Use service.subnetworks().delete
    # - Execute the request and return the response
    
    pass

def delete_network(service, project_id, network_name):
    """
    Delete a VPC network.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        network_name (str): Name of the network to delete
        
    Returns:
        dict: The operation response
    """
    print(f"Deleting VPC network '{network_name}'...")
    
    # TODO: Delete the network
    # - Use service.networks().delete
    # - Execute the request and return the response
    
    pass

def find_subnets_by_network(service, project_id, network_name):
    """
    Find all subnets associated with a network.
    
    Args:
        service: Compute Engine API client
        project_id (str): GCP Project ID
        network_name (str): Name of the network
        
    Returns:
        list: List of [subnet_name, region] pairs
    """
    print(f"Finding subnets for network '{network_name}'...")
    
    # TODO: Find all subnets associated with the network
    # - Use service.subnetworks().aggregatedList to get all subnets
    # - Filter by network name
    # - Return a list of subnet names and their regions
    
    pass

def display_network_info(network):
    """
    Display information about a VPC network.
    
    Args:
        network (dict): The network data
    """
    print("\nNetwork Details:")
    
    info_table = [
        ["Name", network.get("name")],
        ["ID", network.get("id")],
        ["Creation Time", network.get("creationTimestamp")],
        ["Auto Subnet Mode", "Yes" if network.get("autoCreateSubnetworks") else "No"],
        ["Subnet Mode", "Auto" if network.get("autoCreateSubnetworks") else "Custom"],
        ["Routing Mode", network.get("routingConfig", {}).get("routingMode", "Regional")],
        ["Self Link", network.get("selfLink")]
    ]
    
    print(tabulate(info_table, tablefmt="grid"))

def main():
    parser = argparse.ArgumentParser(
        description="Create, list, or delete VPC networks and subnets"
    )
    parser.add_argument("--project_id", required=True, help="Your GCP Project ID")
    parser.add_argument("--credentials_file", help="Path to service account credentials JSON file")
    parser.add_argument("--create", action="store_true", help="Create a new VPC network and subnet")
    parser.add_argument("--list", action="store_true", help="List networks and subnets")
    parser.add_argument("--delete", action="store_true", help="Delete a network and its subnets")
    parser.add_argument("--network_name", help="Name for the VPC network")
    parser.add_argument("--subnet_name", help="Name for the subnet")
    parser.add_argument("--region", default="us-central1", help="Region for the subnet")
    parser.add_argument("--ip_cidr_range", default="10.0.0.0/24", help="CIDR range for the subnet")
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.create or args.delete:
        if not args.network_name:
            print("Error: --network_name is required when using --create or --delete")
            return 1
    
    if args.create and not args.subnet_name:
        print("Error: --subnet_name is required when using --create")
        return 1
    
    if not (args.create or args.list or args.delete):
        print("Error: You must specify at least one action: --create, --list, or --delete")
        return 1
    
    try:
        # Authenticate
        credentials = authenticate(args.credentials_file)
        
        # Build the Compute API client
        service = build_compute_client(credentials)
        
        # Perform the requested action
        if args.list:
            networks = list_networks(service, args.project_id)
            subnets = list_subnets(service, args.project_id)
            
            if not networks and not subnets:
                print("No networks or subnets found in this project.")
        
        if args.create:
            # Create the network
            network_op = create_vpc_network(service, args.project_id, args.network_name)
            
            if network_op and 'name' in network_op:
                operation = wait_for_global_operation(service, args.project_id, network_op['name'])
                
                if operation.get('status') == 'DONE':
                    print(f"VPC network {args.network_name} created successfully!")
                    
                    # Create the subnet
                    subnet_op = create_subnet(
                        service,
                        args.project_id,
                        args.region,
                        args.subnet_name,
                        args.network_name,
                        args.ip_cidr_range
                    )
                    
                    if subnet_op and 'name' in subnet_op:
                        operation = wait_for_region_operation(
                            service, args.project_id, args.region, subnet_op['name']
                        )
                        
                        if operation.get('status') == 'DONE':
                            print(f"Subnet {args.subnet_name} created successfully!")
                            
                            # Create a firewall rule
                            fw_op = create_firewall_rule(service, args.project_id, args.network_name)
                            
                            if fw_op and 'name' in fw_op:
                                operation = wait_for_global_operation(service, args.project_id, fw_op['name'])
                                
                                if operation.get('status') == 'DONE':
                                    print(f"Firewall rule created successfully!")
                                else:
                                    print(f"Firewall rule creation failed: {operation}")
                        else:
                            print(f"Subnet creation failed: {operation}")
                else:
                    print(f"Network creation failed: {operation}")
        
        if args.delete:
            # Find subnets associated with the network
            subnet_regions = find_subnets_by_network(service, args.project_id, args.network_name)
            
            # Delete all subnets first
            for subnet_name, region in subnet_regions:
                subnet_op = delete_subnet(service, args.project_id, region, subnet_name)
                
                if subnet_op and 'name' in subnet_op:
                    operation = wait_for_region_operation(
                        service, args.project_id, region, subnet_op['name']
                    )
                    
                    if operation.get('status') == 'DONE':
                        print(f"Subnet {subnet_name} deleted successfully!")
                    else:
                        print(f"Subnet deletion failed: {operation}")
                        return 1
            
            # Then delete the network
            network_op = delete_network(service, args.project_id, args.network_name)
            
            if network_op and 'name' in network_op:
                operation = wait_for_global_operation(service, args.project_id, network_op['name'])
                
                if operation.get('status') == 'DONE':
                    print(f"VPC network {args.network_name} deleted successfully!")
                else:
                    print(f"Network deletion failed: {operation}")
            
        return 0
    
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 