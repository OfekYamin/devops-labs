# Solutions: Azure SQL Database Automation

This document provides the reference solutions for the Azure SQL Database lab. **Important: Try to complete the lab on your own before looking at these solutions.**

## Complete Implementation

Below is the full implementation of the `create_sql_db.py` script:

```python
#!/usr/bin/env python3
"""
Azure SQL Database Automation Script

This script demonstrates how to automate the creation, management, and deletion
of Azure SQL Databases using the Azure SDK for Python.
"""

import os
import sys
import time
import random
import string
import argparse
import getpass
import re
from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceExistsError, HttpResponseError, ResourceNotFoundError

def get_clients():
    """
    Create Azure SDK clients for SQL and Resource Management.
    
    Returns:
        tuple: (sql_client, resource_client, subscription_id)
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
    
    # Create and return SQL and Resource management clients
    sql_client = SqlManagementClient(credential, subscription_id)
    resource_client = ResourceManagementClient(credential, subscription_id)
    
    return sql_client, resource_client, subscription_id

def validate_password(password):
    """
    Validate that a password meets Azure SQL Server requirements.
    
    Args:
        password (str): Password to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    # At least 8 characters
    if len(password) < 8:
        return False
    
    # Must contain at least one: uppercase, lowercase, digit, special character
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
        return False
    
    return True

def create_sql_server(sql_client, resource_group, server_name, location, 
                     admin_username, admin_password):
    """
    Create an Azure SQL Server instance.
    
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
    
    # Validate admin password
    if not validate_password(admin_password):
        print("Error: Password does not meet Azure SQL Server requirements.")
        print("Password must have at least 8 characters and contain uppercase, lowercase, digits, and special characters.")
        sys.exit(1)
    
    # Create SQL Server with begin_create_or_update and wait for completion
    try:
        # Define server parameters
        server_params = {
            "location": location,
            "administrator_login": admin_username,
            "administrator_login_password": admin_password,
            "version": "12.0",  # Use SQL Server version 12.0
            "minimal_tls_version": "1.2"  # Enforce TLS 1.2
        }
        
        # Create SQL Server (this is a long-running operation)
        server_poller = sql_client.servers.begin_create_or_update(
            resource_group,
            server_name,
            server_params
        )
        
        # Wait for the operation to complete
        server = server_poller.result()
        
        # Print the result
        print(f"SQL Server '{server_name}' created successfully.")
        print(f"Server ID: {server.id}")
        print(f"Fully Qualified Domain Name: {server.fully_qualified_domain_name}")
        
        # Return server properties as a dictionary
        return {
            'id': server.id,
            'name': server.name,
            'location': server.location,
            'fully_qualified_domain_name': server.fully_qualified_domain_name,
            'version': server.version
        }
    
    except ResourceExistsError:
        print(f"SQL Server '{server_name}' already exists.")
        
        # Get the existing server
        server = sql_client.servers.get(resource_group, server_name)
        
        return {
            'id': server.id,
            'name': server.name,
            'location': server.location,
            'fully_qualified_domain_name': server.fully_qualified_domain_name,
            'version': server.version
        }
    
    except HttpResponseError as e:
        print(f"Error creating SQL Server: {e}")
        return None

def create_firewall_rule(sql_client, resource_group, server_name, rule_name, 
                        start_ip, end_ip):
    """
    Create a firewall rule for the SQL Server.
    
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
    
    try:
        # Create the firewall rule
        rule = sql_client.firewall_rules.create_or_update(
            resource_group,
            server_name,
            rule_name,
            {
                "start_ip_address": start_ip,
                "end_ip_address": end_ip
            }
        )
        
        # Print the result
        print(f"Firewall rule '{rule_name}' created successfully.")
        print(f"Rule range: {rule.start_ip_address} - {rule.end_ip_address}")
        
        # Return rule properties as a dictionary
        return {
            'id': rule.id,
            'name': rule.name,
            'start_ip_address': rule.start_ip_address,
            'end_ip_address': rule.end_ip_address
        }
    
    except HttpResponseError as e:
        print(f"Error creating firewall rule: {e}")
        return None

def create_sql_database(sql_client, resource_group, server_name, database_name, 
                       location, sku_name="Basic", sku_tier="Basic"):
    """
    Create an Azure SQL Database.
    
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
    
    try:
        # Define database parameters
        database_params = {
            "location": location,
            "sku": {
                "name": sku_name,
                "tier": sku_tier
            },
            "collation": "SQL_Latin1_General_CP1_CI_AS"
        }
        
        # Create SQL Database (this is a long-running operation)
        database_poller = sql_client.databases.begin_create_or_update(
            resource_group,
            server_name,
            database_name,
            database_params
        )
        
        # Wait for the operation to complete
        database = database_poller.result()
        
        # Print the result
        print(f"SQL Database '{database_name}' created successfully.")
        print(f"Database ID: {database.id}")
        print(f"Edition: {database.sku.tier}")
        
        # Return database properties as a dictionary
        return {
            'id': database.id,
            'name': database.name,
            'location': database.location,
            'collation': database.collation,
            'sku': {
                'name': database.sku.name,
                'tier': database.sku.tier
            },
            'status': database.status
        }
    
    except ResourceExistsError:
        print(f"SQL Database '{database_name}' already exists.")
        
        # Get the existing database
        database = sql_client.databases.get(resource_group, server_name, database_name)
        
        return {
            'id': database.id,
            'name': database.name,
            'location': database.location,
            'collation': database.collation,
            'sku': {
                'name': database.sku.name,
                'tier': database.sku.tier
            },
            'status': database.status
        }
    
    except HttpResponseError as e:
        print(f"Error creating SQL Database: {e}")
        return None

def list_databases(sql_client, resource_group, server_name):
    """
    List all databases on the specified SQL Server.
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        
    Returns:
        list: List of databases
    """
    print(f"Listing databases on SQL Server: {server_name}")
    
    try:
        # Get all databases on the server
        databases = sql_client.databases.list_by_server(
            resource_group,
            server_name
        )
        
        # Convert to list and print details
        database_list = []
        
        for db in databases:
            database_info = {
                'id': db.id,
                'name': db.name,
                'location': db.location,
                'collation': db.collation,
                'sku': {
                    'name': db.sku.name if db.sku else 'N/A',
                    'tier': db.sku.tier if db.sku else 'N/A'
                },
                'status': db.status
            }
            database_list.append(database_info)
            
            print(f"- {db.name} ({db.status}):")
            print(f"  ID: {db.id}")
            print(f"  Edition: {db.sku.tier if db.sku else 'N/A'}")
            print(f"  Collation: {db.collation}")
        
        if not database_list:
            print("No user databases found on the server.")
        
        return database_list
    
    except HttpResponseError as e:
        print(f"Error listing databases: {e}")
        return []

def delete_sql_database(sql_client, resource_group, server_name, database_name):
    """
    Delete an Azure SQL Database.
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        database_name (str): SQL Database name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting SQL Database: {database_name} from server {server_name}")
    
    try:
        # Delete the SQL Database (this is a long-running operation)
        database_poller = sql_client.databases.begin_delete(
            resource_group,
            server_name,
            database_name
        )
        
        # Wait for the operation to complete
        database_poller.result()
        
        print(f"SQL Database '{database_name}' deleted successfully.")
        return True
    
    except ResourceNotFoundError:
        print(f"SQL Database '{database_name}' not found.")
        return False
    
    except HttpResponseError as e:
        print(f"Error deleting SQL Database: {e}")
        return False

def delete_sql_server(sql_client, resource_group, server_name):
    """
    Delete an Azure SQL Server instance.
    
    Args:
        sql_client: Azure SQL Management client
        resource_group (str): Resource group name
        server_name (str): SQL Server name
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting SQL Server: {server_name} from resource group {resource_group}")
    
    try:
        # Delete the SQL Server
        server_poller = sql_client.servers.begin_delete(
            resource_group,
            server_name
        )
        
        # Wait for the operation to complete
        server_poller.result()
        
        print(f"SQL Server '{server_name}' deleted successfully.")
        return True
    
    except ResourceNotFoundError:
        print(f"SQL Server '{server_name}' not found.")
        return False
    
    except HttpResponseError as e:
        print(f"Error deleting SQL Server: {e}")
        return False

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
```

