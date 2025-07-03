# LAB07 - Cloud SQL Instance Automation - Solutions

This document provides solutions to the TODOs in the `create_sql_instance.py` script.

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

## Solution: Build SQL Admin API client

```python
def build_sql_admin_client(credentials):
    """
    Build and return a Cloud SQL Admin API client.
    """
    try:
        service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)
        return service
    except Exception as e:
        raise Exception(f"Failed to build SQL Admin API client: {e}")
```

## Solution: Create SQL instance

```python
def create_sql_instance(service, project_id, instance_name, db_version="MYSQL_8_0", 
                        tier="db-f1-micro", region="us-central1"):
    """
    Create a new Cloud SQL instance.
    """
    print(f"Creating Cloud SQL instance '{instance_name}' in {region}...")
    
    # Define the instance configuration
    instance_body = {
        "name": instance_name,
        "region": region,
        "databaseVersion": db_version,
        "settings": {
            "tier": tier,
            "backupConfiguration": {
                "enabled": True,
                "startTime": "00:00"  # Midnight UTC
            },
            "activationPolicy": "ALWAYS",
            "dataDiskSizeGb": "10",
            "dataDiskType": "PD_SSD",
            "locationPreference": {
                "zone": f"{region}-a"
            },
            "databaseFlags": [],
            "maintenanceWindow": {
                "hour": 5,  # 5 AM
                "day": 7,   # Sunday
                "updateTrack": "stable"
            }
        }
    }
    
    # Send the instance creation request
    request = service.instances().insert(
        project=project_id,
        body=instance_body
    )
    
    try:
        response = request.execute()
        print(f"Cloud SQL instance creation initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to create SQL instance: {e}")
```

## Solution: Wait for operation

```python
def wait_for_operation(service, project_id, operation_name):
    """
    Wait for a SQL Admin operation to complete.
    """
    print(f"Waiting for operation {operation_name} to complete...")
    
    max_retries = 60  # 30 minutes (30 seconds * 60)
    retry_interval = 30  # seconds
    
    for retry in range(max_retries):
        request = service.operations().get(
            project=project_id,
            operation=operation_name
        )
        
        try:
            operation = request.execute()
            operation_status = operation.get('status')
            
            if operation_status == 'DONE':
                if 'error' in operation:
                    error_message = operation['error'].get('message', 'Unknown error')
                    raise Exception(f"Operation failed: {error_message}")
                return operation
            
            print(f"Operation in progress... Status: {operation_status} (Attempt {retry+1}/{max_retries})")
            time.sleep(retry_interval)
            
        except Exception as e:
            raise Exception(f"Error checking operation status: {e}")
    
    raise Exception(f"Operation timed out after {max_retries * retry_interval} seconds")
```

## Solution: List SQL instances

```python
def list_sql_instances(service, project_id):
    """
    List all Cloud SQL instances in the project.
    """
    print(f"Listing Cloud SQL instances in project {project_id}...")
    
    request = service.instances().list(project=project_id)
    
    try:
        response = request.execute()
        instances = response.get('items', [])
        
        if instances:
            # Create table data for display
            table_data = []
            headers = ["Name", "Database", "State", "Region", "Tier", "IP Address"]
            
            for instance in instances:
                ip_address = instance.get("ipAddresses", [{}])[0].get("ipAddress", "None") if instance.get("ipAddresses") else "None"
                
                table_data.append([
                    instance.get("name"),
                    instance.get("databaseVersion"),
                    instance.get("state"),
                    instance.get("region"),
                    instance.get("settings", {}).get("tier"),
                    ip_address
                ])
            
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            
        return instances
    except Exception as e:
        raise Exception(f"Failed to list SQL instances: {e}")
```

## Solution: Delete SQL instance

```python
def delete_sql_instance(service, project_id, instance_name):
    """
    Delete a Cloud SQL instance.
    """
    print(f"Deleting Cloud SQL instance '{instance_name}'...")
    
    request = service.instances().delete(
        project=project_id,
        instance=instance_name
    )
    
    try:
        response = request.execute()
        print(f"Cloud SQL instance deletion initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to delete SQL instance: {e}")
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Create a new MySQL instance:
```bash
python create_sql_instance.py --project_id YOUR_PROJECT_ID --create --instance_name test-mysql-instance
```

3. List all SQL instances in your project:
```bash
python create_sql_instance.py --project_id YOUR_PROJECT_ID --list
```

4. Delete an instance:
```bash
python create_sql_instance.py --project_id YOUR_PROJECT_ID --delete --instance_name test-mysql-instance
```

5. Create a PostgreSQL instance:
```bash
python create_sql_instance.py --project_id YOUR_PROJECT_ID --create --instance_name test-pg-instance --db_version POSTGRES_14 --tier db-g1-small
```

## Notes

When working with Cloud SQL in production environments:

1. Be aware that SQL instances can be expensive if left running
2. Consider enabling point-in-time recovery for production databases
3. Use private IP for connections within GCP instead of public IP when possible
4. Automate regular backups with appropriate retention policies
5. Use a stronger machine type for production workloads

For more information, refer to the [Google Cloud SQL documentation](https://cloud.google.com/sql/docs) 