# AWS LAB09 - SQS Queue Automation with Python (boto3)

This lab guides you through creating a Python script to automate Amazon Simple Queue Service (SQS) operations using the AWS SDK for Python (Boto3). You'll implement various SQS operations including queue creation, message sending, receiving, and queue deletion.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and manage SQS queues programmatically using boto3
- Send messages to SQS queues with custom attributes
- Receive and process messages from queues
- Understand queue types (standard vs. FIFO) and their use cases
- Implement message visibility timeout handling
- Delete messages and queues properly to avoid resource leaks
- Learn how to implement asynchronous communication patterns

---

## 🧰 Prerequisites

- AWS account with appropriate permissions for SQS
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials
- Basic understanding of messaging queues and asynchronous processing

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB09-SQS-Queue-Automation/
├── sqs_script.py         # Main script with TODOs to implement
├── requirements.txt      # Required dependencies
├── README.md             # Lab instructions
└── solutions.md          # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB09-SQS-Queue-Automation/
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

Open the `sqs_script.py` file and complete all the TODOs to implement a comprehensive SQS automation script:

1. In the `create_queue()` function:
   - Create a boto3 client for SQS in the specified region
   - Use the create_queue method to create a new queue
   - Handle queue attributes for configuration options
   - Return the queue URL for further operations

2. In the `list_queues()` function:
   - Create a boto3 client for SQS in the specified region
   - Use the list_queues method to get all queues
   - Handle optional prefix filtering
   - Print and return the queue URLs

3. In the `send_message()` function:
   - Create a boto3 client for SQS in the specified region
   - Use the send_message method to send a message to the queue
   - Add optional message attributes and delay seconds
   - Return the message ID for tracking

4. In the `receive_messages()` function:
   - Create a boto3 client for SQS in the specified region
   - Use the receive_message method with appropriate parameters
   - Configure long polling and visibility timeout
   - Process and return the received messages

5. In the `delete_message()` function:
   - Create a boto3 client for SQS in the specified region
   - Use the delete_message method to remove the processed message
   - Implement proper error handling
   - Return success status

6. In the `delete_queue()` function:
   - Create a boto3 client for SQS in the specified region
   - Use the delete_queue method to remove the queue
   - Implement proper error handling
   - Return success status

The main function is already implemented to call your functions based on command-line arguments.

---

## 🧪 Validation Checklist

✅ Successfully create an SQS queue with appropriate configuration  
✅ List all queues in your account and verify your new queue exists  
✅ Send messages to your queue with and without attributes  
✅ Receive messages from the queue and process them correctly  
✅ Delete messages after successful processing  
✅ Delete the queue when finished with testing  
✅ Handle all error conditions gracefully  

✅ Script runs without errors with these commands:
```bash
# Create a queue
python sqs_script.py --create-queue DevOpsQueue

# List queues
python sqs_script.py --list-queues

# Send a message
python sqs_script.py --queue-url <your-queue-url> --send-message "Test message"

# Send a message with attributes
python sqs_script.py --queue-url <your-queue-url> --send-message "Priority message" --attributes '{"Priority":{"DataType":"String","StringValue":"High"}}'

# Receive messages
python sqs_script.py --queue-url <your-queue-url> --receive

# Delete the queue
python sqs_script.py --delete-queue --queue-url <your-queue-url>
```

---

## 🧹 Cleanup

To avoid ongoing AWS charges, make sure to delete the SQS queue after testing:
```bash
python sqs_script.py --delete-queue --queue-url <your-queue-url>
```

**Important**: While SQS costs are minimal for low usage, it's good practice to clean up resources after testing.

---

## 📚 SQS Key Concepts

- **Queue Types**: Standard queues offer maximum throughput with at-least-once delivery, while FIFO queues guarantee exactly-once processing and message ordering
- **Message Visibility**: After a message is received, it becomes invisible to other consumers for a configurable period (the visibility timeout)
- **Dead Letter Queues**: Special queues where messages that can't be processed successfully are sent after a defined number of attempts
- **Long Polling**: A method to reduce empty responses and costs by waiting for messages to arrive (up to 20 seconds)
- **Message Attributes**: Metadata stored with messages for additional context (up to 10 attributes per message)
- **Delay Queues**: Ability to postpone delivery of new messages to a queue for a specified number of seconds
- **Message Retention**: SQS can retain messages for up to 14 days before automatic deletion

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Create a FIFO queue with message deduplication enabled
2. Implement a dead letter queue for handling failed message processing
3. Add long polling support to your message receiving function
4. Create a producer-consumer pattern with multiple scripts
5. Implement batch operations for sending and deleting messages
6. Add message filtering based on message attributes

---

## 💬 What's Next?

Next: [AWS LAB10 - EventBridge Rule Trigger](../LAB10-EventBridge-Rule-Trigger/) to learn how to automate event-driven workflows in the cloud.

---

## 🙏 Acknowledgments

Amazon SQS is a fundamental building block for creating loosely coupled, distributed systems in AWS. These skills will help you implement asynchronous processing and decouple components in your cloud architecture.

Happy queueing! 📩🐍