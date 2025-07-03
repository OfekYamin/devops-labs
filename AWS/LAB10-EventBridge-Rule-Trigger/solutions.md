# AWS LAB10: EventBridge Rule and Trigger Automation Solutions

This document provides a reference solution for the EventBridge Rule and Trigger Automation lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `eventbridge_script.py`

Below is the complete implementation with all TODO sections completed:

```python
#!/usr/bin/env python3
"""
AWS EventBridge Rule and Trigger Automation Script
This script is part of LAB10 for AWS DevOps Python Course.

It demonstrates how to automate Amazon EventBridge operations using boto3.
"""

import argparse
import boto3
import json
import sys
import time
import uuid
from botocore.exceptions import ClientError

def create_rule(rule_name, schedule=None, event_pattern=None, state='ENABLED', description=None, region='eu-west-1'):
    """
    Create an EventBridge rule with schedule or event pattern
    
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
        # Create a boto3 client for EventBridge
        events_client = boto3.client('events', region_name=region)
        
        # Prepare parameters for put_rule call
        params = {
            'Name': rule_name,
            'State': state
        }
        
        # Add schedule expression if provided
        if schedule:
            params['ScheduleExpression'] = schedule
        
        # Add event pattern if provided
        if event_pattern:
            params['EventPattern'] = json.dumps(event_pattern) if isinstance(event_pattern, dict) else event_pattern
        
        # Add description if provided
        if description:
            params['Description'] = description
        
        # Call put_rule method and return rule ARN
        response = events_client.put_rule(**params)
        print(f"EventBridge rule created successfully")
        return response['RuleArn']
    except Exception as e:
        print(f"Error creating EventBridge rule: {e}")
        sys.exit(1)

def add_lambda_target(rule_name, function_name, input_json=None, region='eu-west-1'):
    """
    Add a Lambda function as a target for an EventBridge rule
    
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
        # Create boto3 clients for EventBridge and Lambda
        events_client = boto3.client('events', region_name=region)
        lambda_client = boto3.client('lambda', region_name=region)
        
        # Get the Lambda function ARN
        lambda_response = lambda_client.get_function(FunctionName=function_name)
        function_arn = lambda_response['Configuration']['FunctionArn']
        
        # Generate a unique target ID
        target_id = str(uuid.uuid4())[:8]
        
        # Prepare parameters for put_targets call
        target_params = {
            'Rule': rule_name,
            'Targets': [
                {
                    'Id': target_id,
                    'Arn': function_arn
                }
            ]
        }
        
        # Add input JSON if provided
        if input_json:
            target_params['Targets'][0]['Input'] = json.dumps(input_json) if isinstance(input_json, dict) else input_json
        
        # Call put_targets method
        events_client.put_targets(**target_params)
        
        # Add permission for EventBridge to invoke Lambda
        lambda_client.add_permission(
            FunctionName=function_name,
            StatementId=f'EventBridge-{rule_name}-{target_id}',
            Action='lambda:InvokeFunction',
            Principal='events.amazonaws.com',
            SourceArn=events_client.describe_rule(Name=rule_name)['Arn']
        )
        
        print(f"Lambda target '{function_name}' added to rule: {rule_name}")
        return target_id
    except Exception as e:
        print(f"Error adding Lambda target to rule: {e}")
        return None

def add_sns_target(rule_name, topic_arn, input_json=None, region='eu-west-1'):
    """
    Add an SNS topic as a target for an EventBridge rule
    
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
        # Create a boto3 client for EventBridge
        events_client = boto3.client('events', region_name=region)
        
        # Generate a unique target ID
        target_id = str(uuid.uuid4())[:8]
        
        # Prepare parameters for put_targets call
        target_params = {
            'Rule': rule_name,
            'Targets': [
                {
                    'Id': target_id,
                    'Arn': topic_arn
                }
            ]
        }
        
        # Add input JSON if provided
        if input_json:
            target_params['Targets'][0]['Input'] = json.dumps(input_json) if isinstance(input_json, dict) else input_json
        
        # Call put_targets method
        events_client.put_targets(**target_params)
        
        print(f"SNS target added to rule: {rule_name}")
        return target_id
    except Exception as e:
        print(f"Error adding SNS target to rule: {e}")
        return None

def list_rules(name_prefix=None, region='eu-west-1'):
    """
    List EventBridge rules, optionally filtered by prefix
    
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
        # Create a boto3 client for EventBridge
        events_client = boto3.client('events', region_name=region)
        
        # Prepare parameters for list_rules call
        params = {}
        if name_prefix:
            params['NamePrefix'] = name_prefix
        
        # Call list_rules method
        response = events_client.list_rules(**params)
        rules = response.get('Rules', [])
        
        # Extract and print rule details
        if rules:
            print("\nEventBridge Rules:")
            print(f"{'Rule Name':<30} {'State':<10} {'Schedule Expression':<30} {'Description'}")
            print("-" * 80)
            
            for rule in rules:
                schedule = rule.get('ScheduleExpression', 'N/A')
                description = rule.get('Description', 'N/A')
                print(f"{rule['Name']:<30} {rule['State']:<10} {schedule:<30} {description[:30]}")
        else:
            print("No EventBridge rules found")
        
        return rules
    except Exception as e:
        print(f"Error listing EventBridge rules: {e}")
        return []

def list_targets(rule_name, region='eu-west-1'):
    """
    List all targets associated with an EventBridge rule
    
    Parameters:
        rule_name (str): Name of the EventBridge rule
        region (str): AWS region
        
    Returns:
        list: List of target details
    """
    print(f"Listing targets for rule: {rule_name}")
    
    try:
        # Create a boto3 client for EventBridge
        events_client = boto3.client('events', region_name=region)
        
        # Call list_targets_by_rule method
        response = events_client.list_targets_by_rule(Rule=rule_name)
        targets = response.get('Targets', [])
        
        # Extract and print target details
        if targets:
            print("\nTargets:")
            print(f"{'Target ID':<15} {'ARN':<60} {'Input'}")
            print("-" * 85)
            
            for target in targets:
                target_id = target['Id']
                arn = target['Arn']
                input_value = target.get('Input', 'Default Event')
                if len(input_value) > 30:
                    input_value = input_value[:27] + '...'
                
                print(f"{target_id:<15} {arn:<60} {input_value}")
        else:
            print(f"No targets found for rule '{rule_name}'")
        
        return targets
    except Exception as e:
        print(f"Error listing targets for rule: {e}")
        return []

def enable_disable_rule(rule_name, enable=True, region='eu-west-1'):
    """
    Enable or disable an EventBridge rule
    
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
        # Create a boto3 client for EventBridge
        events_client = boto3.client('events', region_name=region)
        
        # Call enable_rule or disable_rule method based on the enable parameter
        if enable:
            events_client.enable_rule(Name=rule_name)
        else:
            events_client.disable_rule(Name=rule_name)
        
        print(f"Rule '{rule_name}' is now {state}")
        return True
    except Exception as e:
        print(f"Error changing rule state: {e}")
        return False

def delete_rule(rule_name, region='eu-west-1'):
    """
    Delete an EventBridge rule and all its targets
    
    Parameters:
        rule_name (str): Name of the EventBridge rule to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting rule: {rule_name}")
    
    try:
        # Create a boto3 client for EventBridge
        events_client = boto3.client('events', region_name=region)
        
        # Get targets for the rule
        targets = list_targets(rule_name, region)
        
        # Remove all targets if any exist
        if targets:
            target_ids = [target['Id'] for target in targets]
            events_client.remove_targets(
                Rule=rule_name,
                Ids=target_ids
            )
            print(f"Removed {len(targets)} targets from rule '{rule_name}'")
        
        # Delete the rule
        events_client.delete_rule(Name=rule_name)
        
        print(f"Rule '{rule_name}' deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting rule: {e}")
        return False
```

