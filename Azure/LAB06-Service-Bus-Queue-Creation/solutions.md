# Solutions: Azure Service Bus Queue Automation

This document provides the reference solutions for the Azure Service Bus Queue lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

Below is the full implementation of the `servicebus_queue.py` script:

```python
#!/usr/bin/env python3
"""
Azure Service Bus Queue Automation Script

This script demonstrates how to interact with Azure Service Bus to create namespaces, 
queues, send messages, and receive messages using the Azure SDK for Python.
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
from azure.core.exceptions import ResourceExistsError, HttpResponseError, ResourceNotFoundError

def get_clients():
    """
    Create Azure SDK clients for Service Bus management and messaging.
    
    Returns:
        tuple: (management_client, subscription_id)
    """
    # Get subscription ID from environment variables
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        sys.exit(1)
    
    # Create credential using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
    except Exception as e:
        print(f"Error creating credential: {e}")
        print("Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set.")
        sys.exit(1)
    
    # Create and return Service Bus management client
    sb_client = ServiceBusManagementClient(credential, subscription_id)
    
    return sb_client, subscription_id

def create_namespace(management_client, resource_group, namespace_name, location="eastus", sku="Basic"):
    """
    Create a Service Bus namespace.
    
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
    
    # Create namespace with begin_create_or_update and wait for completion
    try:
        # Define namespace parameters
        namespace_params = {
            'location': location,
            'sku': {'name': sku, 'tier': sku}
        }
        
        # Create namespace (this is a long-running operation)
        namespace_poller = management_client.namespaces.begin_create_or_update(
            resource_group,
            namespace_name,
            namespace_params
        )
        
        # Wait for the operation to complete
        namespace = namespace_poller.result()
        
        # Print the result
        print(f"Service Bus namespace '{namespace_name}' created successfully.")
        print(f"Namespace ID: {namespace.id}")
        print(f"Location: {namespace.location}")
        print(f"SKU: {namespace.sku.name}")
        
        # Return namespace properties as a dictionary
        return {
            'id': namespace.id,
            'name': namespace.name,
            'location': namespace.location,
            'sku': namespace.sku.name,
            'provisioning_state': namespace.provisioning_state
        }
    
    except ResourceExistsError:
        print(f"Namespace '{namespace_name}' already exists.")
        
        # Get the existing namespace
        namespace = management_client.namespaces.get(resource_group, namespace_name)
        
        return {
            'id': namespace.id,
            'name': namespace.name,
            'location': namespace.location,
            'sku': namespace.sku.name,
            'provisioning_state': namespace.provisioning_state
        }
    
    except HttpResponseError as e:
        print(f"Error creating namespace: {e}")
        return None

def create_queue(management_client, resource_group, namespace_name, queue_name, 
                max_size_mb=1024, enable_partitioning=False):
    """
    Create a queue in a Service Bus namespace.
    
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
    
    # Create queue with create_or_update
    try:
        # Define queue parameters
        queue_params = {
            'max_size_in_megabytes': max_size_mb,
            'enable_partitioning': enable_partitioning,
            'dead_lettering_on_message_expiration': True,
            'default_message_time_to_live': 'P14D',  # 14 days
            'lock_duration': 'PT30S'  # 30 seconds
        }
        
        # Create the queue
        queue = management_client.queues.create_or_update(
            resource_group,
            namespace_name,
            queue_name,
            queue_params
        )
        
        # Print the result
        print(f"Queue '{queue_name}' created successfully.")
        print(f"Queue ID: {queue.id}")
        print(f"Max Size: {queue.max_size_in_megabytes} MB")
        print(f"Partitioning: {'Enabled' if queue.enable_partitioning else 'Disabled'}")
        
        # Return queue properties as a dictionary
        return {
            'id': queue.id,
            'name': queue.name,
            'max_size_in_megabytes': queue.max_size_in_megabytes,
            'enable_partitioning': queue.enable_partitioning,
            'status': queue.status
        }
    
    except HttpResponseError as e:
        print(f"Error creating queue: {e}")
        return None

def list_queues(management_client, resource_group, namespace_name):
    """
    List all queues in a Service Bus namespace.
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        
    Returns:
        list: List of queues
    """
    print(f"Listing queues in namespace: {namespace_name}")
    
    try:
        # Get all queues in the namespace
        queues = management_client.queues.list_by_namespace(
            resource_group,
            namespace_name
        )
        
        # Convert to list and print details
        queue_list = []
        
        for queue in queues:
            queue_info = {
                'id': queue.id,
                'name': queue.name,
                'max_size_in_megabytes': queue.max_size_in_megabytes,
                'enable_partitioning': queue.enable_partitioning,
                'status': queue.status
            }
            queue_list.append(queue_info)
            
            print(f"- {queue.name} ({queue.status}):")
            print(f"  ID: {queue.id}")
            print(f"  Max Size: {queue.max_size_in_megabytes} MB")
            print(f"  Partitioning: {'Enabled' if queue.enable_partitioning else 'Disabled'}")
        
        if not queue_list:
            print("No queues found in the namespace.")
        
        return queue_list
    
    except HttpResponseError as e:
        print(f"Error listing queues: {e}")
        return []

def get_queue_connection_string(management_client, resource_group, namespace_name):
    """
    Get the connection string for a Service Bus namespace.
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        
    Returns:
        str: Connection string
    """
    print(f"Getting connection string for namespace: {namespace_name}")
    
    try:
        # List the keys for the namespace
        keys = management_client.namespaces.list_keys(
            resource_group,
            namespace_name,
            'RootManageSharedAccessKey'  # Default authorization rule
        )
        
        # Get the primary connection string
        connection_string = keys.primary_connection_string
        
        # Print a masked version of the connection string
        masked_conn_str = connection_string[:50] + '...' if len(connection_string) > 50 else connection_string
        print(f"Connection string retrieved: {masked_conn_str}")
        
        return connection_string
    
    except HttpResponseError as e:
        print(f"Error getting connection string: {e}")
        return None

def send_messages(connection_string, queue_name, message_count=5):
    """
    Send messages to a Service Bus queue.
    
    Args:
        connection_string (str): The connection string to the Service Bus namespace
        queue_name (str): The name of the queue
        message_count (int): Number of test messages to send
        
    Returns:
        list: List of message IDs that were sent
    """
    print(f"Sending {message_count} messages to queue: {queue_name}")
    
    # Create ServiceBusClient from connection string
    message_ids = []
    
    try:
        # Create a Service Bus client using the connection string
        with ServiceBusClient.from_connection_string(connection_string) as client:
            # Create a sender for the queue
            with client.get_queue_sender(queue_name) as sender:
                # Create and send a batch of messages
                for i in range(message_count):
                    # Create a unique message ID
                    message_id = str(uuid.uuid4())
                    
                    # Create message content
                    message_content = f"Test message {i+1} - {datetime.now().isoformat()}"
                    
                    # Create a Service Bus message
                    message = ServiceBusMessage(
                        body=message_content,
                        message_id=message_id,
                        subject=f"Message {i+1} of {message_count}"
                    )
                    
                    # Send the message
                    sender.send_messages(message)
                    
                    # Record the message ID
                    message_ids.append(message_id)
                    
                    # Print information about the sent message
                    print(f"Sent message {i+1}: ID={message_id}")
        
        print(f"Successfully sent {message_count} messages.")
        return message_ids
    
    except Exception as e:
        print(f"Error sending messages: {e}")
        return message_ids

def receive_messages(connection_string, queue_name, max_message_count=5, max_wait_time=5):
    """
    Receive messages from a Service Bus queue.
    
    Args:
        connection_string (str): The connection string to the Service Bus namespace
        queue_name (str): The name of the queue
        max_message_count (int): Maximum number of messages to receive
        max_wait_time (int): Maximum time to wait in seconds
        
    Returns:
        list: List of received message contents
    """
    print(f"Receiving up to {max_message_count} messages from queue: {queue_name}")
    
    # Create ServiceBusClient from connection string
    messages = []
    
    try:
        # Create a Service Bus client using the connection string
        with ServiceBusClient.from_connection_string(connection_string) as client:
            # Create a receiver for the queue
            with client.get_queue_receiver(queue_name, max_wait_time=max_wait_time) as receiver:
                # Receive a batch of messages
                received_messages = receiver.receive_messages(max_message_count=max_message_count, max_wait_time=max_wait_time)
                
                # Process each message
                for msg in received_messages:
                    # Get message content
                    message_body = str(msg.body.decode('utf-8'))
                    message_id = msg.message_id
                    
                    # Add to the list of received messages
                    messages.append({
                        'id': message_id,
                        'body': message_body,
                        'sequence_number': msg.sequence_number,
                        'subject': msg.subject
                    })
                    
                    # Print information about the received message
                    print(f"Received message: ID={message_id}, Body={message_body}")
                    
                    # Complete the message (remove it from the queue)
                    receiver.complete_message(msg)
                    print(f"Message completed and removed from queue.")
        
        if not messages:
            print("No messages received within the specified time.")
        else:
            print(f"Successfully received {len(messages)} messages.")
        
        return messages
    
    except Exception as e:
        print(f"Error receiving messages: {e}")
        return messages

def delete_queue(management_client, resource_group, namespace_name, queue_name):
    """
    Delete a Service Bus queue.
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        queue_name (str): Queue name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting queue: {queue_name} from namespace {namespace_name}")
    
    try:
        # Delete the queue
        management_client.queues.delete(
            resource_group,
            namespace_name,
            queue_name
        )
        
        print(f"Queue '{queue_name}' deleted successfully.")
        return True
    
    except ResourceNotFoundError:
        print(f"Queue '{queue_name}' not found.")
        return False
    
    except HttpResponseError as e:
        print(f"Error deleting queue: {e}")
        return False

def delete_namespace(management_client, resource_group, namespace_name):
    """
    Delete a Service Bus namespace.
    
    Args:
        management_client: Azure Service Bus Management client
        resource_group (str): Resource group name
        namespace_name (str): Namespace name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting namespace: {namespace_name} from resource group {resource_group}")
    
    try:
        # Delete the namespace (this is a long-running operation)
        namespace_poller = management_client.namespaces.begin_delete(
            resource_group,
            namespace_name
        )
        
        # Wait for the operation to complete
        print("Deleting namespace... This may take a minute or two.")
        namespace_poller.result()
        
        print(f"Namespace '{namespace_name}' deleted successfully.")
        return True
    
    except ResourceNotFoundError:
        print(f"Namespace '{namespace_name}' not found.")
        return False
    
    except HttpResponseError as e:
        print(f"Error deleting namespace: {e}")
        return False

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
```

