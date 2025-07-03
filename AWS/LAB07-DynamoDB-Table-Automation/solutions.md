# LAB07 - DynamoDB Table Automation: Solutions

This document contains the complete solution for the DynamoDB Table Automation lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for dynamodb_script.py

```python
#!/usr/bin/env python3
"""
AWS LAB07 - DynamoDB Table Automation

This script demonstrates how to use boto3 to create and interact with an Amazon DynamoDB table.
It covers table creation, inserting items, retrieving data, and listing tables.

Usage:
    python dynamodb_script.py
"""

import boto3
import time
from botocore.exceptions import ClientError

# Configure the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='eu-west-1')

# Define your table name
table_name = 'DevOpsUsers'


def create_table(table_name):
    """
    Creates a DynamoDB table with a partition key.
    
    Args:
        table_name (str): The name of the table to create
        
    Returns:
        dict: The response from the create_table call
    """
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'  # String type
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            },
            Tags=[
                {
                    'Key': 'Environment',
                    'Value': 'DevOps-Lab'
                }
            ]
        )
        
        print(f"Creating DynamoDB table: {table_name}...")
        print("Table creation initiated. Waiting for table to become active...")
        
        # Wait for the table to be created
        wait_for_table_creation(table_name)
        
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"Table {table_name} already exists")
        else:
            print(f"Error creating table: {e}")
        return None


def wait_for_table_creation(table_name):
    """
    Waits for a table to finish creating by polling its status.
    
    Args:
        table_name (str): The name of the table to wait for
    """
    while True:
        try:
            response = dynamodb.describe_table(TableName=table_name)
            status = response['Table']['TableStatus']
            
            if status == 'ACTIVE':
                print("Table is now active!")
                break
                
            print(f"Table status: {status}, waiting...")
            time.sleep(5)  # Wait for 5 seconds before polling again
            
        except ClientError as e:
            print(f"Error checking table status: {e}")
            break


def list_tables():
    """
    Lists all DynamoDB tables in the account.
    
    Returns:
        list: A list of table names
    """
    try:
        response = dynamodb.list_tables()
        tables = response.get('TableNames', [])
        
        print("\nCurrent DynamoDB tables in your account:")
        for table in tables:
            print(f"- {table}")
            
        return tables
    except ClientError as e:
        print(f"Error listing tables: {e}")
        return []


def insert_item(table_name, item):
    """
    Inserts an item into a DynamoDB table.
    
    Args:
        table_name (str): The name of the table
        item (dict): The item to insert
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Convert Python types to DynamoDB types
        dynamodb_item = {
            'username': {'S': item['username']},
            'role': {'S': item['role']},
            'email': {'S': item['email']},
            'active': {'BOOL': item['active']},
            'last_login': {'S': item['last_login']}
        }
        
        print(f"\nInserting item: {item}")
        response = dynamodb.put_item(
            TableName=table_name,
            Item=dynamodb_item
        )
        
        print("Item inserted successfully!")
        return True
    except ClientError as e:
        print(f"Error inserting item: {e}")
        return False


def get_item(table_name, key):
    """
    Retrieves an item from a DynamoDB table by its key.
    
    Args:
        table_name (str): The name of the table
        key (dict): The key of the item to retrieve
        
    Returns:
        dict: The retrieved item
    """
    try:
        # Convert Python key to DynamoDB format
        dynamodb_key = {
            'username': {'S': key['username']}
        }
        
        print(f"\nRetrieving item with username: {key['username']}")
        response = dynamodb.get_item(
            TableName=table_name,
            Key=dynamodb_key
        )
        
        # Check if item exists
        if 'Item' in response:
            # Convert DynamoDB format back to Python dict
            item = {
                'username': response['Item']['username']['S'],
                'role': response['Item']['role']['S'],
                'email': response['Item']['email']['S'],
                'active': response['Item']['active']['BOOL'],
                'last_login': response['Item']['last_login']['S']
            }
            print(f"Retrieved item: {item}")
            return item
        else:
            print("Item not found")
            return None
            
    except ClientError as e:
        print(f"Error retrieving item: {e}")
        return None


def delete_table(table_name):
    """
    Deletes a DynamoDB table.
    
    Args:
        table_name (str): The name of the table to delete
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"\nDeleting table: {table_name}")
        response = dynamodb.delete_table(TableName=table_name)
        print(f"Table deletion initiated for {table_name}")
        return True
    except ClientError as e:
        print(f"Error deleting table: {e}")
        return False


if __name__ == "__main__":
    print("AWS DynamoDB Table Automation Tool")
    print("================================")
    
    # Create a DynamoDB table
    create_table(table_name)
    
    # List tables to verify creation
    list_tables()
    
    # Insert an item
    user_item = {
        'username': 'alice',
        'role': 'admin',
        'email': 'alice@example.com',
        'active': True,
        'last_login': '2023-09-15'
    }
    insert_item(table_name, user_item)
    
    # Retrieve the item to verify
    get_item(table_name, {'username': 'alice'})
    
    # Uncomment to clean up (delete the table)
    # delete_table(table_name)
    
    print("\n⚠️  IMPORTANT: Remember to delete the table when done to avoid charges!")
    print("To delete the table, run this script with the cleanup flag or use:")
    print("dynamodb.delete_table(TableName=table_name)")
```

## Key Learning Points

1. **Boto3 DynamoDB Client**: 
   - The client interface (`boto3.client('dynamodb')`) provides direct access to DynamoDB operations
   - Client APIs require data to be formatted according to DynamoDB's data types (S, N, BOOL, etc.)

2. **Table Creation**:
   - Tables require a key schema (partition key, optional sort key)
   - AttributeDefinitions must be provided for all key attributes
   - ProvisionedThroughput defines read/write capacity

3. **Waiting for Table Creation**:
   - DynamoDB tables are created asynchronously
   - Best practice is to poll the table status until it becomes 'ACTIVE'

4. **Error Handling**:
   - Using `botocore.exceptions.ClientError` to catch AWS service errors
   - Handling common errors like 'ResourceInUseException'

5. **Item Operations**:
   - Converting between Python native types and DynamoDB attribute types
   - put_item() for insertion, get_item() for retrieval
   - Understanding DynamoDB's data type descriptors (S, N, BOOL, etc.)

6. **Cleanup**:
   - Always clean up resources to avoid unnecessary charges
   - Table deletion is asynchronous, similar to creation

## Common Issues and Troubleshooting

1. **Missing Region**: 
   - Error if you don't specify a region and don't have AWS configuration
   - Solution: Always specify region_name or configure AWS CLI

2. **Permissions Issues**:
   - Ensure your AWS credentials have DynamoDB permissions
   - Check for IAM policies that restrict DynamoDB operations

3. **ResourceInUseException**:
   - Occurs when trying to create a table that already exists
   - Handle with try/except and check if the table exists first

4. **Waiting Time**:
   - Table creation can take time (typically 10-30 seconds)
   - Don't try to use a table before it's in 'ACTIVE' state

5. **Cost Management**:
   - Provisioned capacity incurs charges even when not used
   - Use on-demand billing for testing or delete tables when done 