## Sample Usage

### 1. Create a SQL Server
```bash
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --location eastus create-server
```

### 2. Create a Firewall Rule
```bash
# Allow a specific IP address
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --rule-name allow-my-ip --start-ip 192.168.1.1 --end-ip 192.168.1.1 create-firewall-rule

# Allow Azure services
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --rule-name allow-azure-services --start-ip 0.0.0.0 --end-ip 0.0.0.0 create-firewall-rule
```

### 3. Create a SQL Database
```bash
# Create a Basic database
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --db-name devopsdb --location eastus create-database

# Create a Standard database
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --db-name devopsdb-std --sku-name S0 --sku-tier Standard create-database
```

### 4. List Databases
```bash
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 list-databases
```

### 5. Delete a Database
```bash
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --db-name devopsdb delete-database
```

### 6. Delete a SQL Server
```bash
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 delete-server
```

## Key Learning Points

1. **Azure SQL Database Service Tiers**
   - **Basic**: For small databases with light workloads
   - **Standard**: For medium-sized applications with moderate I/O requirements
   - **Premium**: For mission-critical applications requiring high throughput
   - **General Purpose**: For most business workloads with balanced compute and storage
   - **Business Critical**: For high-performance, mission-critical workloads

2. **SQL Server Administration**
   - Secure administrator credentials are essential
   - SQL Server names must be globally unique within Azure
   - TLS version enforcement is important for security

