#!/usr/bin/env python3
"""
GCP LAB01 - Compute Instance Creation Script
This script automates the creation of a VM instance in Google Cloud Platform
using the google-cloud-compute Python SDK.
"""

import os
import time
import argparse
from google.cloud import compute_v1
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Create a VM instance in Google Cloud Platform'
    )
    parser.add_argument(
        '--project', 
        help='GCP Project ID',
        default=os.environ.get('GCP_PROJECT_ID')
    )
    parser.add_argument(
        '--zone', 
        help='Compute Engine zone', 
        default=os.environ.get('GCP_ZONE', 'us-central1-a')
    )
    parser.add_argument(
        '--instance_name', 
        help='Name for the new instance', 
        default=os.environ.get('GCP_INSTANCE_NAME', 'devops-instance')
    )
    parser.add_argument(
        '--machine_type', 
        help='Machine type for the instance',
        default=os.environ.get('GCP_MACHINE_TYPE', 'e2-micro')
    )
    parser.add_argument(
        '--image_project', 
        help='Project containing the OS image',
        default=os.environ.get('GCP_IMAGE_PROJECT', 'debian-cloud')
    )
    parser.add_argument(
        '--image_family', 
        help='Image family for the OS',
        default=os.environ.get('GCP_IMAGE_FAMILY', 'debian-11')
    )
    
    return parser.parse_args()

def create_instance(project_id, zone, instance_name, machine_type, image_project, image_family):
    """
    Create a new Compute Engine VM instance.
    
    Args:
        project_id (str): GCP Project ID
        zone (str): Compute Engine zone (e.g., 'us-central1-a')
        instance_name (str): Name for the VM instance
        machine_type (str): Machine type (e.g., 'e2-micro')
        image_project (str): Project containing the OS image
        image_family (str): Image family for the OS
    
    Returns:
        operation: The create instance operation
    """
    # TODO: Initialize the InstancesClient for managing Compute Engine VMs
    
    # TODO: Create the VM instance configuration
    # - Set the instance name
    # - Configure the machine type
    # - Configure the boot disk with the specified image
    # - Configure the network interface
    
    # TODO: Submit the instance creation request
    
    # TODO: Return the operation
    pass

def wait_for_operation(compute_client, project_id, zone, operation_name):
    """
    Wait for a zone operation to complete.
    
    Args:
        compute_client: Compute Engine zone operations client
        project_id (str): GCP Project ID
        zone (str): Compute Engine zone
        operation_name (str): Name of the operation to wait for
    """
    print(f"Waiting for operation {operation_name} to complete...")
    
    # TODO: Initialize the ZoneOperationsClient
    
    # TODO: Poll the operation until it's complete
    # Hint: Use a while loop and check the operation status
    
    print(f"Operation {operation_name} completed successfully!")

def main():
    """Main function to create a VM instance."""
    args = parse_arguments()
    
    # Verify we have the project ID
    if not args.project:
        print("Error: GCP Project ID is required. Provide it with --project flag or set GCP_PROJECT_ID environment variable.")
        return 1
    
    # Build full machine type path
    full_machine_type = f"zones/{args.zone}/machineTypes/{args.machine_type}"
    
    # Build full image path
    source_image = f"projects/{args.image_project}/global/images/family/{args.image_family}"
    
    print(f"Creating VM instance '{args.instance_name}' in {args.zone}...")
    print(f"Machine type: {args.machine_type}")
    print(f"Boot disk image: {source_image}")
    
    try:
        # Create the instance
        operation = create_instance(
            args.project,
            args.zone,
            args.instance_name,
            full_machine_type,
            args.image_project,
            args.image_family
        )
        
        # TODO: Get the operation name from the returned operation and pass it to wait_for_operation
        
        print(f"VM instance '{args.instance_name}' created successfully!")
        print(f"You can check the instance in the GCP Console or with:")
        print(f"gcloud compute instances describe {args.instance_name} --zone={args.zone}")
        
        return 0
    except Exception as e:
        print(f"Error creating VM instance: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 