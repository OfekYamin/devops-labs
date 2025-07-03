# GCP LAB05 - Retrieve Cloud Monitoring Metrics with Python

In this lab, you'll use Python and the Google Cloud Monitoring API to access and analyze real-time performance metrics from your GCP resources. This essential skill enables visibility, automated reporting, and proactive health monitoring in cloud environments.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to the Cloud Monitoring API and authenticate properly
- Query time-series metrics for GCP resources (e.g., Compute Engine instances)
- Format and display complex monitoring data in user-friendly formats
- Plot metric data to visualize performance patterns
- Understand how to extend monitoring scripts for different metrics

---

## 🧰 Prerequisites

- Google Cloud account with an active project
- At least one monitored resource (Compute Engine VM, Cloud SQL instance, etc.)
- Cloud Monitoring API enabled in your project
- Service account with Monitoring Viewer role (roles/monitoring.viewer)
- Service account key file (JSON) downloaded to your local machine
- Python 3.8 or higher installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB05-Cloud-Monitoring-Metrics/
├── fetch_metrics.py         # The main Python script (with TODOs)
├── requirements.txt         # Python dependencies
├── solutions.md             # Solutions to the TODOs
└── README.md                # This file
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
cd Cloud-Automation/GCP/LAB05-Cloud-Monitoring-Metrics/
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

In this lab, you will complete the TODOs in the `fetch_metrics.py` script to:

1. Create a time interval for fetching metrics
2. Initialize the Cloud Monitoring API client
3. Query metrics using the appropriate API calls
4. Format and display the results in a readable format
5. Implement basic data visualization with matplotlib

The script already contains:
- A predefined list of common metric types
- Command-line argument parsing
- Error handling and validation
- Utility functions to list available metrics

Your job is to fill in the missing implementation details marked with `TODO` comments.

### Running the script

Once you've completed the TODOs, run your script to list available metrics:

```bash
python fetch_metrics.py --project=your-gcp-project-id --list-metrics
```

Then, retrieve CPU utilization metrics:

```bash
python fetch_metrics.py --project=your-gcp-project-id --metric=cpu
```

You can adjust the time window (in minutes):

```bash
python fetch_metrics.py --project=your-gcp-project-id --metric=cpu --window=30
```

To visualize the metrics with a plot:

```bash
python fetch_metrics.py --project=your-gcp-project-id --metric=cpu --plot
```

---

## 🧪 Validation Checklist

Ensure your implementation:

✅ Successfully authenticates with the Cloud Monitoring API  
✅ Retrieves metric data for the specified time window  
✅ Displays the data in a readable tabular format  
✅ Shows summary statistics for the metrics  
✅ Plots the data graphically when requested  

---

## 🧹 Cleanup

This lab doesn't create any resources; it only reads existing metrics data. There's no cleanup required.

---

## 💬 What's Next?

After completing this lab, proceed to [GCP LAB06 - Pub/Sub Topic and Subscription](../LAB06-PubSub-Topic-and-Subscription/) to learn how to implement event-driven architectures using Google Cloud Pub/Sub.

---

## 🙏 Acknowledgments

Cloud Monitoring is a critical component of any robust cloud architecture, enabling teams to observe, track, and respond to performance trends and incidents. The programmatic access to metrics provides powerful opportunities for custom dashboards, automated reporting, and integration with alerting systems.

Happy cloud monitoring! 📊☁️🐍

