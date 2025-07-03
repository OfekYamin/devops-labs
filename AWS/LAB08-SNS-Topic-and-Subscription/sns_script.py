#!/usr/bin/env python3
"""
AWS SNS Topic and Subscription Automation Script

This script demonstrates how to automate Amazon SNS operations using boto3.
It's part of Lab 08 for the AWS DevOps Python course.

Students should implement the TODO sections to complete the lab.
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
    
    TODO: Implement this function to create an SNS topic.
    1. Create a boto3 client for SNS in the specified region
    2. Use the create_topic method to create a new topic
    3. Return the ARN of the created topic
    
    Parameters:
        topic_name (str): Name of the SNS topic to create
        region (str): AWS region to create the topic in
        
    Returns:
        str: ARN of the created topic
    """
    print(f"Creating SNS topic: {topic_name} in region {region}")
    
    try:
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call create_topic method
        
        # TODO: Return the topic ARN
        return None
    except Exception as e:
        print(f"Error creating SNS topic: {e}")
        sys.exit(1)

def list_topics(region='eu-west-1'):
    """
    List all SNS topics in the account
    
    TODO: Implement this function to list all SNS topics
    1. Create a boto3 client for SNS in the specified region
    2. Use the list_topics method to get all topics
    3. Print each topic's ARN
    
    Parameters:
        region (str): AWS region to list topics from
        
    Returns:
        list: List of topic ARNs
    """
    print(f"Listing SNS topics in region {region}")
    
    try:
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call list_topics method
        
        # TODO: Extract and return topic ARNs
        return []
    except Exception as e:
        print(f"Error listing SNS topics: {e}")
        return []

def subscribe_email(topic_arn, email, region='eu-west-1'):
    """
    Subscribe an email address to an SNS topic
    
    TODO: Implement this function to create an email subscription
    1. Create a boto3 client for SNS in the specified region
    2. Use the subscribe method to subscribe the email
    3. Return the subscription ARN
    
    Parameters:
        topic_arn (str): ARN of the SNS topic
        email (str): Email address to subscribe
        region (str): AWS region
        
    Returns:
        str: ARN of the subscription (will be "pending confirmation" for email)
    """
    print(f"Subscribing {email} to topic: {topic_arn}")
    
    try:
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call subscribe method with protocol='email'
        
        # TODO: Return the subscription ARN
        return None
    except Exception as e:
        print(f"Error subscribing email to topic: {e}")
        return None

def publish_message(topic_arn, message, subject="SNS Notification", region='eu-west-1'):
    """
    Publish a message to an SNS topic
    
    TODO: Implement this function to publish a message to a topic
    1. Create a boto3 client for SNS in the specified region
    2. Use the publish method to send a message
    3. Return the message ID
    
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
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call publish method with message and subject
        
        # TODO: Return the message ID
        return None
    except Exception as e:
        print(f"Error publishing message to topic: {e}")
        return None

def list_subscriptions(topic_arn=None, region='eu-west-1'):
    """
    List subscriptions, optionally filtered by topic ARN
    
    TODO: Implement this function to list subscriptions
    1. Create a boto3 client for SNS in the specified region
    2. If topic_arn is provided, use list_subscriptions_by_topic
    3. Otherwise, use list_subscriptions to get all subscriptions
    4. Print and return subscription details
    
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
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call appropriate list method based on whether topic_arn is provided
        
        # TODO: Extract and return subscription details
        return []
    except Exception as e:
        print(f"Error listing subscriptions: {e}")
        return []

def delete_subscription(subscription_arn, region='eu-west-1'):
    """
    Delete an SNS subscription
    
    TODO: Implement this function to delete a subscription
    1. Create a boto3 client for SNS in the specified region
    2. Use the unsubscribe method to delete the subscription
    
    Parameters:
        subscription_arn (str): ARN of the subscription to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting subscription: {subscription_arn}")
    
    try:
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call unsubscribe method
        
        return False
    except Exception as e:
        print(f"Error deleting subscription: {e}")
        return False

def delete_topic(topic_arn, region='eu-west-1'):
    """
    Delete an SNS topic
    
    TODO: Implement this function to delete an SNS topic
    1. Create a boto3 client for SNS in the specified region
    2. Use the delete_topic method to delete the topic
    
    Parameters:
        topic_arn (str): ARN of the SNS topic to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting topic: {topic_arn}")
    
    try:
        # TODO: Create a boto3 client for SNS
        
        # TODO: Call delete_topic method
        
        return False
    except Exception as e:
        print(f"Error deleting topic: {e}")
        return False

def get_topic_attributes(sns_client, topic_arn):
    """
    Get and display attributes of an SNS topic
    
    Args:
        sns_client: The boto3 SNS client
        topic_arn: The ARN of the topic
    
    Returns:
        dict: The topic attributes
    """
    try:
        # TODO: Implement the get_topic_attributes API call
        # Print relevant attributes like DisplayName, SubscriptionsConfirmed, etc.
        
        # Example (replace with your implementation):
        # response = sns_client.get_topic_attributes(TopicArn=topic_arn)
        # attributes = response['Attributes']
        # print(f"\n--- Topic Attributes ---")
        # print(f"Topic ARN: {attributes['TopicArn']}")
        # print(f"Owner: {attributes['Owner']}")
        # print(f"Display Name: {attributes.get('DisplayName', 'Not set')}")
        # print(f"Subscriptions Confirmed: {attributes['SubscriptionsConfirmed']}")
        # print(f"Subscriptions Pending: {attributes['SubscriptionsPending']}")
        # return attributes
        
        print(f"TODO: Implement get_topic_attributes function to get topic attributes")
        return {}
    except ClientError as e:
        print(f"Error getting topic attributes: {e}")
        return {}

def unsubscribe(sns_client, subscription_arn):
    """
    Unsubscribe from an SNS topic
    
    Args:
        sns_client: The boto3 SNS client
        subscription_arn: The ARN of the subscription to remove
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # TODO: Implement the unsubscribe API call
        # Return True if successful
        
        # Example (replace with your implementation):
        # sns_client.unsubscribe(SubscriptionArn=subscription_arn)
        # print(f"Successfully unsubscribed {subscription_arn}")
        # return True
        
        print(f"TODO: Implement unsubscribe function to unsubscribe from a topic")
        return False
    except ClientError as e:
        print(f"Error unsubscribing: {e}")
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