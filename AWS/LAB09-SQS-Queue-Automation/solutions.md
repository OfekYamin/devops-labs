# Solutions - AWS LAB09: SQS Queue Automation

This document provides the complete solution for the SQS Queue Automation lab exercise. Please use this only as a reference after attempting the lab independently.

## SQS Queue Automation Complete Solution

Below is the complete implementation of the `sqs_script.py` file with all the required functions implemented.

```python
#!/usr/bin/env python3
"""
AWS SQS Queue Automation Script
This script is part of LAB09 for AWS DevOps Python Course.

It demonstrates how to automate Amazon SQS operations using boto3.
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
    
    Parameters:
        queue_name (str): Name of the SQS queue to create
        attributes (dict, optional): Queue attributes
        region (str): AWS region
        
    Returns:
        str: URL of the created queue
    """
    print(f"Creating SQS queue: {queue_name} in region {region}")
    
    try:
        # Create a boto3 client for SQS
        sqs_client = boto3.client('sqs', region_name=region)
        
        # Prepare attributes if none provided
        if attributes is None:
            attributes = {}
        
        # Call create_queue method with name and attributes
        response = sqs_client.create_queue(
            QueueName=queue_name,
            Attributes=attributes
        )
        
        # Return the queue URL
        return response['QueueUrl']
    except Exception as e:
        print(f"Error creating SQS queue: {e}")
        sys.exit(1)

def list_queues(prefix=None, region='eu-west-1'):
    """
    List all SQS queues in the account, optionally filtered by prefix
    
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
        # Create a boto3 client for SQS
        sqs_client = boto3.client('sqs', region_name=region)
        
        # Call list_queues method with appropriate parameters
        params = {}
        if prefix:
            params['QueueNamePrefix'] = prefix
            
        response = sqs_client.list_queues(**params)
        
        # Extract and return queue URLs
        queue_urls = response.get('QueueUrls', [])
        
        # Print each queue URL
        for url in queue_urls:
            print(f"Queue URL: {url}")
            
        return queue_urls
    except Exception as e:
        print(f"Error listing SQS queues: {e}")
        return []

def send_message(queue_url, message_body, attributes=None, delay_seconds=0, region='eu-west-1'):
    """
    Send a message to an SQS queue
    
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
        # Create a boto3 client for SQS
        sqs_client = boto3.client('sqs', region_name=region)
        
        # Prepare parameters for send_message call
        params = {
            'QueueUrl': queue_url,
            'MessageBody': message_body
        }
        
        # Add delay seconds if specified
        if delay_seconds > 0:
            params['DelaySeconds'] = delay_seconds
        
        # Add message attributes if provided
        if attributes:
            params['MessageAttributes'] = attributes
        
        # Call send_message method and return message ID
        response = sqs_client.send_message(**params)
        print(f"Message sent successfully")
        return response['MessageId']
    except Exception as e:
        print(f"Error sending message to queue: {e}")
        return None

def receive_messages(queue_url, max_messages=1, wait_time=0, visibility_timeout=30, region='eu-west-1'):
    """
    Receive messages from an SQS queue
    
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
        # Create a boto3 client for SQS
        sqs_client = boto3.client('sqs', region_name=region)
        
        # Prepare parameters for receive_message call
        params = {
            'QueueUrl': queue_url,
            'MaxNumberOfMessages': min(max_messages, 10),  # SQS limits to 10 max
            'VisibilityTimeout': visibility_timeout,
            'WaitTimeSeconds': min(wait_time, 20),  # SQS limits to 20 seconds max
            'AttributeNames': ['All'],
            'MessageAttributeNames': ['All']
        }
        
        # Call receive_message method
        response = sqs_client.receive_message(**params)
        
        # Extract and return messages
        messages = response.get('Messages', [])
        return messages
    except Exception as e:
        print(f"Error receiving messages from queue: {e}")
        return []

def delete_message(queue_url, receipt_handle, region='eu-west-1'):
    """
    Delete a message from an SQS queue
    
    Parameters:
        queue_url (str): URL of the SQS queue
        receipt_handle (str): Receipt handle of the message to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting message from queue: {queue_url}")
    
    try:
        # Create a boto3 client for SQS
        sqs_client = boto3.client('sqs', region_name=region)
        
        # Call delete_message method
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        
        print(f"Message deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting message from queue: {e}")
        return False

def delete_queue(queue_url, region='eu-west-1'):
    """
    Delete an SQS queue
    
    Parameters:
        queue_url (str): URL of the SQS queue to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Deleting queue: {queue_url}")
    
    try:
        # Create a boto3 client for SQS
        sqs_client = boto3.client('sqs', region_name=region)
        
        # Call delete_queue method
        sqs_client.delete_queue(QueueUrl=queue_url)
        
        print(f"Queue deleted successfully")
        return True
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
```

## Key Learning Points

1. **SQS Queue Management**:
   - SQS offers two types of queues: Standard (high throughput, at-least-once delivery) and FIFO (exactly-once processing, ordered)
   - Queue names must be unique within an AWS account and region
   - FIFO queue names must end with `.fifo` suffix

2. **Message Operations**:
   - Messages can be up to 256KB in size
   - Messages can include custom attributes (metadata)
   - Delay queues can postpone delivery of new messages
   - Messages remain in the queue until explicitly deleted

3. **Visibility Timeout**:
   - When a message is received, it becomes temporarily invisible to other consumers
   - If not deleted within the visibility timeout, it becomes visible again
   - Configurable from 0 seconds to 12 hours (default: 30 seconds)

4. **Long Polling**:
   - Reduces empty responses and API calls by waiting for messages
   - More efficient than short polling, especially for low-volume queues
   - Wait time can be configured up to 20 seconds

5. **Error Handling**:
   - Proper exception handling ensures your automation script is robust
   - Common issues include permissions, queue not found, and invalid parameters

## Common Issues and Troubleshooting

1. **Queue Creation Issues**:
   - Problem: Unable to create queue due to naming constraints
   - Solution: Queue names must use alphanumeric, hyphen, and underscore characters only

2. **Message Visibility Issues**:
   - Problem: Messages reappearing in the queue after processing
   - Solution: Ensure you're deleting messages after processing and that visibility timeout is sufficient

3. **FIFO Queue Constraints**:
   - Problem: Unable to send messages to FIFO queue
   - Solution: FIFO queues require a message group ID and potentially a deduplication ID

4. **Message Size Limitations**:
   - Problem: Message too large error
   - Solution: SQS limits messages to 256KB; for larger payloads, store data in S3 and send a reference

5. **Long Polling Timeouts**:
   - Problem: API calls timing out during long polling
   - Solution: Ensure your client timeout is longer than the SQS wait time

## Best Practices

1. **Use Batch Operations**: For high-throughput scenarios, use batch send/receive operations
2. **Implement Proper Error Handling**: Handle and log all exceptions to identify issues
3. **Configure Dead Letter Queues**: Set up DLQs for messages that fail processing repeatedly
4. **Consider Message Retention**: Default is 4 days, but can be configured up to 14 days
5. **Monitor Queue Metrics**: Set up CloudWatch alarms for queue depth, age, and error rates
6. **Use IAM Roles**: Don't hardcode credentials; use IAM roles for EC2 instances or Lambda functions

## Cleanup Importance

Always remember to clean up SQS resources after completing labs to avoid unnecessary charges:

1. Delete all messages in the queue
2. Delete all queues
3. Verify in the AWS Management Console that resources are removed

The provided script includes the `--delete-queue` option that helps with this cleanup process. 