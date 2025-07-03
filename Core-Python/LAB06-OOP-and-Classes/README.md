# LAB06 - Object-Oriented Programming (OOP) in Python

Object-Oriented Programming is a powerful paradigm for organizing and structuring code in DevOps automation. In this lab, you'll learn how to use classes, objects, and inheritance to build modular, reusable, and maintainable automation tools - essential for creating scalable DevOps solutions.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand the core principles of Object-Oriented Programming (OOP)
- Create custom classes with attributes and methods
- Instantiate objects and use their functionality
- Implement inheritance to extend functionality
- Apply encapsulation principles with properties and protected attributes
- Use polymorphism to write flexible code
- Design class hierarchies for DevOps automation tasks

---

## 🧰 Prerequisites

- Completion of LAB05 (Error Handling and Logging)
- Python 3.8+ installed on your system
- Basic understanding of Python syntax, functions, and data structures
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB06-OOP-and-Classes/
├── main.py                # Python script with TODOs to implement
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB06-OOP-and-Classes/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `main.py` in your code editor and follow the TODO comments.

---

## ✍️ Your Task

Open the `main.py` file and complete all the TODOs to learn about object-oriented programming:

1. Create a Server class:
   - Define a class with an `__init__` method that takes `name` and `ip` parameters
   - Store these parameters as instance attributes
   - Implement a `ping` method that simulates pinging the server

2. Instantiate a Server object:
   - Create an instance of your Server class with a name and IP address
   - Call the ping method on your server instance

3. Create a DatabaseServer class that inherits from Server:
   - Define a class that extends Server with additional database functionality
   - Implement `__init__` method that accepts name, ip, and engine parameters
   - Call the parent class's `__init__` method using `super()`
   - Add a `backup` method specific to database servers

4. Instantiate a DatabaseServer object:
   - Create an instance of your DatabaseServer class
   - Call both the `ping` and `backup` methods to demonstrate inheritance

5. Advanced OOP concepts (Bonus):
   - Add a class variable (shared across all instances)
   - Create a static method for IP validation
   - Implement property getters and setters for controlled attribute access
   - Override a method from the parent class

6. Extra Challenge:
   - Create a WebServer class that also inherits from Server
   - Add methods specific to web servers (deploy, restart, etc.)
   - Demonstrate polymorphism by creating a list of different server types
   - Call common methods on each server type

---

## 🧪 Validation Checklist

✅ You've created a Server class with appropriate attributes and methods  
✅ You've instantiated a Server object and called its methods  
✅ You've implemented inheritance with a DatabaseServer class  
✅ Your DatabaseServer correctly extends the Server functionality  
✅ (Bonus) You've implemented at least one advanced OOP concept  
✅ (Challenge) You've created another derived class and demonstrated polymorphism  
✅ Your script runs without errors:
```bash
python main.py
```

---

## 📚 OOP Concepts for DevOps

- **Classes and Objects**:
  - **Class**: Blueprint or template defining attributes and behaviors
  - **Object**: Instance of a class with specific data and functionality
  - **Instance Attributes**: Data specific to each object (e.g., server name, IP)
  - **Methods**: Functions defined in a class that operate on objects of that class

- **Core OOP Principles**:
  - **Encapsulation**: Bundling data and methods that work on that data within one unit
  - **Inheritance**: Creating new classes that inherit attributes and methods from existing classes
  - **Polymorphism**: Different classes can be treated through the same interface
  - **Abstraction**: Hiding complex implementation details while exposing functionality

- **Special Methods**:
  - **`__init__`**: Constructor method for initializing new objects
  - **`__str__`**: Controls how the object is represented as a string
  - **`__repr__`**: Controls the official string representation of an object

- **Advanced Features**:
  - **Class Variables**: Shared by all instances of a class
  - **Static Methods**: Belong to the class rather than instances
  - **Properties**: Control access to attributes with getters and setters
  - **Method Overriding**: Changing the implementation of an inherited method

- **DevOps Applications**:
  - Server and infrastructure modeling
  - Configuration management abstractions
  - Deployment pipeline objects
  - Cloud resource representations
  - Monitoring and alerting systems

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Implement multiple inheritance with a `MonitoredDatabaseServer` class
2. Add abstract base classes and methods using the `abc` module
3. Create a class hierarchy for different cloud resources (VMs, storage, networks)
4. Implement a class decorator that adds logging to all methods
5. Use composition instead of inheritance for a different approach
6. Design a simple infrastructure-as-code system using OOP principles

---

## 💬 What's Next?

Next: [LAB07 - Virtualenv and Packaging](../LAB07-Virtualenv-and-Packaging/) to learn how to manage dependencies and package your Python code for distribution - essential skills for sharing your DevOps tools and libraries.

---

## 🙏 Acknowledgments

Object-oriented programming is a fundamental paradigm in modern software development. The skills you've learned in this lab will help you create more organized, modular, and maintainable code for your DevOps automation projects.

Happy coding! 🧱🐍

