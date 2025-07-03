# LAB03 - Functions and Modules in Python

Functions and modules are essential building blocks for writing reusable, maintainable, and organized code. In this lab, you will learn how to define your own functions, organize code into separate modules, and import functionality between files - key skills for any Python developer or DevOps engineer.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and use custom Python functions
- Understand function parameters, arguments, and return values
- Add proper documentation to your functions using docstrings
- Split your code into multiple files for better organization
- Import functions from your own custom modules
- Learn when and how to use the `if __name__ == "__main__"` pattern
- Apply best practices for modular code organization

---

## 🧰 Prerequisites

- Completion of LAB02 (Loops and Conditions)
- Python 3.8+ installed on your system
- Basic understanding of Python variables, data types, and control flow
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB03-Functions-and-Modules/
├── main.py                # Script where you'll import and use functions
├── helper.py              # Module where you'll define your functions
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB03-Functions-and-Modules/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open both `helper.py` and `main.py` in your code editor and follow the TODO comments.

---

## ✍️ Your Task

This lab involves working with two files simultaneously - first defining functions in one file, then importing and using them in another.

### In `helper.py`:

1. Define a function called `greet`:
   - It should take a parameter called `name`
   - It should return a greeting string like `"Hello, {name}!"`
   - Add an appropriate docstring describing the function

2. Define a function called `add`:
   - It should take two parameters, `x` and `y`
   - It should return the sum of these values
   - Add an appropriate docstring

3. Define a function called `max_of_three`:
   - It should take three parameters: `a`, `b`, and `c`
   - It should return the maximum value of the three
   - You can use Python's built-in `max()` function
   - Add an appropriate docstring

4. Create an additional function of your choice:
   - Come up with a useful function (e.g., calculate an area, format a string)
   - Make sure it takes parameters and returns a value
   - Include a detailed docstring explaining what it does

### In `main.py`:

1. Import the functions from `helper.py`:
   - Use the `from ... import ...` syntax
   - Import all the functions you've defined

2. Call each function with appropriate arguments:
   - Use the `greet()` function with your name
   - Use the `add()` function with two numbers
   - Use the `max_of_three()` function with three values
   - Use your custom function with appropriate arguments

3. Print the results of each function call with descriptive messages

---

## 🧪 Validation Checklist

✅ All functions in `helper.py` are properly defined with parameters and return values  
✅ All functions have appropriate docstrings  
✅ The `if __name__ == "__main__"` block in `helper.py` is left intact  
✅ Functions are correctly imported in `main.py`  
✅ All functions are called with appropriate arguments in `main.py`  
✅ Results are printed with clear, descriptive messages  
✅ Both scripts run without errors  

Run your main script with:
```bash
python main.py
```

Your output should look similar to:
```
Hello, DevOps Learner!
Sum of 10 and 25 is: 35
Maximum value of 15, 23, and 7 is: 23
Area of rectangle with length 6.5 and width 3.2 is: 20.8

All tasks completed successfully! 🎉
```

---

## 📚 Functions and Modules Concepts

- **Functions**:
  - **Definition**: Reusable blocks of code that perform specific tasks
  - **Syntax**: `def function_name(parameters):`
  - **Parameters**: Variables that receive values when the function is called
  - **Return Values**: Data sent back from the function using the `return` statement
  - **Docstrings**: Documentation strings that explain what the function does

- **Modules**:
  - **Definition**: Python files containing reusable code (functions, classes, variables)
  - **Creating Modules**: Any `.py` file can be a module
  - **Importing**: Using `import module_name` or `from module_name import function_name`
  - **Namespace**: Modules create separate namespaces to avoid naming conflicts
  - **Standard Library**: Python comes with many built-in modules (e.g., `math`, `random`, `os`)

- **Best Practices**:
  - Use clear, descriptive function names (snake_case convention)
  - Each function should do one thing well
  - Include docstrings that explain parameters, return values, and behavior
  - Use the `if __name__ == "__main__":` pattern for code that should run only when the file is executed directly
  - Organize related functions into modules
  - Import only what you need

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Add default parameter values to one of your functions
2. Create a function that accepts a variable number of arguments using `*args`
3. Write a function that uses keyword arguments with `**kwargs`
4. Create a function that calls another function (composition)
5. Create a third module and import functions from both other modules
6. Explore Python's built-in modules like `math`, `random`, or `datetime`

---

## 💬 What's Next?

Next: [LAB04 - File Handling](../LAB04-File-Handling/) to learn how to read from and write to files — a key skill for processing data and creating persistent applications.

---

## 🙏 Acknowledgments

Functions and modules are fundamental to writing maintainable, scalable Python code. By organizing your code into reusable components, you're developing essential skills for creating larger applications, automation scripts, and DevOps tools. These concepts form the foundation of professional Python development.

Happy coding! 🧩🐍

