# LAB06 - CloudFormation Stack Launch: Solutions

This document contains the complete solution for the CloudFormation Stack Launch lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for launch_stack.py

```python
#!/usr/bin/env python3
"""
AWS LAB06 - CloudFormation Stack Launch

This script demonstrates how to use boto3 to deploy infrastructure using AWS CloudFormation.
It reads a YAML template file and deploys resources defined in it as a CloudFormation stack.

Usage:
    python launch_stack.py [--delete] [--config CONFIG_FILE]
"""

import boto3
import time
import sys
import os
import argparse
import configparser
from botocore.exceptions import ClientError


def read_template(template_file):
    """Read CloudFormation template from file"""
    try:
        with open(template_file, 'r') as file:
            template_body = file.read()
        return template_body
    except FileNotFoundError:
        print(f"Error: Template file '{template_file}' not found.")
        sys.exit(1)


def read_config(config_file):
    """Read configuration from ini file"""
    if not os.path.exists(config_file):
        print(f"Error: Configuration file '{config_file}' not found.")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def create_stack(cf_client, stack_name, template_body, parameters=None):
    """Create a new CloudFormation stack"""
    try:
        params = {
            'StackName': stack_name,
            'TemplateBody': template_body,
            'OnFailure': 'ROLLBACK'  # Rollback on failure
        }
        
        # Add parameters if provided
        if parameters:
            params['Parameters'] = parameters
            
        response = cf_client.create_stack(**params)
        return response['StackId']
    except ClientError as e:
        handle_error(e, "creating stack")
        return None


def delete_stack(cf_client, stack_name):
    """Delete a CloudFormation stack"""
    try:
        cf_client.delete_stack(StackName=stack_name)
        print(f"Stack deletion initiated for: {stack_name}")
        return True
    except ClientError as e:
        handle_error(e, "deleting stack")
        return False


def check_stack_status(cf_client, stack_name):
    """Check and return current status of stack"""
    try:
        response = cf_client.describe_stacks(StackName=stack_name)
        status = response['Stacks'][0]['StackStatus']
        return status
    except ClientError as e:
        if 'does not exist' in str(e):
            return 'STACK_NOT_FOUND'
        handle_error(e, "checking stack status")
        return None


def wait_for_stack_completion(cf_client, stack_name):
    """Wait for stack to reach a completion state (CREATE_COMPLETE or CREATE_FAILED)"""
    print(f"Waiting for stack operation to complete...")
    
    # Terminal states that indicate operation completion
    completed_states = [
        'CREATE_COMPLETE', 'CREATE_FAILED', 'ROLLBACK_COMPLETE', 
        'DELETE_COMPLETE', 'DELETE_FAILED'
    ]
    
    # Wait and check status every 10 seconds
    while True:
        status = check_stack_status(cf_client, stack_name)
        
        if status == 'STACK_NOT_FOUND':
            print("Stack not found. It may have been deleted or not created yet.")
            return False
            
        print(f"Current status: {status}")
        
        if status in completed_states:
            if status == 'CREATE_COMPLETE':
                print(f"Stack operation completed successfully!")
                return True
            elif status == 'DELETE_COMPLETE':
                print(f"Stack deletion completed successfully!")
                return True
            else:
                print(f"Stack operation ended with status: {status}")
                # Print error information
                print_stack_events(cf_client, stack_name)
                return False
                
        # Wait before checking again
        time.sleep(10)


def print_stack_events(cf_client, stack_name, limit=5):
    """Print the most recent stack events, especially errors"""
    try:
        print("\nRecent stack events:")
        response = cf_client.describe_stack_events(StackName=stack_name)
        
        # Get the most recent events
        events = response['StackEvents'][:limit]
        
        for event in events:
            status = event['ResourceStatus']
            resource_id = event['LogicalResourceId']
            timestamp = event['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            
            # Include reason for failures
            if 'FAILED' in status:
                reason = event.get('ResourceStatusReason', 'No reason provided')
                print(f"{timestamp} - {resource_id} - {status} - Reason: {reason}")
            else:
                print(f"{timestamp} - {resource_id} - {status}")
                
    except ClientError as e:
        print(f"Error retrieving stack events: {str(e)}")


def print_stack_outputs(cf_client, stack_name):
    """Print the outputs from a CloudFormation stack"""
    try:
        response = cf_client.describe_stacks(StackName=stack_name)
        outputs = response['Stacks'][0].get('Outputs', [])
        
        if outputs:
            print("\nStack Outputs:")
            for output in outputs:
                print(f"  {output['OutputKey']}: {output['OutputValue']}")
                if 'Description' in output:
                    print(f"    Description: {output['Description']}")
        else:
            print("Stack has no outputs defined.")
            
    except ClientError as e:
        print(f"Error retrieving stack outputs: {str(e)}")


def get_parameters_from_config(config):
    """Convert parameters from config to CloudFormation format"""
    parameters = []
    
    if 'Parameters' in config:
        for key, value in config['Parameters'].items():
            parameters.append({
                'ParameterKey': key,
                'ParameterValue': value
            })
            
    return parameters


def handle_error(e, operation):
    """Handle boto3 errors with detailed output"""
    print(f"Error while {operation}: {str(e)}")
    
    # Extract specific error details if available
    if hasattr(e, 'response') and 'Error' in e.response:
        error = e.response['Error']
        print(f"Error code: {error.get('Code', 'Unknown')}")
        print(f"Error message: {error.get('Message', 'No message')}")


def main():
    """Main function to parse arguments and execute CloudFormation operations"""
    parser = argparse.ArgumentParser(description='AWS CloudFormation Stack Deployment Tool')
    parser.add_argument('--delete', action='store_true', help='Delete the CloudFormation stack')
    parser.add_argument('--config', default='config.ini', help='Path to config file (default: config.ini)')
    args = parser.parse_args()
    
    print("AWS CloudFormation Stack Deployment Tool")
    print("======================================")
    
    # Read configuration
    config = read_config(args.config)
    
    # Extract configuration values
    region = config['AWS']['region']
    stack_name = config['Stack']['name']
    template_file = config['Stack']['template_path']
    
    # Initialize CloudFormation client
    print(f"\nConnecting to AWS CloudFormation in region {region}...")
    cf_client = boto3.client('cloudformation', region_name=region)
    
    if args.delete:
        # Delete the stack
        print(f"\nDeleting CloudFormation stack '{stack_name}'...")
        if delete_stack(cf_client, stack_name):
            wait_for_stack_completion(cf_client, stack_name)
    else:
        # Read template
        print(f"\nReading CloudFormation template from {template_file}...")
        template_body = read_template(template_file)
        
        # Convert parameters from config
        parameters = get_parameters_from_config(config)
        
        # Validate template
        try:
            cf_client.validate_template(TemplateBody=template_body)
            print("Template validated successfully!")
        except ClientError as e:
            handle_error(e, "validating template")
            sys.exit(1)
        
        # Create stack
        print(f"\nDeploying CloudFormation stack '{stack_name}'...")
        stack_id = create_stack(cf_client, stack_name, template_body, parameters)
        
        if stack_id:
            print(f"Stack ID: {stack_id}")
            
            # Wait for stack completion
            if wait_for_stack_completion(cf_client, stack_name):
                # Print stack outputs
                print_stack_outputs(cf_client, stack_name)
    
    # Cleanup instructions
    if not args.delete:
        print("\n⚠️  IMPORTANT: Remember to delete the stack when you're done to avoid charges!")
        print(f"To delete the stack, run: python launch_stack.py --delete")


if __name__ == "__main__":
    main()
```

