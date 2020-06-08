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
        self.base = Base(None)

    def test_id(self):
        """this will test the id attribute"""
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base(5,).id, 5)
        self.assertEqual(self.base.id, 1)
        self.assertEqual(Base(-10).id, 2)
        # repet if
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base(10).id, 10)

    def test_id_err(self):
        """check the erros in the id"""
        with self.assertRaises(TypeError):
            Base(1, 2)
