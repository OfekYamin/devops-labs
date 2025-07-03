# AWS LAB01 - Automate EC2 Instance Launch with Python (boto3)

In this lab, you'll learn how to launch an Amazon EC2 instance using Python and the `boto3` SDK. This is your first step into cloud automation using Python!

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how to configure AWS credentials for `boto3`
- Use Python to interact with EC2 APIs using the client interface
- Launch a t2.micro EC2 instance in your default VPC
- Print out the instance ID and public DNS

---

## 🧰 Prerequisites

- AWS account and IAM user with EC2 permissions
- `aws configure` run at least once (to store credentials)
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB01-EC2-Automation/
├── launch_ec2.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB01-EC2-Automation/
```

2. Create and activate a virtual environment:
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

Open `launch_ec2.py` and complete all the TODOs:

1. Initialize the EC2 client with the appropriate region
2. Set the AMI ID for Amazon Linux 2023 in eu-west-1
3. Configure your key pair name and security group ID
4. Define instance tags
5. Implement the `launch_instance()` function to create an EC2 instance
6. Implement the `wait_for_instance()` function to poll until the instance is running
7. Implement the `display_instance_details()` function to print instance information
8. Implement the `terminate_instance()` function for cleanup
9. In the main section, uncomment and complete the required steps

### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ AWS credentials configured  
✅ Instance launched successfully (t2.micro)  
✅ Printed instance ID and public DNS  
✅ Script runs without error:
```bash
python launch_ec2.py
```

---

## 🧹 Cleanup
Make sure to implement the `terminate_instance()` function correctly to avoid unwanted AWS charges.

If needed, you can also terminate the instance manually in the AWS Console:
1. Go to the EC2 Dashboard
2. Select your instance
3. Choose Actions > Instance State > Terminate

---

## 💬 What's Next?
Try [AWS LAB02 - S3 File Upload](../LAB02-S3-File-Upload/) to automate object storage tasks using Python.

---

## 🙏 Acknowledgments
Launching infrastructure with code is the essence of DevOps. Mastering `boto3` enables powerful automations across AWS.

Happy automating! ☁️🐍
