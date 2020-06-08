#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""
    def setUp(self) -> None:
        """This will set all variables in each
        test to improve writting code"""
        self.base = Base(None)

    def test_id(self):
        """this will test the id attribute"""
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(self.base, 1)
        self.assertEqual(Base(-10), 2)
