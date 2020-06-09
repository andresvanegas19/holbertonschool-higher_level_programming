#!/usr/bin/python3
"""Unittest for the test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from os import path
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""
    def setUp(self) -> None:
        """This will set all variables in each
        test to improve writting code"""
        self.r1Json = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'

    def test_id3(self):
        """this will test the id attribute3"""
        self.assertEqual(Base(None).id, 9)

    def test_id(self):
        """this will test the id attribute"""
        self.assertEqual(Base(3).id, 3)

    def test_id1(self):
        """this will test the id attribute5"""
        self.assertEqual(Base(5,).id, 5)

    def test_id4(self):
        """this will test the id attribute2"""
        self.assertEqual(Base(10).id, 10)

    def test_id5(self):
        """this will test the id attribute1"""
        self.assertEqual(Base(10).id, 10)

    def test_id_err(self):
        """check the erros in the id"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_jsonStr(self):
        """this will test the id attribute"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertTrue(type(Base.to_json_string([dictionary])))

    def test_jsonStr1(self):
        """this will test the id attribute"""
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_jsonStr2(self):
        """check the erros in the id"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_save(self):
        """this will test the id attribute"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(path.exists('Rectangle.json'))

    def test_jsonFile(self):
        """check the erros in the id"""
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1, 2, 3])

    def test_jsonFile1(self):
        """check the erros in the id"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_jsonFile2(self):
        """check the erros in the id"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)

    def test_jsonFile3(self):
        """check the erros in the id"""
        a = Rectangle.from_json_string(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(a, [])

    def test_create(self):
        """is test fo create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)

    def test_loadsFiles(self):
        """This function test the created method"""
        class Falsee(Base):
            pass
        list_rectangles_output = Falsee.load_from_file()
        self.assertEqual(list_rectangles_output, [])

    def test_loadFiles2(self):
        """This function test the if it a list"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output) is list)

    def test_csvLoad(self):
        """this will test the id attribute"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for rect in list_rectangles_input:
            self.assertTrue(isinstance(rect, object))

        for rect in list_rectangles_output:
            self.assertTrue(isinstance(rect, object))

    def test_csvLoad1(self):
        """this will test the id attribute"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()

        for square in list_squares_input:
            self.assertTrue(type(square.__str__()) is str)

        for square in list_squares_output:
            self.assertTrue(type(square.__str__()) is str)
