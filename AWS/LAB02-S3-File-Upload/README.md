# AWS LAB02 - Automate File Upload to S3 with Python (boto3)

This lab will teach you how to upload files to an S3 bucket using Python and `boto3`. S3 is one of the most widely used cloud storage solutions, and automating uploads is useful for backups, reports, logs, and more.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to AWS S3 using Python
- Create S3 buckets programmatically 
- Upload a local file to a specific S3 bucket
- Set metadata and access control during the upload
- Generate presigned URLs for private files
- List objects in a bucket
- Clean up resources by deleting buckets and objects

---

## 🧰 Prerequisites

- AWS account and S3 permissions
- Python 3.8+ and `boto3` installed
- Basic understanding of AWS S3 concepts

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB02-S3-File-Upload/
├── upload_file.py
├── sample.txt              # Sample file to upload
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB02-S3-File-Upload/
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install `boto3`:
```bash
pip install -r requirements.txt
```

---

## ✍️ Your Task

Open `upload_file.py` and complete all the TODOs:

1. In the `create_bucket()` function:
   - Initialize the S3 client with the appropriate region
   - Set up the LocationConstraint parameter correctly
   - Create the bucket with appropriate parameters
   - Handle different error codes properly

2. In the `upload_file()` function:
   - Handle the object_name parameter
   - Initialize the S3 client
   - Set the ACL parameter based on the make_public flag
   - Implement the file upload
   - Generate a public URL when appropriate

3. In the `generate_presigned_url()` function:
   - Initialize the S3 client
   - Generate a presigned URL with proper parameters

4. In the `list_bucket_files()` function:
   - Initialize the S3 client
   - List objects in the bucket
   - Extract and print file information

5. In the `delete_bucket()` function:
   - Implement the logic to delete all objects if force=True
   - Delete the bucket once it's empty

6. In the `main()` function:
   - Add command-line arguments to the parser
   - Parse the arguments
   - Generate a unique bucket name when needed
   - Implement the complete workflow

### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ Create a bucket successfully  
✅ Upload a file to the bucket  
✅ Make the file public if specified  
✅ Generate a presigned URL for private files  
✅ List all objects in the bucket  
✅ Clean up resources when requested  
✅ Script runs cleanly:
```bash
python upload_file.py --file sample.txt --public
```

---

## 🧹 Cleanup
Implement the `delete_bucket()` function correctly to handle cleanup. The function should:
- Delete all objects in the bucket when force=True
- Handle pagination for buckets with many objects
- Delete the bucket once it's empty

---

## 💬 What's Next?
Move to [AWS LAB03 - IAM User and Policy Automation](../LAB03-IAM-User-and-Policy-Automation/) to start managing users and permissions with Python.

---

## 🙏 Acknowledgments
Automated S3 operations save time and reduce errors. Combine with cron jobs or CI pipelines for powerful workflows.

Happy scripting! 🪣🐍

