# LAB08 - VPC Network Creation - Solutions

This document provides solutions to the TODOs in the `create_vpc.py` script.

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

## Solution: Build Compute Engine API client

```python
def build_compute_client(credentials):
    """
    Build and return a Compute Engine API client.
    """
    try:
        service = discovery.build('compute', 'v1', credentials=credentials)
        return service
    except Exception as e:
        raise Exception(f"Failed to build Compute Engine API client: {e}")
```

## Solution: Create VPC network

```python
def create_vpc_network(service, project_id, network_name):
    """
    Create a new custom VPC network.
    """
    print(f"Creating VPC network '{network_name}'...")
    
    # Define the network configuration
    network_body = {
        "name": network_name,
        "autoCreateSubnetworks": False,  # Use custom subnet mode
        "routingConfig": {
            "routingMode": "REGIONAL"
        }
    }
    
    # Send the network creation request
    try:
        request = service.networks().insert(
            project=project_id,
            body=network_body
        )
        response = request.execute()
        print(f"VPC network creation initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to create VPC network: {e}")
```

## Solution: Create subnet

```python
def create_subnet(service, project_id, region, subnet_name, network_name, ip_cidr_range="10.0.0.0/24"):
    """
    Create a new subnet in a VPC network.
    """
    print(f"Creating subnet '{subnet_name}' in region '{region}' with CIDR range '{ip_cidr_range}'...")
    
    # Define the subnet configuration
    subnet_body = {
        "name": subnet_name,
        "ipCidrRange": ip_cidr_range,
        "region": region,
        "network": f"projects/{project_id}/global/networks/{network_name}",
        "privateIpGoogleAccess": True  # Allows VMs to access Google APIs without public IP
    }
    
    # Send the subnet creation request
    try:
        request = service.subnetworks().insert(
            project=project_id,
            region=region,
            body=subnet_body
        )
        response = request.execute()
        print(f"Subnet creation initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to create subnet: {e}")
```

## Solution: Create firewall rule

```python
def create_firewall_rule(service, project_id, network_name, rule_name=None):
    """
    Create a basic firewall rule to allow SSH access.
    """
    if rule_name is None:
        rule_name = f"{network_name}-allow-ssh"
    
    print(f"Creating firewall rule '{rule_name}' for network '{network_name}'...")
    
    # Define the firewall rule configuration
    firewall_body = {
        "name": rule_name,
        "network": f"projects/{project_id}/global/networks/{network_name}",
        "direction": "INGRESS",
        "priority": 1000,
        "allowed": [
            {
                "IPProtocol": "tcp",
                "ports": ["22"]
            }
        ],
        "sourceRanges": ["0.0.0.0/0"],  # Allow from any source (public internet)
        "description": "Allow SSH access from anywhere"
    }
    
    # Send the firewall rule creation request
    try:
        request = service.firewalls().insert(
            project=project_id,
            body=firewall_body
        )
        response = request.execute()
        print(f"Firewall rule creation initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to create firewall rule: {e}")
```

## Solution: Wait for global operation

