# LAB10 - API Interaction and REST

Modern DevOps revolves around APIs for infrastructure management, monitoring, and automation. This lab teaches you how to interact with RESTful APIs using Python - skills crucial for integrating with cloud services, monitoring systems, and DevOps tools.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand REST API concepts and HTTP methods
- Use the `requests` library for API interactions
- Handle authentication (API keys, OAuth, tokens)
- Process JSON responses and handle errors
- Work with common status codes and headers
- Build robust error handling for API calls
- Create simple API wrappers and clients
- Document API usage with examples

---

## 🧰 Prerequisites

- Completion of LAB09 (Data Formats)
- Python 3.8+ installed on your system
- Basic understanding of HTTP and web concepts
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB10-API-Interaction/
├── main.py                # Main script with TODOs to implement
├── config.json            # Configuration for API endpoints and credentials
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB10-API-Interaction/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install requests
```

4. Explore the configuration file:
```bash
cat config.json
```

5. Open `main.py` and follow the TODOs to implement API interaction.

---

## ✍️ Your Task

You need to implement several functions in `main.py` to interact with a REST API:

1. **Load Configuration**:
   - Read and parse the `config.json` file
   - Extract API endpoint, authentication details, and other settings

2. **Create API Client**:
   - Initialize a client with proper configuration
   - Set up default headers, timeouts, and other request parameters

3. **Perform GET Requests**:
   - Retrieve data from API endpoints
   - Handle query parameters
   - Process JSON responses

4. **Perform POST Requests**:
   - Send data to API endpoints
   - Format request data properly
   - Handle and validate responses

5. **Handle API Errors**:
   - Implement error handling for different HTTP status codes
   - Extract error messages from responses
   - Create informative error reports

6. **Bonus Challenges**:
   - Implement PUT and DELETE methods
   - Add retry logic for failed requests
   - Create a class-based API client

For this lab, we'll use the free JSONPlaceholder API (https://jsonplaceholder.typicode.com) which provides test endpoints for users, posts, and other resources.

Follow the TODOs and function docstrings in `main.py` for detailed implementation guidance.

---

## 🧪 Validation Checklist

✅ Successfully loads configuration from JSON file  
✅ Creates an API client with proper settings  
✅ Performs GET requests and processes responses  
✅ Performs POST requests with correct data formatting  
✅ Handles API errors and different status codes gracefully  
✅ Properly displays API data in a readable format  
✅ (Bonus) Implements additional HTTP methods  
✅ (Bonus) Adds retry logic for failed requests  

---

## 🧹 Cleanup

No special cleanup is required for this lab.

---

## 💬 What's Next?

Next: [LAB11 - CLI Development](../LAB11-CLI-Development/) to learn how to build professional command-line interfaces for your Python tools - an essential skill for creating usable DevOps utilities. 