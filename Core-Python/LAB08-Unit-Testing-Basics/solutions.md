# Unit Testing Basics - Solutions

This document contains complete solutions for the Unit Testing Basics lab. These solutions should be referenced only after you've attempted to complete the lab on your own.

## Solution for `main.py`

```python
#!/usr/bin/env python3
"""
This module contains functions for unit testing basics.
It demonstrates simple functions that can be tested with unittest.
"""

def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b

def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number: The number to check
        
    Returns:
        True if the number is even, False otherwise
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
    """
    return number % 2 == 0

def get_largest(numbers):
    """
    Get the largest number from a list of numbers.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        The largest number in the list
        
    Raises:
        ValueError: If the list is empty
    
    Example:
        >>> get_largest([1, 5, 3, 9, 2])
        9
    """
    if not numbers:
        raise ValueError("Cannot find largest in an empty list")
    return max(numbers)

def reverse_string(s):
    """
    Reverse a string.
    
    Args:
        s: The string to reverse
        
    Returns:
        The reversed string
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return s[::-1]

if __name__ == "__main__":
    # This code will only run if the script is executed directly
    print("Testing add function:", add(5, 3))
    print("Testing is_even function:", is_even(6))
    print("Testing get_largest function:", get_largest([5, 10, 3, 8]))
    print("Testing reverse_string function:", reverse_string("Python"))
```

## Solution for `test_main.py`

```python
#!/usr/bin/env python3
"""
Unit tests for the main module.
This module demonstrates how to write unit tests using the unittest framework.
"""

import unittest
from main import add, is_even, get_largest, reverse_string

class TestMain(unittest.TestCase):
    """Test case for the main module functions."""

    def test_add(self):
        """Test the add function with various inputs."""
        # Test positive numbers
        self.assertEqual(add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(add(-1, -2), -3)
        # Test mixed numbers
        self.assertEqual(add(-5, 10), 5)
        # Test zeros
        self.assertEqual(add(0, 0), 0)
        # Test with larger numbers
        self.assertEqual(add(1000, 2000), 3000)
        # Test with floating point numbers
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_is_even(self):
        """Test the is_even function."""
        # Test with even numbers
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))
        # Test with odd numbers
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-3))
        # Test with large number
        self.assertTrue(is_even(1000000))

    def test_get_largest(self):
        """Test the get_largest function."""
        # Test with positive numbers
        self.assertEqual(get_largest([1, 5, 3, 9, 2]), 9)
        # Test with negative numbers
        self.assertEqual(get_largest([-1, -5, -3, -9, -2]), -1)
        # Test with mixed numbers
        self.assertEqual(get_largest([-10, 5, 0, -3]), 5)
        # Test with a single number
        self.assertEqual(get_largest([7]), 7)
        # Test with duplicate largest values
        self.assertEqual(get_largest([5, 9, 9, 2, 3]), 9)
        # Test with floating point numbers
        self.assertEqual(get_largest([1.5, 2.5, 1.9]), 2.5)

    def test_get_largest_empty_list(self):
        """Test that get_largest raises ValueError with an empty list."""
        with self.assertRaises(ValueError):
            get_largest([])
            
    def test_reverse_string(self):
        """Test the reverse_string function."""
        # Test with a regular word
        self.assertEqual(reverse_string("hello"), "olleh")
        # Test with an empty string
        self.assertEqual(reverse_string(""), "")
        # Test with a palindrome
        self.assertEqual(reverse_string("radar"), "radar")
        # Test with a sentence
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
        # Test with numbers and special characters
        self.assertEqual(reverse_string("a1b2c3!"), "!3c2b1a")

if __name__ == "__main__":
    unittest.main()
```

## Key Learning Points

### 1. Unit Testing Fundamentals

#### What is Unit Testing?
Unit testing is a software testing technique where individual components or functions of a program are tested in isolation. The purpose is to validate that each unit of software performs as expected.

#### Benefits of Unit Testing
- **Early Bug Detection**: Catch issues early in the development process
- **Documentation**: Tests serve as documentation for how the code should work
- **Refactoring Confidence**: Makes it easier to refactor code
- **Design Improvement**: Encourages better code organization and modular design

### 2. Python's `unittest` Framework

Python's built-in `unittest` module provides a framework for organizing and running tests:

- **Test Case**: A collection of individual tests represented by methods in a class that inherits from `unittest.TestCase`
- **Test Methods**: Individual test methods must start with the word `test_`
- **Assertions**: Special methods provided by `unittest.TestCase` to check if code behaves as expected
- **Test Runner**: Discovers and executes tests, then displays the results

### 3. Assertion Methods

Important assertion methods used in the solution:

- `assertEqual(a, b)`: Verify that `a == b`
- `assertTrue(x)`: Verify that `bool(x) is True`
- `assertFalse(x)`: Verify that `bool(x) is False`
- `assertRaises(exception, callable, *args, **kwargs)`: Verify that the specified exception is raised
- `assertAlmostEqual(a, b)`: Verify that `a` and `b` are approximately equal (useful for floating point comparisons)

### 4. Test Patterns and Best Practices

#### Demonstrated in the Solution:
- **Test Edge Cases**: Empty lists, negative numbers, mixed types, etc.
- **Test Expected Exceptions**: Verifying that functions raise appropriate exceptions
- **Multiple Assertions**: Testing multiple scenarios within a single test method
- **Descriptive Test Names**: Using clear method names that describe what is being tested
- **Test Docstrings**: Including docstrings for test methods to further clarify intent

### 5. Running Tests

To run the tests:
```
python -m unittest test_main.py
```

Or to run with more detailed output:
```
python -m unittest -v test_main.py
```

Alternatively, since we included the `unittest.main()` call in the script, you can run:
```
python test_main.py
```

### 6. Common Issues in Unit Testing

#### Test Isolation
Tests should be independent of each other. The outcome of one test should not affect another.

#### Mocking
For more complex code, you may need to use mocks to replace dependencies. The built-in `unittest.mock` module can help with this.

#### Test Coverage
It's important to test all aspects of your code, including edge cases and error conditions.

## Best Practices

1. **Write Tests First**: Consider test-driven development (TDD) where you write tests before implementation
2. **Keep Tests Small**: Each test should check one specific thing
3. **Test Structure**: Follow the AAA pattern (Arrange, Act, Assert)
4. **Use Descriptive Names**: Name tests clearly to indicate what they're testing
5. **Don't Test Implementation Details**: Test the behavior, not how it's implemented
6. **Maintain Tests**: Update tests when code changes

## Advanced Topics

For more complex applications, you might explore:
- **Fixtures**: Reusable setup code for tests
- **Parameterized Tests**: Running the same test with different inputs
- **Test Coverage Analysis**: Tools like `coverage.py` to measure code coverage
- **Testing Frameworks**: Alternative frameworks like `pytest` which offer more features

Remember, effective unit testing is about finding a balance - too few tests won't catch bugs, but too many can be difficult to maintain. 