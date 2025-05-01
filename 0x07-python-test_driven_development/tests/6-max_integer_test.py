#!/usr/bin/python3
"""The unittestmodule for max_integer"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        list_1 = [1, 8, 2, 7, 3, 6]
        list_2 = [4, 1, -2, 1, 0]
        self.assertEqual(8, max_integer(list_1))
        self.assertEqual(4, max_integer(list_2))
