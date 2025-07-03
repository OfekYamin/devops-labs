#!/usr/bin/env python3
"""
LAB06 - Object-Oriented Programming (OOP) in Python

This lab introduces you to object-oriented programming concepts in Python.
You'll create classes to model servers in a DevOps environment, implement
inheritance for specialized server types, and learn how OOP can make your
automation code more modular and maintainable.

Instructions:
1. Complete the code blocks below according to the TODOs
2. Run the script to see how objects interact
3. Extend the implementation with your own ideas
"""

# TODO: 1. Create a Server class
# Define a class called 'Server' with:
# - An __init__ method that takes 'name' and 'ip' parameters and stores them as attributes
# - A 'ping' method that prints a message showing the server is being pinged
#
# Example structure:
# class Server:
#     def __init__(self, name, ip):
#         # Your code here
#
#     def ping(self):
#         # Your code here


# TODO: 2. Instantiate a Server object
# Create an instance of your Server class with a name and IP address
# Call the ping method on your server instance
# Example:
# web_server = Server("web01", "192.168.1.10")
# web_server.ping()


# TODO: 3. Create a DatabaseServer class that inherits from Server
# Define a class that extends Server with:
# - An __init__ method that takes 'name', 'ip', and 'engine' parameters
# - A call to the parent class's __init__ method using super()
# - An 'engine' attribute to store the database engine type
# - A 'backup' method that prints a message about backing up the database
#
# Example structure:
# class DatabaseServer(Server):
#     def __init__(self, name, ip, engine):
#         # Your code here
#
#     def backup(self):
#         # Your code here


# TODO: 4. Instantiate a DatabaseServer object
# Create an instance of your DatabaseServer class with appropriate parameters
# Call both the ping method (inherited from Server) and the backup method
# Example:
# db_server = DatabaseServer("db01", "192.168.1.11", "PostgreSQL")
# db_server.ping()
# db_server.backup()


# TODO: 5. Add more advanced OOP concepts (Bonus)
# Try implementing some of these advanced concepts:
# - Add a class variable to Server (shared across all instances)
# - Create a static method for IP validation
# - Implement property getters and setters for a 'status' attribute
# - Override the ping method in DatabaseServer to customize its behavior
#
# Example structure for property:
# @property
# def status(self):
#     return self._status
#
# @status.setter
# def status(self, new_status):
#     # Add validation logic here


# TODO: 6. Extra Challenge: Create another derived class
# Create a WebServer class that also inherits from Server with:
# - Additional attributes like 'web_server_type' (e.g., "Nginx", "Apache")
# - Methods specific to web servers (deploy, restart, etc.)
# - Demonstrate polymorphism by creating a list of different server types
#   and calling common methods on them
#
# Example polymorphism:
# servers = [web_server, db_server, web_server2]
# for server in servers:
#     server.ping()  # Each server type will use its own implementation


# Display success message
print("\nGreat job! You've successfully worked with OOP concepts in Python.")
print("You've created classes, instantiated objects, and implemented inheritance.")
print("These skills will help you build modular DevOps automation tools.") 