## Key Learning Points

1. **EventBridge Basic Concepts**:
   - EventBridge is a serverless event bus service that connects your applications with data from various sources
   - Rules match incoming events and route them to targets for processing
   - Each rule can have multiple targets

2. **Rule Configuration**:
   - Rules can be triggered on a schedule using cron or rate expressions
   - Rules can also match event patterns for specific AWS service events
   - State management allows enabling/disabling rules without deleting them

3. **Target Integration**:
   - EventBridge can trigger various AWS services like Lambda, SNS, and more
   - When using Lambda as a target, permission must be granted for EventBridge to invoke the function
   - Custom input transformation allows modifying the event data before it reaches the target

4. **Best Practices**:
   - Use unique rule names prefixed with your application name
   - Always clean up rules and targets when they're no longer needed
   - Use event patterns for fine-grained control over when rules trigger

## Common Issues and Troubleshooting

### Rule Creation Issues

**Problem**: Rule creation fails with validation errors.  
**Solution**: Ensure your schedule expressions (rate/cron) follow the correct syntax. For event patterns, validate your JSON structure. Use the AWS console to test event patterns before implementing them in code.

### Target Invocation Issues

**Problem**: EventBridge rule doesn't trigger the target.  
**Solution**: Check the following:
- Verify that the rule is enabled
- Ensure the permission policy allows EventBridge to invoke the target
- For Lambda targets, verify the function exists and has correct region
- Check CloudWatch Logs for error messages

### Permission Errors

**Problem**: "AccessDenied" errors when adding targets or creating rules.  
**Solution**: Review your IAM permissions. Ensure your IAM role has policies that allow:
- `events:PutRule`, `events:PutTargets` for rule/target creation
- `lambda:AddPermission` when adding Lambda targets
- Service-specific permissions for your target types

### Rule Deletion Errors

**Problem**: Cannot delete a rule because it has targets.  
**Solution**: Always remove all targets before deleting a rule. The solution code handles this by listing targets and removing them before deletion.

## Advanced EventBridge Features

For more advanced use cases, you can explore:

1. **Event Transformation**: Use the `InputTransformer` in target configuration to modify event data before sending to targets
2. **Dead Letter Queues**: Configure DLQs for events that fail delivery
3. **API Destinations**: Send events to HTTP endpoints outside of AWS
4. **Event Replay**: Replay archived events for testing or recovery
5. **Event Buses**: Create custom event buses for application-specific events

## Cleanup Importance

Proper cleanup is critical when working with EventBridge:

1. Rules continue to trigger and may incur charges even if you're not actively using them
2. Lambda invocations, SNS messages, and other target services all have associated costs
3. Deleting a rule without removing its targets can leave orphaned target configurations
4. The provided script includes a `--delete-rule` option to properly clean up both the rule and all its targets

Always run the cleanup procedure after completing the lab:

```
python eventbridge_script.py --delete-rule <your-rule-name> --region eu-west-1
``` 