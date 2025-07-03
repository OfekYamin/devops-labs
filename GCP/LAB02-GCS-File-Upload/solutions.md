# LAB02 - Google Cloud Storage File Upload - Solutions

This document provides solutions to the TODOs in the `upload_file.py` script.

## Solution: Initialize the GCS client in `upload_to_gcs` function

```python
# Initialize the GCS client
client = storage.Client()
```

## Solution: Get the bucket object

```python
# Get the bucket object
bucket = client.bucket(bucket_name)
```

## Solution: Get a blob object

```python
# Get a blob object
blob = bucket.blob(destination_blob_name)
```

## Solution: Upload the file 

```python
# Upload the file
blob.upload_from_filename(source_file_path)
```

## Solution: Print upload confirmation message

```python
# Print upload confirmation message
print(f"File {source_file_path} uploaded to gs://{bucket_name}/{destination_blob_name}")
```

## Solution: Return the blob object

```python
# Return the blob object
return blob
```

## Solution: Initialize the GCS client in `list_blobs` function

```python
# Initialize the GCS client
client = storage.Client()
```

## Solution: List all blobs in the bucket

```python
# List all blobs in the bucket and print their names
for blob in client.list_blobs(bucket_name):
    print(f"- {blob.name} ({blob.size} bytes, updated: {blob.updated})")
```

## Extra Credit: Add code to demonstrate blob metadata and generation

Add this to the main function after listing blobs:

```python
# Add code to demonstrate blob metadata and generation
if blob:
    print("\nBlob Details:")
    print(f"Name: {blob.name}")
    print(f"Size: {blob.size} bytes")
    print(f"Content Type: {blob.content_type}")
    print(f"Updated: {blob.updated}")
    print(f"Generation: {blob.generation}")
    print(f"Metageneration: {blob.metageneration}")
    
    # Setting and getting metadata
    metadata = {"uploaded-by": "gcp-lab-student", "purpose": "training"}
    blob.metadata = metadata
    blob.patch()
    
    # Fetch updated blob to show changes
    updated_blob = bucket.get_blob(blob.name)
    print("\nCustom Metadata:")
    for key, value in updated_blob.metadata.items():
        print(f"- {key}: {value}")
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Run the script with your bucket name:
```bash
python upload_file.py --bucket=your-gcs-bucket-name --list
```

3. To specify a custom destination path:
```bash
python upload_file.py --bucket=your-gcs-bucket-name --destination=folder/custom-filename.txt
```

## Cleanup

Don't forget to clean up the uploaded objects to avoid unnecessary storage charges:

```bash
gsutil rm gs://your-gcs-bucket-name/sample.txt
```

Or, using the Python API:

```python
blob.delete()
``` 