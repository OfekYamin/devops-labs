#!/usr/bin/env python3
"""
Firestore Document Operations Script

This script demonstrates how to perform common operations with Google Cloud Firestore
including creating, reading, updating, and deleting documents.

Usage:
    python firestore_script.py --project_id YOUR_PROJECT_ID [options]

Options:
    --create               Create sample documents in Firestore
    --query                Query documents from Firestore
    --update               Update existing documents
    --delete               Delete documents or collections
    --document_id ID       Specify a document ID for operations
    --collection_name NAME Set the collection name (default: devops-users)
    --field FIELD          Field name for update operations
    --value VALUE          New value for update operations
    --help                 Show this help message
"""

import argparse
import sys
import time
from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from tabulate import tabulate

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Firestore Document Operations')
    parser.add_argument('--project_id', required=True, help='GCP Project ID')
    parser.add_argument('--create', action='store_true', help='Create sample documents')
    parser.add_argument('--query', action='store_true', help='Query documents')
    parser.add_argument('--update', action='store_true', help='Update documents')
    parser.add_argument('--delete', action='store_true', help='Delete documents')
    parser.add_argument('--document_id', help='Document ID for operations')
    parser.add_argument('--collection_name', default='devops-users', help='Collection name')
    parser.add_argument('--field', help='Field name for update operations')
    parser.add_argument('--value', help='New value for update operations')
    return parser.parse_args()

def display_documents(docs):
    """Format and display documents in a table."""
    if not docs:
        print("No documents found.")
        return
    
    # Extract all unique keys from all documents
    all_keys = set()
    for doc in docs:
        all_keys.update(doc.keys())
    
    # Create table data
    headers = ['document_id'] + sorted(all_keys)
    rows = []
    
    for doc_id, data in docs.items():
        row = [doc_id]
        for key in sorted(all_keys):
            value = data.get(key, '')
            # Format dictionaries and lists for better display
            if isinstance(value, (dict, list)):
                value = str(value)
            row.append(value)
        rows.append(row)
    
    # Print table
    print(tabulate(rows, headers=headers, tablefmt='grid'))

def init_firestore_client(project_id):
    """Initialize and return a Firestore client.
    
    Args:
        project_id: The Google Cloud project ID
        
    Returns:
        A Firestore client instance
    """
    # TODO: Initialize the Firestore client with the provided project_id
    # HINT: Use the firestore.Client() constructor with the project parameter
    
    pass  # Replace with your implementation

def create_documents(db, collection_name):
    """Create sample documents in the specified collection.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection to add documents to
    """
    print(f"Creating documents in collection: {collection_name}")
    
    # Sample user data
    users = [
        {
            'id': 'alice',
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'role': 'Developer',
            'department': 'Engineering',
            'skills': ['Python', 'Cloud', 'DevOps'],
            'active': True,
            'joined': firestore.SERVER_TIMESTAMP,
            'projects': {
                'current': 'Database Migration',
                'completed': ['Website Redesign', 'API Integration']
            },
            'performance_rating': 4.7
        },
        {
            'id': 'bob',
            'name': 'Bob Smith',
            'email': 'bob@example.com',
            'role': 'SRE',
            'department': 'Operations',
            'skills': ['Kubernetes', 'Terraform', 'Python'],
            'active': True,
            'joined': firestore.SERVER_TIMESTAMP,
            'projects': {
                'current': 'Infrastructure Automation',
                'completed': ['Cloud Migration']
            },
            'performance_rating': 4.2
        },
        {
            'id': 'charlie',
            'name': 'Charlie Brown',
            'email': 'charlie@example.com',
            'role': 'DevOps Engineer',
            'department': 'Engineering',
            'skills': ['AWS', 'Docker', 'CI/CD'],
            'active': True,
            'joined': firestore.SERVER_TIMESTAMP,
            'projects': {
                'current': 'Pipeline Optimization',
                'completed': ['Monitoring Setup', 'Disaster Recovery']
            },
            'performance_rating': 4.8
        },
        {
            'id': 'diana',
            'name': 'Diana Martinez',
            'email': 'diana@example.com',
            'role': 'Security Engineer',
            'department': 'Security',
            'skills': ['Compliance', 'Security Automation', 'Python'],
            'active': False,
            'joined': firestore.SERVER_TIMESTAMP,
            'projects': {
                'current': None,
                'completed': ['Security Audit', 'Access Control Implementation']
            },
            'performance_rating': 4.5
        }
    ]
    
    # TODO: Implement the creation of documents in Firestore
    # 1. For each user in the users list, create a document with the user's id
    # 2. Set the document data to the user dictionary (excluding the 'id' field)
    # HINT: Use collection.document().set() method

def batch_write_documents(db, collection_name):
    """Perform a batch write operation to add multiple documents atomically.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection to add documents to
    """
    print(f"Performing batch write to collection: {collection_name}")
    
    # Sample data for batch write
    locations = [
        {'id': 'loc1', 'name': 'New York Office', 'country': 'USA', 'employees': 150},
        {'id': 'loc2', 'name': 'London Office', 'country': 'UK', 'employees': 85},
        {'id': 'loc3', 'name': 'Tokyo Office', 'country': 'Japan', 'employees': 65},
        {'id': 'loc4', 'name': 'Sydney Office', 'country': 'Australia', 'employees': 40}
    ]
    
    # TODO: Implement batch write operation
    # 1. Create a batch instance
    # 2. Add set operations for each location to the batch
    # 3. Commit the batch
    # HINT: Use db.batch() to create a batch instance

