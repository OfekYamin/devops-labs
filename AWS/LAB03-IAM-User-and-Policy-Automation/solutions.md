# LAB03 - IAM User and Policy Automation: Solutions

This document contains the complete solution for the IAM User and Policy Automation lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for create_iam_user.py

```python
#!/usr/bin/env python3
"""
AWS LAB03 - IAM User and Policy Automation

This script demonstrates how to automate IAM operations using boto3, including:
- Creating and managing IAM users
- Creating and attaching IAM policies
- Generating and managing access keys
- Creating and assigning roles

Usage:
    python create_iam_user.py --username <username> [--policy <policy_name>] [--cleanup]
"""

import boto3
import argparse
import json
import datetime
import sys
import time
from botocore.exceptions import ClientError

# Default configuration
DEFAULT_REGION = 'eu-west-1'
DEFAULT_PASSWORD_POLICY = {
    'MinimumPasswordLength': 12,
    'RequireSymbols': True,
    'RequireNumbers': True,
    'RequireUppercaseCharacters': True,
    'RequireLowercaseCharacters': True,
    'AllowUsersToChangePassword': True,
    'MaxPasswordAge': 90
}

def create_iam_user(username):
    """
    Create an IAM user
    
    Args:
        username (str): Name of the IAM user to create
        
    Returns:
        dict: User info if created successfully, None on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Create the IAM user
        response = iam_client.create_user(
            UserName=username,
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': 'Dev'
                },
                {
                    'Key': 'Project',
                    'Value': 'DevOps-Lab'
                }
            ]
        )
        
        print(f"Created IAM user: {username}")
        
        return response['User']
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"User {username} already exists.")
            return get_user(username)
        else:
            print(f"Error creating IAM user: {e}")
            return None

def get_user(username):
    """
    Get information about an IAM user
    
    Args:
        username (str): Name of the IAM user
        
    Returns:
        dict: User info if found, None if not found
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Get the user
        response = iam_client.get_user(UserName=username)
        
        return response['User']
    except ClientError as e:
        print(f"Error getting IAM user: {e}")
        return None

def generate_access_key(username):
    """
    Generate access key for an IAM user
    
    Args:
        username (str): Name of the IAM user
        
    Returns:
        dict: Access key details, None on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Create access key
        response = iam_client.create_access_key(UserName=username)
        
        access_key = response['AccessKey']
        
        print(f"\nAccess key created for user {username}:")
        print(f"Access Key ID: {access_key['AccessKeyId']}")
        print(f"Secret Access Key: {access_key['SecretAccessKey']}")
        print("\n⚠️  IMPORTANT: This is the only time the secret will be available!")
        print("Make sure to save these credentials in a secure location.\n")
        
        return access_key
    except ClientError as e:
        print(f"Error creating access key: {e}")
        return None

def list_access_keys(username):
    """
    List all access keys for an IAM user
    
    Args:
        username (str): Name of the IAM user
        
    Returns:
        list: List of access key metadata
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # List access keys
        response = iam_client.list_access_keys(UserName=username)
        
        access_keys = response.get('AccessKeyMetadata', [])
        
        if access_keys:
            print(f"\nAccess keys for user {username}:")
            for key in access_keys:
                creation_date = key['CreateDate'].strftime("%Y-%m-%d %H:%M:%S")
                print(f"- Access Key ID: {key['AccessKeyId']}")
                print(f"  Status: {key['Status']}")
                print(f"  Created: {creation_date}")
        else:
            print(f"No access keys found for user {username}")
        
        return access_keys
    except ClientError as e:
        print(f"Error listing access keys: {e}")
        return []

def delete_access_key(username, access_key_id):
    """
    Delete an access key for an IAM user
    
    Args:
        username (str): Name of the IAM user
        access_key_id (str): Access Key ID to delete
        
    Returns:
        bool: True if deleted successfully, False on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Delete the access key
        iam_client.delete_access_key(
            UserName=username,
            AccessKeyId=access_key_id
        )
        
        print(f"Deleted access key {access_key_id} for user {username}")
        
        return True
    except ClientError as e:
        print(f"Error deleting access key: {e}")
        return False

def create_policy(policy_name, policy_document):
    """
    Create an IAM policy
    
    Args:
        policy_name (str): Name of the policy
        policy_document (dict): Policy document in JSON format
        
    Returns:
        str: Policy ARN if created successfully, None on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Create the policy
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document),
            Description=f"Custom policy created for DevOps Lab: {policy_name}",
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': 'Dev'
                },
                {
                    'Key': 'Project',
                    'Value': 'DevOps-Lab'
                }
            ]
        )
        
        policy_arn = response['Policy']['Arn']
        print(f"Created policy: {policy_name} with ARN: {policy_arn}")
        
        return policy_arn
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            # Get the ARN for the existing policy
            print(f"Policy {policy_name} already exists.")
            account_id = boto3.client('sts').get_caller_identity().get('Account')
            return f"arn:aws:iam::{account_id}:policy/{policy_name}"
        else:
            print(f"Error creating policy: {e}")
            return None

def attach_policy_to_user(username, policy_arn):
    """
    Attach an IAM policy to a user
    
    Args:
        username (str): Name of the IAM user
        policy_arn (str): ARN of the policy to attach
        
    Returns:
        bool: True if attached successfully, False on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Attach policy to user
        iam_client.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        
        print(f"Attached policy {policy_arn} to user {username}")
        
        return True
    except ClientError as e:
        print(f"Error attaching policy to user: {e}")
        return False

def list_user_policies(username):
    """
    List all policies attached to an IAM user
    
    Args:
        username (str): Name of the IAM user
        
    Returns:
        list: List of policy ARNs attached to the user
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # List attached policies
        response = iam_client.list_attached_user_policies(UserName=username)
        
        attached_policies = response.get('AttachedPolicies', [])
        
        if attached_policies:
            print(f"\nPolicies attached to user {username}:")
            for policy in attached_policies:
                print(f"- {policy['PolicyName']} ({policy['PolicyArn']})")
        else:
            print(f"No policies attached to user {username}")
        
        return attached_policies
    except ClientError as e:
        print(f"Error listing policies: {e}")
        return []

def detach_user_policies(username):
    """
    Detach all policies from an IAM user
    
    Args:
        username (str): Name of the IAM user
        
    Returns:
        bool: True if all policies detached successfully, False on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # List attached policies
        response = iam_client.list_attached_user_policies(UserName=username)
        
        # Detach each policy
        for policy in response.get('AttachedPolicies', []):
            iam_client.detach_user_policy(
                UserName=username,
                PolicyArn=policy['PolicyArn']
            )
            
            print(f"Detached policy {policy['PolicyName']} from user {username}")
        
        return True
    except ClientError as e:
        print(f"Error detaching policies: {e}")
        return False

def delete_user(username):
    """
    Delete an IAM user
    
    Args:
        username (str): Name of the IAM user to delete
        
    Returns:
        bool: True if deleted successfully, False on error
    """
    try:
        # Initialize the IAM client
        iam_client = boto3.client('iam')
        
        # Delete access keys
        access_keys = list_access_keys(username)
        for key in access_keys:
            delete_access_key(username, key['AccessKeyId'])
        
        # Detach policies
        detach_user_policies(username)
        
        # Delete the user
        iam_client.delete_user(UserName=username)
        
        print(f"Deleted IAM user: {username}")
        
        return True
    except ClientError as e:
        print(f"Error deleting IAM user: {e}")
        return False

def main():
    """Main function to execute the script"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='IAM User and Policy Automation')
    parser.add_argument('--username', required=True, help='Name of the IAM user to create')
    parser.add_argument('--policy', default='ReadOnlyAccess', help='Name of policy to attach (default: ReadOnlyAccess)')
    parser.add_argument('--custom', action='store_true', help='Create a custom policy instead of using AWS managed policy')
    parser.add_argument('--cleanup', action='store_true', help='Delete the user after creation')
    
    args = parser.parse_args()
    
    print("AWS IAM User and Policy Automation Tool")
    print("======================================")
    
    # Create IAM user
    user = create_iam_user(args.username)
    
    if user:
        # Generate access key
        access_key = generate_access_key(args.username)
        
        # List all access keys for the user
        list_access_keys(args.username)
        
        # Attach policy to user
        if args.custom:
            # Sample custom policy for S3 read-only access
            s3_readonly_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": [
                            "s3:Get*",
                            "s3:List*",
                            "s3-object-lambda:Get*",
                            "s3-object-lambda:List*"
                        ],
                        "Resource": "*"
                    }
                ]
            }
            
            # Create custom policy
            policy_arn = create_policy(f"Custom-{args.policy}", s3_readonly_policy)
        else:
            # Use AWS managed policy
            account_id = boto3.client('sts').get_caller_identity().get('Account')
            if args.policy.startswith('arn:aws:iam::'):
                policy_arn = args.policy
            elif ':policy/' in args.policy:
                policy_arn = args.policy
            else:
                policy_arn = f"arn:aws:iam::aws:policy/{args.policy}"
                print(f"Using AWS managed policy: {policy_arn}")
        
        # Attach policy to user
        if policy_arn:
            attach_policy_to_user(args.username, policy_arn)
        
        # List policies attached to the user
        list_user_policies(args.username)
        
        print(f"\nIAM user {args.username} has been successfully set up!")
        
        if args.cleanup:
            print("\nCleaning up resources...")
            # Wait a moment for AWS to propagate changes
            time.sleep(2)
            delete_user(args.username)
        else:
            print(f"\n⚠️  IMPORTANT: Resources have been created in your AWS account.")
            print(f"To clean up, run this script again with the --cleanup flag.")
    
if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **IAM User Management**:
   - Creating users programmatically through the API
   - Managing user attributes and tags
   - Properly cleaning up users to avoid orphaned resources

2. **Access Key Management**:
   - Creating access keys for programmatic access
   - Listing and managing existing keys
   - Understanding security implications of access key creation and storage

3. **IAM Policy Operations**:
   - Working with both AWS managed policies and custom policies
   - Creating policy documents using JSON
   - Attaching and detaching policies from users

4. **Boto3 IAM API Usage**:
   - Understanding the IAM client API structure
   - Handling common error cases like entity already exists
   - Properly referencing ARNs for AWS resources

5. **Security Best Practices**:
   - Providing warnings about credentials security
   - Implementing cleanup procedures to remove unused resources
   - Using least privilege principles when assigning permissions

## Common Issues and Troubleshooting

1. **Permission Issues**:
   - "Access Denied" errors when your IAM user lacks IAM permissions
   - Solution: Ensure your user has the IAM:* permissions or use AdministratorAccess policy

2. **Policy Attachment Failures**:
   - Failures when attaching non-existent policies or incorrect ARNs
   - Solution: Verify policy ARNs before attachment, especially for custom policies

3. **Access Key Limitations**:
   - Users have a maximum of two access keys
   - Solution: List existing keys and delete unused ones before creating new keys

4. **Policy Document Format**:
   - JSON syntax errors in custom policy documents
   - Solution: Validate JSON format before submitting and use the Policy Validator in AWS console

5. **IAM Resource Naming**:
   - Path prefixes and naming limitations for IAM resources
   - Solution: Follow AWS naming conventions and avoid special characters 
