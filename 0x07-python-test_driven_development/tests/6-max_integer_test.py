#!/usr/bin/python3
"""The unittest module for max_integer"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit test for the max_integer function"""
    def test_max_integer(self):
        """Test cases to validate correct output for max_integer"""
        list_0 = []
        list_1 = [6]
        list_2 = [1, 8, 2, 7, 3, 6]
        list_3 = [4, 1, -2, 1, 0]
        list_4 = [-5, -3, -2, -7]
        list_5 = [1, 3, 5, 2, 9]
        self.assertEqual(None, max_integer(list_0))
        self.assertEqual(6, max_integer(list_1))
        self.assertEqual(8, max_integer(list_2))
        self.assertEqual(4, max_integer(list_3))
        self.assertEqual(-2, max_integer(list_4))
        self.assertEqual(9, max_integer(list_5))
