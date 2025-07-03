# GCP LAB02 - Automate File Upload to Google Cloud Storage (GCS) with Python

In this lab, you'll use Python and the `google-cloud-storage` library to upload files to a Google Cloud Storage (GCS) bucket — one of the most common automation tasks in cloud environments.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to GCS using service account authentication
- Upload a file to a GCS bucket programmatically
- List objects in a bucket with the Python SDK
- Understand blob objects, metadata, and GCS naming conventions

---

## 🧰 Prerequisites

- Google Cloud account with an active project
- GCS bucket already created in your project
- Service account with Storage Admin role (roles/storage.admin)
- Service account key file (JSON) downloaded to your local machine
- Python 3.8 or higher installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB02-GCS-File-Upload/
├── upload_file.py        # The main Python script (with TODOs)
├── sample.txt            # Sample file to upload
├── requirements.txt      # Python dependencies
├── solutions.md          # Solutions to the TODOs
└── README.md             # This file
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
cd Cloud-Automation/GCP/LAB02-GCS-File-Upload/
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

In this lab, you will complete the TODOs in the `upload_file.py` script to:

1. Initialize the Google Cloud Storage client
2. Create a reference to your GCS bucket
3. Create a blob object for the destination file
4. Upload the file to GCS
5. List all objects in the bucket
6. Optional: Explore blob metadata and properties

The script already contains:
- Argument parsing for customizing upload parameters
- Error handling and logging
- A sample file (`sample.txt`) for testing your implementation

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the script

Once you've completed the TODOs, run your script with your bucket name:

```bash
python upload_file.py --bucket=your-gcs-bucket-name
```

To also list all files in the bucket after upload:

```bash
python upload_file.py --bucket=your-gcs-bucket-name --list
```

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully authenticates with GCS  
✅ Uploads the sample file to your bucket  
✅ Lists all objects in the bucket when the `--list` flag is used  
✅ Handles errors appropriately  
✅ Shows the public URL for the uploaded file  

You can verify your upload in the Google Cloud Console or with the gsutil command:

```bash
gsutil ls gs://your-gcs-bucket-name/
```

---

## 🧹 Cleanup

To avoid incurring storage charges, delete the uploaded file when you're done:

```bash
gsutil rm gs://your-gcs-bucket-name/sample.txt
```

---

## 💬 What's Next?

After completing this lab, proceed to [GCP LAB03 - IAM Service Account Creation](../LAB03-IAM-Service-Account-Creation/) to learn how to programmatically manage IAM service accounts and access controls in GCP.

---

## 🙏 Acknowledgments

Google Cloud Storage is an essential component for storing and serving files at scale. Mastering it unlocks endless automation workflows from web hosting to data lakes.

Happy cloud automating! 📂☁️🐍