#!/usr/bin/python3
"""The unittest module for the Rectangle class"""


import unittest
from io import StringIO
import sys


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit rest for the Rectangle class"""
    def test_rectangle(self):
        """Test cases to validate correct output for Rectangle"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(5, 8)

        self.assertEqual(8, r1.id)
        self.assertEqual(9, r2.id)
        self.assertEqual(12, r3.id)
        self.assertEqual(10, r4.id)
        self.assertEqual(40, r4.area())
        self.assertEqual(6, Rectangle(3, 2).area())
        self.assertEqual(35, Rectangle(5, 7, 1, 1, 3).area())

    def test_height_type_error(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_value_error(self):
        #Test with negative height
        with self.assertRaises(ValueError) as context:
            Rectangle(5, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_height_value_error(self):
        #Test with 0 height
        with self.assertRaises(ValueError) as context:
            Rectangle(2, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_width_type_error(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("3", 7)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_value_error(self):
        #Test with negative width
        with self.assertRaises(ValueError) as context:
            Rectangle(-4, 9)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_width_value_error(self):
        #Test with 0 width
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 3)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_x_type_error(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 5, "1", 5)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_value_error(self):
        with self.assertRaises(ValueError) as context:
           Rectangle(4, 1, -3, 2)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_type_error(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(2, 5, 1, "5")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_value_error(self):
        with self.assertRaises(ValueError) as context:
           Rectangle(4, 1, 3, -2)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_display(self):
        rect = Rectangle(2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("##\n##\n", captured_output.getvalue())
