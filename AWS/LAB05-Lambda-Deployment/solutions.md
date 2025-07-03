# LAB05 - Lambda Deployment: Solutions

This document contains the complete solution for the Lambda Deployment lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for deploy_lambda.py

```python
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
        
        # Verify source file exists
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Source file not found: {source_file}")
        
        # Create zip file
        zip_path = "function.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(source_file)
            
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
        
        # Create IAM client
        iam_client = boto3.client('iam', region_name=region)
        
        # Define trust policy for Lambda
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        
        # Create the role
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='Role for Lambda execution created by DevOps lab'
        )
        
        # Attach basic Lambda execution policy
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )
        
        # Give AWS time to propagate the role
        print("Waiting for IAM role to be ready...")
        import time
        time.sleep(10)
        
        role_arn = response['Role']['Arn']
        print(f"Created IAM role with ARN: {role_arn}")
        return role_arn
    except ClientError as e:
        # If role already exists, get its ARN
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"IAM role {role_name} already exists, retrieving ARN...")
            response = iam_client.get_role(RoleName=role_name)
            return response['Role']['Arn']
        else:
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
        
        # Check if zip file exists
        if not zip_file or not os.path.exists(zip_file):
            raise FileNotFoundError(f"Deployment package not found: {zip_file}")
        
        # Create a role if not provided
        if not role_arn:
            role_arn = create_lambda_role(region=region)
        
        # Create Lambda client
        lambda_client = boto3.client('lambda', region_name=region)
        
        # Read the zip file
        with open(zip_file, 'rb') as f:
            zip_content = f.read()
        
        try:
            # Try to get the function (to check if it exists)
            lambda_client.get_function(FunctionName=function_name)
            
            # Function exists, update it
            print(f"Function {function_name} exists, updating code...")
            code_response = lambda_client.update_function_code(
                FunctionName=function_name,
                ZipFile=zip_content,
                Publish=True
            )
            
            # Update configuration
            config_response = lambda_client.update_function_configuration(
                FunctionName=function_name,
                Role=role_arn,
                Handler=handler,
                Runtime=runtime,
                Timeout=timeout,
                MemorySize=memory_size
            )
            
            function_arn = config_response['FunctionArn']
            print(f"Updated Lambda function: {function_arn}")
            
        except ClientError as e:
            # Function doesn't exist, create it
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print(f"Function {function_name} does not exist, creating new function...")
                response = lambda_client.create_function(
                    FunctionName=function_name,
                    Runtime=runtime,
                    Role=role_arn,
                    Handler=handler,
                    Code={'ZipFile': zip_content},
                    Timeout=timeout,
                    MemorySize=memory_size,
                    Publish=True
                )
                
                function_arn = response['FunctionArn']
                print(f"Created Lambda function: {function_arn}")
            else:
                raise
        
        return function_arn
    except Exception as e:
        print(f"Error deploying Lambda function: {e}")
        raise

def invoke_lambda_function(function_name=DEFAULT_FUNCTION_NAME, payload=None, region=DEFAULT_REGION):
    """
    Invoke a Lambda function and return the response
    
    Args:
        function_name (str): Name of the Lambda function
        payload (dict): Input data for the Lambda function
        region (str): AWS region
        
    Returns:
        dict: Response from the Lambda function
    """
    try:
        print(f"Invoking Lambda function: {function_name}")
        
        # Create Lambda client
        lambda_client = boto3.client('lambda', region_name=region)
        
        # Prepare payload
        if payload is None:
            payload = {"message": "Hello from deployment script"}
        
        # Invoke the function
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # Synchronous invocation
            Payload=json.dumps(payload)
        )
        
        # Process and return response
        status_code = response['StatusCode']
        payload = json.loads(response['Payload'].read().decode('utf-8'))
        
        print(f"Invocation status code: {status_code}")
        return payload
    except Exception as e:
        print(f"Error invoking Lambda function: {e}")
        raise

def delete_lambda_function(function_name=DEFAULT_FUNCTION_NAME, region=DEFAULT_REGION):
    """
    Delete a Lambda function
    
    Args:
        function_name (str): Name of the Lambda function to delete
        region (str): AWS region
        
    Returns:
        bool: True if the function was deleted successfully
    """
    try:
        print(f"Deleting Lambda function: {function_name}")
        
        # Create Lambda client
        lambda_client = boto3.client('lambda', region_name=region)
        
        # Delete the function
        lambda_client.delete_function(FunctionName=function_name)
        
        print(f"Lambda function {function_name} deleted successfully")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(f"Function {function_name} does not exist or is already deleted")
            return True
        print(f"Error deleting Lambda function: {e}")
        return False

def main():
    """Main function to parse arguments and execute operations"""
    parser = argparse.ArgumentParser(description='AWS Lambda Deployment Tool')
    
    parser.add_argument('--function-name', default=DEFAULT_FUNCTION_NAME, 
                       help=f'Name of the Lambda function (default: {DEFAULT_FUNCTION_NAME})')
    parser.add_argument('--runtime', default=DEFAULT_RUNTIME, 
                       help=f'Lambda runtime (default: {DEFAULT_RUNTIME})')
    parser.add_argument('--handler', default=DEFAULT_HANDLER, 
                       help=f'Lambda handler (default: {DEFAULT_HANDLER})')
    parser.add_argument('--timeout', type=int, default=DEFAULT_TIMEOUT, 
                       help=f'Function timeout in seconds (default: {DEFAULT_TIMEOUT})')
    parser.add_argument('--memory-size', type=int, default=DEFAULT_MEMORY_SIZE, 
                       help=f'Function memory in MB (default: {DEFAULT_MEMORY_SIZE})')
    parser.add_argument('--region', default=DEFAULT_REGION, 
                       help=f'AWS region (default: {DEFAULT_REGION})')
    parser.add_argument('--role-arn', help='IAM role ARN (if not provided, one will be created)')
    parser.add_argument('--source-file', default=DEFAULT_SOURCE_FILE, 
                       help=f'Path to Lambda function file (default: {DEFAULT_SOURCE_FILE})')
    
    # Action flags
    parser.add_argument('--deploy', action='store_true', help='Deploy/update the Lambda function')
    parser.add_argument('--invoke', action='store_true', help='Invoke the Lambda function')
    parser.add_argument('--delete', action='store_true', help='Delete the Lambda function')
    
    args = parser.parse_args()
    
    print("AWS Lambda Function Deployment Tool")
    print("=================================")
    
    try:
        # If no action specified, default to deploy and invoke
        if not (args.deploy or args.invoke or args.delete):
            args.deploy = True
            args.invoke = True
        
        # Deploy Lambda function
        if args.deploy:
            zip_file = create_deployment_package(args.source_file)
            
            function_arn = deploy_lambda_function(
                function_name=args.function_name,
                zip_file=zip_file,
                handler=args.handler,
                role_arn=args.role_arn,
                runtime=args.runtime,
                timeout=args.timeout,
                memory_size=args.memory_size,
                region=args.region
            )
            
            # Clean up the zip file
            if os.path.exists(zip_file):
                os.remove(zip_file)
        
        # Invoke Lambda function
        if args.invoke:
            response = invoke_lambda_function(
                function_name=args.function_name,
                region=args.region
            )
            
            print("\nLambda Response:")
            print(json.dumps(response, indent=2))
        
        # Delete Lambda function
        if args.delete:
            delete_lambda_function(
                function_name=args.function_name,
                region=args.region
            )
    
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)
    
    # Print cleanup instructions if we deployed but didn't delete
    if args.deploy and not args.delete:
        print("\n⚠️  CLEANUP: Remember to delete the Lambda function when you're done!")
        print(f"Use: python deploy_lambda.py --function-name {args.function_name} --delete")

if __name__ == "__main__":
    main()
```

