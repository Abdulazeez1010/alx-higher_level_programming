#!/usr/bin/python3
"""The unittest module for the base class"""


import unittest
import json


from models.base import Base

class TestBase(unittest.TestCase):
    """Unit test for the Base class"""
    def test_base(self):
        """Test cases to validate correct output for Base class"""
        b1 = Base()
        b2 = Base()
        b3 = Base(13)
        b4 = Base()
        b5 = Base(None)

        self.assertEqual(1, b1.id)
        self.assertEqual(2, b2.id)
        self.assertEqual(13, b3.id)
        self.assertEqual(3, b4.id)
        self.assertEqual(4, b5.id)
