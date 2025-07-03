# LAB05 - API Integration Tool with Python

APIs (Application Programming Interfaces) are fundamental to modern DevOps. In this lab, you'll create a Python tool that interacts with a public REST API, processes the data, and performs actions based on the results - an essential skill for DevOps automation.

---

## 🎯 Objectives

By the end of this lab, you will:
- Make HTTP requests to REST APIs using the `requests` library
- Create a reusable API client class with proper error handling
- Parse and work with JSON responses
- Handle API authentication, retries, and error responses
- Implement a modular and maintainable design pattern

---

## 🧰 Prerequisites

- Completion of LAB04 (System Monitoring Scripts)
- Python 3.8+ installed
- Basic understanding of HTTP and REST APIs

---

## 📁 Lab Files

```
Automation-Scripting/LAB05-API-Integration-Tool/
├── api_client.py         # Skeleton file with TODOs for you to implement
├── config.py             # Configuration file with TODOs to complete
├── requirements.txt      # Required dependencies
├── README.md             # This file with instructions
└── solutions.md          # Reference solutions (only check after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB05-API-Integration-Tool/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Open and explore the provided files:
   - `config.py` contains configuration settings to complete
   - `api_client.py` has TODOs for implementing your API client

---

## ✍️ Your Task

You need to implement an API integration tool that:

1. Uses a configuration file (`config.py`) to store API settings:
   - Base URL, timeout, and other parameters
   - (Optional) Authentication details if needed

2. Creates a reusable API client class (`api_client.py`) that:
   - Makes HTTP requests to different API endpoints
   - Handles response processing and error handling
   - Implements retry logic for failed requests
   - Returns parsed JSON data in a usable format

3. Demonstrates the API client by:
   - Fetching and displaying user data from the API
   - Handling potential errors gracefully
   - (Bonus) Implementing multiple endpoint methods

For this lab, we'll use the free JSONPlaceholder API (https://jsonplaceholder.typicode.com) which provides test endpoints for users, posts, and other resources.

The skeleton code with TODOs is provided in the Python files. Follow the TODOs to complete the implementation.

### API Endpoints to Implement:

Some example endpoints to implement in your client:
- GET `/users` - Retrieve all users
- GET `/users/{id}` - Retrieve a specific user
- GET `/posts` - Retrieve all posts
- GET `/posts?userId={id}` - Retrieve posts for a specific user

---

## 🧪 Validation Checklist

✅ Configuration is properly set up in config.py  
✅ API client successfully connects to the JSONPlaceholder API  
✅ Client handles errors appropriately (timeouts, HTTP errors, etc.)  
✅ JSON responses are properly parsed and processed  
✅ Code follows good practices (comments, error handling, typing)  
✅ (Bonus) Implements retry logic for failed requests  
✅ (Bonus) Supports multiple API endpoints  

---

## 🧹 Cleanup
No cleanup required, all operations are read-only.

---

## 💬 What's Next?
Proceed to [LAB06 - Task Scheduler Automation](../LAB06-Task-Scheduler-Automation/) to learn how to schedule and automate recurring tasks with Python.

---

## 🙏 Acknowledgments
API integration is a cornerstone skill for DevOps engineers—whether connecting to monitoring services, CI/CD pipelines, or cloud providers. This pattern of separating configuration from implementation also teaches good software design practices.

Happy integrating! 🔌🐍 