## Sample Usage

### 1. Create a Service Bus Namespace
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue create-namespace
```

### 2. Create a Queue
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue create-queue
```

### 3. List Queues
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue list-queues
```

### 4. Send Messages
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue send-messages --count 10
```

### 5. Receive Messages
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue receive-messages --count 10 --wait-time 10
```

### 6. Delete Queue
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue delete-queue
```

### 7. Delete Namespace
```bash
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue delete-namespace
```

## Key Learning Points

1. **Azure Service Bus Concepts**
   - Service Bus provides reliable message queuing for asynchronous communication
   - Namespaces are containers for messaging components like queues, topics, and relays
   - Queues provide First In, First Out (FIFO) message delivery to one or more consumers

2. **Service Bus Namespace Tiers**
   - **Basic**: Simplest tier with basic queuing functionality
   - **Standard**: Includes topics for publish/subscribe scenarios
   - **Premium**: Higher throughput, dedicated resources, and predictable performance

3. **Queue Properties**
   - **Partitioning**: Splits a queue across multiple message brokers for higher throughput
   - **Dead-letter queue**: Holds messages that can't be processed
   - **Time-to-live**: Automatic expiration of messages after a period
   - **Lock duration**: Time a message is locked for a receiver

4. **Message Operations**
   - **Sending**: Writing messages to a queue
   - **Receiving**: Reading and processing messages from a queue
   - **Completing**: Removing a message from the queue after successful processing
   - **Abandoning**: Releasing a lock on a message so it can be processed again

