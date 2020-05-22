#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger contains the
    :param arg: The arg is used for ...
    :type class: class
    """
    def setUp(self) -> None:
        self.list_normal = [1, 2, 3, 123123, 2, 3, 4, 5]
        self.list_string = [1, 'c is too', 'python', 3, 'is', 'cool', 2]
        self.list_float = [1.49, 1.44, 1.32, 1.489, 1.49, 1.5, 1.5, 1.5, 1.5]
        self.string = 'HOLBerton'

    def test_normal(self):
        self.assertAlmostEqual(max_integer(self.list_normal), 123123)
        self.assertAlmostEqual(max_integer([1, 2, 12, 3]), 12)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer(self.list_float), 1.5)

    def test_empty(self):
        self.assertAlmostEqual(max_integer({}), None)
        self.assertAlmostEqual(max_integer(()), None)
        self.assertAlmostEqual(max_integer(), None)

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer('Why', 'This', 'Error', 'Is', 'Not raised')
        with self.assertRaises(TypeError):
            max_integer(self.list_string)

    def test_string(self):
        self.assertAlmostEqual(max_integer(self.string), 't')
        self.assertAlmostEqual(max_integer('XXXXtXXXX'), 't')
