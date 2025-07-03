# LAB09: Azure Cosmos DB Document Management - Solutions

This document provides the complete solution for the Cosmos DB Document Management lab, including implementations for all the TODO sections and important learning points.

## Complete Implementation of `cosmos_script.py`

```python
#!/usr/bin/env python3
"""
Azure Cosmos DB Document Management Script

This script demonstrates how to interact with Azure Cosmos DB using the Python SDK.
It shows how to create databases, containers, and documents, as well as how to query,
update, and delete documents.
"""

import os
import uuid
import json
import datetime
import sys
from azure.cosmos import CosmosClient, PartitionKey, exceptions

# Constants
DATABASE_NAME = "devopsdb"
CONTAINER_NAME = "resources"
PARTITION_KEY_PATH = "/resourceType"

def get_cosmos_client():
    """
    Initialize and return a Cosmos DB client.
    
    Returns:
        CosmosClient: Initialized Cosmos DB client
    """
    # Get the connection string from environment variable
    connection_string = os.environ.get("AZURE_COSMOS_CONNECTION_STRING")
    if not connection_string:
        print("Error: AZURE_COSMOS_CONNECTION_STRING environment variable not set.")
        print("Please set this variable with your Cosmos DB connection string.")
        sys.exit(1)
    
    try:
        # Create a client using the connection string
        client = CosmosClient.from_connection_string(connection_string)
        return client
    except Exception as e:
        print(f"Error creating Cosmos DB client: {str(e)}")
        return None

def create_database(client):
    """
    Create a database if it doesn't exist.
    
    Args:
        client (CosmosClient): Cosmos DB client
        
    Returns:
        Database: Created or existing database
    """
    print(f"Creating database '{DATABASE_NAME}' if it doesn't exist...")
    
    try:
        # Create the database if it doesn't exist
        database = client.create_database_if_not_exists(id=DATABASE_NAME)
        print(f"Database '{DATABASE_NAME}' ready")
        return database
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error creating database: {str(e)}")
        return None

def create_container(database):
    """
    Create a container if it doesn't exist.
    
    Args:
        database: Database object
        
    Returns:
        Container: Created or existing container
    """
    print(f"Creating container '{CONTAINER_NAME}' if it doesn't exist...")
    
    try:
        # Create the container if it doesn't exist
        container = database.create_container_if_not_exists(
            id=CONTAINER_NAME,
            partition_key=PartitionKey(path=PARTITION_KEY_PATH),
            offer_throughput=400  # Minimum throughput for Cosmos DB
        )
        print(f"Container '{CONTAINER_NAME}' ready")
        return container
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error creating container: {str(e)}")
        return None

def create_document(container):
    """
    Create a document in the container.
    
    Args:
        container: Container object
        
    Returns:
        dict: Created document
    """
    print("Creating a document...")
    
    # Generate a sample document
    doc_id = str(uuid.uuid4())
    timestamp = datetime.datetime.utcnow().isoformat()
    
    document = {
        "id": doc_id,
        "resourceType": "vm",
        "name": "test-vm-01",
        "location": "eastus",
        "size": "Standard_B1s",
        "created": timestamp,
        "tags": {
            "environment": "dev",
            "project": "devops-lab"
        }
    }
    
    try:
        # Create the document in the container
        created_doc = container.create_item(body=document)
        print(f"Document created with ID: {created_doc['id']}")
        return created_doc
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error creating document: {str(e)}")
        return None

def query_documents(container, query):
    """
    Query documents in the container.
    
    Args:
        container: Container object
        query (str): SQL query
        
    Returns:
        list: List of documents matching the query
    """
    print(f"Querying documents with: {query}")
    
    try:
        # Query documents in the container
        items = list(container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        print(f"Found {len(items)} documents")
        return items
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error querying documents: {str(e)}")
        return []

def update_document(container, doc_id, partition_key_value, updates):
    """
    Update a document in the container.
    
    Args:
        container: Container object
        doc_id (str): Document ID
        partition_key_value (str): Partition key value
        updates (dict): Fields to update
        
    Returns:
        dict: Updated document
    """
    print(f"Updating document with ID: {doc_id}")
    
    try:
        # 1. Read the existing document
        doc = container.read_item(item=doc_id, partition_key=partition_key_value)
        
        # 2. Update the document with new values
        for key, value in updates.items():
            if isinstance(value, dict) and key in doc and isinstance(doc[key], dict):
                # Merge nested dictionaries
                doc[key].update(value)
            else:
                # Replace or add the field
                doc[key] = value
        
        # 3. Replace the document in the container
        updated_doc = container.replace_item(item=doc_id, body=doc)
        print(f"Document with ID {doc_id} updated")
        return updated_doc
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error updating document: {str(e)}")
        return None

def delete_document(container, doc_id, partition_key_value):
    """
    Delete a document from the container.
    
    Args:
        container: Container object
        doc_id (str): Document ID
        partition_key_value (str): Partition key value
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting document with ID: {doc_id}")
    
    try:
        # Delete the document
        container.delete_item(item=doc_id, partition_key=partition_key_value)
        print(f"Document with ID {doc_id} deleted")
        return True
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error deleting document: {str(e)}")
        return False

def delete_database(client):
    """
    Delete the database.
    
    Args:
        client: Cosmos DB client
        
    Returns:
        bool: True if deletion was successful
    """
    print(f"Deleting database '{DATABASE_NAME}'...")
    
    try:
        # Delete the database
        client.delete_database(DATABASE_NAME)
        print(f"Database '{DATABASE_NAME}' deleted")
        return True
    except exceptions.CosmosHttpResponseError as e:
        print(f"Error deleting database: {str(e)}")
        return False

def main():
    """Main function to orchestrate the Cosmos DB operations."""
    print("Azure Cosmos DB Document Management Lab")
    print("---------------------------------------")
    
    # Get Cosmos DB client
    client = get_cosmos_client()
    if not client:
        print("Failed to create Cosmos DB client. Exiting.")
        return
    
    # Create database
    database = create_database(client)
    if not database:
        print("Failed to create database. Exiting.")
        return
    
    # Create container
    container = create_container(database)
    if not container:
        print("Failed to create container. Exiting.")
        return
    
    # Create a document
    document = create_document(container)
    if not document:
        print("Failed to create document. Exiting.")
        return
    
    print(f"Created document: {json.dumps(document, indent=2)}")
    
    # Query for all documents
    all_docs = query_documents(container, "SELECT * FROM c")
    print(f"All documents ({len(all_docs)}):")
    for doc in all_docs:
        print(f" - {doc['id']}: {doc['name']} ({doc['resourceType']})")
    
    # Query with a filter
    vm_docs = query_documents(container, "SELECT * FROM c WHERE c.resourceType = 'vm'")
    print(f"VM documents ({len(vm_docs)}):")
    for doc in vm_docs:
        print(f" - {doc['id']}: {doc['name']} ({doc['location']})")
    
    # Update the document
    if document:
        doc_id = document['id']
        partition_key = document['resourceType']
        
        updates = {
            "size": "Standard_B2s",
            "tags": {
                "environment": "test",
                "project": "devops-lab",
                "updated": True
            }
        }
        
        updated_doc = update_document(container, doc_id, partition_key, updates)
        if updated_doc:
            print(f"Updated document: {json.dumps(updated_doc, indent=2)}")
    
    # Clean up - Delete document and database (commented out for safety)
    # Uncomment these lines to test deletion
    """
    if document:
        doc_id = document['id']
        partition_key = document['resourceType']
        
        if delete_document(container, doc_id, partition_key):
            print(f"Document {doc_id} deleted successfully")
    
    # Caution: This deletes the entire database!
    if delete_database(client):
        print(f"Database {DATABASE_NAME} deleted successfully")
    """
    
    print("\nCosmos DB operations completed. Database and container remain for inspection.")
    print("IMPORTANT: To avoid charges, delete these resources when done:")
    print(f"- Database: {DATABASE_NAME}")
    print(f"- Container: {CONTAINER_NAME}")
    print("\nYou can delete them by uncommenting the deletion code in this script,")
    print("or by using the Azure Portal or Azure CLI.")

if __name__ == "__main__":
    main()
```