def get_document_by_id(db, collection_name, document_id):
    """Retrieve a document by its ID.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection
        document_id: ID of the document to retrieve
        
    Returns:
        Document data as a dictionary, or None if not found
    """
    # TODO: Implement document retrieval by ID
    # 1. Get a reference to the document with the given ID
    # 2. Get the document snapshot
    # 3. Check if the document exists
    # 4. Return the document data if it exists, None otherwise
    # HINT: Use collection.document(document_id).get()
    
    pass  # Replace with your implementation

def query_documents(db, collection_name):
    """Query documents from the specified collection with filters.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection to query
        
    Returns:
        Dictionary of document ID to document data
    """
    print(f"Querying documents from collection: {collection_name}")
    
    results = {}
    
    # TODO: Implement a query to get all active users in the Engineering department
    # 1. Create a query with multiple filters (active=True AND department=Engineering)
    # 2. Execute the query and process the results
    # HINT: Use collection.where() multiple times or use FieldFilter
    
    print("\nActive users in Engineering department:")
    display_documents(results)
    
    # Reset results for next query
    results = {}
    
    # TODO: Implement a query to get users with Python in their skills, sorted by performance_rating
    # 1. Create a query to filter users with 'Python' in their skills array
    # 2. Order the results by performance_rating in descending order
    # 3. Execute the query and process the results
    # HINT: Use collection.where() with array_contains and order_by()
    
    print("\nUsers with Python skills, sorted by rating:")
    display_documents(results)
    
    return results

def update_document(db, collection_name, document_id, field, value):
    """Update a field in a document.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection
        document_id: ID of the document to update
        field: Field name to update
        value: New value for the field
    
    Returns:
        True if the update was successful, False otherwise
    """
    if not document_id or not field:
        print("Error: Document ID and field name are required for updates")
        return False
    
    print(f"Updating document {document_id} in collection {collection_name}")
    print(f"Setting field '{field}' to value: {value}")
    
    # TODO: Implement document update
    # 1. Get a reference to the document
    # 2. Update the specified field with the new value
    # 3. Handle the case where the document doesn't exist
    # HINT: Use document_ref.update() method with a dictionary of fields to update
    
    return True  # Return True if update was successful

def transaction_update(db, collection_name, document_id):
    """Perform a transactional update on a document.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection
        document_id: ID of the document to update in transaction
        
    Returns:
        True if the transaction was successful, False otherwise
    """
    if not document_id:
        print("Error: Document ID is required for transaction")
        return False
    
    print(f"Performing transactional update on document {document_id}")
    
    # TODO: Implement a transaction to atomically update a document
    # 1. Define a transaction function that:
    #    - Takes a transaction object as parameter
    #    - Gets the document in the transaction
    #    - Modifies some data based on current values
    #    - Updates the document in the transaction
    # 2. Execute the transaction using db.transaction()
    # HINT: Use the @firestore.transactional decorator or pass a callback to db.transaction()
    
    return True  # Return True if transaction was successful

def delete_document(db, collection_name, document_id):
    """Delete a document from a collection.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection
        document_id: ID of the document to delete
        
    Returns:
        True if deletion was successful, False otherwise
    """
    if not document_id:
        print("Error: Document ID is required for deletion")
        return False
    
    print(f"Deleting document {document_id} from collection {collection_name}")
    
    # TODO: Implement document deletion
    # 1. Get a reference to the document
    # 2. Delete the document
    # HINT: Use document_ref.delete() method
    
    return True  # Return True if deletion was successful

def delete_collection(db, collection_name, batch_size=5):
    """Delete an entire collection.
    
    Args:
        db: Firestore client instance
        collection_name: Name of the collection to delete
        batch_size: Maximum number of documents to delete in each batch
        
    Returns:
        Number of documents deleted
    """
    print(f"Deleting entire collection: {collection_name}")
    print("WARNING: This will delete all documents in the collection.")
    confirmation = input("Type 'DELETE' to confirm: ")
    
    if confirmation.upper() != "DELETE":
        print("Deletion cancelled.")
        return 0
    
    # TODO: Implement collection deletion
    # 1. Get a reference to the collection
    # 2. Query documents in batches
    # 3. Delete documents in batches
    # 4. Continue until all documents are deleted
    # HINT: This is a multi-step process as Firestore doesn't support direct collection deletion
    
    return 0  # Replace with actual count of deleted documents

def main():
    """Main function to run the script."""
    args = parse_arguments()
    
    try:
        # Initialize Firestore client
        db = init_firestore_client(args.project_id)
        if not db:
            print("Failed to initialize Firestore client")
            sys.exit(1)
        
        if args.create:
            create_documents(db, args.collection_name)
            batch_write_documents(db, f"{args.collection_name}-locations")
        
        if args.query:
            query_documents(db, args.collection_name)
        
        if args.update:
            if args.document_id and args.field:
                update_document(db, args.collection_name, args.document_id, args.field, args.value)
                # Example of transaction update
                if args.field == 'performance_rating':
                    transaction_update(db, args.collection_name, args.document_id)
            else:
                print("Error: Document ID and field name are required for updates")
        
        if args.delete:
            if args.document_id:
                delete_document(db, args.collection_name, args.document_id)
            else:
                deleted_count = delete_collection(db, args.collection_name)
                print(f"Deleted {deleted_count} documents from collection {args.collection_name}")
        
        if not any([args.create, args.query, args.update, args.delete]):
            print("No operation specified. Use --help for usage information.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 