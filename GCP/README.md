# GCP Python Automation Labs

Welcome to the **GCP Python Automation Labs** — a hands-on, real-world lab series designed to teach you how to automate infrastructure and cloud operations on **Google Cloud Platform** using Python.

These labs are part of the broader **Python for DevOps** training program, focusing on cloud-native automation and scripting with real GCP APIs and SDKs.

---

## 🚀 What You'll Learn

By completing these labs, you will gain practical skills in:
- Automating virtual machines, networks, databases, and cloud storage
- Deploying serverless and container-based applications
- Managing IAM roles and security
- Using Python to monitor, interact with, and control GCP services

---

## 🧰 Prerequisites

To get started, you'll need:
- A Google Cloud Platform project with billing enabled
- A service account key with appropriate roles for each lab
- Python 3.8+ installed
- Google Cloud CLI (`gcloud`) and Docker (for some labs)

---

## 🔐 Authentication Setup

Before running the lab code, you need to set up authentication for the Google Cloud Python libraries. Here are several methods you can use:

### Method 1: Service Account Key File (Recommended for Labs)

This is the most straightforward method for our labs:

```bash
# Create a service account (if you don't have one already)
gcloud iam service-accounts create devops-labs \
  --description="Service account for DevOps labs" \
  --display-name="DevOps Labs SA"

# Grant the necessary roles (adjust as needed for specific labs)
gcloud projects add-iam-policy-binding your-project-id \
  --member="serviceAccount:devops-labs@your-project-id.iam.gserviceaccount.com" \
  --role="roles/editor"

# Create and download a key file
gcloud iam service-accounts keys create key.json \
  --iam-account=devops-labs@your-project-id.iam.gserviceaccount.com
```

Then in your Python code:

```python
from google.oauth2 import service_account
from google.cloud import storage

# Authenticate using the key file
credentials = service_account.Credentials.from_service_account_file(
    'key.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Create a client using the credentials
storage_client = storage.Client(credentials=credentials, project='your-project-id')
```

Or, set an environment variable (preferred for most labs):

```bash
# For Linux/Mac
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"

# For Windows PowerShell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\key.json"

# For Windows Command Prompt
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\key.json
```

Then in your Python code:

```python
from google.cloud import storage

# The client library will automatically use the environment variable
storage_client = storage.Client()
```

### Method 2: User Account Authentication (gcloud CLI)

For development and interactive use:

```bash
# Install Google Cloud SDK
# Follow instructions at: https://cloud.google.com/sdk/docs/install

# Log in with your user account
gcloud auth login

# Set your current project
gcloud config set project your-project-id

# Create application default credentials
gcloud auth application-default login
```

Your Python code:

```python
from google.cloud import pubsub_v1

# The client library will use your application default credentials
publisher = pubsub_v1.PublisherClient()
```

### Method 3: Compute Engine / GKE Metadata Server 

If your code runs on Google Cloud services (Compute Engine, GKE, Cloud Run, etc.):

1. Create a VM or container with the appropriate service account:
```bash
gcloud compute instances create instance-name \
  --service-account=your-service-account@your-project-id.iam.gserviceaccount.com \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

2. Your Python code will automatically authenticate:
```python
from google.cloud import bigquery

# No explicit credentials needed - the client library 
# will detect it's running on Google Cloud
client = bigquery.Client()
```

### Method 4: Workload Identity Federation (for non-Google Cloud environments)

For authenticating from AWS, Azure, or on-premises:

```bash
# Create a workload identity pool
gcloud iam workload-identity-pools create my-pool \
  --location="global" \
  --description="Pool for DevOps automation"

# Create a provider in the pool
gcloud iam workload-identity-pools providers create-oidc my-provider \
  --location="global" \
  --workload-identity-pool="my-pool" \
  --issuer-uri="https://sts.amazonaws.com" \
  --allowed-audiences="sts.amazonaws.com"

# Create a service account to impersonate
gcloud iam service-accounts create external-auth \
  --description="Service account for external authentication" \
  --display-name="External Auth SA"

# Allow the external identity to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding \
  external-auth@your-project-id.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/my-pool/*"
```

### Method 5: Impersonating a Service Account

When you need to temporarily act as a service account:

```python
from google.auth import impersonated_credentials
from google.auth.credentials import Credentials
from google.cloud import storage

# Start with your base credentials (user or service account)
source_credentials = Credentials.from_service_account_file('source-key.json')

# Create impersonated credentials
target_credentials = impersonated_credentials.Credentials(
    source_credentials=source_credentials,
    target_principal='target-service-account@your-project-id.iam.gserviceaccount.com',
    target_scopes=['https://www.googleapis.com/auth/cloud-platform'],
    lifetime=3600  # 1 hour in seconds
)

# Use the impersonated credentials
storage_client = storage.Client(credentials=target_credentials)
```

### Security Best Practices

1. **Never hardcode credentials** in your Python scripts
2. Use the principle of least privilege when assigning roles to service accounts
3. Rotate service account keys regularly (ideally every 90 days)
4. Consider workload identity federation instead of service account keys when possible
5. Store service account keys securely and restrict access to them
6. Set short expiration times for service account key usage
7. For production, consider using Secret Manager or other secure storage
8. Revoke unused service account keys

---

## 📁 Lab Structure

```bash
GCP/
├── LAB01-Compute-Instance-Creation/
├── LAB02-GCS-File-Upload/
├── LAB03-IAM-Service-Account-Creation/
├── LAB04-Cloud-Functions-Deployment/
├── LAB05-Cloud-Monitoring-Metrics/
├── LAB06-PubSub-Topic-and-Subscription/
├── LAB07-Cloud-SQL-Instance-Automation/
├── LAB08-VPC-Network-Creation/
├── LAB09-Firestore-Document-Operations/
└── LAB10-Cloud-Run-Deployment/
```

Each folder includes:
- A detailed `README.md` with objectives, steps, and cleanup
- Python scripts to execute the automation
- Dependency and setup files (e.g., `requirements.txt`)

---

## 🧠 Lab Progression

1. **Core Infrastructure**: Compute, Storage, IAM
2. **Serverless & Monitoring**: Functions, Monitoring, Pub/Sub
3. **Databases & Networking**: SQL, Firestore, VPC
4. **Containers & Deployment**: Cloud Run

The labs are designed in an order that builds on your skills incrementally, preparing you for cloud-native development and DevOps roles.

---

## 🙏 Acknowledgments

- Google Cloud Platform & `google-cloud-*` SDK teams
- DevOps educators and open-source contributors
- Python community for enabling clean automation

---

## 💬 Contributing

Want to suggest or add a lab?
- Fork the repo
- Use our lab template for consistency
- Submit a pull request with a clear description and purpose

---

## ☁️ Automate Google Cloud with Python

These GCP labs help you understand how to:
- Write Python scripts to manage infrastructure
- Use GCP APIs for repeatable, scalable operations
- Embrace DevOps principles in the cloud

Happy automating! 🚀☁️🐍