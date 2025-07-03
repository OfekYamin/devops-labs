# GCP LAB01 - Automate Compute Engine Instance Creation with Python

In this lab, you'll use Python and the Google Cloud SDK to programmatically create a virtual machine (VM) instance in Google Cloud Platform (GCP) using the `google-cloud-compute` library.

---

## 🎯 Objectives

By the end of this lab, you will:
- Set up authentication to GCP using a service account
- Implement Python code to create a Compute Engine VM
- Configure machine type, zone, and OS image for your VM
- Learn how to wait for and validate asynchronous GCP operations

---

## 🧰 Prerequisites

- Google Cloud account with an active project
- Service account with Compute Admin role (roles/compute.admin)
- Service account key file (JSON) downloaded to your local machine
- Python 3.8 or higher installed
- Basic understanding of command-line interfaces

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB01-Compute-Instance-Creation/
├── create_instance.py  # The main Python script (with TODOs)
├── requirements.txt    # Python dependencies
├── solutions.md        # Solutions to the TODOs
└── README.md           # This file
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
cd Cloud-Automation/GCP/LAB01-Compute-Instance-Creation/
```

### 3. Create a virtual environment

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

In this lab, you will complete the TODOs in the `create_instance.py` script to:

1. Initialize the Google Cloud Compute Engine clients
2. Create a VM instance configuration with appropriate settings
3. Submit the instance creation request
4. Wait for the operation to complete
5. Verify the instance was created successfully

The script already contains:
- Argument parsing for customizing instance parameters
- Error handling and logging
- Helper functions for building resource paths

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the script

Once you've completed the TODOs, run your script:

```bash
python create_instance.py --project=your-gcp-project-id
```

You can customize other parameters as needed:

```bash
python create_instance.py \
  --project=your-gcp-project-id \
  --zone=us-central1-a \
  --instance_name=my-test-vm \
  --machine_type=e2-medium \
  --image_project=debian-cloud \
  --image_family=debian-11
```

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully authenticates with GCP  
✅ Creates a VM instance with the specified configuration  
✅ Waits for the operation to complete  
✅ Handles and reports errors appropriately  
✅ Provides clear output about the created instance  

You can verify your instance was created using the Google Cloud Console or CLI:

```bash
gcloud compute instances describe YOUR_INSTANCE_NAME --zone=YOUR_ZONE
```

---

## 🧹 Cleanup

To avoid incurring charges, delete the instance when you're done:

```bash
gcloud compute instances delete YOUR_INSTANCE_NAME --zone=YOUR_ZONE
```

Or modify your script to include a cleanup function that deletes the instance.

---

## 💬 What's Next?

After completing this lab, proceed to [GCP LAB02 - GCS File Upload](../LAB02-GCS-File-Upload/) to learn how to automate file operations in Google Cloud Storage.

---

## 🙏 Acknowledgments

Compute Engine is the backbone of GCP infrastructure services. Learning to programmatically create and manage VMs is an essential skill for DevOps engineers and cloud automation specialists.

Happy cloud automating! 🖥️☁️🐍

