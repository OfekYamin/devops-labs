# LAB01 - Python Basics: Variables and Data Types

Welcome to your first Python lab! In this beginner-friendly exercise, you'll explore how to define variables and work with basic data types in Python. This is the foundation for all Python programming and DevOps automation you'll build in the future.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand what variables are and how to use them in Python
- Learn the most common Python data types: `int`, `float`, `str`, `bool`, `list`, and `dict`
- Write and run your first Python script
- Practice using the `print()` function for displaying information
- Explore basic operations with different data types
- Learn how to access elements in lists and dictionaries

---

## 🧰 Prerequisites

- Python 3.8+ installed on your system
- Basic understanding of the command-line interface
- A code editor (Visual Studio Code, PyCharm, etc.)
- No previous Python experience required!

---

## 📁 Lab Files

```
Core-Python/LAB01-Basics-Variables/
├── main.py                # Python script with TODOs to implement
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB01-Basics-Variables/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `main.py` in your code editor and follow the TODO comments.

---

## ✍️ Your Task

Open the `main.py` file and complete all the TODOs to learn about Python variables and data types:

1. Create variables of different types:
   - Create a string variable `name` with your name
   - Create an integer variable `age` with a number
   - Create a float variable `height` with a decimal number
   - Create a boolean variable `is_hungry` 
   - Create a list variable `skills` with at least 3 items
   - Create a dictionary variable `profile` containing name, age, and skills

2. Print the variables using the `print()` function:
   - Add descriptive labels to each printed variable
   - Ensure proper formatting for readability

3. Perform basic operations:
   - Calculate and print your age in 5 years
   - Use `len()` to count the number of skills
   - Access and print the first element of your skills list

4. Bonus tasks:
   - Use string methods like `.upper()` or `.lower()`
   - Add a new skill to your list with `.append()`
   - Add a new key-value pair to your dictionary

---

## 🧪 Validation Checklist

✅ You've created variables using different Python data types  
✅ You've printed all variables with descriptive labels  
✅ You've performed basic operations on the variables  
✅ Your script runs without errors  
✅ The output matches the expected format  

Run your script with:
```bash
python main.py
```

Your output should look similar to (with your own values):
```
Name: DevOps Learner
Age: 25
Height: 1.75
Hungry: True
Skills: ['Python', 'Git', 'Linux']
Profile Dictionary: {'name': 'DevOps Learner', 'age': 25, 'skills': ['Python', 'Git', 'Linux']}
Age in 5 years: 30
Number of skills: 3
First skill: Python
```

---

## 📚 Python Basics Concepts

- **Variables**: Named storage locations in memory
  - Created with the assignment operator `=`
  - No explicit declaration or type specification needed
  - Should use descriptive names following snake_case convention

- **Data Types**:
  - **Strings** (`str`): Text enclosed in quotes - `"Hello"` or `'World'`
  - **Integers** (`int`): Whole numbers without decimals - `42`
  - **Floats** (`float`): Decimal numbers - `3.14`
  - **Booleans** (`bool`): `True` or `False` values
  - **Lists**: Ordered, mutable collections - `[1, 2, 3]`
  - **Dictionaries**: Key-value pairs - `{"name": "John", "age": 30}`

- **Common Operations**:
  - Arithmetic: `+`, `-`, `*`, `/`, `//` (integer division), `%` (modulo)
  - Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - String methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, etc.
  - List methods: `.append()`, `.pop()`, `.sort()`, `.reverse()`, etc.
  - Dictionary methods: `.get()`, `.keys()`, `.values()`, `.items()`, etc.

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Create a complex data structure (e.g., a list of dictionaries)
2. Use string formatting with f-strings: `f"Hello, {name}!"`
3. Try the `input()` function to get user input
4. Learn about type conversion: `int()`, `str()`, `float()`, etc.
5. Use the `type()` function to check the type of your variables

---

## 💬 What's Next?

Next: [LAB02 - Loops and Conditions](../LAB02-Loops-and-Conditions/) to learn how to control the flow of your Python programs with loops and conditional statements.

---

## 🙏 Acknowledgments

Understanding variables and data types is the foundation of Python programming. These concepts will be used in every Python script you write as a DevOps engineer, whether you're automating cloud infrastructure, processing data, or building monitoring tools.

Happy coding! 🐍

