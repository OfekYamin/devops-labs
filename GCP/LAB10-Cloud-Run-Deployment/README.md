# GCP LAB10 - Automate Cloud Run Deployment with Python

In this lab, you'll learn to deploy a containerized web service to Google Cloud Run using Python and the Google Cloud API. Cloud Run provides a serverless platform that lets you run containers without managing infrastructure.

---

## 🎯 Objectives

By the end of this lab, you will:
- Build a Docker container from a simple Flask application
- Push the container to Google Container Registry (GCR)
- Deploy the container to Cloud Run using the Python API
- Make the service accessible via a public URL
- Automate the entire CI/CD pipeline with a single Python script

---

## 🧰 Prerequisites

- Docker installed and running locally
- GCP project with billing enabled
- Cloud Run API and Container Registry APIs enabled
- Service account with Cloud Run Admin and Storage Admin roles
- Python 3.8+ installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB10-Cloud-Run-Deployment/
├── app.py                  # Simple Flask application
├── Dockerfile              # Container configuration
├── deploy_run.py           # Deployment script with TODOs
├── solutions.md            # Solutions for the TODOs (reference only)
├── requirements.txt        # Required Python packages
└── README.md               # Lab instructions
```

---

## 🚀 Getting Started

### 1. Set up your service account credentials:
```bash
# Create a service account (if you don't have one yet)
gcloud iam service-accounts create cloud-run-deployer --display-name="Cloud Run Deployer"

# Grant the required roles
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:cloud-run-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:cloud-run-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

# Download credentials
gcloud iam service-accounts keys create key.json \
    --iam-account=cloud-run-deployer@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Point to your credentials file
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/key.json"
```

### 2. Enable the required APIs:
```bash
gcloud services enable run.googleapis.com containerregistry.googleapis.com
```

### 3. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB10-Cloud-Run-Deployment/
```

### 4. Create and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 5. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📝 Your Task

In this lab, you will complete the TODOs in the `deploy_run.py` script to:

1. Authenticate with Google Cloud using service account credentials
2. Build the Cloud Run API client
3. Build and push a Docker image to Google Container Registry
4. Deploy the container to Cloud Run
5. Wait for the deployment to complete
6. Retrieve the public URL of the deployed service

The script already contains:
- Command-line argument parsing
- Error handling
- Main function structure
- A complete Flask app in `app.py` and Dockerfile

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Understanding the Application

Before implementing the deployment script, take a look at:

1. `app.py` - A simple Flask application with endpoints:
   - `/` - Returns a JSON greeting
   - `/health` - Health check endpoint

2. `Dockerfile` - Instructions for building the container:
   - Uses Python 3.9 base image
   - Copies and installs requirements
   - Runs the Flask app on port 8080

### Running the Script

Once you've completed the TODOs, run the script with your GCP project ID:

```bash
# Deploy to Cloud Run with defaults
python deploy_run.py --project_id YOUR_PROJECT_ID

# Deploy with a custom service name
python deploy_run.py --project_id YOUR_PROJECT_ID --service_name custom-app-name
```

---

## 🔍 Documentation References

- [Cloud Run API](https://cloud.google.com/run/docs/reference/rest)
- [Container Registry API](https://cloud.google.com/container-registry/docs/reference/rest)
- [Python Docker SDK](https://docker-py.readthedocs.io/en/stable/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully builds and pushes the Docker image to GCR  
✅ Creates a Cloud Run service with the specified image  
✅ Waits for the deployment to complete  
✅ Displays the correct service URL  
✅ Makes the service publicly accessible  
✅ Handles errors gracefully with clear messages  

---

## 💡 Hints and Tips

- Docker commands can be run via the `subprocess` module
- The Cloud Run API uses a different structure than other GCP APIs
- The deployment can take 1-2 minutes to complete
- Test your service by making an HTTP request to the returned URL
- Remember to use proper error handling for Docker commands

---

## 🧹 Cleanup

Always delete your Cloud Run services when you're done to avoid unnecessary charges:

```bash
# Using gcloud
gcloud run services delete devops-cloudrun --region=us-central1 --quiet
```

Or add a parameter to your script to enable cleanup:

```bash
# Add a --delete parameter to your script implementation
python deploy_run.py --project_id YOUR_PROJECT_ID --service_name devops-cloudrun --delete
```

---

## 💬 What's Next?

Congratulations! You've completed all 10 GCP Python labs. Consider these next steps:

1. Connect this Cloud Run service to a database like Cloud SQL
2. Set up a CI/CD pipeline using Cloud Build
3. Add authentication to your Cloud Run service
4. Implement monitoring and logging
5. Build and deploy a more complex application

---

## 🙏 Acknowledgments

Cloud Run makes containerized applications easier than ever. You've mastered Python automation across the entire GCP ecosystem! From compute to storage, databases to containers, you've built real automation skills that form the foundation of modern DevOps practices.

Code, containerize, deploy, scale. ☁️🐳🚀

