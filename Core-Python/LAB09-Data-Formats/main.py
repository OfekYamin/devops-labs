#!/usr/bin/env python3
"""
LAB09 - Working with Data Formats in Python

This module demonstrates how to work with common data formats 
(JSON, YAML, XML) used in DevOps and infrastructure automation.
"""

# TODO: Import required libraries for working with different data formats
# import json
# import yaml
# try:
#     import xmltodict
# except ImportError:
#     print("Please install xmltodict: pip install xmltodict")
#     exit(1)


def process_json_data(json_file):
    """
    Process a JSON file and extract key information.
    
    Args:
        json_file (str): Path to the JSON file
        
    Returns:
        dict: Extracted information from the JSON file
    """
    # TODO: Implement JSON processing
    # 1. Open and read the JSON file
    # 2. Parse the JSON data into a Python dictionary
    # 3. Extract and return relevant information
    #    - Application name and version
    #    - Database connection details
    #    - List of services with their hosts and ports
    
    print(f"Processing JSON file: {json_file}")
    return {}


def process_yaml_data(yaml_file):
    """
    Process a YAML file containing infrastructure definition.
    
    Args:
        yaml_file (str): Path to the YAML file
        
    Returns:
        dict: Processed information from the YAML file
    """
    # TODO: Implement YAML processing
    # 1. Open and read the YAML file
    # 2. Parse the YAML data into a Python dictionary
    # 3. Extract and return relevant information
    #    - Infrastructure region and environment
    #    - VPC and subnet information
    #    - Server details (names, types, security groups)
    
    print(f"Processing YAML file: {yaml_file}")
    return {}


def process_xml_data(xml_file):
    """
    Process an XML file containing service definitions.
    
    Args:
        xml_file (str): Path to the XML file
        
    Returns:
        dict: Processed information from the XML file
    """
    # TODO: Implement XML processing
    # 1. Open and read the XML file
    # 2. Parse the XML data using xmltodict
    # 3. Extract and return relevant information
    #    - List of services with their IDs and names
    #    - Service endpoints
    #    - Service dependencies
    
    print(f"Processing XML file: {xml_file}")
    return {}


def convert_formats(data, source_format, target_format):
    """
    Convert data between different formats.
    
    Args:
        data (dict): Data to convert
        source_format (str): Source format ('json', 'yaml', or 'xml')
        target_format (str): Target format ('json', 'yaml', or 'xml')
        
    Returns:
        str: Data in the target format
    """
    # TODO: Implement format conversion
    # 1. Check that source and target formats are valid
    # 2. Convert the data to the target format
    # 3. Return the converted data as a string
    
    print(f"Converting from {source_format} to {target_format}")
    return ""


def validate_data(data, schema=None):
    """
    Validate data against a schema or basic rules.
    
    Args:
        data (dict): Data to validate
        schema (dict, optional): Schema to validate against
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement data validation
    # 1. If a schema is provided, validate against it
    # 2. Otherwise, perform basic validation:
    #    - Check required fields are present
    #    - Verify data types
    #    - Ensure values are within expected ranges
    
    print("Validating data...")
    return True


def main():
    """Main function to demonstrate data format operations."""
    print("LAB09 - Working with Data Formats")
    print("=================================\n")
    
    # File paths
    json_file = "sample_data/config.json"
    yaml_file = "sample_data/servers.yaml"
    xml_file = "sample_data/services.xml"
    
    # TODO: Process each data format
    # 1. Call the process_json_data function
    # 2. Call the process_yaml_data function
    # 3. Call the process_xml_data function
    
    # TODO: Demonstrate format conversion
    # 1. Convert JSON data to YAML
    # 2. Convert YAML data to JSON
    # 3. Convert XML data to JSON
    
    # TODO: Validate the data
    # 1. Perform basic validation on the processed data
    
    # TODO: (Bonus) Save converted data to files
    # 1. Write converted data to new files
    
    print("\nData processing complete!")


if __name__ == "__main__":
    main() 