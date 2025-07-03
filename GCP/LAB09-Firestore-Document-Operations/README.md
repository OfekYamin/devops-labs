# GCP LAB09 - Firestore Document Operations with Python

In this lab, you'll learn how to interact with Google Cloud Firestore using Python. Firestore is a flexible, scalable NoSQL cloud database for storing and synchronizing data for client- and server-side development.

---

## 🎯 Objectives

By the end of this lab, you will:
- Initialize a Firestore client with authentication
- Create, read, update, and delete documents
- Use batch operations for atomic writes
- Perform queries with filters
- Execute transactions for safe updates
- Manage collections efficiently

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Firestore API enabled (enable with `gcloud services enable firestore.googleapis.com`)
- Service account with Firestore access (roles/datastore.user)
- Python 3.7+ installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB09-Firestore-Document-Operations/
├── firestore_script.py   # Main script with TODOs to implement
├── solutions.md          # Solutions for the TODOs (reference only)
├── requirements.txt      # Required Python packages
└── README.md             # Lab instructions
```

---

## 🚀 Getting Started

### 1. Set up your service account credentials:
```bash
# Create a service account (if you don't have one yet)
gcloud iam service-accounts create firestore-lab \
  --description="Service account for Firestore lab" \
  --display-name="Firestore Lab"

# Grant the required role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:firestore-lab@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/datastore.user"

# Download credentials
gcloud iam service-accounts keys create credentials.json \
  --iam-account=firestore-lab@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Point to your credentials file
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials.json"
```

### 2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB09-Firestore-Document-Operations/
```

### 3. Create and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📝 Your Task

In this lab, you will complete the TODOs in the `firestore_script.py` script to:

1. Initialize a Firestore client
2. Create documents in a Firestore collection
3. Implement batch write operations
4. Retrieve specific documents by ID
5. Query documents with filters
6. Implement compound queries
7. Update documents
8. Implement transactional updates
9. Delete specific documents
10. Delete an entire collection

The script already contains:
- Command-line argument parsing
- Sample data structures
- Helper functions for displaying document data
- Error handling patterns

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the Script

Once you've completed the TODOs, run the script with your GCP project ID:

```bash
# Create documents
python firestore_script.py --project_id YOUR_PROJECT_ID --create

# Query documents
python firestore_script.py --project_id YOUR_PROJECT_ID --query

# Update a document
python firestore_script.py --project_id YOUR_PROJECT_ID --update --document_id "alice" --field "active" --value "False"

# Delete a document
python firestore_script.py --project_id YOUR_PROJECT_ID --delete --document_id "alice"
```

Use the `--help` flag to see all available options:

```bash
python firestore_script.py --help
```

---

## 🔍 Documentation References

- [Google Cloud Firestore Python Documentation](https://googleapis.dev/python/firestore/latest/index.html)
- [Firestore Concepts](https://cloud.google.com/firestore/docs/concepts)
- [Firestore Query Operations](https://cloud.google.com/firestore/docs/query-data/queries)
- [Firestore Transactions](https://cloud.google.com/firestore/docs/manage-data/transactions)

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully connects to Firestore  
✅ Creates documents with the correct data structure  
✅ Performs batch writes atomically  
✅ Retrieves documents by ID  
✅ Executes queries with filters correctly  
✅ Updates documents with the specified fields  
✅ Handles transactions properly  
✅ Deletes documents and collections  
✅ Includes proper error handling  

---

## 💡 Hints and Tips

- Firestore supports different data types including strings, numbers, booleans, arrays, maps, and timestamps
- Use server timestamps with `firestore.SERVER_TIMESTAMP` for accurate time tracking
- Batch operations have a limit of 500 operations per batch
- When deleting collections, use batching to avoid timeouts
- Always check if documents exist before trying to update or delete them
- Use transactions when you need to ensure consistency across multiple operations

---

## 🧹 Cleanup

Always clean up your Firestore data when you're done to avoid unnecessary storage charges:

```bash
# Delete specific documents
python firestore_script.py --project_id YOUR_PROJECT_ID --delete --document_id "alice"

# Delete entire collection
python firestore_script.py --project_id YOUR_PROJECT_ID --delete --collection_name "devops-users"
```

You may also want to revoke the service account key:

```bash
gcloud iam service-accounts keys delete KEY_ID \
  --iam-account=firestore-lab@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

---

## 💬 What's Next?
Next lab: [GCP LAB10 - Cloud Run Deployment](../LAB10-Cloud-Run-Deployment/) to deploy containerized applications using Cloud Run.

---

## 🙏 Acknowledgments
Firestore provides a powerful, scalable NoSQL database that integrates seamlessly with other Google Cloud services. Mastering database operations with Python is an essential skill for modern DevOps engineers.

Structure your data, query with precision! 🗄️☁️🐍

