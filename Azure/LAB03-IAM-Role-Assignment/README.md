# Azure LAB03 - Automate IAM Role Assignment with Python

In this lab, you’ll learn how to assign roles to users, groups, or service principals using Python and the Azure SDK. This is essential for automating access control in Azure.

---

## 🎯 Objectives

By the end of this lab, you will:
- Authenticate with Azure using a service principal
- Assign an RBAC role to a principal (e.g., Reader role)
- Query and list existing role assignments

---

## 🧰 Prerequisites

- Azure subscription and service principal credentials
- Resource group or resource to assign roles on
- Python 3.8+ and `azure-mgmt-authorization`, `azure-identity` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB03-IAM-Role-Assignment/
├── assign_role.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Export your Azure service principal environment variables:
```bash
export AZURE_CLIENT_ID="<your-client-id>"
export AZURE_CLIENT_SECRET="<your-client-secret>"
export AZURE_TENANT_ID="<your-tenant-id>"
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB03-IAM-Role-Assignment/
```

3. Set up your Python environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-identity azure-mgmt-authorization
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Assign a role to a user/service principal:
```python
import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
credential = DefaultAzureCredential()
auth_client = AuthorizationManagementClient(credential, subscription_id)

scope = f"/subscriptions/{subscription_id}/resourceGroups/devops-lab-rg"
role_definition_id = f"/subscriptions/{subscription_id}/providers/Microsoft.Authorization/roleDefinitions/acdd72a7-3385-48ef-bd42-f606fba81ae7"  # Reader
principal_id = "<your-assignee-object-id>"

assignment_id = str(uuid.uuid4())
auth_client.role_assignments.create(scope, assignment_id, {
    'role_definition_id': role_definition_id,
    'principal_id': principal_id
})
print("Role assigned successfully.")
```

---

## 🧪 Validation Checklist

✅ Role assigned to principal at the resource group level  
✅ Script runs without errors and confirms assignment  
✅ Assignment visible via Azure Portal or CLI:
```bash
az role assignment list --assignee <your-assignee-object-id>
```

---

## 🧹 Cleanup
Remove the role assignment manually or via CLI:
```bash
az role assignment delete --assignee <your-assignee-object-id> --role "Reader" --scope /subscriptions/<sub>/resourceGroups/devops-lab-rg
```

---

## 💬 What's Next?
Advance to [Azure LAB04 - Azure Function Deployment](../LAB04-Azure-Function-Deployment/) to automate serverless computing in the cloud.

---

## 🙏 Acknowledgments
RBAC automation ensures secure and scalable access control. Perfect for integrating into pipelines or cloud onboarding workflows.

Permission granted, securely! 🔐☁️🐍

