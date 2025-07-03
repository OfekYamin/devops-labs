#!/usr/bin/env python3
"""
LAB04 - File Handling in Python

Instructions:
1. Complete the code blocks below to practice file operations
2. Run the script to test your implementations
3. Check the created files to verify your operations worked correctly
"""

# TODO: 1. Read from a file
# Use a 'with' block to open 'input.txt' in read mode
# Read the content and print it with a header
with open("input.txt", "w") as file:
    file.write("This is the first line!\n")
    file.write("This is the second line!\n")

with open("input.txt", "r") as file:
    contents=file.read()
    print(contents)

# TODO: 2. Write to a new file
# Use a 'with' block to open 'output.txt' in write mode ('w')
# Write a message to the file
# Note: This will create a new file or overwrite an existing one
with open("output.txt", "w") as file:
    file.write("First line of output.")


# TODO: 3. Append to a file
# Use a 'with' block to open 'output.txt' in append mode ('a')
# Add another line of text to the file
with open("output.txt" "a") as file:
    file.write("Second line of output\n")

# TODO: 4. Handle file errors
# Use a try-except block to handle FileNotFoundError
# Try to open a file that doesn't exist
# Print an appropriate error message when the file isn't found

try:
    with 

# TODO: 5. Bonus: Read file line by line
# Open 'input.txt' and read it line by line
# Print each line with its line number
# Example output: "Line 1: This is the first line."


# TODO: 6. Extra Challenge: Work with CSV data
# If you finish early, try creating and reading a simple CSV file
# Hint: You can use the csv module, or work with it as a regular text file
#       with comma-separated values


print("\nGreat job! You've successfully practiced file handling operations.")
print("Check the output.txt file to see the results of your write operations.")
print("Run this script with: python main.py") 