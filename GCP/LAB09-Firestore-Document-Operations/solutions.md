# LAB09: Firestore Document Operations - Solutions

This document provides solution guidance for implementing the TODOs in the `firestore_script.py` script. Remember that these are example implementations, and there may be other valid approaches to solving these tasks.

## 1. Initialize Firestore Client

```python
def init_firestore_client(project_id):
    """Initialize and return a Firestore client."""
    try:
        # Initialize the Firestore client with the provided project_id
        db = firestore.Client(project=project_id)
        print(f"Successfully connected to Firestore in project: {project_id}")
        return db
    except Exception as e:
        print(f"Error initializing Firestore client: {e}")
        return None
```

## 2. Create Documents

```python
def create_documents(db, collection_name):
    """Create sample documents in the specified collection."""
    print(f"Creating documents in collection: {collection_name}")
    
    # Implementation code...
    try:
        collection_ref = db.collection(collection_name)
        count = 0
        
        for user in users:
            user_id = user.pop('id')  # Extract the ID and remove from data
            doc_ref = collection_ref.document(user_id)
            doc_ref.set(user)
            count += 1
            print(f"Added document with ID: {user_id}")
        
        print(f"Successfully created {count} documents in {collection_name}")
    except Exception as e:
        print(f"Error creating documents: {e}")
```

## 3. Batch Write Documents

```python
def batch_write_documents(db, collection_name):
    """Perform a batch write operation to add multiple documents atomically."""
    print(f"Performing batch write to collection: {collection_name}")
    
    try:
        # Create a batch instance
        batch = db.batch()
        collection_ref = db.collection(collection_name)
        count = 0
        
        # Add set operations for each location to the batch
        for location in locations:
            loc_id = location.pop('id')  # Extract ID and remove from data
            doc_ref = collection_ref.document(loc_id)
            batch.set(doc_ref, location)
            count += 1
        
        # Commit the batch
        batch.commit()
        print(f"Successfully batch wrote {count} documents to {collection_name}")
    except Exception as e:
        print(f"Error in batch write: {e}")
```

## 4. Get Document by ID

```python
def get_document_by_id(db, collection_name, document_id):
    """Retrieve a document by its ID."""
    try:
        # Get a reference to the document with the given ID
        doc_ref = db.collection(collection_name).document(document_id)
        
        # Get the document snapshot
        doc_snapshot = doc_ref.get()
        
        # Check if the document exists
        if doc_snapshot.exists:
            print(f"Document {document_id} found")
            return doc_snapshot.to_dict()
        else:
            print(f"Document {document_id} not found")
            return None
    except Exception as e:
        print(f"Error getting document: {e}")
        return None
```

## 5. Query Documents

```python
def query_documents(db, collection_name):
    """Query documents from the specified collection with filters."""
    print(f"Querying documents from collection: {collection_name}")
    
    results = {}
    
    try:
        # Query to get all active users in the Engineering department
        collection_ref = db.collection(collection_name)
        query = (collection_ref
                 .where(filter=FieldFilter("active", "==", True))
                 .where(filter=FieldFilter("department", "==", "Engineering")))
        
        # Execute the query and process the results
        query_results = query.stream()
        for doc in query_results:
            results[doc.id] = doc.to_dict()
        
        print("\nActive users in Engineering department:")
        display_documents(results)
        
        # Reset results for next query
        results = {}
        
        # Query to get users with Python in their skills, sorted by performance_rating
        collection_ref = db.collection(collection_name)
        query = (collection_ref
                 .where(filter=FieldFilter("skills", "array_contains", "Python"))
                 .order_by("performance_rating", direction=firestore.Query.DESCENDING))
        
        # Execute the query and process the results
        query_results = query.stream()
        for doc in query_results:
            results[doc.id] = doc.to_dict()
        
        print("\nUsers with Python skills, sorted by rating:")
        display_documents(results)
        
        return results
    except Exception as e:
        print(f"Error querying documents: {e}")
        return {}
```

## 6. Update Document

