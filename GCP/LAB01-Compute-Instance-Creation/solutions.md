# LAB01 - Compute Instance Creation - Solutions

This document provides solutions to the TODOs in the `create_instance.py` script.

## Solution: Initialize the InstancesClient

```python
# Initialize the InstancesClient for managing Compute Engine VMs
instance_client = compute_v1.InstancesClient()
```

## Solution: Create the VM instance configuration

```python
# Create the VM instance configuration
instance = compute_v1.Instance()
instance.name = instance_name
instance.machine_type = machine_type

# Configure the boot disk with the specified image
disk = compute_v1.AttachedDisk()
disk.auto_delete = True
disk.boot = True
initialize_params = compute_v1.AttachedDiskInitializeParams()
initialize_params.source_image = f"projects/{image_project}/global/images/family/{image_family}"
disk.initialize_params = initialize_params
instance.disks = [disk]

# Configure the network interface (default VPC network)
network_interface = compute_v1.NetworkInterface()
network_interface.name = "global/networks/default"
access_config = compute_v1.AccessConfig()
access_config.name = "External NAT"
access_config.type_ = "ONE_TO_ONE_NAT"
network_interface.access_configs = [access_config]
instance.network_interfaces = [network_interface]
```

## Solution: Submit the instance creation request

```python
# Submit the instance creation request
operation = instance_client.insert(
    project=project_id,
    zone=zone,
    instance_resource=instance
)
```

## Solution: Return the operation

```python
# Return the operation
return operation
```

## Solution: Initialize the ZoneOperationsClient

```python
# Initialize the ZoneOperationsClient
zone_operations_client = compute_v1.ZoneOperationsClient()
```

## Solution: Poll the operation until it's complete

```python
# Poll the operation until it's complete
while True:
    operation = zone_operations_client.get(
        project=project_id,
        zone=zone,
        operation=operation_name
    )
    if operation.status == compute_v1.Operation.Status.DONE:
        if operation.error:
            print(f"Error during operation: {operation.error}")
            raise Exception(operation.error)
        break
    time.sleep(1)  # Wait for 1 second before checking again
```

## Solution: Get the operation name and wait for it to complete

```python
# Get the operation name from the returned operation and pass it to wait_for_operation
if operation:
    wait_for_operation(compute_v1.ZoneOperationsClient(), args.project, args.zone, operation.name)
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Run the script with your project:
```bash
python create_instance.py --project=your-gcp-project-id
```

## Cleanup

Don't forget to clean up the created resources to avoid unnecessary charges:

```bash
gcloud compute instances delete devops-instance --zone=us-central1-a --project=your-gcp-project-id -q
``` 