# LAB10 - Cloud Run Deployment - Solutions

This document provides solutions to the TODOs in the `deploy_run.py` script.

## Solution: Authenticate with Google Cloud

```python
def authenticate(credentials_file=None):
    """
    Authenticate with Google Cloud using service account credentials.
    """
    try:
        if credentials_file:
            # Use the provided service account file
            credentials = service_account.Credentials.from_service_account_file(
                credentials_file,
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
            print(f"Authenticated using provided credentials file: {credentials_file}")
        else:
            # Use the GOOGLE_APPLICATION_CREDENTIALS environment variable
            credentials = service_account.Credentials.from_service_account_file(
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
            print(f"Authenticated using GOOGLE_APPLICATION_CREDENTIALS")
            
        return credentials
    except FileNotFoundError:
        raise Exception("Credentials file not found. Make sure the file exists or the GOOGLE_APPLICATION_CREDENTIALS environment variable is set correctly.")
    except KeyError:
        raise Exception("GOOGLE_APPLICATION_CREDENTIALS environment variable not set. Please set it or provide a credentials file path.")
```

## Solution: Build Cloud Run API client

```python
def build_cloud_run_client(credentials):
    """
    Build and return a Cloud Run API client.
    """
    try:
        service = discovery.build('run', 'v1', credentials=credentials)
        return service
    except Exception as e:
        raise Exception(f"Failed to build Cloud Run API client: {e}")
```

## Solution: Build and push Docker image

```python
def build_and_push_image(project_id, image_name, dockerfile_dir="."):
    """
    Build a Docker image and push it to Google Container Registry.
    """
    print(f"Building and pushing Docker image to Google Container Registry...")
    
    # Full image path for Google Container Registry
    image_path = f"gcr.io/{project_id}/{image_name}"
    
    try:
        # Build the Docker image
        build_cmd = ["docker", "build", "-t", image_path, dockerfile_dir]
        print(f"Running: {' '.join(build_cmd)}")
        subprocess.run(build_cmd, check=True)
        
        # Push the image to Google Container Registry
        push_cmd = ["docker", "push", image_path]
        print(f"Running: {' '.join(push_cmd)}")
        subprocess.run(push_cmd, check=True)
        
        print(f"Successfully built and pushed image: {image_path}")
        return image_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"Docker command failed: {e}")
    except Exception as e:
        raise Exception(f"Failed to build or push Docker image: {e}")
```

## Solution: Deploy to Cloud Run

```python
def deploy_to_cloud_run(service, project_id, service_name, image_path, region="us-central1"):
    """
    Deploy a container image to Cloud Run.
    """
    print(f"Deploying {image_path} to Cloud Run as '{service_name}'...")
    
    # Create the parent resource name
    parent = f"projects/{project_id}/locations/{region}"
    
    # Define the service configuration
    service_config = {
        "apiVersion": "serving.knative.dev/v1",
        "kind": "Service",
        "metadata": {
            "name": service_name,
            "namespace": project_id
        },
        "spec": {
            "template": {
                "spec": {
                    "containers": [{
                        "image": image_path,
                        "resources": {
                            "limits": {
                                "memory": "256Mi",
                                "cpu": "1"
                            }
                        },
                        "ports": [{
                            "containerPort": 8080
                        }]
                    }]
                }
            },
            "traffic": [{
                "percent": 100,
                "latestRevision": True
            }]
        }
    }
    
    try:
        # Create or update the Cloud Run service
        request = service.namespaces().services().create(
            parent=parent,
            body=service_config
        )
        response = request.execute()
        
        print(f"Cloud Run service deployment initiated.")
        return response
    except HttpError as e:
        # If the service already exists, update it
        if e.resp.status == 409:
            print(f"Service {service_name} already exists. Updating...")
            request = service.namespaces().services().replaceService(
                name=f"{parent}/services/{service_name}",
                body=service_config
            )
            response = request.execute()
            return response
        else:
            raise Exception(f"HTTP error {e.resp.status} during deployment: {e.content.decode('utf-8')}")
    except Exception as e:
        raise Exception(f"Failed to deploy to Cloud Run: {e}")
```

## Solution: Wait for deployment

```python
def wait_for_deployment(service, name):
    """
    Wait for a Cloud Run deployment to complete.
    """
    print(f"Waiting for deployment of {name} to complete...")
    
    max_retries = 60  # 10 minutes (10 seconds * 60)
    retry_interval = 10  # seconds
    
    for retry in range(max_retries):
        try:
            # Get the current service status
            request = service.namespaces().services().get(name=name)
            service_details = request.execute()
            
            # Check if the service is ready
            conditions = service_details.get('status', {}).get('conditions', [])
            ready_condition = next((c for c in conditions if c.get('type') == 'Ready'), None)
            
            if ready_condition and ready_condition.get('status') == 'True':
                print(f"Deployment completed successfully after {retry} checks.")
                return service_details
            
            # Get the latest status message
            status_message = "Deployment in progress..."
            if ready_condition:
                status_message = ready_condition.get('message', status_message)
            
            print(f"Waiting for deployment... Status: {status_message} (Attempt {retry+1}/{max_retries})")
            time.sleep(retry_interval)
            
        except Exception as e:
            print(f"Error checking deployment status: {e}")
            time.sleep(retry_interval)
    
    raise Exception(f"Deployment timed out after {max_retries * retry_interval} seconds")
```

## Solution: Get service URL

```python
def get_service_url(service, name):
    """
    Get the URL of a deployed Cloud Run service.
    """
    try:
        # Get the service details
        request = service.namespaces().services().get(name=name)
        service_details = request.execute()
        
        # Extract and return the URL
        url = service_details.get('status', {}).get('url')
        
        if not url:
            raise Exception("Service URL not found in the deployment response")
            
        return url
    except Exception as e:
        raise Exception(f"Failed to get service URL: {e}")
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Deploy a container to Cloud Run:
```bash
python deploy_run.py --project_id YOUR_PROJECT_ID --service_name devops-cloudrun --public
```

3. For custom container image name:
```bash
python deploy_run.py --project_id YOUR_PROJECT_ID --service_name custom-service --image_name custom-image
```

4. For a different region:
```bash
python deploy_run.py --project_id YOUR_PROJECT_ID --region us-east1
```

## Notes

When working with Cloud Run in production environments:

1. Consider setting up continuous deployment with Cloud Build
2. Use Cloud Run's concurrency and scaling features for cost optimization
3. Implement proper error handling and logging in your containerized app
4. Use environment variables for configuration (Cloud Run supports them)
5. For private services, use IAM for access control
6. Consider using VPC connectors for connecting to private resources

For more information, refer to the [Google Cloud Run documentation](https://cloud.google.com/run/docs) 