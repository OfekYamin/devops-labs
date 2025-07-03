# Azure LAB09 - Automate Cosmos DB Document Management with Python

In this lab, you'll use Python to manage documents in Azure Cosmos DB, a globally distributed, multi-model database service.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to Cosmos DB with a Python client
- Create a database and container
- Add, query, and delete documents

---

## 🧰 Prerequisites

- Azure Cosmos DB account (SQL API)
- Connection string or access key
- Python 3.8+ with `azure-cosmos` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB09-CosmosDB-Document-Management/
├── cosmos_script.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set environment variables:
```bash
export AZURE_COSMOS_CONNECTION_STRING="<your-connection-string>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB09-CosmosDB-Document-Management/
```

3. Set up a Python environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-cosmos
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Add, query, and delete a document:
```python
from azure.cosmos import CosmosClient, PartitionKey
import os

conn_str = os.getenv("AZURE_COSMOS_CONNECTION_STRING")
client = CosmosClient.from_connection_string(conn_str)

database = client.create_database_if_not_exists(id="devopsdb")
container = database.create_container_if_not_exists(id="users", partition_key=PartitionKey(path="/username"))

# Create document
user = {"id": "1", "username": "alice", "role": "admin"}
container.create_item(body=user)

# Query document
items = list(container.query_items(query="SELECT * FROM users", enable_cross_partition_query=True))
for item in items:
    print(item)

# Delete document
container.delete_item(item="1", partition_key="alice")
print("Document deleted.")
```

---

## 🧪 Validation Checklist

✅ Cosmos DB connected via connection string  
✅ Document created, queried, and deleted  
✅ Script runs without error:
```bash
python cosmos_script.py
```

---

## 🧹 Cleanup
Manual deletion of the database or container via Azure Portal or CLI is recommended.

---

## 💬 What's Next?
Proceed to [Azure LAB10 - Azure Container Instance Launch](../LAB10-Azure-Container-Instance-Launch/) to deploy containers using Python.

---

## 🙏 Acknowledgments
Cosmos DB is powerful for distributed document storage. Python makes it easy to automate and scale your database operations.

Code smart. Store fast. Query instantly. ☁️📄🐍

