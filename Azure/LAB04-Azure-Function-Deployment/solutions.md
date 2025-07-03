# Solutions: Azure Function Deployment Automation

This document provides the reference solutions for the Azure Function Deployment lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

### HttpTrigger/__init__.py

```python
import logging
import azure.functions as func
import json
import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP trigger function endpoint.
    
    Args:
        req: HTTP request object with headers, params, body
        
    Returns:
        HTTP response with appropriate status code and body
    """
    logging.info('Python HTTP trigger function processed a request.')

    # Get name from query parameter or request body
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    # Get additional parameters
    method = req.method
    headers = dict(req.headers)
    params = dict(req.params)
    
    # Build response with timestamp
    timestamp = datetime.datetime.now().isoformat()
    
    response_data = {
        "message": f"Hello, {name}!" if name else "This HTTP triggered function executed successfully.",
        "method": method,
        "timestamp": timestamp,
        "params": params
    }
    
    if name:
        return func.HttpResponse(
            json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )
    else:
        response_data["help"] = "Pass a name in the query string or in the request body for a personalized response."
        return func.HttpResponse(
            json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )
```

### function_app.py

```python
#!/usr/bin/env python3
"""
Azure Function Deployment Automation Script

This script automates the deployment of an Azure Function using Python and the Azure CLI.
It demonstrates how to create a resource group, storage account, and function app, and
then deploy a function to it.
"""

import os
import sys
import argparse
import subprocess
import time
import json
import requests
import re

def run_az_command(command):
    """
    Run an Azure CLI command using subprocess.
    
    Args:
        command (str): The Azure CLI command to execute
        
    Returns:
        dict or str: JSON output parsed as dict or raw output as string
    """
    print(f"Running: az {command}")
    
    # Run the command
    result = subprocess.run(
        f"az {command}",
        shell=True,
        check=False,
        capture_output=True,
        text=True
    )
    
    # Check for errors
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
        raise Exception(f"Command failed with exit code {result.returncode}: {result.stderr}")
    
    # Try to parse as JSON
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        # Return as string if not JSON
        return result.stdout.strip()

def verify_az_cli():
    """
    Verify that Azure CLI is installed and the user is logged in.
    
    Returns:
        bool: True if Azure CLI is available and logged in
    """
    try:
        # Check if az is in the path
        result = subprocess.run(
            "az --version",
            shell=True,
            check=False,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("Azure CLI is not installed or not in the PATH.")
            print("Please install Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli")
            return False
        
        # Check if the user is logged in
        account_info = run_az_command("account show")
        print(f"Logged in to Azure as: {account_info['user']['name']}")
        print(f"Subscription: {account_info['name']} ({account_info['id']})")
        return True
        
    except Exception as e:
        print(f"Error verifying Azure CLI: {e}")
        print("Please log in using: az login")
        return False

def create_resource_group(name, location):
    """
    Create an Azure resource group.
    
    Args:
        name (str): Resource group name
        location (str): Azure region
        
    Returns:
        bool: True if successful
    """
    print(f"Creating resource group '{name}' in {location}...")
    
    # Check if resource group exists
    try:
        rg = run_az_command(f"group show --name {name}")
        print(f"Resource group '{name}' already exists.")
    except Exception:
        # Create resource group if it doesn't exist
        rg = run_az_command(f"group create --name {name} --location {location}")
        print(f"Resource group '{name}' created successfully.")
    
    return True

def create_storage_account(resource_group, name, location):
    """
    Create an Azure Storage account.
    
    Args:
        resource_group (str): Resource group name
        name (str): Storage account name (must be globally unique)
        location (str): Azure region
        
    Returns:
        str: Storage account name if successful
    """
    print(f"Creating storage account '{name}' in {resource_group}...")
    
    # Validate storage account name (lowercase letters and numbers only, 3-24 chars)
    if not re.match(r'^[a-z0-9]{3,24}$', name):
        raise ValueError(
            "Storage account name must be 3-24 characters long and can only contain "
            "lowercase letters and numbers."
        )
    
    # Check if storage account exists
    try:
        sa = run_az_command(f"storage account show --name {name} --resource-group {resource_group}")
        print(f"Storage account '{name}' already exists.")
    except Exception:
        # Create storage account if it doesn't exist
        sa = run_az_command(
            f"storage account create --name {name} --resource-group {resource_group} "
            f"--location {location} --sku Standard_LRS --kind StorageV2 --https-only true"
        )
        print(f"Storage account '{name}' created successfully.")
    
    # Wait for storage account to be ready
    time.sleep(5)
    
    return name

def create_function_app(resource_group, name, storage_account, location):
    """
    Create an Azure Function App.
    
    Args:
        resource_group (str): Resource group name
        name (str): Function app name
        storage_account (str): Storage account name
        location (str): Azure region
        
    Returns:
        str: Function app name if successful
    """
    print(f"Creating function app '{name}' in {resource_group}...")
    
    # Check if function app exists
    try:
        fa = run_az_command(f"functionapp show --name {name} --resource-group {resource_group}")
        print(f"Function app '{name}' already exists.")
    except Exception:
        # Create function app if it doesn't exist
        fa = run_az_command(
            f"functionapp create --name {name} --resource-group {resource_group} "
            f"--storage-account {storage_account} --consumption-plan-location {location} "
            f"--runtime python --runtime-version 3.9 --functions-version 4 "
            f"--os-type Linux"
        )
        print(f"Function app '{name}' created successfully.")
    
    # Wait for function app to be ready
    time.sleep(5)
    
    return name

def deploy_function(function_app_name, function_path="."):
    """
    Deploy a function to an Azure Function App.
    
    Args:
        function_app_name (str): Function app name
        function_path (str): Path to function project
        
    Returns:
        bool: True if successful
    """
    print(f"Deploying function to '{function_app_name}'...")
    
    # Option 1: Deploy using Azure CLI directly
    try:
        # Navigate to function path if specified
        cwd = os.getcwd()
        if function_path != ".":
            os.chdir(function_path)
        
        # Deploy using Azure CLI
        output = run_az_command(
            f"functionapp deployment source config-zip "
            f"-g devops-lab-rg -n {function_app_name} "
            f"--src ./function_package.zip"
        )
        
        # Return to original directory
        if function_path != ".":
            os.chdir(cwd)
            
        print("Function deployed successfully using Azure CLI.")
        return True
        
    except Exception as e:
        print(f"Error deploying function using Azure CLI: {e}")
        
        # Option 2: Deploy using Azure Functions Core Tools (func)
        try:
            # Navigate to function path if specified
            cwd = os.getcwd()
            if function_path != ".":
                os.chdir(function_path)
            
            # Check if func command is available
            result = subprocess.run(
                "func --version",
                shell=True,
                check=False,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print("Azure Functions Core Tools (func) is not installed or not in the PATH.")
                print("Please install it: npm install -g azure-functions-core-tools@4")
                return False
            
            # Deploy using func command
            result = subprocess.run(
                f"func azure functionapp publish {function_app_name}",
                shell=True,
                check=False,
                capture_output=True,
                text=True
            )
            
            # Return to original directory
            if function_path != ".":
                os.chdir(cwd)
                
            if result.returncode != 0:
                print(f"Error deploying function: {result.stderr}")
                return False
                
            print("Function deployed successfully using Azure Functions Core Tools.")
            return True
            
        except Exception as e2:
            print(f"Error deploying function using Azure Functions Core Tools: {e2}")
            return False

def test_function(function_app_name, function_name="HttpTrigger"):
    """
    Test an HTTP-triggered Azure Function.
    
    Args:
        function_app_name (str): Function app name
        function_name (str): Name of the function to test
        
    Returns:
        bool: True if successful
    """
    print(f"Testing function '{function_name}' in app '{function_app_name}'...")
    
    # Build the function URL
    function_url = f"https://{function_app_name}.azurewebsites.net/api/{function_name}?name=DevOpsUser"
    
    try:
        # Send a test request
        print(f"Sending test request to: {function_url}")
        response = requests.get(function_url)
        
        # Display the response
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")
        
        if response.status_code == 200:
            print("Test successful!")
            return True
        else:
            print(f"Test failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error testing function: {e}")
        return False

def cleanup_resources(resource_group):
    """
    Clean up Azure resources to avoid charges.
    
    Args:
        resource_group (str): Resource group name
        
    Returns:
        bool: True if successful
    """
    print(f"Cleaning up resource group '{resource_group}'...")
    
    try:
        # Delete the resource group
        run_az_command(f"group delete --name {resource_group} --yes")
        print(f"Resource group '{resource_group}' deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting resource group: {e}")
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
        # First verify that az CLI is available
        if not verify_az_cli():
            print("Azure CLI verification failed. Please ensure Azure CLI is installed and you're logged in.")
            sys.exit(1)
        
        # Create the resource group
        rg_success = create_resource_group(args.resource_group, args.location)
        if not rg_success:
            print("Failed to create resource group.")
            sys.exit(1)
        
        # Create the storage account
        storage_account_name = create_storage_account(args.resource_group, args.storage_account, args.location)
        if not storage_account_name:
            print("Failed to create storage account.")
            sys.exit(1)
        
        # Create the function app
        function_app_name = create_function_app(args.resource_group, args.function_app, storage_account_name, args.location)
        if not function_app_name:
            print("Failed to create function app.")
            sys.exit(1)
        
        # Deploy the function
        deploy_success = deploy_function(function_app_name)
        if not deploy_success:
            print("Failed to deploy function.")
            sys.exit(1)
        
        # Test the function if --test is specified
        if args.test:
            test_success = test_function(function_app_name)
            if not test_success:
                print("Function testing failed.")
        
        # Clean up resources if --cleanup is specified
        if args.cleanup:
            cleanup_success = cleanup_resources(args.resource_group)
            if not cleanup_success:
                print("Resource cleanup failed.")
        
        # Print success message with function URL
        function_url = f"https://{function_app_name}.azurewebsites.net/api/HttpTrigger"
        print("\nDeployment completed successfully!")
        print(f"Function URL: {function_url}")
        print("Test with: curl -X GET \"" + function_url + "?name=YourName\"")
        
        if not args.cleanup:
            print("\nDon't forget to clean up resources when you're done to avoid unnecessary charges:")
            print(f"az group delete --name {args.resource_group} --yes")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Installation and Authentication

Before running the script, make sure you have:

1. Installed Azure CLI
```bash
# Install Azure CLI on Windows
winget install -e --id Microsoft.AzureCLI

