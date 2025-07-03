# GCP LAB03 - Automate IAM Service Account Creation with Python

In this lab, you'll learn how to create and manage IAM service accounts in Google Cloud Platform (GCP) using Python and the Google API Client Library. Automating IAM is essential for secure, scalable cloud infrastructure management.

---

## 🎯 Objectives

By the end of this lab, you will:
- Programmatically create service accounts in GCP with Python
- Assign IAM roles to service accounts 
- List existing service accounts in a project
- Understand basic IAM concepts and service account management

---

## 🧰 Prerequisites

- Google Cloud account with an active project
- Project-level permissions to create and manage IAM service accounts (roles/iam.serviceAccountAdmin)
- Service account key file with sufficient permissions downloaded to your local machine
- Python 3.8 or higher installed
- Basic understanding of IAM concepts in GCP

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB03-IAM-Service-Account-Creation/
├── create_service_account.py  # The main Python script (with TODOs)
├── requirements.txt           # Python dependencies
├── solutions.md               # Solutions to the TODOs
└── README.md                  # This file
```

---

## 🚀 Getting Started

### 1. Set up authentication

Before running the script, you need to authenticate with Google Cloud:

```bash
# Set the environment variable to point to your service account key file
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

### 2. Navigate to the lab folder

```bash
cd Cloud-Automation/GCP/LAB03-IAM-Service-Account-Creation/
```

### 3. Create and activate a virtual environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ✍️ Your Task

In this lab, you will complete the TODOs in the `create_service_account.py` script to:

1. Initialize the IAM service API client
2. Create a new service account with custom details
3. Assign roles to the service account
4. List all service accounts in a project

The script already contains:
- Argument parsing for customizing service account parameters
- Error handling and validation
- Helper methods for each key operation

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the script

Once you've completed the TODOs, run your script with your project ID:

```bash
python create_service_account.py --project=your-gcp-project-id
```

To create a service account with custom details:

```bash
python create_service_account.py \
  --project=your-gcp-project-id \
  --account_id=test-service-account \
  --display_name="Test Service Account" \
  --description="For testing automation scripts" \
  --roles=roles/storage.objectViewer,roles/logging.viewer
```

To list all service accounts in your project:

```bash
python create_service_account.py --project=your-gcp-project-id --list
```

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully authenticates with GCP IAM API  
✅ Creates a service account with the specified attributes  
✅ Assigns the requested roles to the service account  
✅ Lists all service accounts in the project when requested  
✅ Shows proper cleanup instructions  

You can verify your service account in the Google Cloud Console:
1. Go to IAM & Admin > Service Accounts
2. Look for the service account you created
3. Check the roles assigned to it

---

## 🧹 Cleanup

To avoid cluttering your project with test service accounts, delete the account when you're done:

```bash
gcloud iam service-accounts delete SERVICE_ACCOUNT_EMAIL --project=PROJECT_ID
```

Where `SERVICE_ACCOUNT_EMAIL` will be in the format `account-id@project-id.iam.gserviceaccount.com`

---

## 💬 What's Next?

After completing this lab, proceed to [GCP LAB04 - Cloud Functions Deployment](../LAB04-Cloud-Functions-Deployment/) to learn how to automate serverless function deployment in GCP.

---

## 🙏 Acknowledgments

IAM automation is a critical skill for cloud engineers and DevOps practitioners. Understanding how to programmatically manage service accounts and their permissions is essential for implementing secure, least-privilege access control in cloud environments.

Happy cloud automating! 🔐☁️🐍