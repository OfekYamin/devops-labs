# LAB08: Azure Virtual Network Setup with Python

## Objectives
By the end of this lab, you'll be able to:
- Create Azure Resource Groups programmatically
- Set up Virtual Networks and Subnets using Azure SDK for Python
- List network resources and retrieve their properties
- Implement proper resource cleanup to avoid unnecessary costs

## Prerequisites
- Azure account with active subscription
- Python 3.8 or higher installed
- Basic knowledge of networking concepts (IP addressing, subnets)
- Azure CLI installed and configured (`az login` completed)

## Lab Files
- `create_vnet.py`: Main Python script to create and manage Azure Virtual Networks
- `requirements.txt`: Contains required Python packages for the lab

## Getting Started
1. Navigate to the lab folder:
   ```
   cd Cloud-Automation/Azure/LAB08-Virtual-Network-Setup
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set your Azure subscription ID as an environment variable:
   ```
   export AZURE_SUBSCRIPTION_ID="your-subscription-id"  # On Windows: set AZURE_SUBSCRIPTION_ID=your-subscription-id
   ```

   You can get your subscription ID by running:
   ```
   az account show --query id -o tsv
   ```

## Tasks
Your task is to complete the TODOs in `create_vnet.py` to implement the following functionality:

1. **Create Resource Group**
   - Implement the `create_resource_group()` function to create a resource group in the specified location
   - Example:
     ```python
     rg_params = {'location': LOCATION}
     resource_group = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, rg_params)
     ```

2. **Create Virtual Network**
   - Implement the `create_virtual_network()` function to create a virtual network with the specified address space
   - Example:
     ```python
     vnet_params = {
         'location': LOCATION,
         'address_space': {
             'address_prefixes': [VNET_ADDRESS_PREFIX]
         }
     }
     # Create the VNet using begin_create_or_update which returns a poller
     ```

3. **Create Subnet**
   - Implement the `create_subnet()` function to create a subnet within the virtual network
   - Example:
     ```python
     subnet_params = {
         'address_prefix': SUBNET_ADDRESS_PREFIX
     }
     # Create the subnet using begin_create_or_update which returns a poller
     ```

4. **Get Virtual Network Details**
   - Implement the `get_virtual_network_details()` function to retrieve information about the created virtual network
   - Example:
     ```python
     vnet = network_client.virtual_networks.get(RESOURCE_GROUP_NAME, VNET_NAME)
     # Extract and print relevant details
     ```

5. **List Subnets**
   - Implement the `list_subnets()` function to list all subnets in the virtual network
   - Example:
     ```python
     subnets = network_client.subnets.list(RESOURCE_GROUP_NAME, VNET_NAME)
     # Iterate through subnets and print details
     ```

6. **Delete Resources**
   - Implement the `delete_vnet_and_resources()` function to clean up all created resources
   - Example:
     ```python
     # Delete the VNet first
     # Then delete the resource group
     ```

## Validation Checklist
- [ ] Resource group created successfully
- [ ] Virtual network created with correct address space
- [ ] Subnet created with correct address prefix
- [ ] Virtual network details retrieved and displayed
- [ ] Subnets listed correctly
- [ ] All resources cleaned up properly

## Understanding IP Address Prefixes
- Virtual Network address space (CIDR notation): `10.0.0.0/16` provides 65,536 addresses
- Subnet address prefix: `10.0.1.0/24` provides 256 addresses within the VNet

## Common Issues and Troubleshooting
- **Authentication errors**: Ensure you're logged in with Azure CLI
- **Permission errors**: Verify your account has proper permissions to create network resources
- **Name conflicts**: If resources already exist with the same names, the script may fail
- **Subnet overlaps**: Ensure subnet address ranges don't overlap with existing subnets

## Next Steps
After completing this lab, you might want to:
- Create multiple subnets within a VNet
- Configure Network Security Groups (NSGs)
- Set up VNet peering between different virtual networks
- Deploy a VM into your created subnet

## Cleanup
Always run the cleanup process at the end of your lab session by pressing Enter when prompted, or by running the script with the delete operation.

---
*Note: This lab is designed for educational purposes. In a production environment, you would implement additional security measures and follow your organization's naming conventions.*