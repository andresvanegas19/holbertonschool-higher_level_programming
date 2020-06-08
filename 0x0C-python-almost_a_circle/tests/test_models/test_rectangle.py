#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""
    def setUp(self) -> None:
        """This will set all variables in each
        test to improve writting code"""
        # different areas
        self.ar = Rectangle(3, 2).area()

    def test_rectangle(self):
        """This will test the class rectangle"""
        # self.assertEqual(Rectangle(1, 2).id, 6)
        # self.assertEqual(Rectangle(2, 10, 3).id, 7)
        # self.assertEqual(Rectangle(10, 2, 0, 4).id, 8)
        self.assertEqual(Rectangle(10, 2, 0, 4, 5).id, 5)
        self.assertEqual(Rectangle(0, 0, 0, 0, 5).id, 5)

    def test_rectagle_errors1(self):
        """This will test  how manage the errors"""
        # self.assertEqual(Rectangle(1), )
        with self.assertRaises(Exception):
            Rectangle(10, 2, 0, 4, 5, 5)
        with self.assertRaises(Exception):
            Rectangle(None)
        with self.assertRaises(Exception):
            Rectangle(1.1, 1.2, 1.3)
        with self.assertRaises(Exception):
            Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3])
        with self.assertRaises(Exception):
            Rectangle()
        with self.assertRaises(Exception):
            Rectangle(set())
        with self.assertRaises(Exception):
            Rectangle(())
        with self.assertRaises(Exception):
            Rectangle({})
        with self.assertRaises(Exception):
            Rectangle(10, 2, 0, 'Hi', 5)

    def calcArea(self):
        self.assertEqual(self.ar, 6)
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_Errmsg(self):
        """This function will check the error message"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 2)
            r.height = -10
        self.assertTrue('height must be > 0' in str(err.exception))

        # This is for check the error mesagge
        with self.assertRaises(TypeError) as err:
            Rectangle(10, "Hello, World!")
        self.assertTrue('height must be an integer' in str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle("Hello, World!", 10)
        self.assertTrue('width must be an integer' in str(err.exception))

        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertTrue('width must be > 0' in str(err.exception))

        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertTrue('x must be an integer' in str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(10, 2, 3, -1)
        self.assertTrue('y must be >= 0' in str(err.exception))




