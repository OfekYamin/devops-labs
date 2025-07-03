# LAB04 - Cloud Functions Deployment - Solutions

This document provides solutions to the TODOs in the `deploy_function.py` script.

## Solution: Create a zip file containing main.py and requirements-function.txt

```python
# Create a zip file containing main.py and requirements-function.txt
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    # Add main.py to the zip file
    main_py_path = os.path.join(source_path, 'main.py')
    if os.path.exists(main_py_path):
        zip_file.write(main_py_path, arcname='main.py')
    else:
        raise FileNotFoundError(f"main.py not found in {source_path}")
    
    # Add requirements-function.txt to the zip file if it exists
    req_path = os.path.join(source_path, 'requirements-function.txt')
    if os.path.exists(req_path):
        zip_file.write(req_path, arcname='requirements.txt')
```

## Solution: Initialize the Google Cloud Storage client

```python
# Initialize the Google Cloud Storage client
storage_client = storage.Client()
```

## Solution: Check if the bucket exists, and create it if it doesn't

```python
# Check if the bucket exists, and create it if it doesn't
try:
    bucket = storage_client.get_bucket(bucket_name)
    print(f"Using existing bucket: {bucket_name}")
except Exception:
    print(f"Creating new bucket: {bucket_name}")
    bucket = storage_client.create_bucket(bucket_name, location="us")
```

## Solution: Upload the zip file to the GCS bucket

```python
# Upload the zip file to the GCS bucket
blob_name = f"source/{function_name}-{int(time.time())}.zip"
blob = bucket.blob(blob_name)
blob.upload_from_filename(zip_path)
```

## Solution: Return the GCS URL of the uploaded source code

```python
# Return the GCS URL of the uploaded source code
source_url = f"gs://{bucket_name}/{blob_name}"
print(f"Source code uploaded to: {source_url}")
return source_url
```

## Solution: Initialize the Cloud Functions API client

```python
# Initialize the Cloud Functions API client
credentials, _ = google.auth.default()
service = discovery.build('cloudfunctions', 'v1', credentials=credentials)
```

## Solution: Create the function configuration

```python
# Create the function configuration
function_config = {
    "name": function_path,
    "entryPoint": entry_point,
    "runtime": runtime,
    "httpsTrigger": {},
    "sourceArchiveUrl": source_gcs_url
}
```

## Solution: Check if the function already exists

```python
# Check if the function already exists
try:
    existing_function = service.projects().locations().functions().get(
        name=function_path
    ).execute()
    print(f"Function '{function_name}' already exists. Updating...")
    update = True
except Exception:
    print(f"Function '{function_name}' does not exist. Creating...")
    update = False
```

## Solution: Create or update the function

```python
# Create or update the function
if update:
    operation = service.projects().locations().functions().patch(
        name=function_path,
        body=function_config
    ).execute()
else:
    location_path = f"projects/{project_id}/locations/{region}"
    operation = service.projects().locations().functions().create(
        location=location_path,
        body=function_config
    ).execute()
```

## Solution: Wait for the operation to complete

```python
# Wait for the operation to complete
operation_name = operation['name']
print(f"Waiting for operation {operation_name} to complete...")

while True:
    operation_status = service.projects().locations().operations().get(
        name=operation_name
    ).execute()
    
    if 'done' in operation_status and operation_status['done']:
        if 'error' in operation_status:
            print(f"Error deploying function: {operation_status['error']}")
            raise Exception(operation_status['error'])
        break
    
    print(".", end="", flush=True)
    time.sleep(2)

print("\nFunction deployment completed.")
```

## Solution: If allow_unauthenticated is True, configure IAM policy for public access

```python
# If allow_unauthenticated is True, configure IAM policy for public access
if allow_unauthenticated:
    print("Configuring public access...")
    policy_client = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
    
    # Get the function details
    function = service.projects().locations().functions().get(
        name=function_path
    ).execute()
    
    # Set the IAM policy to allow unauthenticated invocations
    set_iam_policy = service.projects().locations().functions().setIamPolicy(
        resource=function_path,
        body={
            "policy": {
                "bindings": [
                    {
                        "role": "roles/cloudfunctions.invoker",
                        "members": [
                            "allUsers"
                        ]
                    }
                ]
            }
        }
    ).execute()
```

## Solution: Return the deployed function details

```python
# Return the deployed function details
function = service.projects().locations().functions().get(
    name=function_path
).execute()
return function
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Run the script to deploy your function using the GCP API:
```bash
python deploy_function.py --project=your-gcp-project-id
```

3. Or deploy with gcloud CLI instead:
```bash
python deploy_function.py --project=your-gcp-project-id --use_gcloud
```

4. Deploy with custom settings:
```bash
python deploy_function.py \
  --project=your-gcp-project-id \
  --region=us-west1 \
  --function_name=my-custom-function \
  --entry_point=hello_world \
  --runtime=python311 \
  --allow_unauthenticated
```

## Testing the Function

Once deployed, you can test your function with:

```bash
curl https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME
```

Or with a name parameter:

```bash
curl "https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME?name=YourName"
```

## Cleanup

Don't forget to clean up the created function to avoid incurring charges:

```bash
gcloud functions delete FUNCTION_NAME --project=PROJECT_ID --region=REGION
``` 