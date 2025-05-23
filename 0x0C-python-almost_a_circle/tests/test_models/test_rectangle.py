#!/usr/bin/python3
"""The unittest module for the Rectangle class"""


import unittest


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit rest for the Rectangle class"""
    def test_rectangle(self):
        """Test cases to validate correct output for Rectangle"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(5, 8)

        self.assertEqual(4, r1.id)
        self.assertEqual(5, r2.id)
        self.assertEqual(12, r3.id)
        self.assertEqual(6, r4.id)
