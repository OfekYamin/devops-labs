# LAB01 - Python Basics: Variables and Data Types (Solutions)

This document provides the reference solutions for the LAB01 on Python basics and variables. Please attempt to solve the lab on your own before consulting these solutions.

## Solution for `main.py`

```python
#!/usr/bin/env python3
"""
LAB01 - Python Basics: Variables and Data Types

Instructions:
1. Follow the comments below to create variables and print them
2. Run the script to see your results
3. Try experimenting with different values
"""

# TODO: 1. Create variables of different types
# Create a string variable called 'name'
name = "DevOps Learner"

# Create an integer variable called 'age'
age = 25

# Create a float variable called 'height'
height = 1.75

# Create a boolean variable called 'is_hungry'
is_hungry = True

# Create a list variable called 'skills' with at least 3 skills
skills = ["Python", "Git", "Linux"]

# Create a dictionary variable called 'profile' that includes name, age, and skills
profile = {
    "name": name,
    "age": age,
    "skills": skills
}

# TODO: 2. Print the variables using print()
# Print each variable with a descriptive label
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hungry:", is_hungry)
print("Skills:", skills)
print("Profile Dictionary:", profile)

# TODO: 3. Try basic operations
# Print your age in 5 years
print("Age in 5 years:", age + 5)

# Print the number of skills you have
print("Number of skills:", len(skills))

# Print your first skill from the list
print("First skill:", skills[0])

# BONUS: Try additional operations if you finish early
# Try string methods like .upper() or .lower()
print("Name in uppercase:", name.upper())
print("Name in lowercase:", name.lower())

# Try adding a new skill to your list with .append()
skills.append("Docker")
print("Updated skills list:", skills)

# Try adding a new key-value pair to your dictionary
profile["height"] = height
print("Updated profile dictionary:", profile)

print("\nOnce you're done, run this file with: python main.py")
print("Check your output against the validation checklist in the README.md")
```

## Expected Output

When you run this script, you should see output similar to:

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
Name in uppercase: DEVOPS LEARNER
Name in lowercase: devops learner
Updated skills list: ['Python', 'Git', 'Linux', 'Docker']
Updated profile dictionary: {'name': 'DevOps Learner', 'age': 25, 'skills': ['Python', 'Git', 'Linux', 'Docker'], 'height': 1.75}

Once you're done, run this file with: python main.py
Check your output against the validation checklist in the README.md
```

## Key Learning Points

1. **Variables and Assignment**:
   - In Python, you create variables by assigning values with the `=` operator
   - Variable names should be descriptive and follow snake_case convention
   - No need to declare variable types in advance (dynamic typing)

2. **Basic Data Types**:
   - `str` (strings): Text values enclosed in quotes - `"DevOps Learner"`
   - `int` (integers): Whole numbers - `25`
   - `float` (floating-point): Decimal numbers - `1.75`
   - `bool` (boolean): True/False values - `True`

3. **Collection Types**:
   - `list`: Ordered, mutable collections - `["Python", "Git", "Linux"]`
   - `dict` (dictionaries): Key-value pairs - `{"name": "DevOps Learner", "age": 25}`

4. **Basic Operations**:
   - Arithmetic: `+`, `-`, `*`, `/`
   - String methods: `.upper()`, `.lower()`, `.capitalize()`, etc.
   - List operations: indexing with `[]`, `.append()`, `.pop()`, etc.
   - Dictionary operations: key access with `[]`, adding items with assignment

5. **The `print()` Function**:
   - Displays values to the console
   - Can take multiple arguments separated by commas
   - Good for debugging and visualizing variable values

## Common Issues and Troubleshooting

1. **String Concatenation**:
   - You can't directly concatenate strings and non-string types:
     - Incorrect: `print("Age: " + age)`
     - Correct: `print("Age:", age)` or `print(f"Age: {age}")`

2. **List Indexing**:
   - Python lists are zero-indexed (start at 0)
   - `skills[0]` gets the first item, not `skills[1]`
   - Trying to access an index out of range will raise an `IndexError`

3. **Dictionary Access**:
   - Accessing a key that doesn't exist raises a `KeyError`
   - Use `profile.get("key", default_value)` to safely access keys

4. **Variable Naming**:
   - Variable names can't start with numbers
   - Variable names are case-sensitive (`name` and `Name` are different)
   - Avoid using Python reserved keywords as variable names (e.g., `list`, `dict`, `print`) 