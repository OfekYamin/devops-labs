#!/usr/bin/env python3
"""
Azure Service Bus Queue Automation Script

This script demonstrates how to interact with Azure Service Bus to create namespaces, 
queues, send messages, and receive messages using the Azure SDK for Python.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import uuid
import time
import argparse
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.core.exceptions import ResourceExistsError, HttpResponseError

def get_clients():
    """
    Create Azure SDK clients for Service Bus management and messaging.
    
    TODO: Implement this function to:
    1. Get subscription ID from environment variables
    2. Create DefaultAzureCredential
    3. Create and return ServiceBusManagementClient
    
    Returns:
        tuple: (management_client, subscription_id)
    """
    # TODO: Get subscription ID from environment variables
    
    # TODO: Create credential using DefaultAzureCredential
    
    # TODO: Create and return Service Bus management client
    pass

def create_namespace(management_client, resource_group, namespace_name, location="eastus", sku="Basic"):
    """
    Create a Service Bus namespace.
    
    TODO: Implement this function to:
    1. Create a Service Bus namespace with specified parameters
    2. Wait for the operation to complete
    3. Return namespace properties
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        location (str): Azure region (default: "eastus")
        sku (str): Service tier (default: "Basic")
        
    Returns:
        dict: Namespace properties
    """
    print(f"Creating Service Bus namespace: {namespace_name} in {resource_group}")
    
    # TODO: Create namespace with begin_create_or_update and wait for completion
    
    # TODO: Return namespace properties
    pass

def create_queue(management_client, resource_group, namespace_name, queue_name, 
                max_size_mb=1024, enable_partitioning=False):
    """
    Create a queue in a Service Bus namespace.
    
    TODO: Implement this function to:
    1. Create a queue with specified parameters
    2. Return queue properties
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        queue_name (str): Queue name
        max_size_mb (int): Maximum size in MB
        enable_partitioning (bool): Whether to enable partitioning
        
    Returns:
        dict: Queue properties
    """
    print(f"Creating queue: {queue_name} in namespace {namespace_name}")
    
    # TODO: Create queue with create_or_update
    
    # TODO: Return queue properties
    pass

def list_queues(management_client, resource_group, namespace_name):
    """
    List all queues in a Service Bus namespace.
    
    TODO: Implement this function to:
    1. List all queues in the namespace
    2. Return the list of queues
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        
    Returns:
        list: List of queues
    """
    print(f"Listing queues in namespace: {namespace_name}")
    
    # TODO: List queues and return the result
    pass

def get_queue_connection_string(management_client, resource_group, namespace_name):
    """
    Get the connection string for a Service Bus namespace.
    
    TODO: Implement this function to:
    1. List namespace keys
    2. Return the primary connection string
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        
    Returns:
        str: Connection string
    """
    print(f"Getting connection string for namespace: {namespace_name}")
    
    # TODO: List keys for the namespace
    
    # TODO: Return the primary connection string
    pass

def send_messages(connection_string, queue_name, message_count=5):
    """
    Send messages to a Service Bus queue.
    
    TODO: Implement this function to:
    1. Create a ServiceBusClient from connection string
    2. Create a sender for the queue
    3. Send a batch of test messages
    
    Args:
        connection_string (str): The connection string to the Service Bus namespace
        queue_name (str): The name of the queue
        message_count (int): Number of test messages to send
        
    Returns:
        list: List of message IDs that were sent
    """
    print(f"Sending {message_count} messages to queue: {queue_name}")
    
    # TODO: Create ServiceBusClient from connection string
    
    # TODO: Create a sender for the queue
    
    # TODO: Send messages and return message IDs
    pass

def receive_messages(connection_string, queue_name, max_message_count=5, max_wait_time=5):
    """
    Receive messages from a Service Bus queue.
    
    TODO: Implement this function to:
    1. Create a ServiceBusClient from connection string
    2. Create a receiver for the queue
    3. Receive and process messages
    
    Args:
        connection_string (str): The connection string to the Service Bus namespace
        queue_name (str): The name of the queue
        max_message_count (int): Maximum number of messages to receive
        max_wait_time (int): Maximum time to wait in seconds
        
    Returns:
        list: List of received message contents
    """
    print(f"Receiving up to {max_message_count} messages from queue: {queue_name}")
    
    # TODO: Create ServiceBusClient from connection string
    
    # TODO: Create a receiver for the queue
    
    # TODO: Receive messages, process them, and return contents
    pass

def delete_queue(management_client, resource_group, namespace_name, queue_name):
    """
    Delete a Service Bus queue.
    
    TODO: Implement this function to:
    1. Delete the specified queue
    2. Return success status
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        queue_name (str): Queue name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting queue: {queue_name} from namespace {namespace_name}")
    
    # TODO: Delete the queue
    
    # TODO: Return success status
    pass

