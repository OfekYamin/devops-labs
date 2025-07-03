# LAB03 - IAM Service Account Creation - Solutions

This document provides solutions to the TODOs in the `create_service_account.py` script.

## Solution: Initialize the IAM service API client in `create_service_account` function

```python
# Initialize the IAM service API client
credentials, _ = google.auth.default()
service = discovery.build('iam', 'v1', credentials=credentials)
```

## Solution: Create the service account request body

```python
# Create the service account request body
service_account_details = {
    "accountId": account_id,
    "serviceAccount": {
        "displayName": display_name,
        "description": description
    }
}
```

## Solution: Submit the create service account request

```python
# Submit the create service account request
request = service.projects().serviceAccounts().create(
    name=f"projects/{project_id}",
    body=service_account_details
)
response = request.execute()
print(f"Created service account: {response['email']}")
```

## Solution: Return the service account resource

```python
# Return the service account resource
return response
```

## Solution: Initialize the Resource Manager API client

```python
# Initialize the Resource Manager API client
credentials, _ = google.auth.default()
resource_manager = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
```

## Solution: Get the current IAM policy for the project

```python
# Get the current IAM policy for the project
policy_request = resource_manager.projects().getIamPolicy(
    resource=project_id,
    body={}
)
policy = policy_request.execute()
```

## Solution: Create the binding for the service account and role

```python
# Create the binding for the service account and role
member = f"serviceAccount:{service_account_email}"
new_binding = {
    "role": role,
    "members": [member]
}

# Check if the role already exists in policy
role_exists = False
for binding in policy.get('bindings', []):
    if binding['role'] == role:
        if member not in binding['members']:
            binding['members'].append(member)
        role_exists = True
        break
```

## Solution: Add the new binding to the policy

```python
# Add the new binding to the policy
if not role_exists:
    if 'bindings' not in policy:
        policy['bindings'] = []
    policy['bindings'].append(new_binding)
```

## Solution: Set the updated IAM policy

```python
# Set the updated IAM policy
set_policy_request = resource_manager.projects().setIamPolicy(
    resource=project_id,
    body={"policy": policy}
)
return set_policy_request.execute()
```

## Solution: Initialize the IAM service API client in `list_service_accounts` function

```python
# Initialize the IAM service API client
credentials, _ = google.auth.default()
service = discovery.build('iam', 'v1', credentials=credentials)
```

## Solution: List all service accounts in the project

```python
# List all service accounts in the project
request = service.projects().serviceAccounts().list(
    name=f"projects/{project_id}"
)
response = request.execute()

if 'accounts' in response:
    for account in response['accounts']:
        print(f"Email: {account['email']}")
        print(f"Name: {account['displayName']}")
        print(f"Created: {account.get('createTime', 'N/A')}")
        print(f"Project: {project_id}")
        print("-" * 40)
else:
    print("No service accounts found.")
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Run the script to create a service account:
```bash
python create_service_account.py --project=your-gcp-project-id
```

3. Create a service account with custom details and roles:
```bash
python create_service_account.py \
  --project=your-gcp-project-id \
  --account_id=my-custom-sa \
  --display_name="My Custom Service Account" \
  --description="For testing automation" \
  --roles=roles/storage.admin,roles/logging.viewer
```

4. List all service accounts in your project:
```bash
python create_service_account.py --project=your-gcp-project-id --list
```

## Cleanup

Don't forget to clean up the created service account to avoid cluttering your project:

```bash
gcloud iam service-accounts delete SERVICE_ACCOUNT_EMAIL --project=PROJECT_ID
```

Replace `SERVICE_ACCOUNT_EMAIL` with the email of the created service account, which will be in the format `account-id@project-id.iam.gserviceaccount.com`. 