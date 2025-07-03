#!/usr/bin/env python3
"""
AWS LAB01 - EC2 Instance Launch Automation

This script demonstrates how to use boto3 to launch an EC2 instance in AWS.
It covers basic EC2 instance creation with tags and waiting for the instance to be running.

Usage:
    python launch_ec2.py
"""

import boto3
import time
from botocore.exceptions import ClientError

# TODO: Initialize the EC2 client with the appropriate region
# ec2_client = 

# Define instance parameters
# TODO: Find and set an appropriate Amazon Linux 2023 AMI ID for eu-west-1
AMI_ID = ''  # Amazon Linux 2023 AMI in eu-west-1
INSTANCE_TYPE = 't2.micro'
KEY_NAME = ''  # TODO: Set your key pair name
SECURITY_GROUP_ID = ''  # TODO: Set your security group ID

# TODO: Define tags to identify your instance
INSTANCE_TAGS = [
    # Add appropriate tags here
]

def launch_instance():
    """
    Launch an EC2 instance with defined parameters
    
    Returns:
        str: The ID of the created EC2 instance
    """
    try:
        # TODO: Create a new EC2 instance using run_instances
        # Parameters should include:
        # - ImageId
        # - InstanceType
        # - KeyName
        # - SecurityGroupIds
        # - MinCount/MaxCount
        # - TagSpecifications
        
        # Example structure (you need to complete it):
        # response = ec2_client.run_instances(
        #     ImageId=AMI_ID,
        #     ...
        # )
        
        # TODO: Extract and return the instance ID from the response
        instance_id = None
        print(f"Launched EC2 instance: {instance_id}")
        
        return instance_id
    except ClientError as e:
        print(f"Error launching EC2 instance: {e}")
        return None

def wait_for_instance(instance_id):
    """
    Wait for the instance to be in a running state
    
    Args:
        instance_id (str): EC2 instance ID
        
    Returns:
        dict: Instance details if successful, None otherwise
    """
    try:
        print("Waiting for instance to start running...")
        
        # TODO: Implement a polling mechanism to check instance state
        # Use describe_instances to get the current state
        # Wait until the state is 'running'
        # Return the instance details once running
        
        # Example structure (you need to complete it):
        # while True:
        #     response = ec2_client.describe_instances(InstanceIds=[instance_id])
        #     instance = response['Reservations'][0]['Instances'][0]
        #     instance_state = instance['State']['Name']
        #     
        #     if instance_state == 'running':
        #         ...
            
        return None  # TODO: Return the instance details
            
    except ClientError as e:
        print(f"Error waiting for instance: {e}")
        return None

def display_instance_details(instance):
    """
    Print useful details about the instance
    
    Args:
        instance (dict): EC2 instance details from describe_instances
    """
    # TODO: Print instance details including:
    # - Instance ID
    # - Instance State
    # - Instance Type
    # - AMI ID
    # - Public DNS
    # - Public IP
    # - Private IP
    # - Tags
    
    # Example (you need to complete it):
    # print("\nInstance Details:")
    # print(f"  Instance ID: {instance['InstanceId']}")
    # ...
    pass

def terminate_instance(instance_id):
    """
    Terminate an EC2 instance
    
    Args:
        instance_id (str): EC2 instance ID
    """
    try:
        # TODO: Implement instance termination
        # Use terminate_instances to terminate the instance
        # Wait for the instance to be terminated
        
        # Example structure (you need to complete it):
        # ec2_client.terminate_instances(InstanceIds=[instance_id])
        # print(f"\nTerminating instance: {instance_id}")
        
        return False  # TODO: Return True if terminated successfully
            
    except ClientError as e:
        print(f"Error terminating instance: {e}")
        return False

if __name__ == "__main__":
    print("AWS EC2 Instance Launch Tool")
    print("===========================")
    
    # TODO: Launch a new EC2 instance
    # instance_id = launch_instance()
    
    # TODO: Wait for the instance to be running
    # TODO: Display instance details
    # TODO: Print SSH connection command if public DNS is available
    
    print("\n⚠️  IMPORTANT: Remember to terminate this instance when done to avoid charges!")
    print("To terminate the instance, implement and call the terminate_instance function.")
    
    # TODO: Uncomment and implement to terminate the instance automatically
    # terminate_instance(instance_id)