# LAB09 - Working with Data Formats Solutions

This file provides a reference solution for the Data Formats lab. Please attempt the lab on your own first before referring to this solution.

## Complete Implementation of `main.py`

```python
#!/usr/bin/env python3
"""
LAB09 - Working with Data Formats in Python

This module demonstrates how to work with common data formats 
(JSON, YAML, XML) used in DevOps and infrastructure automation.
"""

import json
import os
import yaml
try:
    import xmltodict
    import jsonschema
except ImportError:
    print("Please install required packages:")
    print("pip install pyyaml xmltodict jsonschema")
    exit(1)


def process_json_data(json_file):
    """
    Process a JSON file and extract key information.
    
    Args:
        json_file (str): Path to the JSON file
        
    Returns:
        dict: Extracted information from the JSON file
    """
    try:
        # Open and read the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Extract relevant information
        result = {
            'application': {
                'name': data.get('application', 'Unknown'),
                'version': data.get('version', 'Unknown'),
                'environment': data.get('environment', 'Unknown')
            },
            'database': {
                'host': data.get('database', {}).get('host', 'Unknown'),
                'port': data.get('database', {}).get('port', 0),
                'name': data.get('database', {}).get('name', 'Unknown'),
                'user': data.get('database', {}).get('user', 'Unknown'),
                'ssl_enabled': data.get('database', {}).get('ssl', False)
            },
            'services': []
        }
        
        # Extract services information
        for service in data.get('services', []):
            result['services'].append({
                'name': service.get('name', 'Unknown'),
                'host': service.get('host', 'Unknown'),
                'port': service.get('port', 0),
                'health_check': service.get('health_check', 'Unknown')
            })
        
        print(f"Successfully processed JSON file: {json_file}")
        return result
    
    except FileNotFoundError:
        print(f"Error: File not found - {json_file}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {json_file} - {str(e)}")
        return {}
    except Exception as e:
        print(f"Error processing JSON file: {str(e)}")
        return {}


def process_yaml_data(yaml_file):
    """
    Process a YAML file containing infrastructure definition.
    
    Args:
        yaml_file (str): Path to the YAML file
        
    Returns:
        dict: Processed information from the YAML file
    """
    try:
        # Open and read the YAML file
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
        
        # Extract infrastructure information
        infrastructure = data.get('infrastructure', {})
        result = {
            'environment': infrastructure.get('environment', 'Unknown'),
            'region': infrastructure.get('region', 'Unknown'),
            'vpc': {
                'id': infrastructure.get('vpc', {}).get('id', 'Unknown'),
                'cidr': infrastructure.get('vpc', {}).get('cidr', 'Unknown'),
                'subnets': []
            },
            'servers': [],
            'security_groups': []
        }
        
        # Extract subnet information
        for subnet in infrastructure.get('vpc', {}).get('subnets', []):
            result['vpc']['subnets'].append({
                'name': subnet.get('name', 'Unknown'),
                'cidr': subnet.get('cidr', 'Unknown'),
                'az': subnet.get('az', 'Unknown'),
                'public': subnet.get('public', False)
            })
        
        # Extract server information
        for server in data.get('servers', []):
            server_info = {
                'name': server.get('name', 'Unknown'),
                'type': server.get('type', 'Unknown'),
                'ami': server.get('ami', 'Unknown'),
                'subnet': server.get('subnet', 'Unknown'),
                'security_groups': server.get('security_groups', []),
                'tags': server.get('tags', {})
            }
            result['servers'].append(server_info)
        
        # Extract security group information
        for sg in data.get('security_groups', []):
            sg_info = {
                'name': sg.get('name', 'Unknown'),
                'description': sg.get('description', 'Unknown'),
                'rules': sg.get('rules', [])
            }
            result['security_groups'].append(sg_info)
        
        print(f"Successfully processed YAML file: {yaml_file}")
        return result
    
    except FileNotFoundError:
        print(f"Error: File not found - {yaml_file}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML format in {yaml_file} - {str(e)}")
        return {}
    except Exception as e:
        print(f"Error processing YAML file: {str(e)}")
        return {}


def process_xml_data(xml_file):
    """
    Process an XML file containing service definitions.
    
    Args:
        xml_file (str): Path to the XML file
        
    Returns:
        dict: Processed information from the XML file
    """
    try:
        # Open and read the XML file
        with open(xml_file, 'r') as file:
            xml_content = file.read()
        
        # Parse the XML data using xmltodict
        data = xmltodict.parse(xml_content)
        
        # Extract service information
        services_data = data.get('services', {}).get('service', [])
        if not isinstance(services_data, list):
            services_data = [services_data]
        
        result = {
            'services': []
        }
        
        for service in services_data:
            # Extract endpoints
            endpoints = []
            endpoints_data = service.get('endpoints', {}).get('endpoint', [])
            if not isinstance(endpoints_data, list):
                endpoints_data = [endpoints_data]
            
            for endpoint in endpoints_data:
                endpoints.append({
                    'protocol': endpoint.get('protocol', 'Unknown'),
                    'host': endpoint.get('host', 'Unknown'),
                    'port': int(endpoint.get('port', 0)),
                    'path': endpoint.get('path', '/')
                })
            
            # Extract dependencies
            dependencies = []
            deps_data = service.get('dependencies', {}).get('dependency', [])
            if deps_data:
                if not isinstance(deps_data, list):
                    deps_data = [deps_data]
                dependencies = deps_data
            
            # Build service information
            service_info = {
                'id': service.get('id', 'Unknown'),
                'name': service.get('name', 'Unknown'),
                'type': service.get('type', 'Unknown'),
                'status': service.get('status', 'Unknown'),
                'endpoints': endpoints,
                'dependencies': dependencies
            }
            
            result['services'].append(service_info)
        
        print(f"Successfully processed XML file: {xml_file}")
        return result
    
    except FileNotFoundError:
        print(f"Error: File not found - {xml_file}")
        return {}
    except Exception as e:
        print(f"Error processing XML file: {str(e)}")
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
    valid_formats = ['json', 'yaml', 'xml']
    
    # Validate formats
    if source_format not in valid_formats:
        raise ValueError(f"Invalid source format: {source_format}. Must be one of {valid_formats}")
    if target_format not in valid_formats:
        raise ValueError(f"Invalid target format: {target_format}. Must be one of {valid_formats}")
    if source_format == target_format:
        print(f"Source and target formats are the same ({source_format}). No conversion needed.")
        return data
    
    try:
        # Convert to target format
        if target_format == 'json':
            return json.dumps(data, indent=2)
        elif target_format == 'yaml':
            return yaml.dump(data, default_flow_style=False, sort_keys=False)
        elif target_format == 'xml':
            # For simplicity, we'll convert to XML using xmltodict's unparse
            # This requires a root element name
            return xmltodict.unparse({'root': data}, pretty=True)
        
    except Exception as e:
        print(f"Error converting from {source_format} to {target_format}: {str(e)}")
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
    # If a schema is provided, use jsonschema for validation
    if schema:
        try:
            jsonschema.validate(instance=data, schema=schema)
            print("Data validation successful (using provided schema)")
            return True
        except jsonschema.exceptions.ValidationError as e:
            print(f"Schema validation error: {str(e)}")
            return False
    
    # Otherwise, perform basic validation
    try:
        # Check if data is a dictionary
        if not isinstance(data, dict):
            print("Error: Data must be a dictionary")
            return False
        
        # Check if data is empty
        if not data:
            print("Error: Data is empty")
            return False
        
        # Example basic validations (customize based on your data structure)
        if 'services' in data and not isinstance(data['services'], list):
            print("Error: 'services' must be a list")
            return False
        
        if 'application' in data and not isinstance(data['application'], dict):
            print("Error: 'application' must be a dictionary")
            return False
        
        print("Basic data validation successful")
        return True
        
    except Exception as e:
        print(f"Error during validation: {str(e)}")
        return False


def save_to_file(data, output_file):
    """
    Save data to a file based on the file extension.
    
    Args:
        data: The data to save
        output_file (str): Output file path with extension
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
        
        # Determine format based on file extension
        _, ext = os.path.splitext(output_file)
        
        with open(output_file, 'w') as file:
            if ext.lower() == '.json':
                if isinstance(data, str):
                    file.write(data)
                else:
                    json.dump(data, file, indent=2)
            elif ext.lower() in ['.yaml', '.yml']:
                if isinstance(data, str):
                    file.write(data)
                else:
                    yaml.dump(data, file, default_flow_style=False, sort_keys=False)
            elif ext.lower() == '.xml':
                file.write(data)
            else:
                # Default to plain text
                file.write(str(data))
                
        print(f"Successfully saved data to {output_file}")
        return True
        
    except Exception as e:
        print(f"Error saving to file {output_file}: {str(e)}")
        return False


def main():
    """Main function to demonstrate data format operations."""
    print("LAB09 - Working with Data Formats")
    print("=================================\n")
    
    # File paths
    json_file = "sample_data/config.json"
    yaml_file = "sample_data/servers.yaml"
    xml_file = "sample_data/services.xml"
    
    # Process each data format
    print("1. Processing data files:")
    print("-----------------------")
    json_data = process_json_data(json_file)
    yaml_data = process_yaml_data(yaml_file)
    xml_data = process_xml_data(xml_file)
    print()
    
    # Display some extracted information
    if json_data:
        app_info = json_data.get('application', {})
        print(f"Application: {app_info.get('name', 'Unknown')} (v{app_info.get('version', 'Unknown')})")
        print(f"Environment: {app_info.get('environment', 'Unknown')}")
        print(f"Database: {json_data.get('database', {}).get('host', 'Unknown')}:{json_data.get('database', {}).get('port', 0)}")
        print(f"Services: {len(json_data.get('services', []))}")
        print()
    
    if yaml_data:
        print(f"Infrastructure Region: {yaml_data.get('region', 'Unknown')}")
        print(f"Environment: {yaml_data.get('environment', 'Unknown')}")
        print(f"VPC CIDR: {yaml_data.get('vpc', {}).get('cidr', 'Unknown')}")
        print(f"Subnets: {len(yaml_data.get('vpc', {}).get('subnets', []))}")
        print(f"Servers: {len(yaml_data.get('servers', []))}")
        print()
    
    if xml_data:
        services = xml_data.get('services', [])
        print(f"Services defined: {len(services)}")
        for service in services[:3]:  # Show first 3 services
            print(f"  - {service.get('name', 'Unknown')} ({service.get('type', 'Unknown')})")
            print(f"    Status: {service.get('status', 'Unknown')}")
            print(f"    Endpoints: {len(service.get('endpoints', []))}")
            print(f"    Dependencies: {len(service.get('dependencies', []))}")
        print()
    
    # Demonstrate format conversion
    print("2. Converting between formats:")
    print("---------------------------")
    if json_data:
        print("Converting JSON data to YAML:")
        yaml_from_json = convert_formats(json_data, 'json', 'yaml')
        print(f"Result length: {len(yaml_from_json)} characters")
        
        # Save converted data to files (bonus)
        output_dir = "output"
        save_to_file(yaml_from_json, f"{output_dir}/config_from_json.yaml")
        print()
    
    if yaml_data:
        print("Converting YAML data to JSON:")
        json_from_yaml = convert_formats(yaml_data, 'yaml', 'json')
        print(f"Result length: {len(json_from_yaml)} characters")
        save_to_file(json_from_yaml, "output/servers_from_yaml.json")
        print()
    
    if xml_data:
        print("Converting XML data to JSON:")
        json_from_xml = convert_formats(xml_data, 'xml', 'json')
        print(f"Result length: {len(json_from_xml)} characters")
        save_to_file(json_from_xml, "output/services_from_xml.json")
        print()
    
    # Validate the data
    print("3. Validating data:")
    print("----------------")
    if json_data:
        is_valid = validate_data(json_data)
        print(f"JSON data validation: {'Passed' if is_valid else 'Failed'}")
    
    if yaml_data:
        is_valid = validate_data(yaml_data)
        print(f"YAML data validation: {'Passed' if is_valid else 'Failed'}")
    
    if xml_data:
        is_valid = validate_data(xml_data)
        print(f"XML data validation: {'Passed' if is_valid else 'Failed'}")
    
    print("\nData processing complete!")


if __name__ == "__main__":
    main()
```

