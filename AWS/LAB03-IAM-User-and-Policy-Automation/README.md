# AWS LAB03 - Automate IAM User and Policy Creation with Python (boto3)

In this lab, you'll learn how to automate the creation of IAM users and attach policies using Python and the `boto3` library. IAM automation is critical for managing access to AWS in a secure and scalable way.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create an IAM user programmatically using `boto3`
- Generate and manage access keys for IAM users
- Create custom IAM policies with specific permissions
- Attach policies to users programmatically
- List and manage user policies
- Clean up IAM resources (users, policies, access keys)

---

## 🧰 Prerequisites

- AWS account with IAM permissions
- AWS credentials configured locally (`aws configure`)
- Python 3.8+ and `boto3` installed
- Basic understanding of IAM concepts (users, policies, permissions)

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB03-IAM-User-and-Policy-Automation/
├── create_iam_user.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB03-IAM-User-and-Policy-Automation/
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

Open `create_iam_user.py` and complete all the TODOs:

1. In the `create_iam_user()` function:
   - Initialize the IAM client
   - Create an IAM user with appropriate tags
   - Handle the case where the user already exists

2. In the `get_user()` function:
   - Initialize the IAM client
   - Get and return user information

3. In the `generate_access_key()` function:
   - Initialize the IAM client
   - Create access keys for the specified user
   - Print access key information with appropriate warnings

4. In the `list_access_keys()` function:
   - List all access keys for a user
   - Print information about each key

5. In the `delete_access_key()` function:
   - Implement deleting an access key for a user

6. In the `create_policy()` function:
   - Create a custom IAM policy
   - Convert the policy document to JSON
   - Handle the case where the policy already exists

7. In the `attach_policy_to_user()` function:
   - Attach a policy to a user using its ARN

8. In the `list_user_policies()` function:
   - List all policies attached to a user

9. In the `detach_user_policies()` function:
   - Detach all policies from a user

10. In the `delete_user()` function:
    - Clean up user resources (access keys, policies)
    - Delete the user

11. In the `main()` function:
    - Set up the argument parser
    - Implement the complete workflow based on provided arguments

### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ Create an IAM user with proper tags  
✅ Generate and view access keys  
✅ Create a custom policy with specific permissions  
✅ Attach the policy to the user  
✅ List user policies successfully  
✅ Clean up all resources when requested  
✅ Script runs without error:
```bash
python create_iam_user.py --username test-user --policy ReadOnlyAccess
```

---

## 🧹 Cleanup

Implement the `delete_user()` function to properly clean up all resources:
1. Delete all access keys associated with the user
2. Detach all policies from the user
3. Delete the user's login profile if it exists
4. Delete the user

Alternatively, you can run the script with the cleanup flag:
```bash
python create_iam_user.py --username test-user --cleanup
```

---

## 💬 What's Next?
Try [AWS LAB04 - CloudWatch Metrics and Alerts](../LAB04-CloudWatch-Metrics-and-Alerts/) to collect metrics and send alerts using Python.

---

## 🙏 Acknowledgments
Security automation is essential in DevOps. Mastering IAM management with Python opens doors to building secure cloud platforms.

Happy securing! 🛡🐍