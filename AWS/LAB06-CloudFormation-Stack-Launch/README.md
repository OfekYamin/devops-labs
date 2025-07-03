# AWS LAB06 - Automate CloudFormation Stack Launch with Python (boto3)

CloudFormation lets you define your infrastructure as code. In this lab, you'll use Python to programmatically deploy a CloudFormation template using `boto3`.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use Python to launch and manage CloudFormation stacks
- Read and parse CloudFormation templates
- Configure stack parameters through configuration files
- Monitor stack creation progress and handle events
- Retrieve and display stack outputs
- Delete stacks when they're no longer needed
- Handle errors and edge cases in CloudFormation operations

---

## 🧰 Prerequisites

- AWS account with CloudFormation and EC2 permissions
- Python 3.8+ and `boto3` installed
- Basic understanding of CloudFormation templates and stack deployments
- Familiarity with configuration file parsing

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB06-CloudFormation-Stack-Launch/
├── launch_stack.py        # Simplified script with TODOs to complete
├── deploy_stack.py        # Advanced script with TODOs to complete
├── ec2_template.yaml      # CloudFormation template for EC2 instance
├── config.ini             # Configuration file for stack parameters
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB06-CloudFormation-Stack-Launch/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Update the configuration:
```ini
# In config.ini
[Parameters]
SubnetID = subnet-xxxxxxxx  # Replace with your actual subnet ID
VpcID = vpc-xxxxxxxx        # Replace with your actual VPC ID
KeyName = your-key-name     # Replace with your EC2 key pair name
```

---

## ✍️ Your Task

You have two options for this lab:

### Option 1: Complete `launch_stack.py` (Beginner)

Open `launch_stack.py` and complete all the TODOs to create a basic CloudFormation deployment script:

1. Import the necessary libraries
2. Implement the function to read the CloudFormation template
3. Create the function to create a CloudFormation stack
4. Implement stack status checking functionality
5. Add a function to wait for stack completion
6. Create a function to delete a CloudFormation stack
7. Implement error handling for AWS operations
8. Complete the main function to orchestrate the deployment

### Option 2: Complete `deploy_stack.py` (Advanced)

Open `deploy_stack.py` and complete all the TODOs to create a comprehensive CloudFormation deployment script:

1. In the `load_config()` function:
   - Check if the config file exists
   - Create a ConfigParser object and read the file

2. In the `load_template()` function:
   - Open and read the template file

3. In the `get_stack_parameters()` and `get_stack_tags()` functions:
   - Extract parameters and tags from the config file

4. In the `create_update_stack()` function:
   - Check if the stack exists
   - Create the stack parameter dictionary
   - Implement the create or update logic

5. In the `wait_for_stack()` function:
   - Implement a polling mechanism for stack status
   - Handle various stack states and timeouts

6. In the `print_stack_events()` and `print_stack_outputs()` functions:
   - Retrieve and display stack events and outputs

7. In the `validate_config_parameters()` function:
   - Check for placeholder values that should be replaced

8. In the `delete_stack()` function:
   - Implement stack deletion functionality

9. In the `main()` function:
   - Parse command line arguments
   - Load and validate configuration
   - Create the CloudFormation client
   - Orchestrate the stack operations

### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ Update configuration with valid AWS resource IDs  
✅ Successfully read and parse the CloudFormation template  
✅ Create a CloudFormation stack with the provided parameters  
✅ Monitor stack creation progress until completion  
✅ Display stack events and handle errors appropriately  
✅ Show stack outputs after successful creation  
✅ Delete the stack when requested  
✅ Script runs without error:
```bash
python deploy_stack.py
# or for deletion
python deploy_stack.py --delete
```

---

## 🧹 Cleanup

To avoid ongoing AWS charges, make sure to delete the stack after testing:
```bash
python deploy_stack.py --delete
```

**Important**: AWS resources like EC2 instances will continue to incur charges until explicitly deleted.

---

## 💬 What's Next?
Next: [AWS LAB07 - DynamoDB Table Automation](../LAB07-DynamoDB-Table-Automation/) to learn how to automate NoSQL databases in the cloud.

---

## 🙏 Acknowledgments
Using CloudFormation with Python empowers you to scale infrastructure as code with precision and control.

Happy stacking! 🏗🐍