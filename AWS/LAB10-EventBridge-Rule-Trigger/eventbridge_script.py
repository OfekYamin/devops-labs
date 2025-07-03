#!/usr/bin/env python3
"""
AWS EventBridge Rule and Trigger Automation Script
This script is part of LAB10 for AWS DevOps Python Course.

It demonstrates how to automate Amazon EventBridge operations using boto3.
Students should implement the TODO sections to complete the lab.
"""

import argparse
import boto3
import json
import sys
import time
from botocore.exceptions import ClientError

def create_rule(rule_name, schedule=None, event_pattern=None, state='ENABLED', description=None, region='eu-west-1'):
    """
    Create an EventBridge rule with schedule or event pattern
    
    TODO: Implement this function to create an EventBridge rule.
    1. Create a boto3 client for EventBridge in the specified region
    2. Use the put_rule method to create a new rule
    3. Handle either schedule expression or event pattern (one must be provided)
    4. Return the rule ARN
    
    Parameters:
        rule_name (str): Name of the EventBridge rule to create
        schedule (str, optional): Schedule expression (rate or cron)
        event_pattern (dict, optional): Event pattern as JSON object
        state (str): 'ENABLED' or 'DISABLED'
        description (str, optional): Description of the rule
        region (str): AWS region
        
    Returns:
        str: ARN of the created rule
    """
    print(f"Creating EventBridge rule: {rule_name} in region {region}")
    
    if not schedule and not event_pattern:
        print("Error: Either schedule or event_pattern must be provided")
        sys.exit(1)
    
    try:
        # TODO: Create a boto3 client for EventBridge
        
        # TODO: Prepare parameters for put_rule call
        params = {
            'Name': rule_name,
            'State': state
        }
        
        # TODO: Add schedule expression if provided
        
        # TODO: Add event pattern if provided
        
        # TODO: Add description if provided
        
        # TODO: Call put_rule method and return rule ARN
        return None
    except Exception as e:
        print(f"Error creating EventBridge rule: {e}")
        sys.exit(1)

def add_lambda_target(rule_name, function_name, input_json=None, region='eu-west-1'):
    """
    Add a Lambda function as a target for an EventBridge rule
    
    TODO: Implement this function to add a Lambda target.
    1. Create boto3 clients for EventBridge and Lambda
    2. Get the Lambda function ARN using the function name
    3. Use put_targets to set the Lambda function as a target
    4. Add necessary permissions for EventBridge to invoke Lambda
    5. Return the target ID
    
    Parameters:
        rule_name (str): Name of the EventBridge rule
        function_name (str): Name of the Lambda function
        input_json (dict, optional): Custom input to pass to the Lambda function
        region (str): AWS region
        
    Returns:
        str: ID of the target
    """
    print(f"Adding Lambda target '{function_name}' to rule: {rule_name}")
    
    try:
        # TODO: Create boto3 clients for EventBridge and Lambda
        
        # TODO: Get the Lambda function ARN
        
        # TODO: Generate a unique target ID
        target_id = '1'  # You can use a UUID here for uniqueness
        
        # TODO: Prepare parameters for put_targets call
        
        # TODO: Call put_targets method
        
        # TODO: Add permission for EventBridge to invoke Lambda
        
        print(f"Lambda target '{function_name}' added to rule: {rule_name}")
        return target_id
    except Exception as e:
        print(f"Error adding Lambda target to rule: {e}")
        return None

def add_sns_target(rule_name, topic_arn, input_json=None, region='eu-west-1'):
    """
    Add an SNS topic as a target for an EventBridge rule
    
    TODO: Implement this function to add an SNS target.
    1. Create a boto3 client for EventBridge
    2. Use put_targets to set the SNS topic as a target
    3. Return the target ID
    
    Parameters:
        rule_name (str): Name of the EventBridge rule
        topic_arn (str): ARN of the SNS topic
        input_json (dict, optional): Custom input to pass to the SNS topic
        region (str): AWS region
        
    Returns:
        str: ID of the target
    """
    print(f"Adding SNS target '{topic_arn}' to rule: {rule_name}")
    
    try:
        # TODO: Create a boto3 client for EventBridge
        
        # TODO: Generate a unique target ID
        target_id = '1'  # You can use a UUID here for uniqueness
        
        # TODO: Prepare parameters for put_targets call
        
        # TODO: Call put_targets method
        
        print(f"SNS target added to rule: {rule_name}")
        return target_id
    except Exception as e:
        print(f"Error adding SNS target to rule: {e}")
        return None

def list_rules(name_prefix=None, region='eu-west-1'):
    """
    List EventBridge rules, optionally filtered by prefix
    
    TODO: Implement this function to list EventBridge rules.
    1. Create a boto3 client for EventBridge
    2. Use list_rules method to get rules, with optional prefix filter
    3. Print rule details and return the list of rules
    
    Parameters:
        name_prefix (str, optional): Prefix to filter rule names
        region (str): AWS region
        
    Returns:
        list: List of rule details
    """
    if name_prefix:
        print(f"Listing EventBridge rules with prefix '{name_prefix}' in region {region}")
    else:
        print(f"Listing all EventBridge rules in region {region}")
    
    try:
        # TODO: Create a boto3 client for EventBridge
        
        # TODO: Prepare parameters for list_rules call
        
        # TODO: Call list_rules method
        
        # TODO: Extract and print rule details
        
        return []
    except Exception as e:
        print(f"Error listing EventBridge rules: {e}")
        return []

