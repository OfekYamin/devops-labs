# Azure LAB05 - Automate Monitor Metrics and Alerts with Python

In this lab, you’ll use Python to interact with Azure Monitor to fetch metrics and create alert rules. Monitoring is key to observability and proactive incident response.

---

## 🎯 Objectives

By the end of this lab, you will:
- Query metrics from a resource (e.g., a virtual machine)
- Create a metric alert rule programmatically
- Understand the structure of Azure monitoring resources

---

## 🧰 Prerequisites

- Azure subscription with monitoring-enabled resources
- Azure Monitor API and Metrics API enabled
- Python 3.8+ and `azure-mgmt-monitor`, `azure-identity` installed

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB05-Monitor-Metrics-And-Alerts/
├── monitor_alert.py
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
cd Cloud-Automation/Azure/LAB05-Monitor-Metrics-And-Alerts/
```

3. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-mgmt-monitor azure-identity
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Fetch CPU metrics for a VM:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from datetime import datetime, timedelta
import os

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_uri = "/subscriptions/<sub>/resourceGroups/devops-lab-rg/providers/Microsoft.Compute/virtualMachines/devops-vm"

client = MonitorManagementClient(DefaultAzureCredential(), subscription_id)
end_time = datetime.utcnow()
start_time = end_time - timedelta(minutes=30)

metrics_data = client.metrics.list(
    resource_uri,
    timespan=f"{start_time}/{end_time}",
    interval='PT1M',
    metricnames='Percentage CPU',
    aggregation='Average'
)

for item in metrics_data.value:
    for data in item.timeseries[0].data:
        print(f"Time: {data.time_stamp}, CPU: {data.average}")
```

---

## 🧪 Validation Checklist

✅ Metrics fetched and displayed from Azure Monitor  
✅ Metrics scoped to VM or resource group  
✅ Script runs without error:
```bash
python monitor_alert.py
```

---

## 🧹 Cleanup
No persistent resources are created. Cleanup only required if alerts are deployed.

---

## 💬 What's Next?
Next: [Azure LAB06 - Service Bus Queue Creation](../LAB06-Service-Bus-Queue-Creation/) to integrate messaging workflows.

---

## 🙏 Acknowledgments
Monitor is your real-time insight engine. Use it to detect problems before your users do.

Observe more, panic less! 📈☁️🐍