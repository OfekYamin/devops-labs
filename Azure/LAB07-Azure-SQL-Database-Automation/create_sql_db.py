#!/usr/bin/env python3
"""
Azure SQL Database Automation Script

This script demonstrates how to automate the creation, management, and deletion
of Azure SQL Databases using the Azure SDK for Python.

Students should implement the TODO sections to complete the lab.
"""

import os
import sys
import time
import random
import string
import argparse
import getpass
from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceExistsError, HttpResponseError

def get_clients():
    """
    Create Azure SDK clients for SQL and Resource Management.
    
    TODO: Implement this function to:
    1. Get subscription ID from environment variables
    2. Create DefaultAzureCredential
    3. Create and return SqlManagementClient and ResourceManagementClient
    
    Returns:
        tuple: (sql_client, resource_client, subscription_id)
    """
    # TODO: Get subscription ID from environment variables
    
    # TODO: Create credential using DefaultAzureCredential
    
    # TODO: Create and return SQL and Resource management clients
    pass

def create_sql_server(sql_client, resource_group, server_name, location, 
                     admin_username, admin_password):
    """
    Create an Azure SQL Server instance.
    
    TODO: Implement this function to:
    1. Create a SQL Server with specified parameters
    2. Wait for the operation to complete
    3. Return server properties
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        location (str): Azure region
        admin_username (str): SQL Server admin username
        admin_password (str): SQL Server admin password
        
    Returns:
        dict: SQL Server properties
    """
    print(f"Creating SQL Server: {server_name} in {resource_group}")
    
    # TODO: Validate admin password (must be at least 8 characters, contain uppercase, lowercase, digits, special chars)
    
    # TODO: Create SQL Server with begin_create_or_update and wait for completion
    
    # TODO: Return server properties
    pass

def create_firewall_rule(sql_client, resource_group, server_name, rule_name, 
                        start_ip, end_ip):
    """
    Create a firewall rule for the SQL Server.
    
    TODO: Implement this function to:
    1. Create a firewall rule with specified IP range
    2. Return rule properties
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        rule_name (str): Firewall rule name
        start_ip (str): Start IP address range
        end_ip (str): End IP address range
        
    Returns:
        dict: Firewall rule properties
    """
    print(f"Creating firewall rule: {rule_name} for SQL Server {server_name}")
    
    # TODO: Create firewall rule and return properties
    pass

def create_sql_database(sql_client, resource_group, server_name, database_name, 
                       location, sku_name="Basic", sku_tier="Basic"):
    """
    Create an Azure SQL Database.
    
    TODO: Implement this function to:
    1. Create a SQL Database with specified parameters
    2. Wait for the operation to complete
    3. Return database properties
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        database_name (str): SQL Database name
        location (str): Azure region
        sku_name (str): SKU name (e.g., "Basic", "Standard", "Premium")
        sku_tier (str): SKU tier (e.g., "Basic", "Standard", "Premium")
        
    Returns:
        dict: SQL Database properties
    """
    print(f"Creating SQL Database: {database_name} on server {server_name}")
    
    # TODO: Create SQL Database with begin_create_or_update and wait for completion
    
    # TODO: Return database properties
    pass

def list_databases(sql_client, resource_group, server_name):
    """
    List all databases on the specified SQL Server.
    
    TODO: Implement this function to:
    1. List all databases on the server
    2. Return the list of databases
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        
    Returns:
        list: List of databases
    """
    print(f"Listing databases on SQL Server: {server_name}")
    
    # TODO: List databases and return the result
    pass

def delete_sql_database(sql_client, resource_group, server_name, database_name):
    """
    Delete an Azure SQL Database.
    
    TODO: Implement this function to:
    1. Delete the specified database
    2. Wait for the operation to complete
    3. Return success status
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        database_name (str): SQL Database name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting SQL Database: {database_name} from server {server_name}")
    
    # TODO: Delete SQL Database and return success status
    pass

def delete_sql_server(sql_client, resource_group, server_name):
    """
    Delete an Azure SQL Server instance.
    
    TODO: Implement this function to:
    1. Delete the specified SQL Server
    2. Wait for the operation to complete
    3. Return success status
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting SQL Server: {server_name} from resource group {resource_group}")
    
    # TODO: Delete SQL Server and return success status
    pass

