#!/usr/bin/env python3
"""
AWS LAB06 - CloudFormation Stack Launch

This script demonstrates how to use boto3 to deploy infrastructure using AWS CloudFormation.
It reads a YAML template file and deploys resources defined in it as a CloudFormation stack.

Usage:
    python launch_stack.py
"""

# TODO: Import necessary libraries
# import boto3
# import time
# import sys
# from botocore.exceptions import ClientError


# TODO: Configure stack parameters
# stack_name = 'DevOpsEC2Stack'
# template_file = 'ec2_template.yaml'
# region = 'eu-west-1'  # Default to Ireland region


# TODO: Function to read the CloudFormation template file
# def read_template(template_file):
#     """Read CloudFormation template from file"""
#     try:
#         with open(template_file, 'r') as file:
#             template_body = file.read()
#         return template_body
#     except FileNotFoundError:
#         print(f"Error: Template file '{template_file}' not found.")
#         sys.exit(1)


# TODO: Function to create a CloudFormation stack
# def create_stack(cf_client, stack_name, template_body):
#     """Create a new CloudFormation stack"""


# TODO: Function to check stack status
# def check_stack_status(cf_client, stack_name):
#     """Check and return current status of stack"""


# TODO: Function to wait for stack completion
# def wait_for_stack_completion(cf_client, stack_name):
#     """Wait for stack to reach a completion state (CREATE_COMPLETE or CREATE_FAILED)"""


# TODO: Function to delete a CloudFormation stack
# def delete_stack(cf_client, stack_name):
#     """Delete a CloudFormation stack"""


# TODO: Error handling function
# def handle_error(e, operation):
#     """Handle boto3 errors with detailed output"""


if __name__ == "__main__":
    print("AWS CloudFormation Stack Deployment Tool")
    print("======================================")
    
    # TODO: Implement your CloudFormation workflow here
    # Example outline:
    # 1. Initialize CloudFormation client
    # 2. Read CloudFormation template
    # 3. Create stack
    # 4. Wait for and report status
    
    # Example implementation
    # try:
    #     # Initialize CloudFormation client
    #     print(f"\nConnecting to AWS CloudFormation in region {region}...")
    #     cf_client = boto3.client('cloudformation', region_name=region)
    #     
    #     # Read template
    #     print(f"\nReading CloudFormation template from {template_file}...")
    #     template_body = read_template(template_file)
    #     
    #     # Create stack
    #     print(f"\nDeploying CloudFormation stack '{stack_name}'...")
    #     stack_id = create_stack(cf_client, stack_name, template_body)
    #     print(f"Stack ID: {stack_id}")
    #     
    #     # Wait for stack completion
    #     print(f"\nWaiting for stack creation to complete...")
    #     wait_for_stack_completion(cf_client, stack_name)
    #     
    # except Exception as e:
    #     print(f"\nError: {str(e)}")
    
    print("\n⚠️  IMPORTANT: Remember to delete the stack when you're done to avoid charges!")
    print("To delete the stack, run:")
    print("python launch_stack.py --delete")
    print("Or programmatically: cf_client.delete_stack(StackName='DevOpsEC2Stack')")

"""
Sample output:

AWS CloudFormation Stack Deployment Tool
======================================

Connecting to AWS CloudFormation in region us-east-1...

Reading CloudFormation template from ec2_template.yaml...
Template validated successfully!

Deploying CloudFormation stack 'DevOpsEC2Stack'...
Stack ID: arn:aws:cloudformation:us-east-1:123456789012:stack/DevOpsEC2Stack/abc123

Waiting for stack creation to complete...
Stack status: CREATE_IN_PROGRESS
Stack status: CREATE_IN_PROGRESS
Stack status: CREATE_COMPLETE

Stack creation completed successfully!
Resources created:
- EC2 Instance ID: i-0abc123def456789

⚠️  IMPORTANT: Remember to delete the stack when you're done to avoid charges!
To delete the stack, run:
python launch_stack.py --delete
Or programmatically: cf_client.delete_stack(StackName='DevOpsEC2Stack')
""" 