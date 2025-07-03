# LAB06 - Object-Oriented Programming (OOP) in Python - Solutions

This file contains the solutions for LAB06. Please attempt to solve the exercises yourself before referring to this solution.

## Complete Implementation of `main.py`

```python
#!/usr/bin/env python3
"""
LAB06 - Object-Oriented Programming (OOP) in Python

Instructions:
1. Complete the code blocks below to implement classes and objects
2. Run the script to see how objects interact
3. Add your own methods and attributes to extend functionality
"""

# Task 1: Create a Server class
class Server:
    # Class variable (shared across all instances)
    total_servers = 0
    
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self._status = "offline"  # Protected attribute for property demonstration
        Server.total_servers += 1  # Increment the counter
    
    def ping(self):
        print(f"Pinging server {self.name} at {self.ip}...")
        return True
    
    @property
    def status(self):
        """Getter for the status property"""
        return self._status
    
    @status.setter
    def status(self, new_status):
        """Setter for the status property with validation"""
        if new_status in ["online", "offline", "maintenance"]:
            self._status = new_status
        else:
            raise ValueError("Status must be 'online', 'offline', or 'maintenance'")
    
    @staticmethod
    def validate_ip(ip):
        """Static method to validate IP address format"""
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False


# Task 2: Instantiate a Server object
web_server = Server("web01", "192.168.1.10")
web_server.ping()
web_server.status = "online"  # Use the setter
print(f"Server status: {web_server.status}")  # Use the getter


# Task 3: Create a DatabaseServer class that inherits from Server
class DatabaseServer(Server):
    def __init__(self, name, ip, engine):
        super().__init__(name, ip)  # Call parent class constructor
        self.engine = engine
    
    def backup(self):
        print(f"Backing up {self.engine} database on {self.name}")
    
    # Override the ping method from the parent class
    def ping(self):
        print(f"Pinging database server {self.name} at {self.ip} running {self.engine}...")
        return True


# Task 4: Instantiate a DatabaseServer object
db_server = DatabaseServer("db01", "192.168.1.11", "PostgreSQL")
db_server.ping()  # Calls the overridden method
db_server.backup()


# Task 5: Add more advanced OOP concepts (Bonus)
print(f"Total servers created: {Server.total_servers}")  # Access class variable

# Validate an IP address using the static method
print(f"Is 192.168.1.1 a valid IP? {Server.validate_ip('192.168.1.1')}")
print(f"Is 256.0.0.1 a valid IP? {Server.validate_ip('256.0.0.1')}")


# Task 6: Extra Challenge: Create another derived class
class WebServer(Server):
    def __init__(self, name, ip, web_server_type):
        super().__init__(name, ip)
        self.web_server_type = web_server_type
    
    def deploy(self, app_name):
        print(f"Deploying {app_name} to {self.web_server_type} on {self.name}")
    
    def restart(self):
        print(f"Restarting {self.web_server_type} web server on {self.name}")


# Demonstrating polymorphism
nginx_server = WebServer("web02", "192.168.1.12", "Nginx")
nginx_server.deploy("e-commerce app")
nginx_server.restart()

# Create a list of different server types and call common methods
servers = [web_server, db_server, nginx_server]
print("\nDemonstrating polymorphism by pinging all servers:")
for server in servers:
    server.ping()  # Calls the appropriate ping method based on the object type

print("\nGreat job! You've successfully worked with OOP concepts in Python.")
print("You've created classes, instantiated objects, and implemented inheritance.")
print("Run this script with: python main.py")
```

## Key Learning Points

1. **Classes and Objects**
   - Classes are blueprints for creating objects
   - Objects are instances of classes with specific attributes and behaviors
   - The `__init__` method initializes new objects with specific attributes

2. **Inheritance**
   - Classes can inherit attributes and methods from parent classes
   - The `super().__init__()` call passes initialization to the parent class
   - Child classes can override parent methods to customize behavior

3. **Properties and Encapsulation**
   - Properties allow controlled access to attributes with getters and setters
   - Encapsulation helps protect data from unintended modifications
   - Protected attributes are conventionally prefixed with an underscore `_`

4. **Class Variables and Static Methods**
   - Class variables are shared across all instances of a class
   - Static methods belong to the class, not the instance, and don't access instance data
   - Static methods are defined using the `@staticmethod` decorator

5. **Polymorphism**
   - Objects of different classes can be treated as objects of a common parent class
   - Methods with the same name behave differently depending on the object type
   - Enables flexible code that works with multiple object types

## Common Issues and Troubleshooting

1. **Forgetting `self` parameter**
   - Class methods must include `self` as the first parameter
   - `self` refers to the instance and is used to access instance attributes

2. **Inheritance issues**
   - Not calling the parent class constructor with `super().__init__()`
   - Forgetting to pass required parameters to the parent constructor

3. **Property access issues**
   - Accessing protected attributes directly instead of using getters/setters
   - Forgetting to implement validation in property setters

4. **Method override problems**
   - Not maintaining the same method signature when overriding methods
   - Not calling the parent method when needed using `super().method_name()`

## Cleanup

No cleanup is required for this lab, as no external resources are used.

---

Remember that object-oriented programming is a powerful paradigm for organizing code, especially for larger projects. The principles you've learned here will be valuable as you build more complex DevOps tools and automation frameworks. 