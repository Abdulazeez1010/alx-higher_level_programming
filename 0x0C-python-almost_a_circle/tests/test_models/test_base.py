#!/usr/bin/python3
"""The unittest module for the base class"""


import unittest
import os
import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit test for the Base class"""

    def setUp(self):
        """Reset the Base class counter before each test."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

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

    def test_save_to_file_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        data = json.loads(content)
        expected_output = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        self.assertEqual(expected_output, data)

    def test_save_to_file_rect_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        data = json.loads(content)
        expected_output = []
        self.assertEqual(expected_output, data)

    def test_save_to_file_rect_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue("Rectangle.json")
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_square(self):
        s1 = Square(7, 2, 8)
        s2 = Square(4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()
        data = json.loads(content)
        expected_output = [{"y": 8, "x": 2, "id": 1, "size": 7}, {"y": 0, "x": 0, "id": 2, "size": 4}]
        self.assertEqual(expected_output, data)

    def test_save_to_file_square_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        data = json.loads(content)
        expected_output = []
        self.assertEqual(expected_output, data)

    def test_save_to_file_square_none(self):
        Square.save_to_file(None)
        self.assertTrue("Square.json")
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        expected_output = [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(expected_output, list_output)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        expected_output = "[Rectangle] (1) 1/0 - 3/5"
        self.assertEqual(expected_output, str(r2))

    def test_create_square(self):
        sq1 = Square(3, 4)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        expected_output = "[Square] (1) 4/0 - 3"
        self.assertEqual(expected_output, str(sq2))

    def test_load_from_file_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for in_rect, out_rect in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(in_rect), str(out_rect))

    def test_load_from_file_square(self):
        s1 = Square(3, 6, 2)
        s2 = Square(5)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for in_sq, out_sq in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(in_sq), str(out_sq))

    def test_load_from_file_square_empty(self):
        list_squares_input = []
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for in_sq, out_sq in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(in_sq), str(out_sq))