def list_targets(rule_name, region='eu-west-1'):
    """
    List all targets associated with an EventBridge rule
    
    TODO: Implement this function to list rule targets.
    1. Create a boto3 client for EventBridge
    2. Use list_targets_by_rule method to get targets
    3. Print target details and return the list of targets
    
    Parameters:
        rule_name (str): Name of the EventBridge rule
        region (str): AWS region
        
    Returns:
        list: List of target details
    """
    print(f"Listing targets for rule: {rule_name}")
    
    try:
        # TODO: Create a boto3 client for EventBridge
        
        # TODO: Call list_targets_by_rule method
        
        # TODO: Extract and print target details
        
        return []
    except Exception as e:
        print(f"Error listing targets for rule: {e}")
        return []

def enable_disable_rule(rule_name, enable=True, region='eu-west-1'):
    """
    Enable or disable an EventBridge rule
    
    TODO: Implement this function to toggle rule state.
    1. Create a boto3 client for EventBridge
    2. Use enable_rule or disable_rule method based on the enable parameter
    3. Return success status
    
    Parameters:
        rule_name (str): Name of the EventBridge rule
        enable (bool): True to enable, False to disable
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    state = "ENABLED" if enable else "DISABLED"
    print(f"Setting rule '{rule_name}' to {state}")
    
    try:
        # TODO: Create a boto3 client for EventBridge
        
        # TODO: Call enable_rule or disable_rule method based on the enable parameter
        
        print(f"Rule '{rule_name}' is now {state}")
        return True
    except Exception as e:
        print(f"Error changing rule state: {e}")
        return False

def delete_rule(rule_name, region='eu-west-1'):
    """
    Delete an EventBridge rule and all its targets
    
    TODO: Implement this function to delete a rule.
    1. Create a boto3 client for EventBridge
    2. Get all targets for the rule
    3. Remove all targets using remove_targets
    4. Delete the rule using delete_rule method
    5. Return success status
    
    Parameters:
        rule_name (str): Name of the EventBridge rule to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting rule: {rule_name}")
    
    try:
        # TODO: Create a boto3 client for EventBridge
        
        # TODO: Get targets for the rule
        
        # TODO: Remove all targets if any exist
        
        # TODO: Delete the rule
        
        print(f"Rule '{rule_name}' deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting rule: {e}")
        return False

def main():
    """Main function to parse arguments and execute EventBridge operations"""
    parser = argparse.ArgumentParser(description='AWS EventBridge Rule and Target Automation')
    
    # Rule operations
    parser.add_argument('--create-rule', metavar='NAME', help='Create an EventBridge rule with the given name')
    parser.add_argument('--schedule', help='Schedule expression for the rule (e.g., "rate(5 minutes)" or "cron(0 12 * * ? *)")')
    parser.add_argument('--event-pattern', type=json.loads, help='Event pattern as JSON string')
    parser.add_argument('--description', help='Description for the rule')
    parser.add_argument('--rule-name', help='Name of an existing EventBridge rule for operations')
    
    # Target operations
    parser.add_argument('--lambda-target', metavar='FUNCTION', help='Add a Lambda function as a target')
    parser.add_argument('--sns-target', metavar='ARN', help='Add an SNS topic as a target by ARN')
    parser.add_argument('--input-json', type=json.loads, help='Custom input to pass to the target as JSON string')
    parser.add_argument('--list-targets', action='store_true', help='List targets for the specified rule')
    
    # Rule management
    parser.add_argument('--enable', action='store_true', help='Enable the specified rule')
    parser.add_argument('--disable', action='store_true', help='Disable the specified rule')
    parser.add_argument('--list-rules', action='store_true', help='List all EventBridge rules')
    parser.add_argument('--rule-prefix', help='Prefix filter for listing rules')
    parser.add_argument('--delete-rule', metavar='NAME', help='Delete the specified rule and its targets')
    
    # Common parameters
    parser.add_argument('--region', default='eu-west-1', help='AWS region (default: eu-west-1)')
    
    args = parser.parse_args()
    
    # Handle rule creation
    if args.create_rule:
        rule_arn = create_rule(
            args.create_rule,
            args.schedule,
            args.event_pattern,
            'ENABLED',
            args.description,
            args.region
        )
        if rule_arn:
            print(f"Rule created with ARN: {rule_arn}")
    
    # Handle rule name argument for other operations
    rule_name = args.rule_name or args.create_rule or args.delete_rule
    
    # Handle Lambda target addition
    if args.lambda_target and rule_name:
        target_id = add_lambda_target(
            rule_name,
            args.lambda_target,
            args.input_json,
            args.region
        )
        if target_id:
            print(f"Lambda target added with ID: {target_id}")
    
    # Handle SNS target addition
    if args.sns_target and rule_name:
        target_id = add_sns_target(
            rule_name,
            args.sns_target,
            args.input_json,
            args.region
        )
        if target_id:
            print(f"SNS target added with ID: {target_id}")
    
    # Handle rule listing
    if args.list_rules:
        rules = list_rules(args.rule_prefix, args.region)
        if rules:
            print(f"\nFound {len(rules)} EventBridge rules")
    
    # Handle target listing
    if args.list_targets and rule_name:
        targets = list_targets(rule_name, args.region)
        if targets:
            print(f"\nFound {len(targets)} targets for rule '{rule_name}'")
    
    # Handle rule enable/disable
    if rule_name and (args.enable or args.disable):
        success = enable_disable_rule(rule_name, args.enable, args.region)
        if success:
            state = "enabled" if args.enable else "disabled"
            print(f"Rule '{rule_name}' has been {state}")
    
    # Handle rule deletion
    if args.delete_rule:
        success = delete_rule(args.delete_rule, args.region)
        if success:
            print(f"Rule '{args.delete_rule}' and its targets have been deleted")
    
    # If no arguments were provided, print help
    if len(sys.argv) == 1:
        parser.print_help()

if __name__ == "__main__":
    main() 