## Key Learning Points

1. **Working with JSON**:
   - Using `json.load()` to parse JSON from a file
   - Using `json.dumps()` to convert Python objects to JSON strings
   - Error handling with `json.JSONDecodeError`

2. **Working with YAML**:
   - Using `yaml.safe_load()` to parse YAML from a file
   - Using `yaml.dump()` to convert Python objects to YAML strings
   - Error handling with `yaml.YAMLError`

3. **Working with XML**:
   - Using `xmltodict.parse()` to convert XML to Python dictionaries
   - Using `xmltodict.unparse()` to convert Python dictionaries to XML
   - Handling XML's hierarchical structure

4. **Data Validation**:
   - Basic validation using type checking and data structure verification
   - Schema validation using the `jsonschema` library
   - Proper error handling and reporting

5. **Format Conversion**:
   - Converting between different data formats
   - Handling format-specific nuances
   - Maintaining data integrity during conversion

6. **File Operations**:
   - Reading from and writing to files
   - Using context managers (`with` statements) for file handling
   - Creating directories with `os.makedirs()`

## Common Issues and Troubleshooting

1. **JSON Parsing Errors**:
   - Ensure the JSON file is properly formatted
   - Check for missing quotes, commas, or brackets
   - Use a JSON validator to verify syntax

2. **YAML Indentation Issues**:
   - YAML is sensitive to indentation
   - Ensure consistent use of spaces (not tabs)
   - Maintain proper hierarchical structure

3. **XML Structure Complexity**:
   - XML can have complex nested structures
   - Be careful with attributes vs. elements
   - Handle lists vs. single items differently

4. **Path and File Access Issues**:
   - Use relative paths or absolute paths consistently
   - Ensure read/write permissions for files
   - Handle file not found errors gracefully

5. **Data Type Mismatches**:
   - Ensure proper type conversion (string, int, bool)
   - Handle None/null values appropriately
   - Check for nested structure differences between formats

## Extension Ideas

1. Implement schema validation for all three formats
2. Create a command-line interface to process files specified by the user
3. Add support for querying data using XPath (for XML) or JSONPath
4. Implement data transformation and filtering capabilities
5. Build a unified configuration system that can read from multiple formats 