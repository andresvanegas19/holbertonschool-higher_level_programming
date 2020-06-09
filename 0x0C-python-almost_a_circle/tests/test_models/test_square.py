#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""
    def test_rectangle(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Square(1).id, 1)

    def test_rectangle1(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Square(10, 4).id, 4)

    def test_rectangle2(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Square(2, 10, 3).id, 3)

    def test_rectangle3(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Square(10, 2, 0, 4).id, 4)

    def test_rectErr(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square(10, 2, 0, 4, 5, 5)

    def test_rectErr1(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square('Hello I"m a mistake')

    def test_rectErr2(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square(10, {}, 0, 4)

    def test_rectErr3(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square(None, 2, 0, 1)

    def test_rectErr4(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square(1, 2, 'a', 1)

    def test_rectErr5(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square(1, 2, 3, 1).size = -1

    def test_rectErr6(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Square(1, 2, 3, 1).size = 'hola'

    def test_functionsRect(self):
        """This function test the rectangle"""
        self.assertGreaterEqual(Square(5).area(), 25)

    def test_errSq(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(5).size = -1