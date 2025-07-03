# LAB07 - Virtual Environments and Python Packaging

Understanding how to isolate project dependencies and create reusable code packages is essential for DevOps professionals. In this lab, you'll learn how to use virtual environments to manage dependencies and how to structure Python code as packages that can be shared across projects and teams.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and manage Python virtual environments with `venv`
- Install, manage, and document dependencies with `pip`
- Structure code as reusable Python packages
- Understand module imports and package hierarchies
- Generate and use `requirements.txt` files for dependency management
- Create a simple package that could be distributed to your team
- Apply Python packaging best practices in a DevOps context

---

## 🧰 Prerequisites

- Completion of LAB06 (OOP and Classes)
- Python 3.8+ installed on your system
- Basic understanding of Python modules and imports
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB07-Virtualenv-and-Packaging/
├── myproject/              # Example Python package
│   ├── __init__.py         # Package initialization file
│   └── core.py             # Core functionality module
├── main.py                 # Script that uses the package
├── requirements.txt        # Dependency documentation
├── README.md               # This file with instructions
└── solutions.md            # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB07-Virtualenv-and-Packaging/
```

2. Create a virtual environment (this isolates your project dependencies):
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. Your command prompt should now show the virtual environment is active.

---

## ✍️ Your Task

### 1. Set up your development environment

- Create and activate a virtual environment as shown above
- Install the `requests` library in your virtual environment:
```bash
pip install requests
```
- Freeze your dependencies to document them:
```bash
pip freeze > requirements.txt
```

### 2. Create a reusable Python package

- Open `myproject/core.py` and implement the `say_hello` function
- Add another utility function of your choice (e.g., for timestamp generation, data formatting)
- Open `myproject/__init__.py` and import your functions to make them available at the package level

### 3. Use your package in an application

- Open `main.py` and complete the TODOs:
  - Import functions from your package
  - Use the functions in meaningful ways
  - Make an HTTP request using the requests library you installed

### 4. Test your complete application

- Run your script to ensure everything works correctly:
```bash
python main.py
```

---

## 🧪 Validation Checklist

✅ Virtual environment is created and activated  
✅ Dependencies are installed and documented in requirements.txt  
✅ Package structure includes a proper __init__.py file  
✅ Core module contains implemented functions with proper docstrings  
✅ Main script successfully imports and uses the package  
✅ Main script demonstrates using an external dependency (requests)  
✅ Script runs without errors and produces expected output  

---

## 📚 Virtual Environments and Packaging Concepts

- **Virtual Environments**:
  - **Purpose**: Isolate project dependencies to prevent conflicts
  - **Creation**: `python -m venv .venv`
  - **Activation**: 
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source .venv/bin/activate`
  - **Deactivation**: `deactivate`

- **Dependency Management**:
  - **Installing packages**: `pip install <package_name>`
  - **Freezing dependencies**: `pip freeze > requirements.txt`
  - **Installing from requirements**: `pip install -r requirements.txt`
  - **Version pinning**: Specify exact versions to ensure reproducibility

- **Package Structure**:
  - **`__init__.py`**: Marks a directory as a Python package
  - **Module**: Single Python file (`.py`)
  - **Package**: Directory with `__init__.py`
  - **Subpackage**: Package inside another package

- **Import System**:
  - **Absolute imports**: `from myproject.core import say_hello`
  - **Relative imports**: `from .core import say_hello`
  - **Package-level imports**: Exposing functions in `__init__.py`

- **Distribution**:
  - **`setup.py`**: Configuration for distributable packages
  - **PyPI**: Python Package Index for sharing public packages
  - **Private repositories**: For team/company-specific packages

- **DevOps Applications**:
  - Consistent environments across development, testing, and production
  - Reproducible automation scripts with exact dependency versions
  - Reusable modules for common tasks (monitoring, deployment, testing)
  - Sharing tools among team members with clear requirements

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Create a more complex package structure with subpackages for different functions
2. Add a `setup.py` file to make your package installable with pip
3. Create a command-line interface for your package using `argparse`
4. Add advanced logging to your package
5. Create a Docker container that uses your package
6. Set up a local PyPI server (like `pypiserver`) to host your package

---

## 🧹 Cleanup

After completing the lab, you can:
- Deactivate your virtual environment: `deactivate`
- Optionally remove the virtual environment directory:
  - Windows: `rmdir /s /q .venv`
  - macOS/Linux: `rm -rf .venv`

---

## 💬 What's Next?

Next: [LAB08 - Unit Testing Basics](../LAB08-Unit-Testing-Basics/) to learn how to test your code to ensure reliability and correctness - a critical skill for creating robust DevOps automation tools.

---

## 🙏 Acknowledgments

Virtual environments and packaging are fundamental concepts for professional Python development in DevOps. These skills enable you to create consistent, reproducible environments and share code effectively across teams and projects.

Happy packaging! 📦🐍