## Understanding CloudFormation Parameters

The script uses the `ec2_template.yaml` file which defines the CloudFormation template for an EC2 instance with its security group. The template accepts the following parameters:

1. `InstanceType`: Type of EC2 instance (t2.micro, t2.small, etc.)
2. `KeyName`: Name of an existing EC2 key pair for SSH access
3. `SubnetID`: The subnet ID where the EC2 instance will be launched
4. `VpcID`: The VPC ID where resources will be created
5. `SSHLocation`: IP address range that can SSH to the EC2 instance

These parameters are defined in the `config.ini` file which provides a clean separation of configuration from code.

## Key Learning Points

1. **Infrastructure as Code (IaC)**:
   - How to define AWS resources using CloudFormation templates
   - Understanding the YAML format for declaring resources
   - Mapping regions to AMI IDs for portability

2. **CloudFormation Stack Management**:
   - Creating stacks from templates using boto3
   - Monitoring stack creation progress
   - Handling stack updates and deletions
   - Working with stack outputs

3. **Configuration Handling**:
   - Using .ini files for configuration
   - Separating environment-specific parameters from code
   - Converting configuration into CloudFormation parameters

4. **Error Handling and Status Monitoring**:
   - Implementing wait logic for asynchronous operations
   - Handling various stack states
   - Retrieving and displaying stack events on failure

