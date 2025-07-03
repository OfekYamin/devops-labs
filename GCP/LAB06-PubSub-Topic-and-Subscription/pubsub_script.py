#!/usr/bin/env python3
"""
GCP LAB06 - Pub/Sub Topic and Subscription Automation
This script demonstrates how to create, use, and clean up Google Cloud Pub/Sub
resources programmatically using Python.
"""

import os
import argparse
import time
from google.cloud import pubsub_v1

def create_topic_and_subscription(project_id, topic_id, subscription_id):
    """
    Creates a Pub/Sub topic and a subscription to that topic.
    
    Args:
        project_id (str): Google Cloud Project ID
        topic_id (str): Name for the new topic
        subscription_id (str): Name for the new subscription
    
    Returns:
        tuple: (topic_path, subscription_path)
    """
    # TODO: Initialize the publisher client
    
    # TODO: Create the topic path using project_id and topic_id
    
    # TODO: Create the topic and print confirmation message
    
    # TODO: Initialize the subscriber client
    
    # TODO: Create the subscription path
    
    # TODO: Create the subscription that listens to the topic
    # and print confirmation message
    
    return topic_path, subscription_path

def publish_messages(project_id, topic_id, messages):
    """
    Publishes multiple messages to a Pub/Sub topic.
    
    Args:
        project_id (str): Google Cloud Project ID
        topic_id (str): The topic to publish to
        messages (list): List of message strings to publish
    """
    # TODO: Initialize the publisher client
    
    # TODO: Get the topic path
    
    # TODO: Publish each message in the list
    # TIP: Use a for loop to iterate through messages
    # TIP: Remember to encode string messages to bytes
    # TIP: Consider storing and returning the message IDs
    
    print(f"Published {len(messages)} messages to {topic_path}")

def pull_messages(project_id, subscription_id, max_messages=5):
    """
    Pulls messages from a Pub/Sub subscription and acknowledges them.
    
    Args:
        project_id (str): Google Cloud Project ID
        subscription_id (str): The subscription to pull from
        max_messages (int): Maximum number of messages to pull
    """
    # TODO: Initialize the subscriber client
    
    # TODO: Get the subscription path
    
    # TODO: Pull messages from the subscription
    # TIP: Use the pull method with max_messages parameter
    
    # TODO: Process each received message
    # TIP: Print the message data and any attributes
    
    # TODO: Acknowledge the received messages
    # TIP: Collect ack_ids and acknowledge them in a batch
    
    return len(received_messages) if 'received_messages' in locals() else 0

def delete_topic_and_subscription(project_id, topic_id, subscription_id):
    """
    Deletes a Pub/Sub subscription and topic.
    
    Args:
        project_id (str): Google Cloud Project ID
        topic_id (str): Topic to delete
        subscription_id (str): Subscription to delete
    """
    # TODO: Initialize the clients
    
    # TODO: Get the paths
    
    # TODO: Delete the subscription first, then the topic
    # TIP: Delete resources in reverse order of creation
    
    print(f"Cleaned up subscription {subscription_path} and topic {topic_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Create and use Google Cloud Pub/Sub topics and subscriptions"
    )
    parser.add_argument("--project_id", required=True, help="Your Google Cloud Project ID")
    parser.add_argument("--topic", default="devops-demo-topic", help="The Pub/Sub topic name")
    parser.add_argument("--subscription", default="devops-demo-sub", help="The Pub/Sub subscription name")
    parser.add_argument("--message", action="append", help="Message to publish (can be used multiple times)")
    parser.add_argument("--cleanup", action="store_true", help="Delete the topic and subscription after running")
    
    args = parser.parse_args()
    
    # Default messages if none provided
    messages = args.message or [
        "Hello from GCP DevOps Lab!", 
        "Learning Pub/Sub automation",
        "Message published with Python"
    ]
    
    try:
        print("\n=== Creating Topic and Subscription ===")
        topic_path, subscription_path = create_topic_and_subscription(
            args.project_id, 
            args.topic, 
            args.subscription
        )
        
        print("\n=== Publishing Messages ===")
        publish_messages(args.project_id, args.topic, messages)
        
        # Small delay to ensure messages are available to pull
        print("\nWaiting for messages to be available...")
        time.sleep(3)
        
        print("\n=== Pulling Messages ===")
        count = pull_messages(args.project_id, args.subscription)
        print(f"Pulled and processed {count} messages")
        
        if args.cleanup:
            print("\n=== Cleaning Up Resources ===")
            delete_topic_and_subscription(args.project_id, args.topic, args.subscription)
            
    except Exception as e:
        print(f"Error: {e}")
        
    print("\nLab completed!")

if __name__ == "__main__":
    main() 