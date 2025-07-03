# Azure LAB10 - Launch Azure Container Instance with Python

In this final Azure lab, you’ll deploy a containerized application to Azure Container Instances (ACI) using Python. ACI is great for quick, serverless container execution.

---

## 🎯 Objectives

By the end of this lab, you will:
- Define a container group and image settings
- Deploy it using Python and the Azure SDK
- Retrieve the container’s public IP for access

---

## 🧰 Prerequisites

- Azure subscription
- Docker image available in Docker Hub or Azure Container Registry
- Python 3.8+ with `azure-identity`, `azure-mgmt-containerinstance` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB10-Azure-Container-Instance-Launch/
├── launch_container.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set your environment variables:
```bash
export AZURE_CLIENT_ID="<your-client-id>"
export AZURE_CLIENT_SECRET="<your-client-secret>"
export AZURE_TENANT_ID="<your-tenant-id>"
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB10-Azure-Container-Instance-Launch/
```

3. Set up Python environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-identity azure-mgmt-containerinstance
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Launch an Azure container:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
import os

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = "devops-lab-rg"
container_group_name = "devops-container"
image = "mcr.microsoft.com/azuredocs/aci-helloworld"

credential = DefaultAzureCredential()
aci_client = ContainerInstanceManagementClient(credential, subscription_id)

aci_client.container_groups.begin_create_or_update(
    resource_group,
    container_group_name,
    {
        "location": "eastus",
        "containers": [
            {
                "name": "helloworld",
                "image": image,
                "resources": {
                    "requests": {
                        "cpu": 1,
                        "memory_in_gb": 1.5
                    }
                },
                "ports": [{"port": 80}]
            }
        ],
        "os_type": "Linux",
        "ip_address": {
            "type": "Public",
            "ports": [{"protocol": "tcp", "port": 80}]
        }
    }
).result()
print("Container launched successfully.")
```

---

## 🧪 Validation Checklist

✅ Container instance launched  
✅ Public IP accessible for HTTP requests  
✅ Script runs without error:
```bash
python launch_container.py
```

---

## 🧹 Cleanup
```bash
az container delete --name devops-container --resource-group devops-lab-rg --yes
```

---

## 🎉 Congratulations!
You’ve completed all 10 Azure labs. You now have real skills to provision, automate, and deploy workloads on Microsoft Azure using Python.

---

## 🙏 Acknowledgments
ACI brings speed and simplicity to container deployments. It’s the perfect final step in a modern DevOps workflow.

Code, push, deploy. ☁️🐳🐍

