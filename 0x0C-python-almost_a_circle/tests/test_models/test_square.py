#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""
    def setUp(self):
        """This will set all variables in each
        test to improve writting code"""
        # different areas
        self.s1 = Square(404)

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
        """This will test the class rectangle"""
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(5).size = -1

    def test_errSq1(self):
        """This will test the class rectangle"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(5).size = 'Hi'

    def test_update(self):
        """This will test the class rectangle"""
        self.s1.update(10)
        self.assertIn(self.s1.__str__(), '[Square] (10) 0/0 - 404')

    def test_update1(self):
        """This will test the class rectangle"""
        self.s1.update(1, 2)
        self.assertIn(self.s1.__str__(), '[Square] (1) 0/0 - 2')

    def test_update2(self):
        """This will test the class rectangle"""
        self.s1.update(89, 2, 3)
        self.assertIn(self.s1.__str__(), '[Square] (89) 3/0 - 2')

    def test_update3(self):
        """This will test the class rectangle"""
        self.s1.update(1, 2, 3, 4)
        self.assertIn(self.s1.__str__(), '[Square] (1) 3/4 - 2')

    def test_update4(self):
        """This will test the class rectangle"""
        self.s1.update(x=12)
        self.assertIn(self.s1.__str__(), '[Square] (308) 12/0 - 404')

    def test_update5(self):
        """This will test the class rectangle"""
        self.s1.update(size=7, id=89, y=1, x=1)
        self.assertIn(self.s1.__str__(), '[Square] (89) 1/1 - 7')

    def test_update6(self):
        """This will test the class rectangle"""
        s1_dictionary = self.s1.to_dictionary()
        self.s1.update(**s1_dictionary)
        self.assertIn(self.s1.__str__(), '[Square] (89) 1/1 - 7')

    def test_updErr(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            self.s1.update(size=7, id=-1, y={}, x=1)

    def test_updErr1(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            self.s1.update(1, 2, 'a', 4)