# Install Azure CLI on Mac
brew install azure-cli

# Install Azure CLI on Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

2. Installed Azure Functions Core Tools
```bash
npm install -g azure-functions-core-tools@4
```

3. Logged in to Azure
```bash
az login
```

4. Selected your subscription (if you have multiple)
```bash
az account set --subscription "Your Subscription Name or ID"
```

## Sample Usage

### Basic Deployment
```bash
python function_app.py
```

### Custom Resource Group and Location
```bash
python function_app.py --resource-group my-functions-rg --location westus2
```

### Custom Storage Account and Function App Names
```bash
python function_app.py --storage-account mystorageacct --function-app my-function-app
```

### Deploy, Test, and Clean Up
```bash
python function_app.py --test --cleanup
```

## Key Learning Points

1. **Azure Functions Core Concepts**
   - Serverless compute service for event-driven architectures
   - Functions are triggered by events (HTTP requests, timers, queue messages, etc.)
   - Consumption plan offers automatic scaling with pay-per-use pricing

2. **Azure Functions Project Structure**
   - `host.json`: Configuration for all functions in the app
   - Function folders (e.g., `HttpTrigger`) containing:
     - `__init__.py`: Main function code
     - `function.json`: Bindings and trigger configuration

3. **Deployment Methods**
   - Azure Functions Core Tools (`func` command)
   - Azure CLI with ZIP deployment
   - CI/CD with GitHub Actions or Azure DevOps

