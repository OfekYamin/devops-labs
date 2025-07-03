#!/usr/bin/env python3
"""
DynamoDB Table Automation Script

This script demonstrates how to automate DynamoDB operations using boto3.
Complete the TODOs to implement full functionality.
"""

import boto3
import time
import argparse
import sys
from botocore.exceptions import ClientError

# Default settings
DEFAULT_REGION = 'eu-west-1'
DEFAULT_TABLE_NAME = 'DevOpsUsers'

def create_table(table_name, region=DEFAULT_REGION):
    """
    Create a DynamoDB table with a partition key.
    
    Args:
        table_name (str): Name of the table to create
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO: Implement table creation with the following:
    # - Create a boto3 DynamoDB client with boto3.client('dynamodb', region_name=region)
    # - Create a table with 'username' as the partition key (string type)
    # - Set provisioned throughput to 5 read and 5 write capacity units
    # - Add a tag with key 'Environment' and value 'DevOps-Lab'
    # - Implement error handling (check if table already exists)
    
    print(f"TODO: Create DynamoDB table '{table_name}' in region '{region}'")
    return False

def wait_for_table_creation(table_name, region=DEFAULT_REGION, max_attempts=10):
    """
    Wait for a table to finish creating and become ACTIVE.
    
    Args:
        table_name (str): Name of the table to wait for
        region (str): AWS region
        max_attempts (int): Maximum number of attempts to check status
        
    Returns:
        bool: True if table is active, False otherwise
    """
    # TODO: Implement waiting logic:
    # - Create a boto3 DynamoDB client
    # - Poll the table status in a loop with a wait time between attempts
    # - Use client.describe_table() to get the table status
    # - Exit the loop when the table becomes ACTIVE
    # - Implement a timeout mechanism using max_attempts
    
    print(f"TODO: Wait for table '{table_name}' to become active")
    return False

def list_tables(region=DEFAULT_REGION):
    """
    List all DynamoDB tables in the account.
    
    Args:
        region (str): AWS region
        
    Returns:
        list: Names of tables in the region
    """
    # TODO: Implement table listing:
    # - Create a boto3 DynamoDB client
    # - Use client.list_tables() to get a list of all table names
    # - Print the table names in a formatted way
    # - Return the list of table names
    
    print(f"TODO: List all DynamoDB tables in region '{region}'")
    return []

def insert_item(table_name, item, region=DEFAULT_REGION):
    """
    Insert an item into a DynamoDB table.
    
    Args:
        table_name (str): Name of the table
        item (dict): Item to insert (must contain the partition key)
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO: Implement item insertion:
    # - Create a boto3 DynamoDB client
    # - Convert Python types to DynamoDB format (e.g., strings to {'S': value})
    # - Use client.put_item() to insert the item
    # - Print confirmation message
    # - Implement error handling
    
    print(f"TODO: Insert item into table '{table_name}': {item}")
    return False

def get_item(table_name, key_value, key_name='username', region=DEFAULT_REGION):
    """
    Retrieve an item from a DynamoDB table.
    
    Args:
        table_name (str): Name of the table
        key_value (str): Value of the partition key
        key_name (str): Name of the partition key
        region (str): AWS region
        
    Returns:
        dict: The retrieved item or None if not found
    """
    # TODO: Implement item retrieval:
    # - Create a boto3 DynamoDB client
    # - Format the key in DynamoDB format (e.g., {key_name: {'S': key_value}})
    # - Retrieve the item using client.get_item() with the key
    # - Convert the returned DynamoDB format to Python dict
    # - Print the retrieved item if found
    # - Handle the case when the item is not found
    # - Implement error handling
    
    print(f"TODO: Get item with {key_name}='{key_value}' from table '{table_name}'")
    return None

def delete_table(table_name, region=DEFAULT_REGION):
    """
    Delete a DynamoDB table.
    
    Args:
        table_name (str): Name of the table to delete
        region (str): AWS region
        
    Returns:
        bool: True if successful, False otherwise
    """
    # TODO: Implement table deletion:
    # - Create a boto3 DynamoDB client
    # - Use client.delete_table() to delete the table
    # - Print confirmation message
    # - Implement error handling
    
    print(f"TODO: Delete table '{table_name}' in region '{region}'")
    return False

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='AWS DynamoDB Table Automation Tool')
    parser.add_argument('--table-name', default=DEFAULT_TABLE_NAME,
                        help=f'Name of the DynamoDB table (default: {DEFAULT_TABLE_NAME})')
    parser.add_argument('--region', default=DEFAULT_REGION,
                        help=f'AWS region (default: {DEFAULT_REGION})')
    parser.add_argument('--cleanup', action='store_true',
                        help='Delete the table after running the script')
    
    args = parser.parse_args()
    
    print("AWS DynamoDB Table Automation Tool")
    print("================================")
    
    # Create the table
    print(f"Creating DynamoDB table: {args.table_name}...")
    success = create_table(args.table_name, args.region)
    if not success:
        print("Failed to initiate table creation.")
        return
    
    # Wait for the table to become active
    print("Table creation initiated. Waiting for table to become active...")
    success = wait_for_table_creation(args.table_name, args.region)
    if not success:
        print("Failed to confirm table creation.")
        return
    
    # List tables to verify the table was created
    print("\nCurrent DynamoDB tables in your account:")
    tables = list_tables(args.region)
    
    # Insert a sample item
    sample_item = {
        'username': 'alice',
        'role': 'admin',
        'email': 'alice@example.com',
        'active': True,
        'last_login': '2023-09-15'
    }
    print(f"\nInserting item: {sample_item}")
    success = insert_item(args.table_name, sample_item, args.region)
    if not success:
        print("Failed to insert item.")
    
    # Retrieve the inserted item
    print(f"\nRetrieving item with username: {sample_item['username']}")
    retrieved_item = get_item(args.table_name, sample_item['username'], 'username', args.region)
    
    # Cleanup if requested
    if args.cleanup:
        print(f"\nCleaning up - deleting table {args.table_name}...")
        delete_table(args.table_name, args.region)
    else:
        print(f"\n⚠️  IMPORTANT: Remember to delete the table '{args.table_name}' when done to avoid charges!")
        print(f"To delete: python {sys.argv[0]} --table-name {args.table_name} --region {args.region} --cleanup")

if __name__ == "__main__":
    main() 