3. **Firewall Rules**
   - Specific IP addresses can be allowed for targeted access
   - Setting start/end IP to 0.0.0.0 allows Azure services to access
   - Multiple firewall rules can be created for different access needs

4. **Long-Running Operations**
   - SQL Server and Database creation are async operations
   - Using `begin_create_or_update().result()` waits for completion
   - Error handling is important for these operations

5. **Azure SDK for Python**
   - **SqlManagementClient**: Provides access to SQL Server and Database management
   - **DefaultAzureCredential**: Simplifies authentication
   - **ResourceManagementClient**: For resource group operations

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "DefaultAzureCredential failed to retrieve a token"
   - **Solution**: Ensure AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, and AZURE_TENANT_ID environment variables are set correctly

2. **SQL Server Name Conflicts**
   - **Problem**: "SqlServerName 'X' already exists"
   - **Solution**: SQL Server names must be globally unique in Azure. Choose a different name with unique characters or add random elements.

3. **Password Requirements**
   - **Problem**: Password doesn't meet complexity requirements
   - **Solution**: Use a password with at least 8 characters, including uppercase, lowercase, digits, and special characters.

4. **Firewall Access**
   - **Problem**: Cannot connect to SQL Server
   - **Solution**: Create firewall rules to allow your client IP address or Azure services (0.0.0.0).

5. **Resource Deletion**
   - **Problem**: "Cannot delete server because there are databases"
   - **Solution**: Delete all databases before deleting the server, or use `--force` with the Azure CLI.

## Azure SQL Database Best Practices

1. **Security**
   - Use strong, randomly generated passwords
   - Limit firewall rules to only necessary IP ranges
   - Enable Advanced Threat Protection
   - Use Azure Key Vault for credential storage

2. **Performance**
   - Choose the right service tier for your workload
   - Consider elastic pools for multiple databases with varying usage patterns
   - Monitor performance using Azure Monitor
   - Use query performance insights for optimization

3. **Cost Management**
   - Start with lower tiers and scale up as needed
   - Use serverless option for unpredictable workloads
   - Consider reserved capacity for predictable workloads
   - Schedule automatic pausing for dev/test databases

4. **Backup and Recovery**
   - Understand built-in backup retention policies
   - Configure long-term backup retention for compliance
   - Practice point-in-time recovery
   - Set up geo-replication for critical databases

5. **Operational Excellence**
   - Automate deployment with Python scripts
   - Use Infrastructure as Code (IaC) for consistent environments
   - Implement proper error handling
   - Document server and database configurations

## SQL Database Pricing Tiers Reference

| Tier | Description | Use Cases | DTUs/vCores |
|------|-------------|-----------|------------|
| Basic | Simple databases with light workloads | Development, small apps | 5 DTUs |
| Standard (S0-S12) | Most business workloads | Web apps, workgroups | 10-4000 DTUs |
| Premium (P1-P15) | Mission-critical applications | High-throughput apps | 125-4000 DTUs |
| General Purpose | Business workloads with balanced performance | Most business apps | 1-80 vCores |
| Business Critical | Mission-critical with high performance | OLTP, analytics | 1-80 vCores |
| Hyperscale | Very large databases with elastic scale | Data warehousing, large DBs | 1-80 vCores |

## Cleanup

Always clean up Azure resources when you're done to avoid unexpected charges:

```bash
# Delete the database
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 --db-name devopsdb delete-database

# Delete the server (this will delete all databases and firewall rules)
python create_sql_db.py --resource-group devops-lab-rg --server-name devopssqlsrv123 delete-server

# Or use Azure CLI
az sql db delete -g devops-lab-rg -s devopssqlsrv123 -n devopsdb --yes
az sql server delete -g devops-lab-rg -n devopssqlsrv123 --yes
```

## Extending This Lab

1. **Connection Example**: Add a function to connect to the database using pyodbc
2. **Database Import/Export**: Implement database import/export operations
3. **Elastic Pools**: Create and manage elastic pools for multiple databases
4. **Geo-Replication**: Set up geo-replication for disaster recovery
5. **Advanced Monitoring**: Add Azure Monitor alerts for database performance 