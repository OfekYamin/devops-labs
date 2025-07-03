# GCP LAB06 - Automate Pub/Sub Topic and Subscription with Python

In this lab, you'll use Python to create a Pub/Sub topic and a subscription, publish messages, and pull them from the queue — all using the `google-cloud-pubsub` library. This is a fundamental skill for implementing event-driven architectures in Google Cloud.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a Pub/Sub topic using Python
- Subscribe to the topic with a pull subscription
- Publish messages to the topic and retrieve them
- Implement proper resource cleanup

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Pub/Sub API enabled (enable with `gcloud services enable pubsub.googleapis.com`)
- Service account with Pub/Sub Editor role (roles/pubsub.editor)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB06-PubSub-Topic-and-Subscription/
├── pubsub_script.py      # Main script with TODOs to implement
├── solutions.md          # Solutions for the TODOs (reference only)
├── requirements.txt      # Required Python packages
└── README.md             # Lab instructions
```

---

## 🚀 Getting Started

### 1. Set up your service account credentials:
```bash
# Create a service account (if you don't have one yet)
gcloud iam service-accounts create pubsub-automation --display-name="PubSub Automation Account"

# Grant the required role
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:pubsub-automation@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/pubsub.editor"

# Download credentials
gcloud iam service-accounts keys create key.json \
    --iam-account=pubsub-automation@YOUR_PROJECT_ID.iam.gserviceaccount.com

# Point to your credentials file
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/key.json"
```

### 2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB06-PubSub-Topic-and-Subscription/
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

In this lab, you will complete the TODOs in the `pubsub_script.py` script to:

1. Create a Pub/Sub topic and subscription
2. Publish multiple messages to the topic
3. Pull and acknowledge messages from the subscription
4. Properly clean up resources when finished

The script already contains:
- Command-line argument parsing
- Error handling
- Helper functions and structure

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the Script

Once you've completed the TODOs, run the script with your GCP project ID:

```bash
python pubsub_script.py --project_id YOUR_PROJECT_ID --cleanup
```

The script accepts several arguments:
- `--project_id`: Your GCP project ID (required)
- `--topic`: Custom topic name (default: "devops-demo-topic")
- `--subscription`: Custom subscription name (default: "devops-demo-sub")
- `--message`: Custom message to publish (can be used multiple times)
- `--cleanup`: Flag to delete resources after running

---

## 🔍 Documentation References

- [Pub/Sub Client Libraries](https://cloud.google.com/pubsub/docs/reference/libraries)
- [Python Pub/Sub Documentation](https://googleapis.dev/python/pubsub/latest/index.html)
- [Google Cloud Pub/Sub Concepts](https://cloud.google.com/pubsub/docs/overview)

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Topic is created successfully  
✅ Subscription is created and attached to the topic  
✅ Messages are published to the topic  
✅ Messages are pulled and acknowledged  
✅ Resources are properly cleaned up  
✅ No errors or exceptions during execution

---

## 💡 Hints and Tips

- Remember to encode string messages to bytes before publishing
- When pulling messages, check if any were received before acknowledging
- Always delete resources in the reverse order they were created
- Use the `future.result()` pattern to get message IDs when publishing
- Check the GCP console to verify your resources are created/deleted

---

## 🧹 Cleanup

The script includes cleanup functionality when the `--cleanup` flag is used. However, if you need to manually clean up:

```bash
# Using gcloud (alternative cleanup)
gcloud pubsub subscriptions delete devops-demo-sub
gcloud pubsub topics delete devops-demo-topic
```

---

## 💬 What's Next?
Advance to [GCP LAB07 - Cloud SQL Instance Automation](../LAB07-Cloud-SQL-Instance-Automation/) to provision and interact with relational databases.

---

## 🙏 Acknowledgments
Pub/Sub is the backbone of event-driven architecture in GCP. Automating it brings your applications one step closer to full cloud integration.

Push, pull, and automate! ☁️📨🐍