## Solution for lambda_function.py

This is the Lambda function code that we're deploying to AWS. It's a simple function that returns a success message.

```python
"""
Lambda function for AWS LAB05

This file contains a simple AWS Lambda function handler that returns a successful response.
This is the function that will be deployed to AWS Lambda.
"""

def lambda_handler(event, context):
    """
    Simple Lambda function handler.
    
    Parameters:
    - event: The event data passed to the Lambda function
    - context: Runtime information provided by AWS Lambda
    
    Returns:
    - A dictionary containing the response with status code and body message
    """
    # Process the incoming event data
    print("Lambda function invoked!")
    print(f"Event data: {event}")
    
    # You can extract data from the event
    message = event.get('message', 'No message provided')
    
    # In a real application, you might:
    # - Process data from an S3 event
    # - Handle API Gateway requests
    # - Process SQS messages
    # - Respond to CloudWatch scheduled events
    
    # Return a response
    return {
        'statusCode': 200,
        'body': f'Hello from Lambda! Received message: {message}',
        'event': event
    }
```

## Key Learning Points

1. **Lambda Deployment Process**:
   - Creating deployment packages (zip files) for Lambda functions
   - Understanding Lambda configuration parameters (runtime, handler, timeout, memory)
   - Creating and updating Lambda functions via the AWS SDK

