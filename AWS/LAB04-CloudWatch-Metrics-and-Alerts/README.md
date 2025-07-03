# AWS LAB04 - Monitor CloudWatch Metrics and Create Alerts with Python (boto3)

This lab guides you through collecting EC2 metrics and setting up an alarm using AWS CloudWatch via Python. Monitoring is a core DevOps skill, and automating it is even better.

---

## 🎯 Objectives

By the end of this lab, you will:
- Retrieve EC2 CPU utilization metrics using CloudWatch API
- Create CloudWatch alarms based on metric thresholds
- List and manage existing CloudWatch alarms
- Delete CloudWatch alarms when they're no longer needed
- Verify EC2 instance states programmatically

---

## 🧰 Prerequisites

- AWS account with EC2 and CloudWatch permissions
- A running EC2 instance (or create one in LAB01)
- Python 3.8+ and `boto3` installed
- Basic understanding of CloudWatch metrics and alarms

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB04-CloudWatch-Metrics-and-Alerts/
├── monitor.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB04-CloudWatch-Metrics-and-Alerts/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ✍️ Your Task

Open `monitor.py` and complete all the TODOs:

1. In the `get_cpu_metrics()` function:
   - Initialize the CloudWatch client
   - Set default time ranges for metrics queries
   - Retrieve CPU utilization metrics using get_metric_statistics
   - Process and return the results sorted by timestamp

2. In the `create_cpu_alarm()` function:
   - Initialize the CloudWatch client
   - Create a CloudWatch alarm using put_metric_alarm
   - Configure all required parameters for the alarm

3. In the `list_alarms()` function:
   - Initialize the CloudWatch client
   - Retrieve alarms using describe_alarms
   - Format and display alarm information

4. In the `delete_alarm()` function:
   - Initialize the CloudWatch client
   - Delete a CloudWatch alarm using delete_alarms

5. In the `check_instance_exists()` function:
   - Initialize the EC2 client
   - Check if an instance exists and is in the running state
   - Handle different instance states appropriately

6. In the `print_metrics()` function:
   - Format and display CloudWatch metrics in a readable format

7. In the `main()` function:
   - Set up command-line arguments
   - Implement the main workflow based on provided arguments
   - Add appropriate error handling

### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ Successfully retrieve CPU metrics for an EC2 instance  
✅ Display metrics in a readable format  
✅ Create a CloudWatch alarm for high CPU usage  
✅ List all CloudWatch alarms in your account  
✅ Delete a CloudWatch alarm when it's no longer needed  
✅ Properly validate that an instance exists before monitoring it  
✅ Script runs without error:
```bash
python monitor.py --instance-id i-0123456789abcdef --create-alarm
```

---

## 🧹 Cleanup

To clean up the resources created during this lab, run:
```bash
python monitor.py --delete-alarm HighCPUAlert
```

Make sure to implement the `delete_alarm()` function correctly to avoid unnecessary charges from CloudWatch alarms.

---

## 💬 What's Next?
Advance to [AWS LAB05 - Lambda Deployment](../LAB05-Lambda-Deployment/) to start working with serverless functions.

---

## 🙏 Acknowledgments
Automated monitoring ensures visibility and helps prevent downtime. DevOps teams rely on CloudWatch to alert before things break.

Happy monitoring! 📊🐍