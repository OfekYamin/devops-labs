#!/usr/bin/env python3
"""
AWS SQS Queue Automation Script
This script is part of LAB09 for AWS DevOps Python Course.

It demonstrates how to automate Amazon SQS operations using boto3.
Students should implement the TODO sections to complete the lab.
"""

import argparse
import boto3
import json
import sys
import time
from botocore.exceptions import ClientError

def create_queue(queue_name, attributes=None, region='eu-west-1'):
    """
    Create an SQS queue with the given name and optional attributes
    
    TODO: Implement this function to create an SQS queue.
    1. Create a boto3 client for SQS in the specified region
    2. Use the create_queue method to create a new queue
    3. Handle any specific attributes (like FIFO, visibility timeout, etc.)
    4. Return the queue URL
    
    Parameters:
        queue_name (str): Name of the SQS queue to create
        attributes (dict, optional): Queue attributes
        region (str): AWS region
        
    Returns:
        str: URL of the created queue
    """
    print(f"Creating SQS queue: {queue_name} in region {region}")
    
    try:
        # TODO: Create a boto3 client for SQS
        
        # TODO: Prepare attributes if none provided
        if attributes is None:
            attributes = {}
        
        # TODO: Call create_queue method with name and attributes
        
        # TODO: Return the queue URL
        return None
    except Exception as e:
        print(f"Error creating SQS queue: {e}")
        sys.exit(1)

def list_queues(prefix=None, region='eu-west-1'):
    """
    List all SQS queues in the account, optionally filtered by prefix
    
    TODO: Implement this function to list SQS queues
    1. Create a boto3 client for SQS in the specified region
    2. Use the list_queues method to get all queues
    3. If prefix is provided, only return queues that start with that prefix
    4. Print and return the queue URLs
    
    Parameters:
        prefix (str, optional): Prefix filter for queue names
        region (str): AWS region
        
    Returns:
        list: List of queue URLs
    """
    if prefix:
        print(f"Listing SQS queues with prefix '{prefix}' in region {region}")
    else:
        print(f"Listing all SQS queues in region {region}")
    
    try:
        # TODO: Create a boto3 client for SQS
        
        # TODO: Call list_queues method with appropriate parameters
        
        # TODO: Extract and return queue URLs
        return []
    except Exception as e:
        print(f"Error listing SQS queues: {e}")
        return []

def send_message(queue_url, message_body, attributes=None, delay_seconds=0, region='eu-west-1'):
    """
    Send a message to an SQS queue
    
    TODO: Implement this function to send a message to a queue
    1. Create a boto3 client for SQS in the specified region
    2. Use the send_message method to send the message
    3. Handle message attributes and delay if provided
    4. Return the message ID
    
    Parameters:
        queue_url (str): URL of the SQS queue
        message_body (str): Message content to send
        attributes (dict, optional): Message attributes
        delay_seconds (int): Delay delivery of the message
        region (str): AWS region
        
    Returns:
        str: Message ID of the sent message
    """
    print(f"Sending message to queue: {queue_url}")
    
    try:
        # TODO: Create a boto3 client for SQS
        
        # TODO: Prepare parameters for send_message call
        params = {
            'QueueUrl': queue_url,
            'MessageBody': message_body
        }
        
        # TODO: Add delay seconds if specified
        
        # TODO: Add message attributes if provided
        
        # TODO: Call send_message method and return message ID
        return None
    except Exception as e:
        print(f"Error sending message to queue: {e}")
        return None

def receive_messages(queue_url, max_messages=1, wait_time=0, visibility_timeout=30, region='eu-west-1'):
    """
    Receive messages from an SQS queue
    
    TODO: Implement this function to receive messages from a queue
    1. Create a boto3 client for SQS in the specified region
    2. Use the receive_message method to get messages
    3. Handle wait time and visibility timeout parameters
    4. Return the list of received messages
    
    Parameters:
        queue_url (str): URL of the SQS queue
        max_messages (int): Maximum number of messages to receive (1-10)
        wait_time (int): Long polling wait time in seconds (0-20)
        visibility_timeout (int): Visibility timeout in seconds
        region (str): AWS region
        
    Returns:
        list: List of received messages
    """
    print(f"Receiving up to {max_messages} messages from queue: {queue_url}")
    
    try:
        # TODO: Create a boto3 client for SQS
        
        # TODO: Prepare parameters for receive_message call
        
        # TODO: Call receive_message method
        
        # TODO: Extract and return messages
        return []
    except Exception as e:
        print(f"Error receiving messages from queue: {e}")
        return []

