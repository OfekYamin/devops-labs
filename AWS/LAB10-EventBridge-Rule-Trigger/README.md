# AWS LAB10 - EventBridge Rule Trigger Automation with Python (boto3)

This lab guides you through creating a Python script to automate Amazon EventBridge operations using the AWS SDK for Python (Boto3). You'll implement various EventBridge operations including rule creation, target configuration, and event pattern definition.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and manage EventBridge rules programmatically using boto3
- Configure schedule expressions (cron and rate) for time-based events
- Define event patterns for responding to AWS service events
- Add Lambda functions and SNS topics as rule targets
- Enable and disable rules based on operational needs
- Understand the event-driven architecture pattern in AWS
- Implement proper error handling and resource cleanup

---

## 🧰 Prerequisites

- AWS account with appropriate permissions for EventBridge, Lambda, and SNS
- A deployed Lambda function (from LAB05 or create one manually)
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials
- Basic understanding of event-driven architecture

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB10-EventBridge-Rule-Trigger/
├── eventbridge_script.py  # Main script with TODOs to implement
├── requirements.txt       # Required dependencies
├── README.md              # Lab instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB10-EventBridge-Rule-Trigger/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Verify your AWS credentials are configured:
```bash
aws configure list
```

---

## ✍️ Your Task

Open the `eventbridge_script.py` file and complete all the TODOs to implement a comprehensive EventBridge automation script:

1. In the `create_rule()` function:
   - Create a boto3 client for EventBridge in the specified region
   - Use the put_rule method to create a new rule
   - Handle either schedule expression or event pattern configuration
   - Return the rule ARN for further operations

2. In the `add_lambda_target()` function:
   - Create boto3 clients for EventBridge and Lambda
   - Get the Lambda function ARN using the function name
   - Use put_targets to set the Lambda function as a target
   - Add necessary permissions for EventBridge to invoke Lambda
   - Return the target ID

3. In the `add_sns_target()` function:
   - Create a boto3 client for EventBridge
   - Use put_targets to set the SNS topic as a target
   - Configure custom input transformation if needed
   - Return the target ID

4. In the `list_rules()` function:
   - Create a boto3 client for EventBridge
   - Use list_rules method to get rules, with optional prefix filter
   - Print rule details and handle pagination
   - Return the list of rules

5. In the `list_targets()` function:
   - Create a boto3 client for EventBridge
   - Use list_targets_by_rule method to get targets
   - Format and display target information
   - Return the list of targets

6. In the `enable_disable_rule()` function:
   - Create a boto3 client for EventBridge
   - Use enable_rule or disable_rule method based on parameters
   - Implement proper error handling

7. In the `delete_rule()` function:
   - Create a boto3 client for EventBridge
   - Remove all targets from the rule first
   - Delete the rule using delete_rule method
   - Implement proper error handling

The main function is already implemented to call your functions based on command-line arguments.

---

## 🧪 Validation Checklist

✅ Successfully create an EventBridge rule with a schedule expression  
✅ Configure a Lambda function as a target for the rule  
✅ Verify the rule appears in the AWS EventBridge console  
✅ Check CloudWatch Logs to confirm the Lambda function is triggered on schedule  
✅ List all rules and targets in your account  
✅ Enable and disable rules as needed  
✅ Delete the rule and targets when testing is complete  
✅ Handle all error conditions gracefully  

✅ Script runs without errors with these commands:
```bash
# Create a rule with a schedule (runs every 5 minutes)
python eventbridge_script.py --create-rule DevOpsScheduleRule --schedule "rate(5 minutes)"

# Create a rule with an event pattern (triggers on EC2 instance state changes)
python eventbridge_script.py --create-rule DevOpsEC2Rule --event-pattern '{"source": ["aws.ec2"], "detail-type": ["EC2 Instance State-change Notification"]}'

# Add a Lambda target to the rule
python eventbridge_script.py --rule-name DevOpsScheduleRule --add-lambda-target your-lambda-function-name

# List all rules
python eventbridge_script.py --list-rules

# List targets for a specific rule
python eventbridge_script.py --rule-name DevOpsScheduleRule --list-targets

# Disable a rule
python eventbridge_script.py --rule-name DevOpsScheduleRule --disable

# Delete a rule
python eventbridge_script.py --rule-name DevOpsScheduleRule --delete
```

---

## 🧹 Cleanup

To avoid ongoing AWS charges, make sure to delete the EventBridge rule and targets after testing:
```bash
python eventbridge_script.py --rule-name DevOpsScheduleRule --delete
```

**Important**: While EventBridge costs are minimal, it's good practice to clean up all resources after testing, especially if you've configured Lambda targets that might be invoked on a schedule.

---

## 📚 EventBridge Key Concepts

- **Rules**: Define when automated actions are triggered, based on events or schedules
- **Events**: JSON messages that indicate a change in environment or resource state
- **Targets**: Resources that process events (Lambda, SNS, SQS, etc.)
- **Event Buses**: Channels that receive events and route them to targets
- **Schedule Expressions**: 
  - **Rate expressions**: `rate(5 minutes)`, `rate(1 hour)`, `rate(1 day)`
  - **Cron expressions**: `cron(0 12 * * ? *)` (noon every day)
- **Event Patterns**: JSON patterns that filter which events trigger the rule
- **Input Transformers**: Modify the event data before it's sent to the target

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Create a rule that responds to AWS service events (e.g., S3 object creation)
2. Configure multiple targets for a single rule
3. Use input transformers to customize the event data sent to targets
4. Set up cross-account event routing
5. Create a dead-letter queue for failed event deliveries
6. Implement a CloudWatch dashboard to monitor rule invocations

---

## 💬 Congratulations!

You've completed all 10 AWS labs in this series! You now have practical experience with a wide range of AWS services and automation techniques using Python. These skills form the foundation of modern DevOps practices in the AWS cloud.

---

## 🙏 Acknowledgments

Amazon EventBridge is a critical service for building event-driven architectures in AWS. These skills will help you implement serverless workflows, automated responses to infrastructure changes, and loosely coupled systems in your cloud architecture.

Happy automating! 🕒🐍