## Key Learning Points

### Azure Cosmos DB Concepts

1. **What is Azure Cosmos DB?**
   - A globally distributed, multi-model database service
   - Fully managed NoSQL database with guaranteed single-digit millisecond response times
   - Supports multiple data models: document, key-value, graph, and column-family

2. **Core Components**
   - **Databases**: Logical containers for collections/containers
   - **Containers**: Store JSON documents with a defined partition key
   - **Documents**: Individual JSON items stored in containers
   - **Partition Keys**: Used to distribute data across physical partitions
   - **Request Units (RUs)**: Currency for provisioned throughput

3. **Consistency Levels**
   - **Strong**: Linearizable guarantees
   - **Bounded Staleness**: Consistent prefix guarantees, bounded by time or operations
   - **Session**: Consistent prefix guarantees for a client session
   - **Consistent Prefix**: Updates returned in order
   - **Eventual**: No ordering guarantees

### Azure Python SDK for Cosmos DB

1. **Connection Methods**
   - Connection string-based: `CosmosClient.from_connection_string()`
   - Key-based: `CosmosClient(endpoint, key)`
   - RBAC/MSI authentication: Using `DefaultAzureCredential`

2. **Key Concepts in the SDK**
   - **Client**: The entry point for all operations (`CosmosClient`)
   - **Database**: Managed via the client (`create_database_if_not_exists()`)
   - **Container**: Managed via the database (`create_container_if_not_exists()`)
   - **Item**: Managed via the container (`create_item()`, `read_item()`, etc.)