2. **IAM Role Management**:
   - Creating IAM roles programmatically for Lambda execution
   - Understanding trust relationships between services
   - Attaching policies to roles to grant necessary permissions

3. **Lambda Function Invocation**:
   - Invoking functions programmatically with boto3
   - Handling function responses and payloads
   - Understanding synchronous vs. asynchronous invocation

4. **Command Line Interface Design**:
   - Building a CLI tool with argparse for flexible deployments
   - Implementing flags for different operations (deploy, invoke, delete)
   - Providing helpful feedback and error messages

5. **Error Handling**:
   - Detecting and handling AWS-specific exceptions
   - Implementing graceful error handling for deployment failures
   - Checking for existing resources before creation

## Common Issues and Troubleshooting

1. **IAM Role Issues**:
   - "Access Denied" or insufficient permissions errors
   - Solution: Ensure the IAM role has appropriate permissions (AWSLambdaBasicExecutionRole at minimum)
   - Note: IAM role propagation can take time, which is why we added a delay

2. **Deployment Package Problems**:
   - "Invalid ZIP file" errors when Lambda can't process the package
   - Solution: Ensure the zip file structure is correct (files at root level, not in subdirectories)

3. **Handler Configuration**:
   - "Handler not found" errors due to incorrect handler notation
   - Solution: Use the correct format (filename.function_name) and ensure the file contains the function

4. **Lambda Runtime Compatibility**:
   - Errors when using unsupported Python versions
   - Solution: Ensure you're using a supported runtime (python3.7, python3.8, python3.9, etc.)

5. **Payload Size Limits**:
   - Errors when deploying large functions or when passing large payloads
   - Solution: Keep deployment packages small, use S3 for larger files, and respect payload size limits

## Best Practices

1. **Use Descriptive Function Names**: Include purpose and environment in the function name
2. **Implement Proper Error Handling**: Add try/except blocks in Lambda functions
3. **Set Appropriate Timeouts**: Match timeouts to expected execution time
4. **Minimize Package Size**: Include only necessary dependencies in deployment packages
5. **Use Environment Variables**: Store configuration in environment variables instead of hardcoding
6. **Implement Logging**: Use print() statements or the logging module for diagnostics
7. **Clean Up Resources**: Always delete test functions to avoid unnecessary charges

## Extended Applications

This lab focuses on basic Lambda deployment, but you can extend it to:

1. **API Integration**:
   - Connect Lambda functions to API Gateway for HTTP endpoints
   - Create serverless web services and REST APIs

2. **Event-Driven Processing**:
   - Configure event sources like S3, DynamoDB, or SQS
   - Build event-driven architectures for data processing

3. **Custom Layers**:
   - Create Lambda layers for shared code and dependencies
   - Reduce deployment package sizes with reusable components

4. **Multi-Function Applications**:
   - Deploy multiple functions that work together
   - Implement serverless microservices architectures

## Cleanup Importance

Always remember to clean up Lambda resources after completing labs:

1. Delete Lambda functions you've created
2. Remove IAM roles if they're no longer needed
3. Verify in the AWS Management Console that resources are removed

This prevents unnecessary charges and keeps your AWS account organized. 