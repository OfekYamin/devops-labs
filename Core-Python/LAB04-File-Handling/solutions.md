# LAB04 - File Handling in Python Solutions

This document provides solutions to the File Handling lab. Use it as a reference only after attempting to solve the exercises yourself.

## Solution Implementation

Below you'll find the complete solution for the `main.py` file with all tasks implemented.

```python
#!/usr/bin/env python3
"""
LAB04 - File Handling in Python

Instructions:
1. Complete the code blocks below to practice file operations
2. Run the script to test your implementations
3. Check the created files to verify your operations worked correctly
"""

# Task 1: Read from a file
# Use a 'with' block to open 'input.txt' in read mode
# Read the content and print it with a header
print("\n--- Reading from input.txt ---")
with open("input.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Task 2: Write to a new file
# Use a 'with' block to open 'output.txt' in write mode ('w')
# Write a message to the file
# Note: This will create a new file or overwrite an existing one
print("\n--- Writing to output.txt ---")
with open("output.txt", "w") as file:
    file.write("This is a new file created by Python!\n")
    file.write("Learning file handling is essential for automation tasks.\n")
print("Successfully wrote to output.txt")

# Task 3: Append to a file
# Use a 'with' block to open 'output.txt' in append mode ('a')
# Add another line of text to the file
print("\n--- Appending to output.txt ---")
with open("output.txt", "a") as file:
    file.write("This line was appended to the existing file.\n")
    file.write("The 'a' mode preserves existing content and adds new content at the end.\n")
print("Successfully appended to output.txt")

# Task 4: Handle file errors
# Use a try-except block to handle FileNotFoundError
# Try to open a file that doesn't exist
# Print an appropriate error message when the file isn't found
print("\n--- Handling file errors ---")
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file 'missing.txt' was not found.")
    print("This is how we can gracefully handle missing files.")

# Task 5: Bonus: Read file line by line
# Open 'input.txt' and read it line by line
# Print each line with its line number
print("\n--- Reading input.txt line by line ---")
with open("input.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")

# Task 6: Extra Challenge: Work with CSV data
# If you finish early, try creating and reading a simple CSV file
print("\n--- Working with CSV data ---")
# First, create a simple CSV file
with open("data.csv", "w") as file:
    file.write("Name,Age,Role\n")
    file.write("Alice,28,DevOps Engineer\n")
    file.write("Bob,34,System Administrator\n")
    file.write("Charlie,31,Cloud Architect\n")
print("Created data.csv file")

# Now read and display the CSV data
print("\nReading CSV data:")
with open("data.csv", "r") as file:
    header = file.readline().strip().split(',')
    print(f"CSV Headers: {header}")
    print("\nData:")
    for line in file:
        data = line.strip().split(',')
        print(f"  - {data[0]} is {data[1]} years old and works as a {data[2]}")

# Optional: Using the csv module for more robust handling
print("\nReading CSV with the csv module:")
import csv
with open("data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"  - {row['Name']} is {row['Age']} years old and works as a {row['Role']}")

print("\nGreat job! You've successfully practiced file handling operations.")
print("Check the output.txt and data.csv files to see the results of your write operations.")
print("Run this script with: python main.py")
```

## Key Learning Points

1. **Opening Files**: Use the `open()` function with different modes:
   - `"r"` for reading (default)
   - `"w"` for writing (creates new file or overwrites existing)
   - `"a"` for appending (adds to existing file)
   - `"r+"` for reading and writing

2. **Using `with` Blocks**: Always use `with` blocks when working with files to ensure proper file closing, even if exceptions occur.

3. **Reading Methods**:
   - `file.read()` - reads entire file content
   - `file.readline()` - reads one line at a time
   - `file.readlines()` - reads all lines into a list
   - Iterating directly over the file object reads line by line

4. **Error Handling**: Always handle potential file errors, especially `FileNotFoundError`, with appropriate try-except blocks.

5. **CSV Processing**: Simple CSV files can be processed using string methods like `split(',')`, but the `csv` module offers more robust handling for complex cases.

## Common Issues and Troubleshooting

1. **File Not Found Errors**: Always verify file paths, especially when working with relative paths.

2. **File Not Closing**: Use `with` blocks to ensure files are properly closed, even when exceptions occur.

3. **Encoding Issues**: When dealing with non-ASCII text, specify the encoding:
   ```python
   with open("file.txt", "r", encoding="utf-8") as file:
       content = file.read()
   ```

4. **File Modes Confusion**:
   - `"w"` will overwrite existing files
   - Use `"a"` to preserve content and add new data
   - Use `"x"` for exclusive creation (fails if file exists)

5. **Reading Binary Files**: Use `"rb"`, `"wb"`, etc. for binary files like images or executables.

## Cleanup

To clean up after this lab:
```python
import os

# Remove files created during the lab
for filename in ["output.txt", "data.csv"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Removed {filename}")
``` 