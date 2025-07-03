# Azure Python Automation Labs

Welcome to the **Azure Python Automation Labs** — a curated, hands-on lab series designed to teach you how to automate Microsoft Azure resources using Python.

These labs are part of the larger **Python for DevOps** learning path and are structured to take you from beginner-level cloud scripting to advanced automation and deployment practices.

---

## 🚀 What You'll Learn

By completing these labs, you'll gain practical experience in:
- Automating core Azure services such as VMs, storage, and networking
- Managing security and permissions via role-based access control (RBAC)
- Deploying serverless and containerized applications
- Monitoring and integrating Azure services for real-world DevOps workflows

---

## 🧰 Prerequisites

To get started, you'll need:
- An active Azure subscription
- Python 3.8+ installed on your system
- Azure CLI and credentials (service principal or CLI login)

Each lab includes:
- Step-by-step `README.md`
- Python scripts and supporting files
- Sample input data (where relevant)
- Cleanup instructions to avoid unnecessary charges

---

## 🔐 Authentication Setup

Before running the lab code, you need to set up authentication for the Azure SDK for Python. Here are several authentication methods to choose from:

### Method 1: Azure CLI Authentication (Simplest for Development)

This method uses your existing Azure CLI login:

```bash
# Install Azure CLI
# For Windows: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows
# For macOS: brew install azure-cli
# For Linux: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login to Azure
az login

# (Optional) Set your subscription if you have multiple
az account set --subscription "Your Subscription Name or ID"
```

Then in your Python code:

```python
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient

# Get credential from Azure CLI
credential = AzureCliCredential()
subscription_id = "your-subscription-id"

# Create a client using the credential
compute_client = ComputeManagementClient(credential, subscription_id)
```

### Method 2: Service Principal with Client Secret

For automation scenarios, create a service principal:

```bash
# Create a service principal and assign a role
az ad sp create-for-rbac --name "DevOpsLabsSP" --role contributor --scopes /subscriptions/your-subscription-id

# The command returns JSON with your credentials:
# {
#   "appId": "...",        # This is your client_id
#   "displayName": "...",
#   "password": "...",     # This is your client_secret
#   "tenant": "..."        # This is your tenant_id
# }
```

Then in your Python code:

```python
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

# Authenticate using service principal credentials
credential = ClientSecretCredential(
    tenant_id="your-tenant-id",
    client_id="your-client-id",
    client_secret="your-client-secret"
)

# Create a resource client
resource_client = ResourceManagementClient(credential, "your-subscription-id")
```

Or using environment variables:

```bash
# Set environment variables
# For Linux/Mac
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"

# For Windows PowerShell
$env:AZURE_TENANT_ID="your-tenant-id"
$env:AZURE_CLIENT_ID="your-client-id"
$env:AZURE_CLIENT_SECRET="your-client-secret"

# For Windows Command Prompt
set AZURE_TENANT_ID=your-tenant-id
set AZURE_CLIENT_ID=your-client-id
set AZURE_CLIENT_SECRET=your-client-secret
```

And in your Python code:

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

# DefaultAzureCredential checks environment variables automatically
credential = DefaultAzureCredential()
subscription_id = "your-subscription-id"

# Create a storage client
storage_client = StorageManagementClient(credential, subscription_id)
```

### Method 3: Managed Identity (for Azure-hosted applications)

If your code runs on Azure (VM, App Service, Functions, etc.) with Managed Identity:

```python
from azure.identity import ManagedIdentityCredential
from azure.mgmt.network import NetworkManagementClient

# Use the managed identity
credential = ManagedIdentityCredential()
subscription_id = "your-subscription-id"

# Create a network client
network_client = NetworkManagementClient(credential, subscription_id)
```

### Method 4: Interactive Browser Authentication

For desktop applications or development:

```python
from azure.identity import InteractiveBrowserCredential
from azure.mgmt.resource.resources import ResourceManagementClient

# Authenticate via browser
credential = InteractiveBrowserCredential()
subscription_id = "your-subscription-id"

# Create a client
client = ResourceManagementClient(credential, subscription_id)
```

### Method 5: Using a JSON Configuration File

Create a config file (`azure.json`):

```json
{
  "subscriptionId": "your-subscription-id",
  "tenantId": "your-tenant-id",
  "clientId": "your-client-id",
  "clientSecret": "your-client-secret"
}
```

Then load it in your Python code:

```python
import json
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

# Load configuration
with open('azure.json', 'r') as config_file:
    config = json.load(config_file)

# Create credential
credential = ClientSecretCredential(
    tenant_id=config['tenantId'],
    client_id=config['clientId'],
    client_secret=config['clientSecret']
)

# Create a client
compute_client = ComputeManagementClient(credential, config['subscriptionId'])
```

### Security Best Practices

1. **Never hardcode credentials** in your Python scripts
2. Use Managed Identities for Azure-hosted applications when possible
3. Grant least privilege (use specific roles instead of Contributor/Owner)
4. Rotate service principal secrets regularly
5. Use DefaultAzureCredential for flexibility across environments
6. For production, consider Azure Key Vault for storing credentials securely
7. Set short expiration times for secrets and tokens
8. Audit and monitor service principal usage

---

## 📁 Lab Structure

```bash
Azure/
├── LAB01-VM-Creation-With-AzureSDK/
├── LAB02-Blob-Storage-Upload/
├── LAB03-IAM-Role-Assignment/
├── LAB04-Azure-Function-Deployment/
├── LAB05-Monitor-Metrics-And-Alerts/
├── LAB06-Service-Bus-Queue-Creation/
├── LAB07-Azure-SQL-Database-Automation/
├── LAB08-Virtual-Network-Setup/
├── LAB09-CosmosDB-Document-Management/
└── LAB10-Azure-Container-Instance-Launch/
```

---

## 🧠 Lab Progression

1. **Core Infrastructure**: VMs, Storage, IAM
2. **Serverless and Monitoring**: Functions, Metrics, Service Bus
3. **Databases and Networking**: SQL, Cosmos DB, Virtual Networks
4. **Containers**: Azure Container Instances (ACI)

These labs build on each other and are ideal for learners progressing toward cloud-native DevOps roles.

---

## 🙏 Acknowledgments

- Azure SDK for Python team
- Microsoft Docs and contributors
- DevOps education and automation communities

---

## 💬 Contributing

Have an idea for a lab or improvement?
- Fork the repo
- Create a branch (e.g., `feature/lab11-azure-monitoring`) 
- Submit a pull request with a clear description

---

## ☁️ Automate Azure with Python

Master the power of the Microsoft cloud using Pythonic tools. Whether you're scripting for small tasks or building full CI/CD pipelines, these labs will get you there.

Happy automating! 🧠⚙️🐍