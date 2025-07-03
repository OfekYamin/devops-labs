# LAB01 - EC2 Automation: Solutions

This document contains the complete solution for the EC2 Instance Launch Automation lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for launch_ec2.py

```python
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

# Initialize the EC2 client with specified region
ec2_client = boto3.client('ec2', region_name='eu-west-1')

# Define instance parameters
AMI_ID = 'ami-0fe0b2cf0e1f25c8a'  # Amazon Linux 2023 AMI in eu-west-1
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'devops-key'  # Replace with your key pair name
SECURITY_GROUP_ID = 'sg-xxxxxxxxxxxx'  # Replace with your security group ID

# Tags to identify your instance
INSTANCE_TAGS = [
    {
        'Key': 'Name',
        'Value': 'DevOps-Lab-Instance'
    },
    {
        'Key': 'Environment',
        'Value': 'Training'
    },
    {
        'Key': 'Project',
        'Value': 'AWS-Automation'
    }
]

def launch_instance():
    """
    Launch an EC2 instance with defined parameters
    
    Returns:
        str: The ID of the created EC2 instance
    """
    try:
        # Create a new EC2 instance
        response = ec2_client.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            SecurityGroupIds=[SECURITY_GROUP_ID] if SECURITY_GROUP_ID else None,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': INSTANCE_TAGS
                }
            ]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
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
        
        # Using a custom polling mechanism instead of waiters
        while True:
            response = ec2_client.describe_instances(InstanceIds=[instance_id])
            instance = response['Reservations'][0]['Instances'][0]
            instance_state = instance['State']['Name']
            
            if instance_state == 'running':
                print("Instance is now running!")
                return instance
            
            if instance_state in ['terminated', 'shutting-down']:
                print(f"Instance entered {instance_state} state unexpectedly.")
                return None
                
            print(f"Current state: {instance_state}. Waiting...")
            time.sleep(5)  # Wait for 5 seconds before checking again
            
    except ClientError as e:
        print(f"Error waiting for instance: {e}")
        return None

def display_instance_details(instance):
    """
    Print useful details about the instance
    
    Args:
        instance (dict): EC2 instance details from describe_instances
    """
    print("\nInstance Details:")
    print(f"  Instance ID: {instance['InstanceId']}")
    print(f"  Instance State: {instance['State']['Name']}")
    print(f"  Instance Type: {instance['InstanceType']}")
    print(f"  AMI ID: {instance['ImageId']}")
    
    # Some attributes may not exist in all instances
    public_dns = instance.get('PublicDnsName', 'N/A')
    public_ip = instance.get('PublicIpAddress', 'N/A')
    private_ip = instance.get('PrivateIpAddress', 'N/A')
    
    print(f"  Public DNS: {public_dns}")
    print(f"  Public IP: {public_ip}")
    print(f"  Private IP: {private_ip}")
    
    # Print the instance tags
    if 'Tags' in instance:
        print("\nInstance Tags:")
        for tag in instance['Tags']:
            print(f"  {tag['Key']}: {tag['Value']}")

def terminate_instance(instance_id):
    """
    Terminate an EC2 instance
    
    Args:
        instance_id (str): EC2 instance ID
    """
    try:
        # Terminate the instance
        ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(f"\nTerminating instance: {instance_id}")
        print("Waiting for instance to terminate...")
        
        # Poll until instance is terminated
        while True:
            response = ec2_client.describe_instances(InstanceIds=[instance_id])
            instance = response['Reservations'][0]['Instances'][0]
            instance_state = instance['State']['Name']
            
            if instance_state == 'terminated':
                print("Instance terminated successfully.")
                return True
                
            if instance_state in ['shutting-down', 'terminated']:
                print(f"Instance state: {instance_state}")
            else:
                print(f"Unexpected instance state: {instance_state}")
                
            time.sleep(5)  # Wait for 5 seconds before checking again
            
    except ClientError as e:
        print(f"Error terminating instance: {e}")
        return False

if __name__ == "__main__":
    print("AWS EC2 Instance Launch Tool")
    print("===========================")
    
    # Launch a new EC2 instance
    instance_id = launch_instance()
    
    if instance_id:
        # Wait for the instance to be running
        instance = wait_for_instance(instance_id)
        
        if instance:
            # Display instance details
            display_instance_details(instance)
            
            # Provide SSH connection command if the instance has a public DNS
            public_dns = instance.get('PublicDnsName')
            if public_dns:
                print(f"\nTo connect to your instance via SSH:")
                print(f"ssh -i /path/to/{KEY_NAME}.pem ec2-user@{public_dns}")
        
        # Warning about charges
        print("\n⚠️  IMPORTANT: Remember to terminate this instance when done to avoid charges!")
        print("To terminate the instance, uncomment the terminate_instance call below or use the AWS console.")
        
        # Uncomment the line below to terminate the instance automatically
        # terminate_instance(instance_id)
```

## Key Learning Points

1. **AWS SDK Setup**:
   - Using boto3 to interact with AWS services
   - Initializing an EC2 client with a specific region

2. **EC2 Instance Creation**:
   - Using the run_instances API to launch EC2 instances
   - Configuring instance parameters: AMI ID, instance type, key pair, etc.
   - Adding tags for resource identification and organization
   - Using security groups to control network access

3. **Resource Monitoring**:
   - Using describe_instances to check instance status
   - Implementing custom polling mechanisms to wait for state changes
   - Extracting instance information from API responses

4. **Error Handling**:
   - Implementing try/except blocks to handle AWS API errors
   - Using ClientError from botocore.exceptions

5. **Resource Management**:
   - Creating helpful utility functions for common operations
   - Using terminate_instances to properly clean up resources
   - Checking termination status to confirm cleanup

## Common Issues and Troubleshooting

1. **Missing Credentials**:
   - Error when AWS credentials are not configured
   - Solution: Set up AWS CLI with `aws configure` or use environment variables

2. **Permission Issues**:
   - Error when your IAM user lacks EC2 permissions
   - Solution: Attach appropriate policies to your IAM user or role

3. **Resource Availability**:
   - Error when instance type is not available in the selected region
   - Solution: Choose a different instance type or region

4. **Key Pair Access**:
   - Unable to connect to instance if key pair is not specified correctly
   - Solution: Ensure you have the private key file (.pem) for the specified key pair

5. **Security Group Configuration**:
   - Unable to connect to instance if security group doesn't allow SSH access
   - Solution: Update security group to allow inbound traffic on port 22

6. **API Rate Limiting**:
   - Consider adding retry logic or backoff mechanisms for API calls
   - Solution: Implement exponential backoff for API polling 