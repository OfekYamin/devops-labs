#!/usr/bin/env python3
"""
Azure Function Deployment Automation Script

This script automates the deployment of an Azure Function using Python and the Azure CLI.
It demonstrates how to create a resource group, storage account, and function app, and
then deploy a function to it.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import argparse
import subprocess
import time

def run_az_command(command):
    """
    Run an Azure CLI command using subprocess.
    
    TODO: Implement this function to:
    1. Execute the Azure CLI command using subprocess
    2. Handle errors and return the command output
    
    Args:
        command (str): The Azure CLI command to execute
        
    Returns:
        dict or str: JSON output parsed as dict or raw output as string
    """
    # TODO: Run the command using subprocess.run()
    
    # TODO: Check for errors in the execution
    
    # TODO: Parse and return the output
    pass

def create_resource_group(name, location):
    """
    Create an Azure resource group.
    
    TODO: Implement this function to:
    1. Check if the resource group exists
    2. Create the resource group if it doesn't exist
    
    Args:
        name (str): Resource group name
        location (str): Azure region
        
    Returns:
        bool: True if successful
    """
    print(f"Creating resource group '{name}' in {location}...")
    
    # TODO: Check if resource group exists
    
    # TODO: Create resource group if it doesn't exist
    
    # TODO: Return success status
    return False

def create_storage_account(resource_group, name, location):
    """
    Create an Azure Storage account.
    
    TODO: Implement this function to:
    1. Create a storage account in the specified resource group
    2. Wait for it to be ready
    
    Args:
        resource_group (str): Resource group name
        name (str): Storage account name (must be globally unique)
        location (str): Azure region
        
    Returns:
        str: Storage account name if successful
    """
    print(f"Creating storage account '{name}' in {resource_group}...")

    # TODO: Check if storage account exists
    
    # TODO: Create storage account if it doesn't exist
    
    # TODO: Wait for storage account to be ready
    
    # TODO: Return storage account name
    return name

def create_function_app(resource_group, name, storage_account, location):
    """
    Create an Azure Function App.
    
    TODO: Implement this function to:
    1. Create a consumption plan function app
    2. Configure it for Python
    
    Args:
        resource_group (str): Resource group name
        name (str): Function app name
        storage_account (str): Storage account name
        location (str): Azure region
        
    Returns:
        str: Function app name if successful
    """
    print(f"Creating function app '{name}' in {resource_group}...")
    
    # TODO: Create function app with consumption plan
    
    # TODO: Return function app name
    return name

def deploy_function(function_app_name, function_path):
    """
    Deploy a function to an Azure Function App.
    
    TODO: Implement this function to:
    1. Pack and publish the function to Azure
    2. Handle deployment errors
    
    Args:
        function_app_name (str): Function app name
        function_path (str): Path to function project
        
    Returns:
        bool: True if successful
    """
    print(f"Deploying function to '{function_app_name}'...")
    
    # TODO: Deploy the function using Azure CLI or Azure Functions Core Tools
    
    # TODO: Return success status
    return False

def test_function(function_app_name, function_name="HttpTrigger"):
    """
    Test an HTTP-triggered Azure Function.
    
    TODO: Implement this function to:
    1. Construct the function URL
    2. Send a test request
    3. Display the response
    
    Args:
        function_app_name (str): Function app name
        function_name (str): Name of the function to test
        
    Returns:
        bool: True if successful
    """
    print(f"Testing function '{function_name}' in app '{function_app_name}'...")
    
    # TODO: Build the function URL
    
    # TODO: Send a test request and display the response
    
    # TODO: Return success status
    return False

def cleanup_resources(resource_group):
    """
    Clean up Azure resources to avoid charges.
    
    TODO: Implement this function to:
    1. Delete the resource group and all resources within it
    
    Args:
        resource_group (str): Resource group name
        
    Returns:
        bool: True if successful
    """
    print(f"Cleaning up resource group '{resource_group}'...")
    
    # TODO: Delete the resource group
    
    # TODO: Return success status
    return False

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description='Azure Function Deployment Tool')
    
    # Add arguments
    parser.add_argument('--resource-group', default='devops-lab-rg', help='Resource group name')
    parser.add_argument('--location', default='eastus', help='Azure region')
    parser.add_argument('--storage-account', help='Storage account name (will be auto-generated if not provided)')
    parser.add_argument('--function-app', help='Function app name (will be auto-generated if not provided)')
    parser.add_argument('--cleanup', action='store_true', help='Clean up resources after deployment')
    parser.add_argument('--test', action='store_true', help='Test the function after deployment')
    
    args = parser.parse_args()
    
    # Set generated names if not provided
    if not args.storage_account:
        args.storage_account = f"devopssa{int(time.time())}"
    if not args.function_app:
        args.function_app = f"devops-func-{int(time.time())}"
    
    try:
        # TODO: First verify that az CLI is available
        
        # TODO: Create the resource group
        
        # TODO: Create the storage account
        
        # TODO: Create the function app
        
        # TODO: Deploy the function
        
        # TODO: Test the function if --test is specified
        
        # TODO: Clean up resources if --cleanup is specified
        
        # TODO: Print success message with function URL
        
        pass
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 