```python
def wait_for_global_operation(service, project_id, operation_name):
    """
    Wait for a global operation to complete.
    """
    print(f"Waiting for operation {operation_name} to complete...")
    
    max_retries = 30  # 15 minutes (30 seconds * 30)
    retry_interval = 30  # seconds
    
    for retry in range(max_retries):
        request = service.globalOperations().get(
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

## Solution: Wait for region operation

```python
def wait_for_region_operation(service, project_id, region, operation_name):
    """
    Wait for a regional operation to complete.
    """
    print(f"Waiting for operation {operation_name} in region {region} to complete...")
    
    max_retries = 30  # 15 minutes (30 seconds * 30)
    retry_interval = 30  # seconds
    
    for retry in range(max_retries):
        request = service.regionOperations().get(
            project=project_id,
            region=region,
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

## Solution: List networks

```python
def list_networks(service, project_id):
    """
    List all VPC networks in the project.
    """
    print(f"Listing VPC networks in project {project_id}...")
    
    try:
        request = service.networks().list(project=project_id)
        response = request.execute()
        networks = response.get('items', [])
        
        if networks:
            # Create table data for display
            table_data = []
            headers = ["Name", "Subnet Mode", "Mode", "Creation Time"]
            
            for network in networks:
                subnet_mode = "Auto" if network.get("autoCreateSubnetworks") else "Custom"
                
                table_data.append([
                    network.get("name"),
                    "Yes" if network.get("autoCreateSubnetworks") else "No",
                    subnet_mode,
                    network.get("creationTimestamp")
                ])
            
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            
            # Display detailed information for each network
            for network in networks:
                display_network_info(network)
                
        return networks
    except Exception as e:
        raise Exception(f"Failed to list networks: {e}")
```

## Solution: List subnets

```python
def list_subnets(service, project_id, region="all"):
    """
    List all subnets in the project, optionally filtered by region.
    """
    print(f"Listing subnets in project {project_id}{' in region ' + region if region != 'all' else ''}...")
    
    try:
        subnets = []
        
        if region != "all":
            # List subnets in specific region
            request = service.subnetworks().list(
                project=project_id,
                region=region
            )
            response = request.execute()
            subnets = response.get('items', [])
        else:
            # List subnets in all regions using aggregatedList
            request = service.subnetworks().aggregatedList(project=project_id)
            response = request.execute()
            items = response.get('items', {})
            
            # Flatten the aggregated list
            for region_key, region_data in items.items():
                if 'subnetworks' in region_data:
                    subnets.extend(region_data['subnetworks'])
        
        if subnets:
            # Create table data for display
            table_data = []
            headers = ["Name", "Region", "Network", "IP Range", "Private Google Access"]
            
            for subnet in subnets:
                # Extract the region from the selfLink URL
                subnet_region = subnet.get("region", "").split('/')[-1]
                
                # Extract the network name from the full URL
                network_url = subnet.get("network", "")
                network_name = network_url.split('/')[-1]
                
                table_data.append([
                    subnet.get("name"),
                    subnet_region,
                    network_name,
                    subnet.get("ipCidrRange"),
                    "Yes" if subnet.get("privateIpGoogleAccess") else "No"
                ])
            
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            
        return subnets
    except Exception as e:
        raise Exception(f"Failed to list subnets: {e}")
```

## Solution: Delete subnet

```python
def delete_subnet(service, project_id, region, subnet_name):
    """
    Delete a subnet.
    """
    print(f"Deleting subnet '{subnet_name}' in region '{region}'...")
    
    try:
        request = service.subnetworks().delete(
            project=project_id,
            region=region,
            subnetwork=subnet_name
        )
        response = request.execute()
        print(f"Subnet deletion initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to delete subnet: {e}")
```

## Solution: Delete network

```python
def delete_network(service, project_id, network_name):
    """
    Delete a VPC network.
    """
    print(f"Deleting VPC network '{network_name}'...")
    
    try:
        request = service.networks().delete(
            project=project_id,
            network=network_name
        )
        response = request.execute()
        print(f"Network deletion initiated. Operation: {response.get('name')}")
        return response
    except Exception as e:
        raise Exception(f"Failed to delete network: {e}")
```

## Solution: Find subnets by network

```python
def find_subnets_by_network(service, project_id, network_name):
    """
    Find all subnets associated with a network.
    """
    print(f"Finding subnets for network '{network_name}'...")
    
    try:
        # Get all subnets across all regions
        request = service.subnetworks().aggregatedList(project=project_id)
        response = request.execute()
        items = response.get('items', {})
        
        # Create a list to store subnet name and region pairs
        subnet_regions = []
        
        # Check each region
        for region_key, region_data in items.items():
            # Skip if there are no subnetworks in this region
            if 'subnetworks' not in region_data:
                continue
                
            # Get the region name from the key (format: regions/region-name)
            region = region_key.split('/')[-1]
            
            # Check each subnet in this region
            for subnet in region_data['subnetworks']:
                # Get the network URL and extract the name
                network_url = subnet.get('network', '')
                subnet_network_name = network_url.split('/')[-1]
                
                # If this subnet belongs to our target network, add it to the list
                if subnet_network_name == network_name:
                    subnet_regions.append([subnet.get('name'), region])
        
        if subnet_regions:
            print(f"Found {len(subnet_regions)} subnet(s) for network '{network_name}':")
            for subnet_name, region in subnet_regions:
                print(f"  - {subnet_name} (region: {region})")
        else:
            print(f"No subnets found for network '{network_name}'")
            
        return subnet_regions
    except Exception as e:
        raise Exception(f"Failed to find subnets for network: {e}")
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Create a new VPC network and subnet:
```bash
python create_vpc.py --project_id YOUR_PROJECT_ID --create --network_name custom-vpc --subnet_name custom-subnet
```

3. List all networks and subnets in your project:
```bash
python create_vpc.py --project_id YOUR_PROJECT_ID --list
```

4. Delete a network and its subnets:
```bash
python create_vpc.py --project_id YOUR_PROJECT_ID --delete --network_name custom-vpc
```

5. Create a network with a custom CIDR range:
```bash
python create_vpc.py --project_id YOUR_PROJECT_ID --create --network_name custom-vpc --subnet_name custom-subnet --ip_cidr_range 192.168.1.0/24
```

## Notes

When working with VPC networks in production environments:

1. Plan your IP address space carefully to avoid overlapping CIDRs
2. Use meaningful names that reflect the purpose of networks and subnets
3. Implement proper firewall rules to restrict traffic appropriately
4. Consider using private Google access for VM instances that don't need external IPs
5. Remember that VPC networks are global resources, but subnets are regional

For more information, refer to the [Google Cloud VPC documentation](https://cloud.google.com/vpc/docs/vpc) 