# LAB12 - Asynchronous Programming

Modern DevOps automation often requires handling multiple operations concurrently. This lab teaches you asynchronous programming with Python's `asyncio` - essential for building high-performance monitoring tools, service orchestrators, and responsive automation systems.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand asynchronous programming concepts
- Use Python's `asyncio` library for concurrent operations
- Write code with async/await syntax
- Manage multiple concurrent tasks
- Handle errors in asynchronous code
- Work with asynchronous queues and events
- Implement timeouts and cancellations
- Apply best practices for async programming in DevOps contexts
- Measure and optimize async code performance

---

## 🧰 Prerequisites

- Completion of LAB11 (CLI Development)
- Python 3.8+ installed on your system
- Solid understanding of Python functions and error handling
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB12-Async-Programming/
├── main.py                # Main script with TODOs to implement
├── helpers/               # Helper modules for async operations
│   ├── __init__.py
│   └── async_utils.py     # Async utility functions
├── README.md              # This file with instructions
├── requirements.txt       # Required dependencies
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB12-Async-Programming/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Explore the project structure to understand the code organization:
```bash
ls -la helpers/
```

5. Open `main.py` and follow the TODOs to implement the asynchronous programming examples.

---

## ✍️ Your Task

You need to implement several components to learn asynchronous programming:

1. **Basic Async Functions (`demo_simple_tasks`)**:
   - Create simple async functions with `async def`
   - Run multiple tasks concurrently with `asyncio.gather`
   - Compare sequential vs concurrent execution times
   - Understand coroutines and task scheduling

2. **Async Web Requests (`demo_web_requests`)**:
   - Use `aiohttp` for asynchronous HTTP requests
   - Implement the `fetch_url` utility in `async_utils.py`
   - Fetch multiple URLs concurrently
   - Process responses asynchronously

3. **Error Handling (`demo_error_handling`)**:
   - Implement proper exception handling in async code
   - Create the `retry_async` utility in `async_utils.py`
   - Understand how exceptions propagate in async code
   - Apply retry patterns with exponential backoff

4. **Timeouts and Cancellation (`demo_timeouts_and_cancellation`)**:
   - Implement the `timeout_after` utility in `async_utils.py`
   - Apply timeouts to async operations
   - Cancel tasks and handle cancellation
   - Clean up resources properly when tasks are cancelled

5. **Async Patterns (`demo_async_patterns`)**:
   - Use `asyncio.Semaphore` for concurrency control
   - Implement the `run_tasks` utility in `async_utils.py`
   - Work with `asyncio.Queue` for producer-consumer patterns
   - Apply rate limiting to async operations

Throughout the lab, you'll learn how to structure asynchronous code, manage resources, and avoid common pitfalls like race conditions and deadlocks.

Follow the TODOs and function docstrings in each file for detailed implementation guidance.

---

## 🧪 Validation Checklist

✅ All demo functions are implemented and working correctly  
✅ Concurrent operations show performance improvement over sequential operations  
✅ Error handling properly catches and manages exceptions  
✅ Timeouts prevent operations from hanging indefinitely  
✅ Async utilities in `async_utils.py` are fully implemented  
✅ Code follows best practices for async programming  
✅ Race conditions and deadlocks are avoided  
✅ Resources are properly managed and cleaned up  

---

## 🧹 Cleanup

No special cleanup is required for this lab.

---

## 💬 What's Next?

Congratulations on completing the Core Python section! Next, you can move on to the **Automation-Scripting** section to apply your Python knowledge to real-world DevOps automation scenarios. 