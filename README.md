# Python Development & DevOps Automation Labs

This repository provides a structured and practical journey to master **Python for DevOps**, beginning with fundamental programming concepts and progressing toward automation, scripting, and finally cloud integration with **AWS**, **Azure**, and **GCP**.

It is designed to help DevOps engineers and aspiring automation experts become proficient in Python as a powerful tool for infrastructure operations and system automation.

## 📦 About This Repository

These labs are ideal for learners who want to:
- Learn Python from the ground up
- Build real-world scripts and DevOps automation tools
- Understand how Python fits into modern infrastructure and CI/CD workflows
- Interact with cloud providers using Python SDKs

## 📁 Repository Structure

```bash
python-labs/
│
├── Core-Python/                # Foundational Python programming labs
│   ├── LAB01-Basics-Variables/
│   ├── LAB02-Loops-and-Conditions/
│   ├── LAB03-Functions-and-Modules/
│   ├── LAB04-File-Handling/
│   ├── LAB05-Error-Handling-and-Logging/
│   ├── LAB06-OOP-and-Classes/
│   ├── LAB07-Virtualenv-and-Packaging/
│   ├── LAB08-Unit-Testing-Basics/
│   ├── LAB09-Data-Formats/
│   ├── LAB10-API-Interaction/
│   ├── LAB11-CLI-Development/
│   └── LAB12-Async-Programming/
│
├── Automation-Scripting/       # DevOps scripting and tool building
│   ├── LAB01-Simple-CLI-Tool/
│   ├── LAB02-Automate-File-Downloads/
│   ├── LAB03-Process-Logs-and-Reports/
│   ├── LAB04-System-Monitoring-Scripts/
│   ├── LAB05-API-Integration-Tool/
│   └── LAB06-Task-Scheduler-Automation/
│
├── Cloud-Automation/           # Python SDK automation with AWS, Azure, GCP
│   ├── AWS/                    # AWS automation with boto3
│   │   ├── LAB01-EC2-Automation/
│   │   ├── LAB02-S3-File-Upload/
│   │   ├── LAB03-IAM-User-and-Policy-Automation/
│   │   ├── LAB04-CloudWatch-Metrics-and-Alerts/
│   │   ├── LAB05-Lambda-Deployment/
│   │   ├── LAB06-CloudFormation-Stack-Launch/
│   │   ├── LAB07-DynamoDB-Table-Automation/
│   │   ├── LAB08-SNS-Topic-and-Subscription/
│   │   ├── LAB09-SQS-Queue-Automation/
│   │   └── LAB10-EventBridge-Rule-Trigger/
│   │
│   ├── Azure/                  # Azure automation with azure-mgmt
│   │   ├── LAB01-VM-Creation-With-AzureSDK/
│   │   ├── LAB02-Blob-Storage-Upload/
│   │   ├── LAB03-IAM-Role-Assignment/
│   │   ├── LAB04-Azure-Function-Deployment/
│   │   ├── LAB05-Monitor-Metrics-And-Alerts/
│   │   ├── LAB06-Service-Bus-Queue-Creation/
│   │   ├── LAB07-Azure-SQL-Database-Automation/
│   │   ├── LAB08-Virtual-Network-Setup/
│   │   ├── LAB09-CosmosDB-Document-Management/
│   │   └── LAB10-Azure-Container-Instance-Launch/
│   │
│   └── GCP/                    # GCP automation with google-cloud
│       ├── LAB01-Compute-Instance-Creation/
│       ├── LAB02-GCS-File-Upload/
│       ├── LAB03-IAM-Service-Account-Creation/
│       ├── LAB04-Cloud-Functions-Deployment/
│       ├── LAB05-Cloud-Monitoring-Metrics/
│       ├── LAB06-PubSub-Topic-and-Subscription/
│       ├── LAB07-Cloud-SQL-Instance-Automation/
│       ├── LAB08-VPC-Network-Creation/
│       ├── LAB09-Firestore-Document-Operations/
│       └── LAB10-Cloud-Run-Deployment/
│
└── ROADMAP.md                  # Complete learning path and progression
```

Each lab folder includes:
- Python scripts (`main.py`, `utils.py`, etc.) with TODOs for student implementation
- Complete solution reference in `solutions.md`
- `README.md` with lab purpose, steps, and cleanup instructions
- Optional: `requirements.txt`, `env.example`, or `config.yaml`

## 🧰 Prerequisites

To complete these labs, you should have:
- Python 3.8+ with `pip` or `venv`
- A basic code editor and terminal setup
- Optional for cloud labs: AWS, Azure, or GCP account with credentials

## 🚀 How to Use These Labs

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-org>/python-labs.git
   cd python-labs
   ```

2. Navigate to any lab (e.g., `Core-Python/LAB02-Loops-and-Conditions/`)

3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

4. Install dependencies (if present):
   ```bash
   pip install -r requirements.txt
   ```

5. Follow the lab instructions in the README.md and implement the code by completing the TODOs.

6. Check your solution against the reference implementation in solutions.md.

## 📈 Learning Progression

Our labs follow a clear learning path:

1. **Phase 1: Core Python** — Master Python fundamentals, OOP, data formats, API interaction, CLI development, and async programming
2. **Phase 2: Automation Scripting** — Build practical automation tools and scripts for file operations, monitoring, and task scheduling
3. **Phase 3: Cloud Automation** — Use cloud SDKs to manage resources programmatically across AWS, Azure, and GCP

## 🌐 Detailed Lab Roadmap

See the [Python Labs Roadmap](./ROADMAP.md) for a comprehensive breakdown of:
- All labs by category and difficulty level
- Future lab additions and topics
- Suggested learning paths based on your goals

## 🤝 Contributing

We welcome contributions!
1. Fork the repo
2. Create a branch (`feature/lab-name`)
3. Add your lab under the relevant section
4. Submit a pull request with a clear description and test steps

## 🙏 Acknowledgments

- Python.org
- Cloud SDKs: `boto3`, `azure-mgmt`, `google-cloud`
- Open source contributors and DevOps mentors

## 🧠 Python First, Automation Always

Master the language before the clouds. These labs will help you build a solid Python foundation, empowering you to automate systems, workflows, and cloud infrastructure with confidence.

Happy automating! 🐍️✨

