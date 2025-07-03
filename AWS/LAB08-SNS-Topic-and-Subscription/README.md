# AWS LAB08 - SNS Topic and Subscription Automation with Python (boto3)

This lab guides you through creating a Python script to automate Amazon Simple Notification Service (SNS) operations using the AWS SDK for Python (Boto3). You'll implement various SNS operations including topic creation, subscription management, and message publishing.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create SNS topics programmatically using boto3
- Subscribe email endpoints to receive notifications
- Publish messages to SNS topics
- List and manage topic subscriptions
- Delete SNS topics and clean up resources
- Understand SNS pub/sub architecture and messaging patterns
- Implement error handling for SNS operations

---

## 🧰 Prerequisites

- AWS account with appropriate permissions for SNS
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials
- Basic understanding of messaging systems and pub/sub architecture

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB08-SNS-Topic-and-Subscription/
├── sns_script.py         # Main script with TODOs to implement
├── requirements.txt      # Required dependencies
├── README.md             # Lab instructions
└── solutions.md          # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB08-SNS-Topic-and-Subscription/
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

Open the `sns_script.py` file and complete all the TODOs to implement a comprehensive SNS automation script:

1. In the `create_topic()` function:
   - Create a boto3 client for SNS in the specified region
   - Use the create_topic method to create a new topic
   - Return the ARN of the created topic

2. In the `list_topics()` function:
   - Create a boto3 client for SNS in the specified region
   - Use the list_topics method to get all topics
   - Print each topic's ARN and handle pagination
   - Return the list of topic ARNs

3. In the `subscribe_email()` function:
   - Create a boto3 client for SNS in the specified region
   - Use the subscribe method to subscribe the email endpoint
   - Implement appropriate error handling
   - Return the subscription ARN

4. In the `publish_message()` function:
   - Create a boto3 client for SNS in the specified region
   - Use the publish method to send a message with subject
   - Return the message ID for tracking

5. In the `list_subscriptions()` function:
   - Create a boto3 client for SNS in the specified region
   - Use list_subscriptions_by_topic or list_subscriptions based on input
   - Handle pagination for large subscription lists
   - Return subscription details

6. In the `delete_subscription()` function:
   - Create a boto3 client for SNS in the specified region
   - Use the unsubscribe method to delete the subscription
   - Implement proper error handling

7. In the `delete_topic()` function:
   - Create a boto3 client for SNS in the specified region
   - Use the delete_topic method to delete the topic
   - Implement proper error handling

The main function is already implemented to call your functions based on command-line arguments.

---

## 🧪 Validation Checklist

✅ Successfully create an SNS topic with appropriate naming  
✅ List all topics in your account and verify your new topic exists  
✅ Subscribe an email address to your topic (check inbox for confirmation)  
✅ Publish a message to the topic and verify it's received  
✅ List all subscriptions for your topic  
✅ Delete the subscription when no longer needed  
✅ Delete the topic when finished with testing  
✅ Handle all error conditions gracefully  

✅ Script runs without errors with these commands:
```bash
# Create a topic
python sns_script.py --create-topic DevOpsNotifications

# Subscribe an email (confirm subscription in your inbox)
python sns_script.py --topic-arn <your-topic-arn> --subscribe your.email@example.com

# Publish a message
python sns_script.py --topic-arn <your-topic-arn> --publish "Test message" --subject "Test Subject"

# List subscriptions
python sns_script.py --list-subscriptions --topic-arn <your-topic-arn>

# Delete resources when finished
python sns_script.py --delete-topic --topic-arn <your-topic-arn>
```

---

## 🧹 Cleanup

To avoid ongoing AWS charges, make sure to delete the SNS topic after testing:
```bash
python sns_script.py --delete-topic --topic-arn <your-topic-arn>
```

**Important**: While SNS costs are minimal, it's good practice to clean up resources after testing.

---

## 📚 SNS Key Concepts

- **Topic**: The communication channel to which publishers send messages and subscribers receive notifications
- **Subscription**: The endpoint (email, SMS, Lambda, etc.) that receives messages published to a topic
- **Publish/Subscribe Model**: Pattern where publishers send messages to topics without knowledge of subscribers
- **Fan-out Pattern**: Sending a single message to multiple recipients simultaneously
- **Subscription Confirmation**: Email subscribers must confirm subscription before receiving messages
- **Delivery Policies**: Rules that define how SNS delivers messages to specific endpoints
- **Message Filtering**: Using filter policies to control which messages subscribers receive

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Add SMS subscription support (requires AWS account verification for production use)
2. Implement topic attributes management (DisplayName, DeliveryPolicy)
3. Add support for publishing structured messages in JSON format
4. Implement subscription filtering with filter policies
5. Create an HTTP/HTTPS endpoint subscription with a simple web server
6. Add support for AWS Lambda function subscriptions

---

## 💬 What's Next?

Next: [AWS LAB09 - SQS Queue Automation](../LAB09-SQS-Queue-Automation/) to learn how to automate queue-based messaging services in the cloud.

---

## 🙏 Acknowledgments

Amazon SNS is a critical service for building event-driven architectures in AWS. These skills will help you implement notification systems and pub/sub patterns in your cloud infrastructure.

Happy messaging! 📨🐍