# GCP LAB07 - Automate Cloud SQL Instance Creation with Python

In this lab, you'll use Python to create a Cloud SQL instance in GCP using the `google-api-python-client`. Cloud SQL provides fully managed relational databases that are secure, reliable, and easy to manage.

---

## 🎯 Objectives

By the end of this lab, you will:
- Programmatically create a Cloud SQL instance
- Specify database type, version, and machine size
- Configure backup settings for your database
- List existing SQL instances in your project
- Clean up resources to avoid unnecessary charges

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Cloud SQL Admin API enabled (enable with `gcloud services enable sqladmin.googleapis.com`)
- Service account with Cloud SQL Admin role (roles/cloudsql.admin)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB07-Cloud-SQL-Instance-Automation/
├── create_sql_instance.py   # Main script with TODOs to implement
├── solutions.md             # Solutions for the TODOs (reference only)
├── requirements.txt         # Required Python packages
└── README.md                # Lab instructions
```

---

## 🚀 Getting Started

### 1. Set up your service account credentials:
```bash
# Create a service account (if you don't have one yet)
gcloud iam service-accounts create sql-automation --display-name="SQL Automation Account"

# Grant the required role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:sql-automation@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.admin"

# Download credentials
gcloud iam service-accounts keys create key.json \
    --iam-account=sql-automation@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Point to your credentials file
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/key.json"
```

### 2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB07-Cloud-SQL-Instance-Automation/
```

### 3. Create and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📝 Your Task

In this lab, you will complete the TODOs in the `create_sql_instance.py` script to:

1. Authenticate with Google Cloud using service account credentials
2. Build the SQL Admin API client
3. Define the Cloud SQL instance configuration
4. Create and monitor the SQL instance deployment
5. List existing SQL instances
6. Implement a cleanup function to delete the instance

The script already contains:
- Command-line argument parsing
- Error handling
- Helper functions for displaying instance information

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the Script

Once you've completed the TODOs, run the script with your GCP project ID:

```bash
# Create a new MySQL instance
python create_sql_instance.py --project_id YOUR_PROJECT_ID --create --instance_name test-mysql-instance

# List existing instances
python create_sql_instance.py --project_id YOUR_PROJECT_ID --list

# Delete an instance (cleanup)
python create_sql_instance.py --project_id YOUR_PROJECT_ID --delete --instance_name test-mysql-instance
```

---

## 🔍 Documentation References

- [Cloud SQL Admin API](https://cloud.google.com/sql/docs/mysql/admin-api/rest)
- [Python Google API Client](https://googleapis.github.io/google-api-python-client/docs/)
- [Cloud SQL Instance Resource](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully authenticates with the Cloud SQL Admin API  
✅ Creates a SQL instance with the specified configuration  
✅ Lists all SQL instances in the project correctly  
✅ Properly deletes the SQL instance when cleanup is requested  
✅ Handles errors gracefully with clear messages  

---

## 💡 Hints and Tips

- Cloud SQL instance creation can take several minutes to complete
- Use unique instance names to avoid conflicts with existing instances
- Remember that SQL instances incur charges as long as they exist
- The instance name must comply with the pattern: `[a-z][a-z0-9-]+` (start with a letter, only lowercase letters, numbers, and hyphens)
- Consider setting a smaller machine type (db-f1-micro) for testing

---

## 🧹 Cleanup

Always delete your Cloud SQL instances when you're done with them to avoid unnecessary charges:

```bash
# Using your script
python create_sql_instance.py --project_id YOUR_PROJECT_ID --delete --instance_name test-mysql-instance

# Or using gcloud (alternative)
gcloud sql instances delete test-mysql-instance
```

---

## 💬 What's Next?
Next lab: [GCP LAB08 - VPC Network Creation](../LAB08-VPC-Network-Creation/) to build private networks and subnets with Python.

---

## 🙏 Acknowledgments
Cloud SQL powers secure, scalable relational databases. Automating the provisioning process ensures fast, repeatable deployments and consistent configurations across your environments.

Scale your data, Pythonically! 🗄☁️🐍

