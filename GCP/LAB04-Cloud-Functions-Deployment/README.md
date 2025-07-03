# GCP LAB04 - Automate Cloud Functions Deployment with Python

In this lab, you'll learn how to programmatically deploy Google Cloud Functions using Python. You'll work with both the Google Cloud Functions API and the gcloud CLI to implement serverless functions that respond to HTTP triggers.

---

## 🎯 Objectives

By the end of this lab, you will:
- Package and deploy a Cloud Function using Python
- Configure function runtime, trigger settings, and entry points
- Compare API-based deployment with gcloud CLI deployment
- Test and validate your deployed function
- Understand basic serverless concepts in GCP

---

## 🧰 Prerequisites

- Google Cloud account with an active project
- Cloud Functions API enabled in your project
- Service account with Cloud Functions Developer role (roles/cloudfunctions.developer)
- Service account key file (JSON) downloaded to your local machine
- Python 3.8 or higher installed
- gcloud CLI installed (for CLI deployment option)

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB04-Cloud-Functions-Deployment/
├── main.py                    # Cloud Function source code
├── requirements-function.txt  # Dependencies for the Cloud Function
├── deploy_function.py         # Deployment script (with TODOs)
├── requirements.txt           # Dependencies for the deployment script
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
cd Cloud-Automation/GCP/LAB04-Cloud-Functions-Deployment/
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

In this lab, you will:

1. Review the sample Cloud Function (`main.py`) that returns a JSON greeting
2. Complete the TODOs in the `deploy_function.py` script to:
   - Create a deployment package (zip file) of the function
   - Upload the package to Google Cloud Storage
   - Configure and deploy the function using the Cloud Functions API
   - Set up public access for the function (if requested)

The script already contains:
- Argument parsing for various deployment options
- A gcloud CLI deployment method
- Error handling and validation
- Helper functions for each step of the process

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the script

Once you've completed the TODOs, run your script to deploy using the API:

```bash
python deploy_function.py --project=your-gcp-project-id
```

Or use the gcloud CLI for deployment:

```bash
python deploy_function.py --project=your-gcp-project-id --use_gcloud
```

Make the function publicly accessible:

```bash
python deploy_function.py --project=your-gcp-project-id --allow_unauthenticated
```

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully packages the Cloud Function source code  
✅ Uploads the package to Google Cloud Storage (if using API)  
✅ Deploys the function with proper configuration  
✅ Makes the function publicly accessible (if requested)  
✅ Shows the HTTP trigger URL for testing  

You can test your deployed function with:

```bash
curl https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME
```

Or with a parameter:

```bash
curl "https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME?name=YourName"
```

The function should return a JSON response with a greeting and timestamp.

---

## 🧹 Cleanup

To avoid incurring charges for the deployed function, delete it when you're done:

```bash
gcloud functions delete hello-world --region=us-central1 --project=your-gcp-project-id
```

The script will output the exact cleanup command at the end of a successful deployment.

---

## 💬 What's Next?

After completing this lab, proceed to [GCP LAB05 - Cloud Monitoring Metrics](../LAB05-Cloud-Monitoring-Metrics/) to learn how to monitor resources and retrieve metrics in GCP.

---

## 🙏 Acknowledgments

Cloud Functions is a key serverless computing service in GCP that enables you to run code without provisioning or managing servers. Mastering programmatic deployment is an essential skill for DevOps engineers and cloud automation specialists.

Happy cloud automating! ☁️⚡🐍

