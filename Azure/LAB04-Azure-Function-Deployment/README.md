# Azure LAB04 - Automate Azure Function Deployment with Python

In this lab, you'll learn how to deploy an Azure Function using Python. Azure Functions let you run event-driven code without provisioning infrastructure, ideal for serverless automation.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a Python-based Azure Function
- Deploy it using Azure CLI and Python
- Trigger the function via HTTP

---

## 🧰 Prerequisites

- Azure subscription with Function App and Storage access
- Azure CLI installed and configured
- Python 3.8+ with `azure-functions` and `azure-cli-core` (or use subprocess)

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB04-Azure-Function-Deployment/
├── HttpTrigger/__init__.py         # Function code
├── function_app.py                 # Automation script
├── host.json
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Log in to Azure CLI:
```bash
az login
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/Azure/LAB04-Azure-Function-Deployment/
```

3. Install Python dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-functions
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create the Azure Function project (via CLI or manually):
```bash
func init FunctionApp --python
cd FunctionApp
func new --name HttpTrigger --template "HTTP trigger"
```

### 2. Deploy the function using the CLI or subprocess:
```bash
az functionapp create \
  --resource-group devops-lab-rg \
  --consumption-plan-location eastus \
  --runtime python \
  --functions-version 4 \
  --name devops-func-app \
  --storage-account <your-storage-account>

func azure functionapp publish devops-func-app
```

### 3. Trigger the function with curl or browser:
```bash
curl https://devops-func-app.azurewebsites.net/api/HttpTrigger
```

---

## 🧪 Validation Checklist

✅ Azure Function created and deployed  
✅ HTTP request returns expected response  
✅ Script or CLI runs cleanly:
```bash
python function_app.py  # if automating with subprocess
```

---

## 🧹 Cleanup
```bash
az functionapp delete --name devops-func-app --resource-group devops-lab-rg
```

---

## 💬 What's Next?
Move to [Azure LAB05 - Monitor Metrics and Alerts](../LAB05-Monitor-Metrics-And-Alerts/) to automate observability tasks.

---

## 🙏 Acknowledgments
Azure Functions help you build microservices quickly. Automate deployments to deliver faster, with less infrastructure hassle.

Serverless success starts here! ⚡☁️🐍

