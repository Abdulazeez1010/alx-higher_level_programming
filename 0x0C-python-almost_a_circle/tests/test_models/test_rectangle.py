#!/usr/bin/python3
"""The unittest module for the Rectangle class"""


import unittest
from io import StringIO
import sys


from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit rest for the Rectangle class"""

    def setUp(self):
        """Reset the Base class counter before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """Test cases to validate correct output for Rectangle"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(5, 8)

        self.assertEqual(1, r1.id)
        self.assertEqual(2, r2.id)
        self.assertEqual(12, r3.id)
        self.assertEqual(3, r4.id)
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

    def test_display_without_x_and_y(self):
        rect = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_without_y(self):
        rect = Rectangle(3, 2, 2, 0)
        expected_output = "  ###\n  ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display(self):
        rect = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", str(rect))

    def test_str_method(self):
        rect = Rectangle(5, 5, 1)
        self.assertEqual("[Rectangle] (1) 1/0 - 5/5", str(rect))

    def test_update_method_with_id(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_update_method_with_id_and_w(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 3/10", str(rect))

    def test_update_method_with_id_w_and_h(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 4, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 4/2", str(rect))

    def test_update_method_with_id_w_h_and_x(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 5, 4, 1)
        self.assertEqual("[Rectangle] (89) 1/10 - 5/4", str(rect))

    def test_update_method_with_id_w_h_x_and_y(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 3, 2, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 3/2", str(rect))

    def test_update_method_with_height(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/1", str(rect))

    def test_update_method_with_width_and_x(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(width=1, x=2)
        self.assertEqual("[Rectangle] (1) 2/10 - 1/10", str(rect))

    def test_update_method_with_y_width_x_and_id(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/10", str(rect))

    def test_update_method_with_x_height_y_and_width(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (1) 1/3 - 4/2", str(rect))

    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9)
        result = rect.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(expected, result)

    def test_save_to_file_rect_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")