5. **Azure SDK for Python**
   - **ServiceBusManagementClient**: For creating and managing namespaces and queues
   - **ServiceBusClient**: For sending and receiving messages
   - **DefaultAzureCredential**: For simplified authentication

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "DefaultAzureCredential failed to retrieve a token"
   - **Solution**: Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set correctly

2. **Namespace Creation Delays**
   - **Problem**: Namespace creation takes a long time
   - **Solution**: Service Bus namespace creation is a long-running operation and can take several minutes. The code uses `begin_create_or_update().result()` to wait for completion.

3. **Queue Not Found**
   - **Problem**: "Queue 'X' not found" when trying to send or receive messages
   - **Solution**: Ensure the queue exists in the namespace. Use the list-queues operation to verify.

4. **Message Visibility**
   - **Problem**: Messages received but not visible to other receivers
   - **Solution**: This is expected behavior. Messages are locked when received and must be completed to be removed from the queue or abandoned to be visible again.

5. **Connection String Format**
   - **Problem**: "Invalid connection string format" when sending or receiving
   - **Solution**: Ensure you're using the primary connection string from the namespace keys. The connection string should start with "Endpoint=sb://".

## Service Bus Best Practices

1. **Exception Handling**
   - Implement proper exception handling for transient errors
   - Use exponential backoff for retries (not shown in this example)

2. **Message Size**
   - Keep messages small (<256 KB for Basic/Standard tiers)
   - Use message batching for better throughput

3. **Security**
   - Use Managed Identity where possible instead of connection strings
   - Implement the principle of least privilege for SAS tokens

4. **Queue Design**
   - Consider partitioning for high-throughput scenarios
   - Set appropriate TTL for your business requirements
   - Use dead-letter queues for handling poison messages

5. **Operational Considerations**
   - Monitor queue length and processing rates
   - Implement proper cleanup of resources
   - Consider using auto-forwarding for complex workflows

## Cleanup

Always clean up Azure resources when you're done to avoid unexpected charges:

```bash
# Delete the queue
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue delete-queue

# Delete the namespace (this will delete all queues in the namespace)
python servicebus_queue.py --resource-group devops-lab-rg --namespace devopsbus --queue devopsqueue delete-namespace
```

## Extending This Lab

1. **Topics and Subscriptions**: Implement publish/subscribe patterns using topics
2. **Message Sessions**: Group related messages that need to be processed together
3. **Scheduled Messages**: Send messages to be delivered at a future time
4. **Auto-Forwarding**: Chain queues together for complex workflows
5. **Message Filters**: Filter messages for specific subscriptions based on properties 