#!/usr/bin/env python3
"""
Azure Cosmos DB Document Management Script

This script demonstrates how to interact with Azure Cosmos DB using the Python SDK.
Students should implement the TODO sections to complete the lab.
"""

import os
import uuid
import json
import datetime
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
    # TODO: Get the connection string from environment variable
    # Hint: Use os.environ.get() to retrieve "AZURE_COSMOS_CONNECTION_STRING"
    # If not found, print an error message and exit gracefully
    
    try:
        # TODO: Create and return a CosmosClient using the connection string
        # Hint: Use CosmosClient.from_connection_string()
        pass
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
        # TODO: Create the database if it doesn't exist
        # Hint: Use client.create_database_if_not_exists(id=DATABASE_NAME)
        # Return the database object
        pass
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
        # TODO: Create the container if it doesn't exist
        # Hint: Use database.create_container_if_not_exists with:
        #   - id=CONTAINER_NAME
        #   - partition_key=PartitionKey(path=PARTITION_KEY_PATH)
        # Return the container object
        pass
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
        # TODO: Create the document in the container
        # Hint: Use container.create_item(body=document)
        # Return the created document
        pass
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
        # TODO: Query documents in the container
        # Hint: Use container.query_items(
        #    query=query,
        #    enable_cross_partition_query=True
        # )
        # Convert the results to a list and return
        pass
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
        # TODO: Implement the following steps:
        # 1. Read the existing document using container.read_item(item=doc_id, partition_key=partition_key_value)
        # 2. Update the document properties with the values in 'updates'
        # 3. Replace the document using container.replace_item(item=doc_id, body=updated_doc)
        # Return the updated document
        pass
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
        # TODO: Delete the document
        # Hint: Use container.delete_item(item=doc_id, partition_key=partition_key_value)
        # Return True if successful
        pass
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
        # TODO: Delete the database
        # Hint: Use client.delete_database(DATABASE_NAME)
        # Return True if successful
        pass
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