# Solutions - AWS LAB08: SNS Topic and Subscription Automation

This document provides the complete solution for the SNS Topic and Subscription Automation lab exercise. Please use this only as a reference after attempting the lab independently.

## SNS Topic and Subscription Complete Solution

Below is the complete implementation of the `sns_script.py` file with all the required functions implemented.

```python
#!/usr/bin/env python3
"""
AWS SNS Topic and Subscription Automation Script
This script is part of LAB08 for AWS DevOps Python Course.

It demonstrates how to automate Amazon SNS operations using boto3.
"""

import argparse
import boto3
import time
import sys
import json
from botocore.exceptions import ClientError

def create_topic(topic_name, region='eu-west-1'):
    """
    Create an SNS topic with the given name
    
    Parameters:
        topic_name (str): Name of the SNS topic to create
        region (str): AWS region to create the topic in
        
    Returns:
        str: ARN of the created topic
    """
    print(f"Creating SNS topic: {topic_name} in region {region}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call create_topic method
        response = sns_client.create_topic(Name=topic_name)
        
        # Return the topic ARN
        return response['TopicArn']
    except Exception as e:
        print(f"Error creating SNS topic: {e}")
        sys.exit(1)

def list_topics(region='eu-west-1'):
    """
    List all SNS topics in the account
    
    Parameters:
        region (str): AWS region to list topics from
        
    Returns:
        list: List of topic ARNs
    """
    print(f"Listing SNS topics in region {region}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call list_topics method
        response = sns_client.list_topics()
        
        # Extract and return topic ARNs with pagination handling
        topic_arns = []
        for topic in response.get('Topics', []):
            topic_arns.append(topic['TopicArn'])
            print(f"Topic ARN: {topic['TopicArn']}")
            
        # Handle pagination if there are more topics
        while 'NextToken' in response:
            response = sns_client.list_topics(NextToken=response['NextToken'])
            for topic in response.get('Topics', []):
                topic_arns.append(topic['TopicArn'])
                print(f"Topic ARN: {topic['TopicArn']}")
                
        return topic_arns
    except Exception as e:
        print(f"Error listing SNS topics: {e}")
        return []

def subscribe_email(topic_arn, email, region='eu-west-1'):
    """
    Subscribe an email address to an SNS topic
    
    Parameters:
        topic_arn (str): ARN of the SNS topic
        email (str): Email address to subscribe
        region (str): AWS region
        
    Returns:
        str: ARN of the subscription (will be "pending confirmation" for email)
    """
    print(f"Subscribing {email} to topic: {topic_arn}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call subscribe method with protocol='email'
        response = sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
        )
        
        print(f"Subscription created. Check {email} to confirm the subscription.")
        # Return the subscription ARN
        return response['SubscriptionArn']
    except Exception as e:
        print(f"Error subscribing email to topic: {e}")
        return None

def publish_message(topic_arn, message, subject="SNS Notification", region='eu-west-1'):
    """
    Publish a message to an SNS topic
    
    Parameters:
        topic_arn (str): ARN of the SNS topic
        message (str): Message to publish
        subject (str): Subject line for the message
        region (str): AWS region
        
    Returns:
        str: Message ID
    """
    print(f"Publishing message to topic: {topic_arn}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call publish method with message and subject
        response = sns_client.publish(
            TopicArn=topic_arn,
            Subject=subject,
            Message=message
        )
        
        # Return the message ID
        return response['MessageId']
    except Exception as e:
        print(f"Error publishing message to topic: {e}")
        return None

def list_subscriptions(topic_arn=None, region='eu-west-1'):
    """
    List subscriptions, optionally filtered by topic ARN
    
    Parameters:
        topic_arn (str, optional): ARN of the SNS topic
        region (str): AWS region
        
    Returns:
        list: List of subscription details
    """
    if topic_arn:
        print(f"Listing subscriptions for topic: {topic_arn}")
    else:
        print(f"Listing all subscriptions in region {region}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call appropriate list method based on whether topic_arn is provided
        subscriptions = []
        if topic_arn:
            # Get subscriptions for specific topic
            response = sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)
            
            # Process first page of results
            subscriptions.extend(response.get('Subscriptions', []))
            
            # Handle pagination
            while 'NextToken' in response:
                response = sns_client.list_subscriptions_by_topic(
                    TopicArn=topic_arn,
                    NextToken=response['NextToken']
                )
                subscriptions.extend(response.get('Subscriptions', []))
        else:
            # Get all subscriptions
            response = sns_client.list_subscriptions()
            
            # Process first page of results
            subscriptions.extend(response.get('Subscriptions', []))
            
            # Handle pagination
            while 'NextToken' in response:
                response = sns_client.list_subscriptions(NextToken=response['NextToken'])
                subscriptions.extend(response.get('Subscriptions', []))
        
        # Extract and return subscription details
        for sub in subscriptions:
            print(f"Protocol: {sub['Protocol']}, Endpoint: {sub['Endpoint']}")
            
        return subscriptions
    except Exception as e:
        print(f"Error listing subscriptions: {e}")
        return []

def delete_subscription(subscription_arn, region='eu-west-1'):
    """
    Delete an SNS subscription
    
    Parameters:
        subscription_arn (str): ARN of the subscription to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting subscription: {subscription_arn}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call unsubscribe method
        sns_client.unsubscribe(SubscriptionArn=subscription_arn)
        
        print(f"Subscription {subscription_arn} deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting subscription: {e}")
        return False

def delete_topic(topic_arn, region='eu-west-1'):
    """
    Delete an SNS topic
    
    Parameters:
        topic_arn (str): ARN of the SNS topic to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting topic: {topic_arn}")
    
    try:
        # Create a boto3 client for SNS
        sns_client = boto3.client('sns', region_name=region)
        
        # Call delete_topic method
        sns_client.delete_topic(TopicArn=topic_arn)
        
        print(f"Topic {topic_arn} deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting topic: {e}")
        return False

def main():
    """Main function to parse arguments and execute SNS operations"""
    parser = argparse.ArgumentParser(description='AWS SNS Topic and Subscription Automation')
    
    # Topic operations
    parser.add_argument('--create-topic', metavar='NAME', help='Create an SNS topic with the given name')
    parser.add_argument('--list-topics', action='store_true', help='List all SNS topics')
    parser.add_argument('--delete-topic', action='store_true', help='Delete the specified SNS topic')
    
    # Subscription operations
    parser.add_argument('--subscribe', metavar='EMAIL', help='Subscribe an email address to a topic')
    parser.add_argument('--list-subscriptions', action='store_true', help='List subscriptions, optionally for a specific topic')
    parser.add_argument('--delete-subscription', metavar='SUBSCRIPTION_ARN', help='Delete a subscription by ARN')
    
    # Message publishing
    parser.add_argument('--publish', metavar='MESSAGE', help='Publish a message to an SNS topic')
    parser.add_argument('--subject', metavar='SUBJECT', default='SNS Lab Notification', help='Subject for the published message')
    
    # Common parameters
    parser.add_argument('--topic-arn', metavar='ARN', help='ARN of an existing SNS topic')
    parser.add_argument('--region', default='eu-west-1', help='AWS region (default: eu-west-1)')
    
    args = parser.parse_args()
    
    # Perform requested operations
    if args.create_topic:
        topic_arn = create_topic(args.create_topic, args.region)
        print(f"Created topic: {topic_arn}")
    
    if args.list_topics:
        topics = list_topics(args.region)
        if topics:
            print("\nAvailable topics:")
            for i, topic in enumerate(topics, 1):
                print(f"{i}. {topic}")
    
    if args.subscribe and args.topic_arn:
        subscription = subscribe_email(args.topic_arn, args.subscribe, args.region)
        print(f"Subscription status: {subscription}")
        print("⚠️ Check your email to confirm the subscription!")
    
    if args.publish and args.topic_arn:
        message_id = publish_message(args.topic_arn, args.publish, args.subject, args.region)
        print(f"Message published with ID: {message_id}")
    
    if args.list_subscriptions:
        subscriptions = list_subscriptions(args.topic_arn, args.region)
        if subscriptions:
            print("\nSubscriptions:")
            for i, sub in enumerate(subscriptions, 1):
                print(f"{i}. {sub}")
    
    if args.delete_subscription:
        success = delete_subscription(args.delete_subscription, args.region)
        if success:
            print(f"Successfully deleted subscription: {args.delete_subscription}")
    
    if args.delete_topic and args.topic_arn:
        success = delete_topic(args.topic_arn, args.region)
        if success:
            print(f"Successfully deleted topic: {args.topic_arn}")
    
    # If no arguments were provided, print help
    if len(sys.argv) == 1:
        parser.print_help()

if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **SNS Topic Management**:
   - SNS topics are communication channels to which publishers send messages and subscribers receive them
   - Topic names must be unique within your AWS account and region
   - Topic ARNs (Amazon Resource Names) uniquely identify each topic across AWS

2. **Subscription Operations**:
   - Various protocols are supported (email, SMS, HTTP(S), Lambda, SQS)
   - Email subscriptions require manual confirmation by the recipient
   - Subscription ARNs will show as "PendingConfirmation" until confirmed

3. **Message Publishing**:
   - Messages can include a subject line and body
   - Messages are distributed to all confirmed subscriptions of the topic
   - You can track message delivery using the returned MessageId

4. **Pagination Handling**:
   - AWS API responses are often paginated to manage large result sets
   - NextToken handling is essential for retrieving all resources

5. **Error Handling**:
   - Proper exception handling ensures your automation script is robust
   - ClientError exceptions provide detailed information about failures

## Common Issues and Troubleshooting

1. **Email Confirmation Issues**:
   - Problem: Subscriptions remain in "PendingConfirmation" state
   - Solution: Verify email address is correct; check spam folders; manually confirm

2. **Topic Naming Constraints**:
   - Problem: Cannot create topic due to name constraints
   - Solution: Topic names must be alphanumeric with hyphens and underscores, no spaces

3. **Permission Errors**:
   - Problem: "AccessDenied" errors when performing SNS operations
   - Solution: Verify IAM permissions include appropriate SNS actions

4. **Topic Deletion Issues**:
   - Problem: Cannot delete a topic
   - Solution: Ensure all operations on the topic are complete; check IAM permissions

5. **Message Delivery Issues**:
   - Problem: Messages not being received by subscribers
   - Solution: Verify subscriptions are confirmed; check delivery policy settings

## Best Practices

1. **Use Topic Tags**: Add tags to topics for better organization and cost tracking
2. **Implement Structured Messages**: For advanced use cases, use structured message formats (JSON)
3. **Setup Dead Letter Queues**: For critical notifications, configure dead letter queues
4. **Use IAM Policies**: Restrict SNS actions to specific principals and resources
5. **Enable Encryption**: For sensitive data, enable server-side encryption for SNS topics
6. **Monitor SNS Usage**: Set up CloudWatch Alarms to monitor SNS usage and costs

## Cleanup Importance

Always remember to clean up SNS resources after completing labs to avoid unnecessary charges:

1. Delete all subscriptions
2. Delete all topics
3. Verify in the AWS Management Console that resources are removed

The provided script includes the `--delete-topic` option that helps with this cleanup process. 