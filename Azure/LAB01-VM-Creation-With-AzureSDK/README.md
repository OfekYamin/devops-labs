# Azure LAB01 - Automate VM Creation with Python (Azure SDK)

In this lab, you'll use the Azure Python SDK to create a virtual machine (VM) in Microsoft Azure. Automating VM deployment is foundational for cloud infrastructure management.

---

## 🎯 Objectives

By the end of this lab, you will:
- Authenticate to Azure using a service principal
- Create a resource group and virtual machine
- Understand VM size, image, and location settings

---

## 🧰 Prerequisites

- Azure subscription
- Azure CLI installed (`az login` configured)
- Service principal credentials (client ID, secret, tenant ID)
- Python 3.8+ and `azure-identity`, `azure-mgmt-compute`, `azure-mgmt-resource` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB01-VM-Creation-With-AzureSDK/
├── create_vm.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set environment variables for authentication:
```bash
export AZURE_CLIENT_ID="<your-client-id>"
export AZURE_CLIENT_SECRET="<your-client-secret>"
export AZURE_TENANT_ID="<your-tenant-id>"
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB01-VM-Creation-With-AzureSDK/
```

3. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install azure-identity azure-mgmt-resource azure-mgmt-compute
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Write a script to create a VM:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
resource_group = "devops-lab-rg"
location = "eastus"
vm_name = "devops-vm"

credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

# Create resource group
resource_client.resource_groups.create_or_update(resource_group, {"location": location})

# Define VM parameters
vm_parameters = {
    "location": location,
    "storage_profile": {
        "image_reference": {
            "publisher": "Canonical",
            "offer": "UbuntuServer",
            "sku": "18.04-LTS",
            "version": "latest"
        }
    },
    "hardware_profile": {
        "vm_size": "Standard_B1s"
    },
    "os_profile": {
        "computer_name": vm_name,
        "admin_username": "azureuser",
        "admin_password": "P@ssw0rd1234"
    },
    "network_profile": {
        "network_interfaces": [
            {
                "id": "/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/networkInterfaces/devops-nic"
            }
        ]
    }
}

# Create VM
async_vm_creation = compute_client.virtual_machines.begin_create_or_update(
    resource_group, vm_name, vm_parameters
)
async_vm_creation.result()
print("VM created successfully.")
```

> **Note**: A NIC must exist for the VM to be deployed successfully — consider adding NIC creation in future labs.

---

## 🧪 Validation Checklist

✅ Resource group created  
✅ VM created in specified region with correct specs  
✅ Script runs cleanly:
```bash
python create_vm.py
```

---

## 🧹 Cleanup
```bash
az group delete --name devops-lab-rg --yes --no-wait
```

---

## 💬 What's Next?
Advance to [Azure LAB02 - Blob Storage Upload](../LAB02-Blob-Storage-Upload/) to automate file uploads to Azure Storage.

---

## 🙏 Acknowledgments
VM automation is the first step in building repeatable infrastructure. Combine it with other Azure services for full-stack deployments.

Happy provisioning! 💻☁️🐍

