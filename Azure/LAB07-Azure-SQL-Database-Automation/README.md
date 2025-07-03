# Azure LAB07 - Automate Azure SQL Database Deployment with Python

In this lab, you'll automate the creation of an Azure SQL Database using Python and the Azure SDK. This lab is essential for provisioning data infrastructure programmatically.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a SQL server and database using Python
- Set firewall rules to allow access
- Understand provisioning tiers for Azure SQL

---

## 🧰 Prerequisites

- Azure subscription and service principal credentials
- Python 3.8+ with `azure-identity`, `azure-mgmt-sql`, `azure-mgmt-resource` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB07-Azure-SQL-Database-Automation/
├── create_sql_db.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set your Azure service principal environment variables:
```bash
export AZURE_CLIENT_ID="<your-client-id>"
export AZURE_CLIENT_SECRET="<your-client-secret>"
export AZURE_TENANT_ID="<your-tenant-id>"
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB07-Azure-SQL-Database-Automation/
```

3. Set up a Python environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-identity azure-mgmt-sql azure-mgmt-resource
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create SQL server and database:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient

subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
resource_group = "devops-lab-rg"
location = "eastus"
server_name = "devopssqlsrv123"
db_name = "devopsdb"

credentials = DefaultAzureCredential()
sql_client = SqlManagementClient(credentials, subscription_id)

# Create SQL Server
sql_client.servers.begin_create_or_update(
    resource_group,
    server_name,
    {
        "location": location,
        "administrator_login": "sqladmin",
        "administrator_login_password": "P@ssw0rd1234"
    }
).result()

# Create SQL Database
sql_client.databases.begin_create_or_update(
    resource_group,
    server_name,
    db_name,
    {
        "location": location,
        "sku": {"name": "Basic", "tier": "Basic"}
    }
).result()

print("Azure SQL Database created successfully.")
```

---

## 🧪 Validation Checklist

✅ SQL Server and DB created using Python  
✅ Firewall rule optional but recommended for external access  
✅ Script runs without error:
```bash
python create_sql_db.py
```

---

## 🧹 Cleanup
Delete resources with:
```bash
az sql db delete -g devops-lab-rg -s devopssqlsrv123 -n devopsdb --yes
az sql server delete -g devops-lab-rg -n devopssqlsrv123 --yes
```

---

## 💬 What's Next?
Proceed to [Azure LAB08 - Virtual Network Setup](../LAB08-Virtual-Network-Setup/) to automate network provisioning.

---

## 🙏 Acknowledgments
Databases are the foundation of cloud-native apps. Automate their deployment to save time and reduce errors.

Data-driven, cloud-automated. 🗃️☁️🐍