def delete_message(queue_url, receipt_handle, region='eu-west-1'):
    """
    Delete a message from an SQS queue
    
    TODO: Implement this function to delete a message from a queue
    1. Create a boto3 client for SQS in the specified region
    2. Use the delete_message method to remove the message
    3. Return success status
    
    Parameters:
        queue_url (str): URL of the SQS queue
        receipt_handle (str): Receipt handle of the message to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting message from queue: {queue_url}")
    
    try:
        # TODO: Create a boto3 client for SQS
        
        # TODO: Call delete_message method
        
        return False
    except Exception as e:
        print(f"Error deleting message from queue: {e}")
        return False

def delete_queue(queue_url, region='eu-west-1'):
    """
    Delete an SQS queue
    
    TODO: Implement this function to delete an SQS queue
    1. Create a boto3 client for SQS in the specified region
    2. Use the delete_queue method to remove the queue
    3. Return success status
    
    Parameters:
        queue_url (str): URL of the SQS queue to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting queue: {queue_url}")
    
    try:
        # TODO: Create a boto3 client for SQS
        
        # TODO: Call delete_queue method
        
        return False
    except Exception as e:
        print(f"Error deleting queue: {e}")
        return False

def main():
    """Main function to parse arguments and execute SQS operations"""
    parser = argparse.ArgumentParser(description='AWS SQS Queue Automation')
    
    # Queue operations
    parser.add_argument('--create-queue', metavar='NAME', help='Create an SQS queue with the given name')
    parser.add_argument('--list-queues', action='store_true', help='List all SQS queues')
    parser.add_argument('--queue-prefix', help='Filter queues by prefix when listing')
    parser.add_argument('--delete-queue', action='store_true', help='Delete the specified SQS queue')
    
    # Message operations
    parser.add_argument('--send-message', metavar='MSG', help='Send a message to the queue')
    parser.add_argument('--attributes', type=json.loads, help='Message attributes as JSON string')
    parser.add_argument('--delay', type=int, default=0, help='Delay message delivery in seconds')
    parser.add_argument('--receive', action='store_true', help='Receive messages from the queue')
    parser.add_argument('--max-messages', type=int, default=1, help='Maximum number of messages to receive')
    parser.add_argument('--wait-time', type=int, default=0, help='Wait time for long polling in seconds')
    parser.add_argument('--visibility', type=int, default=30, help='Visibility timeout in seconds')
    
    # Common parameters
    parser.add_argument('--queue-url', help='URL of an existing SQS queue')
    parser.add_argument('--region', default='eu-west-1', help='AWS region (default: eu-west-1)')
    parser.add_argument('--fifo', action='store_true', help='Create a FIFO queue')
    
    args = parser.parse_args()
    
    # Handle queue creation
    if args.create_queue:
        queue_name = args.create_queue
        attributes = {}
        
        # Handle FIFO queue creation
        if args.fifo:
            if not queue_name.endswith('.fifo'):
                queue_name += '.fifo'
            attributes['FifoQueue'] = 'true'
            attributes['ContentBasedDeduplication'] = 'true'
        
        queue_url = create_queue(queue_name, attributes, args.region)
        if queue_url:
            print(f"Queue created with URL: {queue_url}")
    
    # Handle queue listing
    if args.list_queues:
        queues = list_queues(args.queue_prefix, args.region)
        if queues:
            print("\nAvailable queues:")
            for i, url in enumerate(queues, 1):
                print(f"{i}. {url}")
    
    # Handle message sending
    if args.send_message and args.queue_url:
        message_id = send_message(
            args.queue_url, 
            args.send_message,
            args.attributes,
            args.delay,
            args.region
        )
        if message_id:
            print(f"Message sent with ID: {message_id}")
    
    # Handle message receiving
    if args.receive and args.queue_url:
        messages = receive_messages(
            args.queue_url,
            args.max_messages,
            args.wait_time,
            args.visibility,
            args.region
        )
        
        if messages:
            print(f"\nReceived {len(messages)} messages:")
            for i, msg in enumerate(messages, 1):
                print(f"\nMessage {i}:")
                print(f"  Body: {msg['Body']}")
                print(f"  ID: {msg['MessageId']}")
                
                # Print message attributes if any
                if 'MessageAttributes' in msg and msg['MessageAttributes']:
                    print("  Attributes:")
                    for key, attr in msg['MessageAttributes'].items():
                        print(f"    {key}: {attr['StringValue']}")
                
                # Prompt for deletion
                if input("\nDelete this message? (y/n): ").lower() == 'y':
                    if delete_message(args.queue_url, msg['ReceiptHandle'], args.region):
                        print("Message deleted.")
                    else:
                        print("Failed to delete message.")
        else:
            print("No messages received.")
    
    # Handle queue deletion
    if args.delete_queue and args.queue_url:
        success = delete_queue(args.queue_url, args.region)
        if success:
            print(f"Queue {args.queue_url} deleted successfully.")
    
    # If no arguments were provided, print help
    if len(sys.argv) == 1:
        parser.print_help()

if __name__ == "__main__":
    main() 