def generate_password():
    """
    Generate a random password that meets Azure SQL Server requirements.
    
    Returns:
        str: Random password
    """
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    
    # Ensure at least one character from each category
    pwd = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Add more random characters to reach the minimum length of 12
    all_chars = uppercase + lowercase + digits + special
    pwd.extend(random.choice(all_chars) for _ in range(8))
    
    # Shuffle the password
    random.shuffle(pwd)
    return ''.join(pwd)

def main():
    """Main function to handle command line arguments and execute operations."""
    parser = argparse.ArgumentParser(description='Azure SQL Database Automation Tool')
    
    # Resource group, server, database arguments
    parser.add_argument('--resource-group', required=True, help='Resource group name')
    parser.add_argument('--server-name', required=True, help='SQL Server name')
    parser.add_argument('--location', default='eastus', help='Azure region (default: eastus)')
    parser.add_argument('--db-name', help='SQL Database name')
    
    # Operations
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')
    
    # Create SQL Server operation
    create_server_parser = subparsers.add_parser('create-server', help='Create a SQL Server')
    create_server_parser.add_argument('--admin-username', default='sqladmin', help='SQL Server admin username')
    create_server_parser.add_argument('--admin-password', help='SQL Server admin password (if not provided, a random one will be generated)')
    
    # Create Firewall Rule operation
    create_fw_parser = subparsers.add_parser('create-firewall-rule', help='Create a firewall rule for the SQL Server')
    create_fw_parser.add_argument('--rule-name', required=True, help='Firewall rule name')
    create_fw_parser.add_argument('--start-ip', required=True, help='Start IP address')
    create_fw_parser.add_argument('--end-ip', required=True, help='End IP address')
    
    # Create SQL Database operation
    create_db_parser = subparsers.add_parser('create-database', help='Create a SQL Database')
    create_db_parser.add_argument('--sku-name', default='Basic', choices=['Basic', 'Standard', 'Premium', 'GeneralPurpose', 'BusinessCritical'], 
                                help='SKU name (default: Basic)')
    create_db_parser.add_argument('--sku-tier', default='Basic', choices=['Basic', 'Standard', 'Premium', 'GeneralPurpose', 'BusinessCritical'], 
                                help='SKU tier (default: Basic)')
    
    # List Databases operation
    list_parser = subparsers.add_parser('list-databases', help='List databases on a SQL Server')
    
    # Delete SQL Database operation
    delete_db_parser = subparsers.add_parser('delete-database', help='Delete a SQL Database')
    
    # Delete SQL Server operation
    delete_server_parser = subparsers.add_parser('delete-server', help='Delete a SQL Server')
    
    args = parser.parse_args()
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    try:
        # Get Azure clients
        sql_client, resource_client, subscription_id = get_clients()
        
        # Process the requested operation
        if args.operation == "create-server":
            # If no admin password provided, generate one
            admin_password = args.admin_password
            if not admin_password:
                admin_password = generate_password()
                print(f"Generated Admin Password: {admin_password}")
                print("Please save this password securely!")
            
            create_sql_server(
                sql_client,
                args.resource_group,
                args.server_name,
                args.location,
                args.admin_username,
                admin_password
            )
            
        elif args.operation == "create-firewall-rule":
            create_firewall_rule(
                sql_client,
                args.resource_group,
                args.server_name,
                args.rule_name,
                args.start_ip,
                args.end_ip
            )
            
        elif args.operation == "create-database":
            if not args.db_name:
                print("Error: --db-name is required for create-database operation")
                sys.exit(1)
                
            create_sql_database(
                sql_client,
                args.resource_group,
                args.server_name,
                args.db_name,
                args.location,
                args.sku_name,
                args.sku_tier
            )
            
        elif args.operation == "list-databases":
            list_databases(
                sql_client,
                args.resource_group,
                args.server_name
            )
            
        elif args.operation == "delete-database":
            if not args.db_name:
                print("Error: --db-name is required for delete-database operation")
                sys.exit(1)
                
            delete_sql_database(
                sql_client,
                args.resource_group,
                args.server_name,
                args.db_name
            )
            
        elif args.operation == "delete-server":
            delete_sql_server(
                sql_client,
                args.resource_group,
                args.server_name
            )
    
    except HttpResponseError as e:
        print(f"Azure API error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 