```python
def update_document(db, collection_name, document_id, field, value):
    """Update a field in a document."""
    if not document_id or not field:
        print("Error: Document ID and field name are required for updates")
        return False
    
    print(f"Updating document {document_id} in collection {collection_name}")
    print(f"Setting field '{field}' to value: {value}")
    
    try:
        # Get a reference to the document
        doc_ref = db.collection(collection_name).document(document_id)
        
        # Check if the document exists
        if not doc_ref.get().exists:
            print(f"Document {document_id} does not exist")
            return False
        
        # Update the specified field with the new value
        # Convert value to appropriate type if needed
        if value.isdigit():
            value = int(value)
        elif value.lower() in ['true', 'false']:
            value = value.lower() == 'true'
        
        doc_ref.update({field: value})
        print(f"Document {document_id} updated successfully")
        return True
    except Exception as e:
        print(f"Error updating document: {e}")
        return False
```

## 7. Transaction Update

```python
def transaction_update(db, collection_name, document_id):
    """Perform a transactional update on a document."""
    if not document_id:
        print("Error: Document ID is required for transaction")
        return False
    
    print(f"Performing transactional update on document {document_id}")
    
    try:
        # Define a transaction function
        @firestore.transactional
        def update_in_transaction(transaction, doc_ref):
            # Get the document in the transaction
            doc_snapshot = doc_ref.get(transaction=transaction)
            
            if not doc_snapshot.exists:
                print(f"Document {document_id} does not exist")
                return False
            
            # Get current data
            current_data = doc_snapshot.to_dict()
            current_rating = current_data.get('performance_rating', 0)
            
            # Add a 'last_review' field with timestamp
            # This demonstrates modifying data based on current values
            new_data = {
                'last_review': firestore.SERVER_TIMESTAMP,
                'performance_history': firestore.ArrayUnion([current_rating])
            }
            
            # Update the document in the transaction
            transaction.update(doc_ref, new_data)
            return True
        
        # Get a reference to the document
        doc_ref = db.collection(collection_name).document(document_id)
        
        # Execute the transaction
        result = db.transaction().run(lambda tx: update_in_transaction(tx, doc_ref))
        
        if result:
            print(f"Transaction completed successfully for document {document_id}")
        return result
    except Exception as e:
        print(f"Error in transaction: {e}")
        return False
```

## 8. Delete Document

```python
def delete_document(db, collection_name, document_id):
    """Delete a document from a collection."""
    if not document_id:
        print("Error: Document ID is required for deletion")
        return False
    
    print(f"Deleting document {document_id} from collection {collection_name}")
    
    try:
        # Get a reference to the document
        doc_ref = db.collection(collection_name).document(document_id)
        
        # Check if the document exists
        if not doc_ref.get().exists:
            print(f"Document {document_id} does not exist")
            return False
        
        # Delete the document
        doc_ref.delete()
        print(f"Document {document_id} deleted successfully")
        return True
    except Exception as e:
        print(f"Error deleting document: {e}")
        return False
```

## 9. Delete Collection

```python
def delete_collection(db, collection_name, batch_size=5):
    """Delete an entire collection."""
    print(f"Deleting entire collection: {collection_name}")
    print("WARNING: This will delete all documents in the collection.")
    confirmation = input("Type 'DELETE' to confirm: ")
    
    if confirmation.upper() != "DELETE":
        print("Deletion cancelled.")
        return 0
    
    try:
        # Get a reference to the collection
        collection_ref = db.collection(collection_name)
        docs_deleted = 0
        
        # Query documents in batches
        while True:
            # Get a batch of documents
            docs = collection_ref.limit(batch_size).stream()
            deleted_count = 0
            
            # Delete documents in this batch
            for doc in docs:
                print(f"Deleting document {doc.id}")
                doc.reference.delete()
                deleted_count += 1
                docs_deleted += 1
            
            # If we deleted fewer documents than batch_size, we're done
            if deleted_count < batch_size:
                break
        
        print(f"Successfully deleted {docs_deleted} documents from collection {collection_name}")
        return docs_deleted
    except Exception as e:
        print(f"Error deleting collection: {e}")
        return 0
```

## Important Notes

1. **Error Handling**: Always implement proper error handling in your code, especially when working with external services like Firestore.

2. **Security Best Practices**:
   - Never hardcode service account credentials in your code
   - Use environment variables or secure secret management solutions
   - Assign the minimal required permissions to service accounts

3. **Performance Considerations**:
   - Batch operations for multiple document writes
   - Consider indexes for complex queries
   - Use transactions for operations that need to be atomic

4. **Cleanup**:
   - Always clean up test data when you're done
   - Delete service account keys when no longer needed

Remember that this lab is focused on learning the Firestore Python API. In a production environment, you would need to consider additional factors like security, scalability, and cost optimization. 