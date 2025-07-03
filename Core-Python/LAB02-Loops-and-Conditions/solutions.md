# LAB02 - Python Basics: Loops and Conditional Logic (Solutions)

This document provides the reference solutions for LAB02 on Python loops and conditional logic. Please attempt to solve the lab on your own before consulting these solutions.

## Solution for `main.py`

```python
#!/usr/bin/env python3
"""
LAB02 - Python Basics: Loops and Conditional Logic

Instructions:
1. Complete each of the exercises below
2. Add your own code where indicated by the TODO comments
3. Run the script to test your implementations
"""

# TODO: 1. Conditional Statements
# Create a variable 'age' and write conditional logic to print 
# different messages based on the age value
# - If age is 18 or older: "You are an adult."
# - If age is between 13-17: "You are a teenager."
# - Otherwise: "You are a child."

age = 20
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# TODO: 2. Loop Over a List
# Create a list called 'skills' with at least 3 technology skills
# Use a for loop to iterate over the list and print each skill
# Example output: "Learning: Python"

skills = ["Python", "Bash", "Docker"]
for skill in skills:
    print("Learning:", skill)


# TODO: 3. Use a While Loop
# Create a counter variable
# Write a while loop that prints the counter value until it reaches 3
# Don't forget to increment the counter inside the loop!

counter = 0
while counter < 3:
    print("Counter is:", counter)
    counter += 1


# TODO: 4. Bonus: Loop with Conditional Logic
# Create a list of 'users' including at least "admin", "guest", and one other username
# Loop through the users and print a different greeting message for "admin" vs other users

users = ["admin", "guest", "devops"]
for user in users:
    if user == "admin":
        print("Welcome, administrator!")
    else:
        print(f"Hello, {user}!")


# TODO: 5. Extra Challenge: Nested Loops
# Create a small 2D structure (e.g., a 3x3 grid using a list of lists)
# Use nested loops to iterate through each element and print its position and value

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index, row in enumerate(grid):
    for col_index, value in enumerate(row):
        print(f"Position ({row_index},{col_index}) contains: {value}")


print("\nGreat job! You've successfully worked with loops and conditionals.")
print("Run this script with: python main.py")
print("Check your implementation against the validation checklist in the README.md")
```

## Expected Output

When you run this script, you should see output similar to:

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
Position (0,2) contains: 3
Position (1,0) contains: 4
Position (1,1) contains: 5
Position (1,2) contains: 6
Position (2,0) contains: 7
Position (2,1) contains: 8
Position (2,2) contains: 9

Great job! You've successfully worked with loops and conditionals.
Run this script with: python main.py
Check your implementation against the validation checklist in the README.md
```

## Key Learning Points

1. **Conditional Logic**:
   - **`if` statements**: Execute code only if a condition is true
   - **`elif` statements**: Provide alternative conditions to check
   - **`else` statements**: Execute when no previous condition is met
   - Comparison operators: `==`, `!=`, `>`, `>=`, `<`, `<=`
   - Logical operators: `and`, `or`, `not`

2. **For Loops**:
   - Iterate over elements in a sequence (like lists, strings, dictionaries)
   - Syntax: `for item in collection:`
   - Useful with `range()` function: `for i in range(5):`
   - Access both index and value with `enumerate()`: `for index, value in enumerate(collection):`

3. **While Loops**:
   - Continue execution as long as a condition remains true
   - Syntax: `while condition:`
   - Always ensure the condition will eventually become false (to avoid infinite loops)
   - Common patterns: counters, input validation loops, waiting loops

4. **Nested Loops**:
   - Placing one loop inside another loop
   - Useful for working with multi-dimensional data structures
   - Each iteration of the outer loop triggers a complete execution of the inner loop
   - Performance consideration: nested loops multiply the number of iterations

5. **Control Flow Keywords**:
   - `break`: Exit a loop immediately
   - `continue`: Skip to the next iteration
   - `pass`: Do nothing (placeholder)

## Common Issues and Troubleshooting

1. **Infinite Loops**:
   - **Problem**: While loop never terminates because the condition is always true
   - **Solution**: Always ensure something inside the loop changes the condition to eventually become false
   - **Example**: Forgetting to increment a counter - `counter += 1`

2. **Indentation Errors**:
   - **Problem**: Python uses indentation to define code blocks; incorrect indentation causes errors
   - **Solution**: Use consistent indentation (4 spaces per level is standard)
   - **Example**: All code inside an `if` statement must be indented at the same level

3. **Off-by-One Errors**:
   - **Problem**: Loop runs one too many or one too few times
   - **Solution**: Double-check loop conditions, especially when using `<` vs `<=`
   - **Example**: `range(3)` gives `0, 1, 2` not `1, 2, 3`

4. **Condition Always True/False**:
   - **Problem**: Condition never changes state due to logic error
   - **Solution**: Verify your logical expressions, especially when using compound conditions
   - **Example**: Using assignment `=` instead of comparison `==` in a condition

5. **String vs. Integer Comparison**:
   - **Problem**: Comparing different data types can lead to unexpected results
   - **Solution**: Ensure variables are the expected type before comparison
   - **Example**: Comparing a string input `"18"` with numeric value `18` using `==`

## Advanced Techniques to Explore

1. **List Comprehensions**: Compact way to create lists based on existing lists
   ```python
   squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
   ```

2. **Conditional List Comprehensions**: Filtering items in a list comprehension
   ```python
   even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
   ```

3. **Ternary Conditional Operator**: Compact way to write simple if-else statements
   ```python
   status = "adult" if age >= 18 else "minor"
   ```

4. **Loop with `else` Clause**: Executes when loop completes normally (not via `break`)
   ```python
   for item in collection:
       if condition:
           break
   else:
       # This runs if the loop completes without a break
   ``` 