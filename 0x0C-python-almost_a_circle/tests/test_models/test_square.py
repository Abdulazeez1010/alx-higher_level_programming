#!/usr/bin/python3
"""The unittest module for the Square class."""


import unittest
from io import StringIO
import sys


from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit test for the Square class."""
    def test_str_method(self):
        self.assertEqual("[Square] (36) 0/0 - 5", str(Square(5)))

    def test_str_method_with_x(self):
        self.assertEqual("[Square] (37) 4/0 - 3", str(Square(3, 4)))

    def test_str_method_with_x_and_y(self):
        self.assertEqual("[Square] (38) 2/6 - 4", str(Square(4, 2, 6)))

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
