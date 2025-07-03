# AWS LAB05 - Deploy an AWS Lambda Function with Python (boto3)

In this lab, you'll deploy a basic AWS Lambda function using Python and the `boto3` SDK. Lambda is a powerful serverless compute service that enables you to run code without provisioning infrastructure.

---

## 🎯 Objectives

By the end of this lab, you will:
- Package a Python function into a Lambda deployment zip file
- Create an IAM role with proper permissions for Lambda execution
- Deploy a Lambda function using boto3
- Update an existing Lambda function's code and configuration
- Invoke the Lambda function and process its response
- Clean up Lambda resources when no longer needed

---

## 🧰 Prerequisites

- AWS account with Lambda and IAM permissions
- Python 3.8+ and `boto3` installed
- Basic understanding of AWS Lambda concepts

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB05-Lambda-Deployment/
├── lambda_function.py       # Lambda function code
├── deploy_lambda.py         # Deployment script with TODOs
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB05-Lambda-Deployment/
```

2. Create a virtual environment:
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

Open `deploy_lambda.py` and complete all the TODOs:

1. In the `create_deployment_package()` function:
   - Verify that the source file exists
   - Create a zip file containing the Lambda function code
   - Return the path to the created zip file

2. In the `create_lambda_role()` function:
   - Create an IAM client
   - Define a trust policy document for Lambda
   - Create the role with appropriate permissions
   - Attach the basic Lambda execution policy
   - Handle the case where the role already exists

3. In the `deploy_lambda_function()` function:
   - Check if the zip file exists
   - Create a Lambda role if one isn't provided
   - Create a Lambda client
   - Read the zip file content
   - Implement logic to update an existing function or create a new one
   - Return the function ARN

4. In the `invoke_lambda_function()` function:
   - Create a Lambda client
   - Set up a default payload if none is provided
   - Invoke the Lambda function
   - Process and return the response

5. In the `delete_lambda_function()` function:
   - Create a Lambda client
   - Delete the Lambda function
   - Handle the case where the function doesn't exist

6. In the `main()` function:
   - Set up the argument parser with appropriate options
   - Implement the workflow based on the provided arguments
   - Handle the function deployment, invocation, and deletion

### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ Create a deployment package containing the Lambda code  
✅ Create an IAM role with appropriate permissions  
✅ Deploy the Lambda function with the correct configuration  
✅ Update the function if it already exists  
✅ Invoke the function and process its response  
✅ Delete the function when requested  
✅ Script runs without error:
```bash
python deploy_lambda.py --function-name MyDevOpsLambda
```

---

## 🧹 Cleanup

You can delete the Lambda function and associated resources by running:
```bash
python deploy_lambda.py --function-name MyDevOpsLambda --delete
```

Make sure to implement the `delete_lambda_function()` to properly handle the function deletion.

---

## 💬 What's Next?
Move on to [AWS LAB06 - CloudFormation Stack Launch](../LAB06-CloudFormation-Stack-Launch/) to automate infrastructure as code deployments.

---

## 🙏 Acknowledgments
Lambda lets you run code instantly in the cloud. Automating Lambda deployment is a great step toward fully serverless systems.

Happy deploying! ⚡🐍