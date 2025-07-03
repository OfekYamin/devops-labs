# LAB09 - Working with Data Formats in Python

Data formats like JSON, YAML, and XML are the backbone of modern DevOps configuration and infrastructure. In this lab, you'll learn how to parse, manipulate, and generate these common data formats - essential skills for working with configuration files, APIs, and infrastructure as code.

---

## 🎯 Objectives

By the end of this lab, you will:
- Work with JSON for configuration and data exchange
- Parse and generate YAML for infrastructure definitions
- Process XML data for legacy systems and APIs
- Convert data between different formats
- Validate data against basic rules
- Handle common data format errors
- Apply best practices for working with configuration data

---

## 🧰 Prerequisites

- Completion of LAB08 (Unit Testing Basics)
- Python 3.8+ installed on your system
- Basic understanding of Python dictionaries and file operations
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB09-Data-Formats/
├── main.py                # Main script with TODOs to implement
├── sample_data/           # Sample data files in different formats
│   ├── config.json        # Example JSON configuration
│   ├── servers.yaml       # Example YAML infrastructure definition
│   └── services.xml       # Example XML service definition
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB09-Data-Formats/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install pyyaml xmltodict jsonschema
```

4. Explore the sample data files in the `sample_data` directory to understand their structure.

5. Open `main.py` and follow the TODOs to implement the data processing functions.

---

## ✍️ Your Task

You need to implement several functions in `main.py` to work with different data formats:

1. **Process JSON Data**:
   - Read and parse the sample JSON configuration file
   - Extract key information like application details, database settings, and service configurations

2. **Process YAML Data**:
   - Read and parse the sample YAML infrastructure definition
   - Extract information about the infrastructure region, VPC, subnets, and servers

3. **Process XML Data**:
   - Read and parse the sample XML service definitions
   - Extract service details, endpoints, and dependencies

4. **Convert Between Formats**:
   - Implement a function to convert data between JSON, YAML, and XML formats
   - Ensure proper formatting and structure in the converted output

5. **Validate Data**:
   - Implement basic validation for the data
   - Check for required fields, proper data types, and value constraints

6. **Bonus Challenges**:
   - Save converted data to new files
   - Implement schema validation using jsonschema
   - Create a function to merge data from multiple formats

Follow the TODOs and function docstrings in `main.py` for detailed implementation guidance.

---

## 🧪 Validation Checklist

✅ Successfully reads and parses JSON, YAML, and XML files  
✅ Correctly extracts and displays key information from each format  
✅ Converts data between different formats accurately  
✅ Validates data against basic rules or schemas  
✅ Handles errors gracefully with informative messages  
✅ Code is well-organized with proper docstrings and comments  

---

## 🧹 Cleanup

No special cleanup is required for this lab.

---

## 💬 What's Next?

Next: [LAB10 - API Interaction](../LAB10-API-Interaction/) to learn how to work with RESTful APIs - a critical skill for interacting with modern DevOps tools and cloud services. 