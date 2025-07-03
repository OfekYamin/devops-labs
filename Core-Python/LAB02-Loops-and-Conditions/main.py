#!/usr/bin/env python3
"""
LAB02 - Python Basics: Loops and Conditional Logic

Instructions:
1. Complete each of the exercises below
2. Add your own code where indicated by the TODO comments
3. Run the script to test your implementations
"""



# age = 18
# if age >= 18:
#     print("You are an adult.")
# elif age >= 13:
#     print("You are a teenager.")
# else:
#     print("You are a child.")



# TODO: 2. Loop Over a List
# Create a list called 'skills' with at least 3 technology skills
# Use a for loop to iterate over the list and print each skill
# Example output: "Learning: Python"

# skills = ["Typing" ,"Coding","Gaming"]
# for skill in skills:
#     print("Learning:", skill)
    

# skills = ["Python", "Bash", "Docker"]
# for skill in skills:
#     print("Learning:", skill)

# TODO: 3. Use a While Loop
# Create a counter variable
# Write a while loop that prints the counter value until it reaches 3
# Don't forget to increment the counter inside the loop!

# counter = 0
# while counter < 3:
#     print("Counter is:", counter)
#     counter += 1

# TODO: 4. Bonus: Loop with Conditional Logic
# Create a list of 'users' including at least "admin", "guest", and one other username
# Loop through the users and print a different greeting message for "admin" vs other users

# users=("admin","guest","ofek")
# for user in users:
#   if user == "admin":
#         print("Hello, Admin!")
# else:
#         print(f"Hello {user}!")


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