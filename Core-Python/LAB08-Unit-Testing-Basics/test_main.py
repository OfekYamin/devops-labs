#!/usr/bin/env python3
"""
LAB08 - Unit Testing Basics in Python

This module contains unit tests for the functions in main.py.
It demonstrates how to structure test cases, use assertions,
and test different aspects of your code.
"""

import unittest
# TODO: Import the functions you'll be testing from main.py
# Example:
# from main import add, is_even, get_largest, reverse_string


class TestMain(unittest.TestCase):
    """Test case for the functions in main.py."""
    
    # TODO: Write a test method for the add function
    # The method should:
    # - Be named test_add
    # - Test multiple scenarios (positive numbers, negative numbers, zeros)
    # - Use assertEqual to verify that the function returns the expected sum
    # 
    # Example:
    # def test_add(self):
    #     """Test the add function with various inputs."""
    #     # Test positive numbers
    #     self.assertEqual(add(2, 3), 5)
    #     # Test negative numbers
    #     self.assertEqual(add(-1, -2), -3)
    #     # Test mixed numbers
    #     self.assertEqual(add(-5, 10), 5)
    #     # Test zeros
    #     self.assertEqual(add(0, 0), 0)
    
    
    # TODO: Write a test method for the is_even function
    # The method should:
    # - Be named test_is_even
    # - Test both even and odd numbers
    # - Use assertTrue for even numbers and assertFalse for odd numbers
    # - Include edge cases like zero and negative numbers
    # 
    # Example:
    # def test_is_even(self):
    #     """Test the is_even function."""
    #     # Test with even numbers
    #     self.assertTrue(is_even(2))
    #     self.assertTrue(is_even(0))
    #     self.assertTrue(is_even(-4))
    #     # Test with odd numbers
    #     self.assertFalse(is_even(1))
    #     self.assertFalse(is_even(-3))
    
    
    # TODO: Write a test method for the get_largest function
    # The method should:
    # - Be named test_get_largest
    # - Test with various list inputs
    # - Use assertEqual to verify the function returns the largest number
    # - Include tests for negative numbers, duplicates, and single-element lists
    # 
    # Example:
    # def test_get_largest(self):
    #     """Test the get_largest function."""
    #     # Test with positive numbers
    #     self.assertEqual(get_largest([1, 5, 3]), 5)
    #     # Test with negative numbers
    #     self.assertEqual(get_largest([-1, -5, -3]), -1)
    #     # Test with mixed numbers
    #     self.assertEqual(get_largest([-10, 5, 0]), 5)
    #     # Test with a single element
    #     self.assertEqual(get_largest([7]), 7)
    
    
    # TODO: Write a test method for the get_largest function with empty list
    # The method should:
    # - Be named test_get_largest_empty_list
    # - Use assertRaises to verify that an empty list raises ValueError
    # 
    # Example:
    # def test_get_largest_empty_list(self):
    #     """Test that get_largest raises ValueError with an empty list."""
    #     with self.assertRaises(ValueError):
    #         get_largest([])
    
    
    # TODO: Write a test method for the reverse_string function
    # The method should:
    # - Be named test_reverse_string
    # - Test with various string inputs
    # - Use assertEqual to verify the function returns the reversed string
    # - Include tests for empty strings, single characters, and palindromes
    # 
    # Example:
    # def test_reverse_string(self):
    #     """Test the reverse_string function."""
    #     # Test with a regular word
    #     self.assertEqual(reverse_string("hello"), "olleh")
    #     # Test with an empty string
    #     self.assertEqual(reverse_string(""), "")
    #     # Test with a palindrome
    #     self.assertEqual(reverse_string("radar"), "radar")
    #     # Test with a sentence
    #     self.assertEqual(reverse_string("Hello World"), "dlroW olleH")
    
    
    # BONUS: Explore other assertion methods
    # Try using different assertion methods like:
    # - assertIn: Check if an item is in a container
    # - assertIsNone: Check if something is None
    # - assertAlmostEqual: Compare floats with tolerance
    # - assertGreater: Check if a value is greater than another
    # 
    # Example:
    # def test_bonus_assertions(self):
    #     """Demonstrate various assertion methods."""
    #     # assertIn example
    #     self.assertIn(5, [1, 3, 5, 7])
    #     # assertIsNone example
    #     self.assertIsNone(None)
    #     # assertAlmostEqual example (useful for floating point)
    #     self.assertAlmostEqual(0.1 + 0.2, 0.3, places=10)
    #     # assertGreater example
    #     self.assertGreater(10, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Run tests with detailed output 