# Azure LAB02 - Automate Blob Storage Upload with Python

In this lab, you’ll learn how to automate file uploads to Azure Blob Storage using Python and the Azure SDK. This is useful for backups, logs, and application file delivery.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to Azure Blob Storage using Python
- Upload a file to a storage container
- List blobs inside a container

---

## 🧰 Prerequisites

- Azure subscription and storage account
- Access key or connection string for the storage account
- Python 3.8+ and `azure-storage-blob` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB02-Blob-Storage-Upload/
├── upload_blob.py
├── sample.txt              # Sample file to upload
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set your storage connection string:
```bash
export AZURE_STORAGE_CONNECTION_STRING="<your-storage-connection-string>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB02-Blob-Storage-Upload/
```

3. Set up your Python environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-storage-blob
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Upload a file to Blob Storage:
```python
from azure.storage.blob import BlobServiceClient
import os

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "devops-container"
blob_name = "uploads/sample.txt"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)
container_client.create_container()  # Ignore if it already exists

with open("sample.txt", "rb") as data:
    container_client.upload_blob(name=blob_name, data=data, overwrite=True)

print(f"File uploaded to container '{container_name}' as '{blob_name}'")
```

### 2. List blobs in the container:
```python
print("Blobs in container:")
for blob in container_client.list_blobs():
    print("-", blob.name)
```

---

## 🧪 Validation Checklist

✅ File uploaded to Azure Blob Storage  
✅ Blob is listed when you query the container  
✅ Script runs cleanly:
```bash
python upload_blob.py
```

---

## 🧹 Cleanup
To remove uploaded blobs:
```python
container_client.delete_blob(blob_name)
```

---

## 💬 What's Next?
Move to [Azure LAB03 - IAM Role Assignment](../LAB03-IAM-Role-Assignment/) to manage permissions using Python.

---

## 🙏 Acknowledgments
Blob Storage is ideal for scalable file storage. Automating uploads helps integrate with CI/CD pipelines and serverless workflows.

Store smartly, script freely! 🗃️☁️🐍

