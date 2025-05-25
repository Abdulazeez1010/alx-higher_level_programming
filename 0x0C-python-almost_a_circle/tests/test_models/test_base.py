#!/usr/bin/python3
"""The unittest module for the base class"""


import unittest
import json

from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Unit test for the Base class"""

    def setUp(self):
        """Reset the Base class counter before each test."""
        Base._Base__nb_objects = 0

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

    def test_to_json_string(self):
        rect = Rectangle(10, 7, 2, 8)
        dictionary = rect.to_dictionary()
        result = Base.to_json_string([dictionary])
        expected_output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(sorted(expected_output), sorted(result))

    def test_json_string_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        data = json.loads(content)
        expected_output = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        self.assertEqual(expected_output, data)