5. **Resource Cleanup**:
   - Properly deleting CloudFormation stacks
   - Understanding the importance of cleanup to avoid charges

## Common Issues and Troubleshooting

1. **Invalid Template Errors**:
   - YAML syntax errors in the template
   - Solution: Validate the template before deployment using the validate_template API call

2. **Parameter Validation Failures**:
   - Using incorrect formats for parameter values (like CIDR ranges)
   - Solution: Check parameter constraints and ensure values match required formats

3. **Resource Creation Failures**:
   - Insufficient permissions to create resources
   - Resources that can't be created due to service limits
   - Solution: Review stack events to identify specific failure reasons

4. **VPC and Subnet Configuration**:
   - Using placeholder values instead of actual AWS resource IDs
   - Solution: Update the config.ini file with real VPC/Subnet IDs before deployment

5. **Stack Deletion Issues**:
   - Resources that are protected from deletion or have termination protection
   - Solution: Disable termination protection and dependencies before deletion

## Best Practices

1. **Template Validation**: Always validate CloudFormation templates before deployment
2. **Parameter Type Checking**: Use parameter types and constraints to validate input
3. **Resource Tagging**: Tag all resources for better organization and cost tracking
4. **Capability Acknowledgment**: Explicitly acknowledge capabilities like IAM resource creation
5. **Output Variables**: Use outputs to expose important resource information
6. **Wait for Completion**: Implement proper waiter logic for asynchronous operations
7. **Error Handling**: Provide clear error messages and handle exceptions gracefully
8. **Resource Cleanup**: Always include cleanup procedures in automation scripts

## Extended Applications

This lab focuses on basic CloudFormation deployment, but the same principles apply to:

1. **Multi-Resource Stacks**:
   - Deploying multiple related resources in a single stack
   - Creating complete application environments with databases, load balancers, etc.

2. **Nested Stacks**:
   - Building modular templates that reference other templates
   - Creating reusable infrastructure components

3. **Change Sets**:
   - Previewing changes before applying them
   - Understanding the impact of template modifications

4. **Cross-Stack References**:
   - Exporting values from one stack for use in another
   - Building layered infrastructure with dependencies

## Cleanup Importance

Always remember to delete CloudFormation stacks after completing labs:

1. AWS resources like EC2 instances will continue to incur charges until explicitly deleted
2. CloudFormation makes cleanup easy by deleting all resources in the stack
3. You can use the `--delete` flag with the deployment script to remove the stack:
   ```bash
   python launch_stack.py --delete
   ```

## Advanced Stack Management Concepts

For more advanced CloudFormation usage (demonstrated in the `deploy_stack.py` reference implementation):

1. **Stack Updates**: Updating existing stacks with modified templates
2. **Custom Resources**: Extending CloudFormation with custom resources via Lambda
3. **Dynamic References**: Using SSM Parameter Store or Secrets Manager references
4. **Drift Detection**: Identifying when resources have changed outside of CloudFormation
5. **Stack Policies**: Protecting resources from unintended updates 