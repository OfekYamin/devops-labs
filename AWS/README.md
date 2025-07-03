# AWS Python Automation Labs

Welcome to the **AWS Python Automation Labs** — a hands-on collection of real-world labs focused on automating AWS services using Python and the `boto3` SDK. These labs are part of the broader **Python for DevOps** training path.

Each lab is designed to progressively teach you how to use Python to automate cloud operations, from launching EC2 instances to setting up serverless workflows and event-driven triggers.

---

## 🚀 What You'll Learn

By completing these labs, you'll gain practical experience in:
- Automating compute, storage, and networking services
- Managing permissions and security policies
- Deploying serverless applications and event-based infrastructure
- Monitoring resources and responding to cloud events

---

## 🧰 Prerequisites

To complete these labs, you should have:
- A valid AWS account
- AWS CLI configured (`aws configure`)
- Python 3.8+ installed
- Basic familiarity with Python scripting

Each lab includes:
- Step-by-step instructions
- Sample code using `boto3`
- Validation checklist
- Cleanup steps to avoid extra charges

---

## 🔐 Authentication Setup

Before running the lab code, you need to set up authentication for the boto3 SDK. There are several methods you can use:

### Method 1: AWS CLI Configuration (Recommended for Development)

This method uses credentials stored by the AWS CLI:

```bash
# Install AWS CLI
pip install awscli

# Configure your credentials
aws configure
```

When prompted, enter:
- Your AWS Access Key ID
- Your AWS Secret Access Key
- Default region name (use `eu-west-1` for these labs)
- Default output format (use `json`)

The credentials are stored in `~/.aws/credentials` (Linux/Mac) or `%USERPROFILE%\.aws\credentials` (Windows).

### Method 2: Environment Variables

Set your credentials as environment variables:

```bash
# For Linux/Mac
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_DEFAULT_REGION="eu-west-1"

# For Windows PowerShell
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
$env:AWS_DEFAULT_REGION="eu-west-1"

# For Windows Command Prompt
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key
set AWS_DEFAULT_REGION=eu-west-1
```

### Method 3: Boto3 Session with Profile

If you have multiple AWS profiles configured, you can specify which one to use:

```python
import boto3

# Create a session using a specific profile
session = boto3.Session(profile_name='my-profile')

# Use the session to create clients
s3 = session.client('s3')
ec2 = session.client('ec2')
```

### Method 4: IAM Roles (for EC2 or Lambda)

If you're running your code on AWS services like EC2 or Lambda, use IAM roles instead of hardcoded credentials:

1. Create an IAM role with the necessary permissions
2. Attach the role to your EC2 instance or Lambda function
3. Boto3 will automatically use the role's credentials

### Method 5: Assume Role (for Cross-Account Access)

To access resources in another AWS account:

```python
import boto3

# Create an STS client
sts_client = boto3.client('sts')

# Assume a role in another account
assumed_role = sts_client.assume_role(
    RoleArn="arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME",
    RoleSessionName="AssumeRoleSession"
)

# Extract the temporary credentials
credentials = assumed_role['Credentials']

# Create a client using the temporary credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)
```

### Security Best Practices

1. **Never hardcode credentials** in your Python scripts
2. Use IAM roles when possible instead of access keys
3. Grant the minimum permissions necessary for your task
4. Rotate access keys regularly
5. Use temporary credentials when possible
6. For production, consider using AWS Secrets Manager or Parameter Store

---

## 📁 Lab Structure

```bash
AWS/
├── LAB01-EC2-Automation/
├── LAB02-S3-File-Upload/
├── LAB03-IAM-User-and-Policy-Automation/
├── LAB04-CloudWatch-Metrics-and-Alerts/
├── LAB05-Lambda-Deployment/
├── LAB06-CloudFormation-Stack-Launch/
├── LAB07-DynamoDB-Table-Automation/
├── LAB08-SNS-Topic-and-Subscription/
├── LAB09-SQS-Queue-Automation/
└── LAB10-EventBridge-Rule-Trigger/
```

Each folder includes a fully documented `README.md`, example code, and any additional resources required.

---

## 🧠 Lab Progression

1. **Core Services**: EC2, S3, IAM
2. **Monitoring & Notifications**: CloudWatch, SNS
3. **Serverless & NoSQL**: Lambda, DynamoDB
4. **Infrastructure as Code**: CloudFormation
5. **Messaging & Events**: SQS, EventBridge

These labs follow a natural DevOps lifecycle and reinforce the principles of **Infrastructure as Code**, **automation**, and **cloud-native architecture**.

---

## 🌐 Lab Environment

- **AWS Region**: These labs use `eu-west-1` (Ireland) as the default region
- **Required Permissions**: Labs require appropriate IAM permissions
- **Cost Warning**: Some resources created may incur AWS charges if not deleted

---

## 🙏 Acknowledgments

- AWS & the boto3 team for Python SDK support
- DevOps engineers and educators for open learning content
- Contributors to the Python & cloud automation community

---

## 💬 Contributing

Want to improve a lab or add a new one?
- Fork the repository
- Create a branch (e.g. `feature/lab11-cloudtrail`)
- Submit a pull request with your lab folder and README

---

## 🌍 Automate the Cloud, Pythonically

This AWS lab series will equip you to build powerful automations and become fluent in managing cloud infrastructure through Python.

Happy automating! ☁️🐍

