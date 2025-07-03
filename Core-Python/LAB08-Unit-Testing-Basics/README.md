# LAB08 - Unit Testing Basics in Python

Writing reliable, maintainable code is essential for DevOps automation. Unit testing helps ensure your scripts work correctly and continue to function after changes. In this lab, you'll learn how to write tests using Python's built-in `unittest` framework - a critical skill for creating robust DevOps tools.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand the importance of testing in DevOps automation
- Write unit tests using Python's built-in `unittest` module
- Master common assertion methods: assertEqual, assertTrue, assertFalse, assertRaises
- Run tests from the command line
- Structure test cases for maximum effectiveness
- Test edge cases and error conditions
- Follow best practices for Python testing
- Apply TDD (Test-Driven Development) principles

---

## 🧰 Prerequisites

- Completion of LAB07 (Virtualenv and Packaging)
- Python 3.8+ installed on your system
- Basic understanding of Python functions and modules
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB08-Unit-Testing-Basics/
├── main.py                # Module with functions to test
├── test_main.py           # Unit tests for main.py
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB08-Unit-Testing-Basics/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. Open `main.py` and `test_main.py` in your code editor.

---

## ✍️ Your Task

### 1. Implement functions in main.py

Open `main.py` and implement the following functions:

- `add`: Add two numbers together
- `is_even`: Check if a number is even
- `get_largest`: Find the largest number in a list
- `reverse_string`: Reverse a string

Each function should include proper docstrings and handle edge cases appropriately.

### 2. Write unit tests in test_main.py

Open `test_main.py` and create test methods to verify your functions:

- Import the functions from main.py
- Create test methods for each function (test_add, test_is_even, etc.)
- Use appropriate assertion methods to verify correct behavior
- Test normal cases, edge cases, and error conditions
- Explore different unittest assertion methods

### 3. Run your tests

Execute the tests using the unittest module:

```bash
python -m unittest test_main.py
```

Or with more detailed output:

```bash
python -m unittest -v test_main.py
```

Alternatively, you can run the test file directly:

```bash
python test_main.py
```

---

## 🧪 Validation Checklist

✅ All required functions are implemented in main.py  
✅ Functions include proper docstrings explaining purpose, parameters, and return values  
✅ Edge cases are handled appropriately (empty lists, special inputs, etc.)  
✅ Test methods are created for each function in test_main.py  
✅ Tests use a variety of assertion methods (assertEqual, assertTrue, assertRaises, etc.)  
✅ Tests cover normal cases, edge cases, and error conditions  
✅ All tests pass when running unittest  
✅ Code follows Python best practices for testing  

---

## 📚 Unit Testing Concepts

- **Test Case Class**:
  - Inherits from `unittest.TestCase`
  - Contains test methods
  - Can include setUp and tearDown methods for test initialization/cleanup

- **Test Methods**:
  - Must start with `test_`
  - Should test a specific aspect of functionality
  - Should be independent of other tests
  - Follow the AAA pattern: Arrange, Act, Assert

- **Common Assertion Methods**:
  - `assertEqual(a, b)`: Check if a equals b
  - `assertTrue(x)`: Check if x is True
  - `assertFalse(x)`: Check if x is False
  - `assertRaises(exception, callable, *args)`: Check if function raises expected exception
  - `assertIn(a, b)`: Check if a is in b
  - `assertIsNone(x)`: Check if x is None
  - `assertAlmostEqual(a, b)`: Check if floats a and b are approximately equal

- **Test-Driven Development (TDD)**:
  - Write tests before implementing functionality
  - Red: Write a failing test
  - Green: Implement code to make the test pass
  - Refactor: Clean up the code while keeping tests passing

- **Testing in DevOps**:
  - Ensures automation scripts work as expected
  - Prevents regressions when code is modified
  - Documents expected behavior
  - Facilitates collaboration in teams
  - Critical for CI/CD pipelines
  - Reduces risk in production environments

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Add a test fixture using setUp and tearDown methods
2. Create a test for a function that interacts with files (using temporary files)
3. Use unittest.mock to mock external dependencies
4. Write parameterized tests to run the same test with different inputs
5. Explore test coverage tools (like coverage.py) to measure test coverage
6. Create a CI/CD pipeline (using GitHub Actions or similar) to run tests automatically

---

## 🧹 Cleanup

No special cleanup is required for this lab, as all files are local and no external resources are created.

If you created a virtual environment, you can deactivate it when finished:

```bash
deactivate
```

---

## 💬 What's Next?

Congratulations on completing the Core Python section! You've built a solid foundation in Python programming with a DevOps focus.

Next, move on to the **Automation-Scripting** section to apply your Python knowledge to real-world DevOps automation scenarios.

---

## 🙏 Acknowledgments

Unit testing is a fundamental skill for professional developers and DevOps engineers. The practices you've learned in this lab will help you create more reliable, maintainable automation tools and give you confidence when modifying existing code.

Happy testing! ✅🐍

