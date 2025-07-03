# LAB02 - Python Basics: Loops and Conditional Logic

In this lab, you'll learn how to control the flow of your Python programs using loops and conditional statements. These control structures are fundamental for creating dynamic scripts that can make decisions and process data efficiently.

---

## 🎯 Objectives

By the end of this lab, you will:
- Master `if`, `elif`, and `else` statements for decision-making
- Create and use `for` loops to iterate through collections
- Implement `while` loops for condition-based iteration
- Combine loops with conditional logic for powerful data processing
- Work with nested loops for multi-dimensional data structures
- Learn how to avoid common pitfalls like infinite loops

---

## 🧰 Prerequisites

- Completion of LAB01 (Variables and Data Types)
- Python 3.8+ installed on your system
- Basic understanding of Python variables and data types
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB02-Loops-and-Conditions/
├── main.py                # Python script with TODOs to implement
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB02-Loops-and-Conditions/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `main.py` in your code editor and follow the TODO comments.

---

## ✍️ Your Task

Open the `main.py` file and complete all the TODOs to learn about loops and conditional statements:

1. Conditional Statements:
   - Create a variable `age` and assign it a value
   - Write an `if/elif/else` structure to print different messages based on age
   - Test your code with different age values

2. Loop Over a List:
   - Create a list of technology skills
   - Use a `for` loop to iterate through the list
   - Print each skill with a descriptive message

3. Use a While Loop:
   - Create a counter variable
   - Implement a `while` loop that runs until the counter reaches a specific value
   - Print the counter value in each iteration
   - Ensure you increment the counter to avoid an infinite loop

4. Loop with Conditional Logic:
   - Create a list of users including "admin" and other usernames
   - Use a `for` loop to iterate through the users
   - Use conditional logic to print different messages for admin vs. regular users

5. Extra Challenge - Nested Loops:
   - Create a 2D data structure (e.g., a grid using a list of lists)
   - Use nested loops to iterate through each element
   - Print each element's position and value

---

## 🧪 Validation Checklist

✅ Your conditional statements correctly evaluate different conditions  
✅ Your `for` loop successfully iterates through list items  
✅ Your `while` loop executes the correct number of times  
✅ Your conditional logic inside loops works as expected  
✅ Your nested loops correctly process multi-dimensional data  
✅ Your script runs without errors  

Run your script with:
```bash
python main.py
```

Your output should look similar to (with your own values):
```
You are an adult.
Learning: Python
Learning: Bash
Learning: Docker
Counter is: 0
Counter is: 1
Counter is: 2
Welcome, administrator!
Hello, guest!
Hello, devops!
Position (0,0) contains: 1
Position (0,1) contains: 2
...
```

---

## 📚 Control Flow Concepts

- **Conditional Statements**:
  - **`if` statement**: Executes code block when condition is `True`
  - **`elif` statement**: Provides additional conditions to check if previous conditions are `False`
  - **`else` statement**: Executes when all previous conditions are `False`
  - **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - **Logical operators**: `and`, `or`, `not`

- **For Loops**:
  - Used to iterate over a sequence (list, tuple, string, etc.)
  - Syntax: `for item in sequence:`
  - Common patterns:
    - `for i in range(n)`: Loop n times
    - `for index, value in enumerate(sequence)`: Get both index and value

- **While Loops**:
  - Executes as long as a condition remains `True`
  - Syntax: `while condition:`
  - Always include a way to change the condition to avoid infinite loops

- **Loop Control**:
  - **`break`**: Exit the loop immediately
  - **`continue`**: Skip to the next iteration
  - **`pass`**: Do nothing (placeholder)

- **Nested Loops**:
  - Loops inside other loops
  - Useful for processing multi-dimensional data
  - Each iteration of the outer loop triggers the entire inner loop

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Implement a loop that uses `break` to exit early when a condition is met
2. Create a loop that uses `continue` to skip specific iterations
3. Write a list comprehension to create a list of squares: `[x**2 for x in range(10)]`
4. Use a ternary conditional operator: `result = "yes" if condition else "no"`
5. Create a nested dictionary and iterate through its keys and values

---

## 💬 What's Next?

Next: [LAB03 - Functions and Modules](../LAB03-Functions-and-Modules/) to learn how to organize and reuse your Python code through functions and modules.

---

## 🙏 Acknowledgments

Control flow structures are the backbone of programming logic. Mastering loops and conditionals will allow you to create dynamic, responsive scripts that can make decisions and process data efficiently - essential skills for any DevOps engineer or Python developer.

Happy coding! 🔄🐍