4. **HTTP Triggers in Python**
   - Working with `func.HttpRequest` object
   - Extracting query parameters and request body
   - Returning `func.HttpResponse` with appropriate status code

5. **Resource Management**
   - Creating resource groups, storage accounts, and function apps
   - Using unique naming patterns for global resources
   - Cleaning up resources to avoid costs

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "Not logged in" errors
   - **Solution**: Run `az login` to authenticate with your Azure account

2. **Storage Account Naming**
   - **Problem**: Invalid storage account name
   - **Solution**: Use only lowercase letters and numbers, 3-24 characters

3. **Deployment Failures**
   - **Problem**: Function app deployment fails
   - **Solution**: Check logs with `az functionapp logs` or Azure Portal

4. **CORS Issues**
   - **Problem**: Browser can't access function due to CORS
   - **Solution**: Configure CORS in Azure Portal or via `az functionapp cors` command

5. **Cold Start Performance**
   - **Problem**: First function invocation is slow
   - **Solution**: Use premium plan or implement warm-up strategies

## Best Practices

1. **Use Environment-Specific Settings**
   - Store configuration in application settings
   - Use different settings for dev/test/prod environments

2. **Implement Proper Error Handling**
   - Catch and log exceptions
   - Return appropriate HTTP status codes

3. **Monitor Your Functions**
   - Use Application Insights for logging and monitoring
   - Set up alerts for failures or performance issues

4. **Security Considerations**
   - Use function keys to secure HTTP endpoints
   - Implement proper authentication for protected resources

5. **Optimize for Cost and Performance**
   - Keep functions small and focused
   - Use durable functions for complex workflows
   - Choose the right hosting plan (Consumption, Premium, App Service)

## Cleanup Importance

Always remember to clean up Azure resources when they're no longer needed:

1. Function apps incur charges when they execute
2. Storage accounts incur charges for stored data
3. Use the `--cleanup` flag or manual cleanup with Azure CLI

The provided script includes cleanup functionality to help manage costs.

## Extending This Lab

1. Add more function triggers (Timer, Queue, Blob)
2. Implement input and output bindings
3. Set up CI/CD with GitHub Actions
4. Add monitoring with Application Insights
5. Create a custom domain for your function app 