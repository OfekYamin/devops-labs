# GCP LAB08 - Automate VPC Network Creation with Python

In this lab, you'll learn how to automate the creation of a VPC network and subnet in Google Cloud using Python and the `google-api-python-client`. Private networks are essential for organizing cloud infrastructure securely and efficiently.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a custom VPC network programmatically
- Add a subnet with a specific IP CIDR range
- Configure firewall rules to control network traffic
- List existing networks and subnets in your project
- Implement proper resource cleanup to avoid orphaned networks

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Compute Engine API enabled (enable with `gcloud services enable compute.googleapis.com`)
- Service account with Compute Network Admin role (roles/compute.networkAdmin)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB08-VPC-Network-Creation/
├── create_vpc.py         # Main script with TODOs to implement
├── solutions.md          # Solutions for the TODOs (reference only)
├── requirements.txt      # Required Python packages
└── README.md             # Lab instructions
```

---

## 🚀 Getting Started

### 1. Set up your service account credentials:
```bash
# Create a service account (if you don't have one yet)
gcloud iam service-accounts create network-automation --display-name="Network Automation Account"

# Grant the required role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:network-automation@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/compute.networkAdmin"

# Download credentials
gcloud iam service-accounts keys create key.json \
    --iam-account=network-automation@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Point to your credentials file
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/key.json"
```

### 2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB08-VPC-Network-Creation/
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

In this lab, you will complete the TODOs in the `create_vpc.py` script to:

1. Authenticate with Google Cloud using service account credentials
2. Build the Compute Engine API client
3. Create a custom VPC network with custom subnet mode
4. Create a subnet with a specific CIDR range
5. Configure a basic firewall rule to allow SSH access
6. List existing networks and subnets
7. Implement cleanup functionality to delete resources

The script already contains:
- Command-line argument parsing
- Error handling
- Helper functions for displaying network information

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the Script

Once you've completed the TODOs, run the script with your GCP project ID:

```bash
# Create a new VPC network and subnet
python create_vpc.py --project_id YOUR_PROJECT_ID --create --network_name custom-vpc --subnet_name custom-subnet

# List existing networks and subnets
python create_vpc.py --project_id YOUR_PROJECT_ID --list

# Delete a network and its subnets (cleanup)
python create_vpc.py --project_id YOUR_PROJECT_ID --delete --network_name custom-vpc
```

---

## 🔍 Documentation References

- [VPC Network Overview](https://cloud.google.com/vpc/docs/vpc)
- [Compute Engine API - Networks](https://cloud.google.com/compute/docs/reference/rest/v1/networks)
- [Compute Engine API - Subnetworks](https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks)
- [Python Google API Client](https://googleapis.github.io/google-api-python-client/docs/)

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully creates a custom VPC network  
✅ Creates a subnet with the specified CIDR range  
✅ Configures appropriate firewall rules  
✅ Lists networks and subnets correctly  
✅ Properly cleans up resources when requested  
✅ Handles errors gracefully with clear messages  

---

## 💡 Hints and Tips

- Use `autoCreateSubnetworks: False` to create a custom mode VPC network
- Remember that subnet CIDR ranges cannot overlap within the same network
- VPC networks exist at the global level, while subnets are regional resources
- When creating resources, check if they already exist to avoid errors
- Always delete resources in the right order: subnets before networks
- Use meaningful names for your networks and subnets to simplify management

---

## 🧹 Cleanup

Always clean up your resources to avoid unnecessary charges:

```bash
# Using your script
python create_vpc.py --project_id YOUR_PROJECT_ID --delete --network_name custom-vpc

# Or using gcloud (alternative)
gcloud compute networks subnets delete custom-subnet --region=us-central1
gcloud compute networks delete custom-vpc
```

---

## 💬 What's Next?
Next lab: [GCP LAB09 - Firestore Document Operations](../LAB09-Firestore-Document-Operations/) to automate NoSQL document creation and queries.

---

## 🙏 Acknowledgments
VPC networks are the foundation of your cloud network architecture. Automating their creation ensures consistency, reduces errors, and enables infrastructure as code practices for your networking resources.

Design smart networks! 🌐☁️🐍

