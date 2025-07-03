#!/usr/bin/env python3
"""
AWS LAB05 - Lambda Deployment Script

This script demonstrates how to package and deploy an AWS Lambda function using boto3.
It creates a zip file from the Lambda function code and deploys it to AWS.

Usage:
    python deploy_lambda.py [--function-name NAME] [--delete] [--invoke]
"""

import boto3
import zipfile
import os
import json
import argparse
import sys
from botocore.exceptions import ClientError

# Default configuration
DEFAULT_REGION = 'eu-west-1'
DEFAULT_FUNCTION_NAME = 'MyDevOpsLambda'
DEFAULT_RUNTIME = 'python3.9'
DEFAULT_TIMEOUT = 10
DEFAULT_MEMORY_SIZE = 128
DEFAULT_SOURCE_FILE = 'lambda_function.py'
DEFAULT_HANDLER = 'lambda_function.lambda_handler'

def create_deployment_package(source_file=DEFAULT_SOURCE_FILE):
    """
    Create a zip file containing the Lambda function code
    
    Args:
        source_file (str): Path to the Lambda function file
        
    Returns:
        str: Path to the created zip file
    """
    try:
        print(f"Creating deployment package from: {source_file}")
        
        # TODO: Verify source file exists
        # Use os.path.exists to check if source_file exists
        # Raise FileNotFoundError if it doesn't exist
        
        # TODO: Create a zip file containing the source file
        # 1. Define the zip file path
        # 2. Create a ZipFile object in write mode with ZIP_DEFLATED compression
        # 3. Add the source file to the zip
        
        zip_path = None  # Replace with your implementation
        
        print(f"Created deployment package: {zip_path}")
        return zip_path
    except Exception as e:
        print(f"Error creating deployment package: {e}")
        raise

def create_lambda_role(role_name="lambda-execute-role", region=DEFAULT_REGION):
    """
    Create an IAM role for Lambda execution
    
    Args:
        role_name (str): Name for the IAM role
        region (str): AWS region
        
    Returns:
        str: ARN of the created role
    """
    try:
        print(f"Creating IAM role: {role_name}")
        
        # TODO: Create IAM client
        
        # TODO: Define trust policy for Lambda
        # Create a policy document that allows lambda.amazonaws.com to assume this role
        
        # TODO: Create the role using create_role method
        # Use the role_name and trust policy document
        
        # TODO: Attach basic Lambda execution policy
        # Attach the AWSLambdaBasicExecutionRole policy
        
        # TODO: Wait for the role to propagate
        # Use time.sleep to wait a few seconds
        
        # TODO: Extract and return the role ARN
        role_arn = None  # Replace with your implementation
        
        print(f"Created IAM role with ARN: {role_arn}")
        return role_arn
    except ClientError as e:
        # TODO: Handle the case where the role already exists
        # If error code is 'EntityAlreadyExists', retrieve the existing role's ARN
        print(f"Error creating IAM role: {e}")
        raise

def deploy_lambda_function(function_name=DEFAULT_FUNCTION_NAME, 
                          zip_file=None, 
                          handler=DEFAULT_HANDLER, 
                          role_arn=None, 
                          runtime=DEFAULT_RUNTIME, 
                          timeout=DEFAULT_TIMEOUT, 
                          memory_size=DEFAULT_MEMORY_SIZE,
                          region=DEFAULT_REGION):
    """
    Create or update a Lambda function
    
    Args:
        function_name (str): Name of the Lambda function
        zip_file (str): Path to the deployment package
        handler (str): Handler function name (file.function)
        role_arn (str): IAM role ARN for execution
        runtime (str): Lambda runtime
        timeout (int): Function timeout in seconds
        memory_size (int): Function memory in MB
        region (str): AWS region
        
    Returns:
        str: ARN of the deployed function
    """
    try:
        print(f"Deploying Lambda function: {function_name}")
        
        # TODO: Check if zip file exists
        # Raise FileNotFoundError if zip_file doesn't exist
        
        # TODO: Create a role if not provided
        # If role_arn is None, call create_lambda_role
        
        # TODO: Create Lambda client
        
        # TODO: Read the zip file content
        # Open the zip file in binary mode and read its content
        zip_content = None  # Replace with your implementation
        
        # TODO: Try to get the function (to check if it exists)
        # If function exists, update its code and configuration
        # If function doesn't exist, create a new function
        # Handle ClientError with ResourceNotFoundException to distinguish between update and create
        
        function_arn = None  # Replace with your implementation
        print(f"Lambda function deployed: {function_arn}")
        return function_arn
        
    except ClientError as e:
        print(f"Error deploying Lambda function: {e}")
        return None

def invoke_lambda_function(function_name=DEFAULT_FUNCTION_NAME, payload=None, region=DEFAULT_REGION):
    """
    Invoke a Lambda function and return the result
    
    Args:
        function_name (str): Name of the Lambda function
        payload (dict): JSON payload to send to the function
        region (str): AWS region
        
    Returns:
        dict: Function response
    """
    try:
        print(f"Invoking Lambda function: {function_name}")
        
        # TODO: Create Lambda client
        
        # TODO: Create default payload if none is provided
        # If payload is None, create a simple test payload
        
        # TODO: Convert payload to JSON string
        
        # TODO: Invoke the Lambda function
        # Use the invoke method with FunctionName and Payload parameters
        
        # TODO: Process and return the response
        # Extract the StatusCode and Payload from the response
        # Convert the Payload from bytes to string and parse as JSON
        
        return None  # Replace with your implementation
    except ClientError as e:
        print(f"Error invoking Lambda function: {e}")
        return None

def delete_lambda_function(function_name=DEFAULT_FUNCTION_NAME, region=DEFAULT_REGION):
    """
    Delete a Lambda function
    
    Args:
        function_name (str): Name of the Lambda function
        region (str): AWS region
        
    Returns:
        bool: True if deleted successfully, False on error
    """
    try:
        print(f"Deleting Lambda function: {function_name}")
        
        # TODO: Create Lambda client
        
        # TODO: Delete the Lambda function
        # Use the delete_function method with FunctionName parameter
        
        print(f"Lambda function {function_name} deleted successfully")
        return True
    except ClientError as e:
        # TODO: Handle the case where the function doesn't exist
        # If error code is 'ResourceNotFoundException', print a message and return True
        print(f"Error deleting Lambda function: {e}")
        return False

def main():
    """
    Main function to parse arguments and execute Lambda operations
    """
    # TODO: Set up argument parser
    # Add arguments for:
    # - function-name: Name of the Lambda function
    # - source-file: Source file path
    # - handler: Handler function name
    # - runtime: Lambda runtime
    # - timeout: Function timeout
    # - memory-size: Function memory
    # - region: AWS region
    # - invoke: Flag to invoke the function after deployment
    # - delete: Flag to delete the function
    
    # TODO: Parse arguments
    args = None  # Replace with parser.parse_args()
    
    # TODO: Implement the main workflow based on arguments
    # 1. If delete flag is set, delete the function and exit
    # 2. Otherwise, create deployment package
    # 3. Deploy the Lambda function
    # 4. If invoke flag is set, invoke the function
    
    print("\nLambda deployment completed successfully!")


if __name__ == "__main__":
    main()