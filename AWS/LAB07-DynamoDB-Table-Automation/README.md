# AWS LAB07 - DynamoDB Table Automation with Python (boto3)

This lab guides you through creating a Python script to automate DynamoDB table operations using the AWS SDK for Python (Boto3). You'll implement various DynamoDB operations including table creation, item insertion, retrieval, and table deletion.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how to use boto3 to interact with DynamoDB
- Create and manage DynamoDB tables programmatically
- Implement basic CRUD operations for DynamoDB items
- Handle AWS SDK exceptions properly
- Learn about DynamoDB's data model and indexing
- Gain practical experience with NoSQL database operations in the cloud

---

## 🧰 Prerequisites

- AWS account with appropriate permissions for DynamoDB
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials
- Basic understanding of NoSQL database concepts

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB07-DynamoDB-Table-Automation/
├── dynamodb_script.py     # Main script with TODOs to implement
├── requirements.txt       # Required dependencies
├── README.md              # Lab instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB07-DynamoDB-Table-Automation/
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

Open the `dynamodb_script.py` file and complete all the TODOs to implement a comprehensive DynamoDB automation script:

1. In the `create_table()` function:
   - Create a boto3 DynamoDB client
   - Set up a table with 'username' as the partition key (string type)
   - Configure provisioned throughput (5 read/write capacity units)
   - Add appropriate tagging
   - Implement error handling for existing tables

2. In the `wait_for_table_creation()` function:
   - Create a polling mechanism to check table status
   - Handle the transition to ACTIVE state
   - Implement timeout logic

3. In the `list_tables()` function:
   - List all DynamoDB tables in your account
   - Format and display the results

4. In the `insert_item()` function:
   - Convert Python types to DynamoDB format
   - Insert an item into the table
   - Implement proper error handling

5. In the `get_item()` function:
   - Format the key for DynamoDB
   - Retrieve an item using the key
   - Convert the response back to Python types
   - Handle the case when an item is not found

6. In the `delete_table()` function:
   - Implement table deletion functionality
   - Handle errors appropriately

The main function is already implemented to call your functions in sequence.

---

## 🧪 Validation Checklist

✅ Successfully create a DynamoDB table with the correct configuration  
✅ Wait for the table to become active before proceeding  
✅ List all tables in your account and confirm your new table exists  
✅ Insert a sample item with the correct attribute types  
✅ Retrieve the item and verify all attributes match what was inserted  
✅ Delete the table when running with --cleanup flag  
✅ Handle all error conditions gracefully  
✅ Script runs without errors:
```bash
python dynamodb_script.py
```

✅ Try running with custom parameters:
```bash
python dynamodb_script.py --table-name MyCustomTable --region us-east-1
```

---

## 🧹 Cleanup

To avoid ongoing AWS charges, make sure to delete the DynamoDB table after testing:
```bash
python dynamodb_script.py --cleanup
```

**Important**: DynamoDB tables will continue to incur charges until explicitly deleted.

---

## 📚 DynamoDB Key Concepts

- **Partition Key**: Unique identifier for items in the table (hash key)
- **Sort Key**: Optional second part of a composite key for more complex data models
- **Provisioned Throughput**: Read and write capacity units that determine performance and cost
- **Table Status**: Tables transition through states like CREATING, UPDATING, ACTIVE
- **Item Operations**: How to put, get, update, and delete items
- **Error Handling**: Common DynamoDB exceptions and how to handle them

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Add `update_item()` functionality to modify existing items
2. Implement batch operations to insert or retrieve multiple items at once
3. Add a secondary (sort) key to the table for more complex data modeling
4. Implement a scan operation to retrieve items without knowing the key
5. Add support for conditional operations when inserting or updating items

---

## 💬 What's Next?

Next: [AWS LAB08 - SNS Topic and Subscription](../LAB08-SNS-Topic-and-Subscription/) to learn how to automate messaging services in the cloud.

---

## 🙏 Acknowledgments

DynamoDB automation is fundamental for building scalable, serverless applications in AWS. These skills will help you manage NoSQL databases as part of your infrastructure as code strategy.

Happy NoSQL automating! 📊🐍