3. **Document Operations**
   - **Create**: `container.create_item(body=document)`
   - **Read**: `container.read_item(item=id, partition_key=pk)`
   - **Update**: `container.replace_item(item=id, body=updated_doc)`
   - **Delete**: `container.delete_item(item=id, partition_key=pk)`
   - **Query**: `container.query_items(query="SELECT * FROM c", enable_cross_partition_query=True)`

### Best Practices

1. **Partition Key Selection**
   - Choose a property with high cardinality
   - Evenly distribute requests and storage
   - Common examples: `id`, `userId`, `tenantId`, or `resourceType`

2. **Query Optimization**
   - Use partition key in queries when possible
   - Use `enable_cross_partition_query=True` for queries that span partitions
   - Be mindful of RU consumption for large queries

3. **Error Handling**
   - Use specific `exceptions.CosmosHttpResponseError` for Cosmos-specific errors
   - Implement retries for transient failures
   - Handle rate limiting (429 responses) with backoff

4. **Resource Management**
   - Use `create_if_not_exists` methods for idempotent operations
   - Clean up resources when done to avoid unexpected charges
   - Monitor RU consumption for cost optimization

## Common Issues and Troubleshooting

1. **Authentication Issues**
   - **Problem**: "Failed to create Cosmos DB client" error
   - **Solution**: Check that your connection string is correctly set in the environment variable

2. **Permission Issues**
   - **Problem**: "Access is forbidden" error
   - **Solution**: Verify that your account has permissions for the requested operations

3. **Resource Not Found**
   - **Problem**: "Resource Not Found" when reading or updating documents
   - **Solution**: Verify that the document ID and partition key are correct

4. **Partition Key Issues**
   - **Problem**: "Cross partition query is required but disabled" error
   - **Solution**: Enable cross-partition queries with `enable_cross_partition_query=True`

5. **Request Unit (RU) Limitations**
   - **Problem**: "Request rate is large" (HTTP 429) errors
   - **Solution**: Implement retry logic with exponential backoff or increase provisioned throughput

## Advanced Concepts

1. **Bulk Operations**
   - Use batch operations for improved performance
   - Example: `container.create_items(documents, enable_automatic_id_generation=True)`

2. **Change Feed**
   - Monitor changes to containers in real-time
   - Useful for event-driven architectures and data sync scenarios

3. **TTL (Time-to-Live)**
   - Automatically expire documents after a certain period
   - Set at container or document level

4. **Indexing Policies**
   - Customize which properties are indexed
   - Control index types and precision

5. **Stored Procedures and Triggers**
   - Server-side JavaScript for atomic transactions
   - Pre and post-triggers for document operations

## Cleanup Instructions

Always remember to clean up your Azure resources when you're done experimenting:

1. **Delete Individual Documents**: Use `container.delete_item(item=doc_id, partition_key=partition_key)`
2. **Delete the Container**: Use `database.delete_container(CONTAINER_NAME)`
3. **Delete the Database**: Use `client.delete_database(DATABASE_NAME)`

For manual cleanup in the Azure Portal:
1. Navigate to your Cosmos DB account
2. Select "Data Explorer"
3. Find and delete your database and containers

Remember: Keeping unused Cosmos DB resources can result in unexpected charges to your Azure account. 