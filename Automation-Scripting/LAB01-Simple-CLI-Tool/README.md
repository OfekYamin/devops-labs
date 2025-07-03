# LAB01 - Building a Simple CLI Tool with Python

Command-line interfaces (CLIs) are essential in DevOps. In this lab, you'll create your first CLI tool using Python's built-in `argparse` module. This tool will accept user input from the terminal and perform arithmetic operations based on it.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how to use `argparse` to build command-line tools
- Accept and validate input from the user
- Build a simple calculator CLI that performs arithmetic operations
- Learn to handle errors gracefully (e.g., division by zero)

---

## 🧰 Prerequisites

- Completion of Core-Python labs
- Python 3.8+ installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB01-Simple-CLI-Tool/
├── cli_tool.py         # Skeleton file with TODOs for you to implement
├── README.md           # This file with instructions
└── solutions.md        # Reference solutions (only check after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB01-Simple-CLI-Tool/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `cli_tool.py` and follow the TODOs to implement your CLI calculator

---

## ✍️ Your Task

You need to implement a command-line calculator that:

1. Accepts two numbers as positional arguments
2. Accepts an operation flag (--op) that specifies what operation to perform
3. Supports at least these operations:
   - Addition (`add`)
   - Subtraction (`sub`)
   - Multiplication (`mul`)
   - Division (`div`)
4. Handles errors gracefully (e.g., division by zero)
5. Displays the result to the user

The skeleton code with TODOs is provided in `cli_tool.py`. Follow the TODOs to complete the implementation.

### Example Usage (after implementation):

```bash
python cli_tool.py 10 5 --op add    # Result: 15
python cli_tool.py 10 5 --op sub    # Result: 5
python cli_tool.py 10 5 --op mul    # Result: 50
python cli_tool.py 10 5 --op div    # Result: 2.0
```

---

## 🧪 Validation Checklist

✅ CLI accepts two numbers and an operation  
✅ Supports at least four operations (`add`, `sub`, `mul`, `div`)  
✅ Handles errors gracefully (e.g., division by zero)  
✅ Displays result correctly for each operation  
✅ Script runs successfully from command line  

---

## 🧹 Cleanup
No cleanup required.

---

## 💬 What's Next?
Advance to [LAB02 - Automate File Downloads](../LAB02-Automate-File-Downloads/) to write a script that interacts with the internet and saves data programmatically.

---

## 🙏 Acknowledgments
A great DevOps tool starts at the terminal. CLIs are powerful and can control anything from deployments to monitoring.

Happy scripting! 🖥🐍