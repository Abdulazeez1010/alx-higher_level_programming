#!/usr/bin/python3
"""The unittest module for the Square class."""


import unittest
from io import StringIO
import sys


from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Unit test for the Square class."""
    def setUp(self):
        """Reset the Base class counter before each test."""
        Base._Base__nb_objects = 0

    def test_str_method(self):
        self.assertEqual("[Square] (1) 0/0 - 5", str(Square(5)))

    def test_str_method_with_x(self):
        self.assertEqual("[Square] (1) 4/0 - 3", str(Square(3, 4)))

    def test_str_method_with_x_and_y(self):
        self.assertEqual("[Square] (1) 2/6 - 4", str(Square(4, 2, 6)))

    def test_type_error_with_x(self):
        with self.assertRaises(TypeError) as context:
            Square(3, "4")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_type_error_with_y(self):
        with self.assertRaises(TypeError) as context:
            Square(3, 5, "4")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_type_error_with_value(self):
        with self.assertRaises(TypeError) as context:
            Square("4", 3, 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_value_error_with_x(self):
        with self.assertRaises(ValueError) as context:
            Square(3, -2)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_value_error_with_y(self):
        with self.assertRaises(ValueError) as context:
            Square(3, 5, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_value_error_with_value(self):
        with self.assertRaises(ValueError) as context:
            Square(-3, 5, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_value_error_with_0_value(self):
        with self.assertRaises(ValueError) as context:
            Square(0)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_square_area_method(self):
        sq = Square(6)
        self.assertEqual(36, sq.area())

    def test_square_area_method_with_x(self):
        sq = Square(4, 1)
        self.assertEqual(16, sq.area())

    def test_square_area_method_with_x_and_y(self):
        sq = Square(7, 3, 2)
        self.assertEqual(49, sq.area())

    def test_square_display_with_value(self):
        sq = Square(4)
        expected_output = "####\n####\n####\n####\n"
        captured_string = StringIO()
        sys.stdout = captured_string
        sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, captured_string.getvalue())

    def test_square_display_with_value_and_x(self):
        sq = Square(2, 2)
        expected_output = "  ##\n  ##\n"
        captured_string = StringIO()
        sys.stdout = captured_string
        sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, captured_string.getvalue())

    def test_square_display_with_value_x_and_y(self):
        sq = Square(3, 1, 3)
        expected_output = "\n\n\n ###\n ###\n ###\n"
        captured_string = StringIO()
        sys.stdout = captured_string
        sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, captured_string.getvalue())

    def test_update_with_id(self):
        sq = Square(5)
        sq.update(10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(sq))

    def test_update_with_id_and_size(self):
        sq = Square(5)
        sq.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(sq))

    def test_update_with_id_size_and_x(self):
        sq = Square(5)
        sq.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(sq))

    def test_update_with_id_size_x_and_y(self):
        sq = Square(5)
        sq.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(sq))

    def test_update_with_x(self):
        sq = Square(1, 2, 3, 4)
        sq.update(x=12)
        self.assertEqual("[Square] (4) 12/3 - 1", str(sq))

    def test_update_with_size_and_y(self):
        sq = Square(1, 2, 3, 4)
        sq.update(size=7, y=1)
        self.assertEqual("[Square] (4) 2/1 - 7", str(sq))

    def test_update_with_size_id_and_y(self):
        sq = Square(1, 2, 3, 4)
        sq.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 2/1 - 7", str(sq))

    def test_square_dict(self):
        sq = Square(10, 2, 1)
        result = sq.to_dictionary()
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(expected_output, result)
