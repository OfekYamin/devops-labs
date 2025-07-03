# Azure LAB06 - Automate Service Bus Queue Creation with Python

This lab walks you through creating and managing a Service Bus queue in Azure using Python. Messaging services like Azure Service Bus are foundational for decoupled and event-driven architectures.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a Service Bus namespace and queue
- Send and receive messages programmatically
- Understand basic queue management

---

## 🧰 Prerequisites

- Azure subscription with Service Bus access
- Python 3.8+ with `azure-servicebus`, `azure-identity`, and `azure-mgmt-servicebus`

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB06-Service-Bus-Queue-Creation/
├── servicebus_queue.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set up your Azure credentials:
```bash
export AZURE_CLIENT_ID="<your-client-id>"
export AZURE_CLIENT_SECRET="<your-client-secret>"
export AZURE_TENANT_ID="<your-tenant-id>"
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB06-Service-Bus-Queue-Creation/
```

3. Create and activate a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-servicebus azure-mgmt-servicebus azure-identity
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create Service Bus namespace and queue:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.servicebus import ServiceBusManagementClient
import os

subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
resource_group = 'devops-lab-rg'
namespace_name = 'devopsbus'
queue_name = 'devopsqueue'

credential = DefaultAzureCredential()
sb_client = ServiceBusManagementClient(credential, subscription_id)

sb_client.namespaces.begin_create_or_update(
    resource_group,
    namespace_name,
    {
        'location': 'eastus',
        'sku': {'name': 'Basic', 'tier': 'Basic'}
    }
).result()

sb_client.queues.create_or_update(
    resource_group,
    namespace_name,
    queue_name,
    {'enable_partitioning': False}
)
print("Service Bus queue created.")
```

---

## 🧪 Validation Checklist

✅ Service Bus namespace and queue created successfully  
✅ Script runs without error:
```bash
python servicebus_queue.py
```

---

## 🧹 Cleanup
```bash
az servicebus queue delete --resource-group devops-lab-rg --namespace-name devopsbus --name devopsqueue
az servicebus namespace delete --resource-group devops-lab-rg --name devopsbus
```

---

## 💬 What's Next?
Continue to [Azure LAB07 - Azure SQL Database Automation](../LAB07-Azure-SQL-Database-Automation/) to manage databases with Python.

---

## 🙏 Acknowledgments
Azure Service Bus is essential for scalable message-driven solutions. Automate queues to simplify distributed systems.

Queue it up and code on! 📬☁️🐍