def delete_namespace(management_client, resource_group, namespace_name):
    """
    Delete a Service Bus namespace.
    
    TODO: Implement this function to:
    1. Delete the specified namespace
    2. Return success status
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting namespace: {namespace_name} from resource group {resource_group}")
    
    # TODO: Delete the namespace
    
    # TODO: Return success status
    pass

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description='Azure Service Bus Queue Tool')
    
    # Resource group and namespace arguments
    parser.add_argument('--resource-group', required=True, help='Resource group name')
    parser.add_argument('--namespace', required=True, help='Service Bus namespace name')
    parser.add_argument('--queue', required=True, help='Queue name')
    parser.add_argument('--location', default='eastus', help='Azure region (default: eastus)')
    
    # Operations
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')
    
    # Create namespace operation
    create_ns_parser = subparsers.add_parser('create-namespace', help='Create a Service Bus namespace')
    create_ns_parser.add_argument('--sku', default='Basic', choices=['Basic', 'Standard', 'Premium'], 
                                help='Service tier (default: Basic)')
    
    # Create queue operation
    create_q_parser = subparsers.add_parser('create-queue', help='Create a queue in a Service Bus namespace')
    create_q_parser.add_argument('--max-size', type=int, default=1024, help='Maximum size in MB (default: 1024)')
    create_q_parser.add_argument('--enable-partitioning', action='store_true', help='Enable partitioning')
    
    # List queues operation
    list_parser = subparsers.add_parser('list-queues', help='List queues in a Service Bus namespace')
    
    # Send messages operation
    send_parser = subparsers.add_parser('send-messages', help='Send messages to a queue')
    send_parser.add_argument('--count', type=int, default=5, help='Number of messages to send (default: 5)')
    
    # Receive messages operation
    receive_parser = subparsers.add_parser('receive-messages', help='Receive messages from a queue')
    receive_parser.add_argument('--count', type=int, default=5, help='Maximum number of messages to receive (default: 5)')
    receive_parser.add_argument('--wait-time', type=int, default=5, help='Maximum wait time in seconds (default: 5)')
    
    # Delete queue operation
    delete_q_parser = subparsers.add_parser('delete-queue', help='Delete a Service Bus queue')
    
    # Delete namespace operation
    delete_ns_parser = subparsers.add_parser('delete-namespace', help='Delete a Service Bus namespace')
    
    args = parser.parse_args()
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    try:
        # Get Azure clients
        management_client, subscription_id = get_clients()
        
        # Process the requested operation
        if args.operation == "create-namespace":
            create_namespace(
                management_client, 
                args.resource_group, 
                args.namespace, 
                args.location, 
                args.sku
            )
            
        elif args.operation == "create-queue":
            create_queue(
                management_client, 
                args.resource_group, 
                args.namespace, 
                args.queue,
                args.max_size,
                args.enable_partitioning
            )
            
        elif args.operation == "list-queues":
            queues = list_queues(
                management_client, 
                args.resource_group, 
                args.namespace
            )
            
        elif args.operation == "send-messages":
            connection_string = get_queue_connection_string(
                management_client, 
                args.resource_group, 
                args.namespace
            )
            
            if connection_string:
                message_ids = send_messages(
                    connection_string, 
                    args.queue, 
                    args.count
                )
            
        elif args.operation == "receive-messages":
            connection_string = get_queue_connection_string(
                management_client, 
                args.resource_group, 
                args.namespace
            )
            
            if connection_string:
                messages = receive_messages(
                    connection_string, 
                    args.queue, 
                    args.count,
                    args.wait_time
                )
            
        elif args.operation == "delete-queue":
            delete_queue(
                management_client, 
                args.resource_group, 
                args.namespace, 
                args.queue
            )
            
        elif args.operation == "delete-namespace":
            delete_namespace(
                management_client, 
                args.resource_group, 
                args.namespace
            )
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 