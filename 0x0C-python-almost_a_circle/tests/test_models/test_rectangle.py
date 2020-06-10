#!/usr/bin/python3
"""Unittest for test the rect"""
import unittest
from models.rectangle import Rectangle
import io
import sys


class TestBaseClass(unittest.TestCase):
    """This will test the class base"""

    def setUp(self):
        """This will set all variables in each
        test to improve writting code"""
        # different areas
        self.ar = Rectangle(3, 2).area()
        self.rect = Rectangle(10, 2, 1, 9)
        self.rDict = {'x': 1, 'y': 9, 'id': 487, 'height': 2, 'width': 10}
        self.guide1 = "##\n  ##\n  ##"
        self.guide2 = '##\n  ##\n  ##\n ###\n ###'
        self.guide3_5 = '##\n  ##\n  ##\n ###\n ###\n#'
        self.guide4 = '##\n  ##\n  ##\n ###\n ###\n#\n\n #'
        self.guide6 = '##\n  ##\n  ##\n ###\n ###\n#\n\n #\n#'
        sys.stdout = capturedOutput = io.StringIO()
        # todo everything that is going to be printed
        # THIS IS  A EXAMPLE: correct = capturedOutput.getvalue().strip()
        Rectangle(2, 3, 2, 2).display()
        self.case1 = capturedOutput.getvalue().strip()
        Rectangle(3, 2, 1, 0).display()
        self.case2 = capturedOutput.getvalue().strip()
        Rectangle(1, 1).display()
        self.case3 = capturedOutput.getvalue().strip()
        Rectangle(1, 1, 1, 1).display()
        self.case4 = capturedOutput.getvalue().strip()
        Rectangle(1, 1, 0, 0).display()
        self.case5 = capturedOutput.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.r1 = Rectangle(10, 10, 10, 10)

    def test_rectangle(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Rectangle(1, 2).id, 2)

    def test_rectangle1(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Rectangle(2, 10, 3).id, 3)

    def test_rectangle11(self):
        """This will test  how manage the errors"""
        with self.assertRaises(Exception):
            Rectangle(10, 2, -2)

    def test_rectangle2(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Rectangle(10, 2, 0, 4).id, 4)

    def test_rectangle3(self):
        """This will test the class rectangle"""
        self.assertEqual(Rectangle(10, 2, 0, 4, 5).id, 5)

    def test_rectangle4(self):
        """This will test the class rectangle"""
        self.assertGreaterEqual(Rectangle(10, 2, 0, 4, None).id, 6)

    def test_rectangle5(self):
        """This will test the class rectangle"""
        self.assertEqual(Rectangle(1, 1, 0, 0, 5).id, 5)

    def test_rectangle6(self):
        """This will test the class rectangle"""
        self.assertEqual(Rectangle(1, 1, 0, 1, 5).id, 5)

    def test_rectagleErrors1(self):
        """This will test  how manage the errors"""
        with self.assertRaises(Exception):
            Rectangle(10, 2, 0, 4, 5, 5)

    def test_rectagleErrors2(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(None, 2)

    def test_rectagleErrors3(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(1.1, 1.2, 1.3)

    def test_rectagleErrors4(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle([1, 2, 3], [1, 2, 3], [1, 2, 3])

    def test_rectagleErrors5(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle()

    def test_rectagleErrors6(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(None, 5)

    def test_rectagleErrors7(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(set())

    def test_rectagleErrors8(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(())

    def test_rectagleErrors9(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle({})

    def test_rectagleErrors10(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(1, 1, None, None)

    def test_rectagleErrors11(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 2, 0, 'Hi', 5)

    def test_rectagleErrors12(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(0, 2, 0, 1, 5)

    def test_rectagleErrors13(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5)

    def test_searchError(self):
        """This will test the class rectangle"""
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 1)

    def test_searchError1(self):
        """This will test the class rectangle"""
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, 0)

    def test_Errmsg(self):
        """This function will check the error message"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 2)
            r.height = -10
        self.assertTrue('height must be > 0' in str(err.exception))

    def test_Errmsg1(self):
        """This will test the class rectangle"""
        # This is for check the error message
        with self.assertRaises(TypeError) as err:
            Rectangle(10, "Hello, World!")
        self.assertTrue('height must be an integer' in str(err.exception))

    def test_Errmsg2(self):
        """This will test the class rectangle"""
        with self.assertRaises(TypeError) as err:
            Rectangle("Hello, World!", 10)
        self.assertTrue('width must be an integer' in str(err.exception))

    def test_Errmsg3(self):
        """This will test the class rectangle"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertTrue('width must be > 0' in str(err.exception))

    def test_Errmsg4(self):
        """This will test the class rectangle"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertTrue('x must be an integer' in str(err.exception))

    def test_Errmsg5(self):
        """This will test the class rectangle"""
        with self.assertRaises(ValueError) as err:
            Rectangle(10, 2, 3, -1)
        self.assertTrue('y must be >= 0' in str(err.exception))

    def test_calcArea(self):
        """This will test the class rectangle"""
        self.assertEqual(self.ar, 6)

    def test_calcArea1(self):
        """This will test the class rectangle"""
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_calcArea2(self):
        """This will test the class rectangle"""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_errArea(self):
        """This will test the class rectangle"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(12, {}, 0, 0, 12).area()

    def test_errArea1(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5).area('Hello')

    def test_errArea2(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5).area(1.1)

    def test_magic_str(self):
        """This will test the class rectangle"""
        self.assertIn(Rectangle(4, 6, 2, 1, 12).__str__(),
                      '[Rectangle] (12) 2/1 - 4/6')

    def test_magic_str1(self):
        """This will test the class rectangle"""
        self.assertIn(Rectangle(10, 10, 2, 1, 12).__str__(),
                      '[Rectangle] (12) 2/1 - 10/10')

    def test_magic_str2(self):
        """This will test the class rectangle"""
        a = Rectangle(10, 12)
        self.assertIn(a.__str__(), '[Rectangle] ({}) 0/0 - 10/12'.format(a.id))

    def test_magic_str3(self):
        """This will test the class rectangle"""
        a = Rectangle(1, 2, 0, 0)
        self.assertIn(a.__str__(), '[Rectangle] ({}) 0/0 - 1/2'.format(a.id))

    def test_displayBasic(self):
        """This will test the class rectangle"""
        self.assertEqual(self.case1, self.guide1)

    def test_displayBasic1(self):
        """This will test the class rectangle"""
        self.assertEqual(self.case2, self.guide2)

    def test_displayBasic2(self):
        """This will test the class rectangle"""
        self.assertEqual(self.case3, self.guide3_5)

    def test_displayBasic3(self):
        """This will test the class rectangle"""
        self.assertEqual(self.case4, self.guide4)

    def test_displayBasic4(self):
        """This will test the class rectangle"""
        self.assertEqual(self.case5, self.guide6)

    def test_update(self):
        """This will test the class rectangle"""
        self.r1.update(89)
        self.assertIn(self.r1.__str__(), '[Rectangle] (89) 10/10 - 10/10')

    def test_update2(self):
        """This will test the class rectangle"""
        self.r1.update(89, 2)
        self.assertIn(self.r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')

    def test_update3(self):
        """This will test the class rectangle"""
        self.r1.update(89, 2, 3)
        self.assertIn(self.r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')

    def test_update4(self):
        """This will test the class rectangle"""
        self.r1.update(89, 2, 3, 4)
        self.assertIn(self.r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')

    def test_update5(self):
        """This will test the class rectangle"""
        self.r1.update(89, 2, 3, 4, 5)
        self.assertIn(self.r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')

    def test_updateNormal(self):
        """This will test the class rectangle"""
        self.assertIsNone(Rectangle(1, 1).update())

    def test_updateErr(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5).update(1, -1)

    def test_updateErr1(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5).update(1, -1, {})

    def test_updateErr2(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5).update(1, 12, 3, (1, 2, 3))

    def test_updateErr3(self):
        """This will test the class rectangle"""
        with self.assertRaises(Exception):
            Rectangle(10, 0, 0, 1, 5).update(1, 2, 3, 4, "Hello")

    def test_kwargs(self):
        """This will test the class rectangle"""
        self.r1.update(x=1, height=2, y=3, width=4)
        self.assertIn(self.r1.__str__(), '[Rectangle] ({}) 1/3 - 4/2'
                      .format(self.r1.id))

    def test_kwargs1(self):
        """This will test the class rectangle"""
        self.r1.update(height=2)
        self.assertIn(self.r1.__str__(), '[Rectangle] ({}) 10/10 - 10/2'
                      .format(self.r1.id))

    def test_kwargs2(self):
        """This will test the class rectangle"""
        self.assertIsNone(self.r1.update())

    def test_kwargs3(self):
        """This will test the class rectangle"""
        self.assertIsNone(Rectangle(2, 3, 2, 2)
                          .update(peso=4, altura=1, equis=1, ye=2))

    def test_valDict(self):
        """This will test the class rectangle"""
        self.rDict['id'] = self.rect.id
        self.assertDictEqual(self.rect.to_dictionary(), self.rDict)

    def test_sav_file(self):
        """This will test the class rectangle"""
        class Rectangle:
            pass
        with self.assertRaises(Exception):
            Rectangle.save_to_file([])

    def test_sav_file1(self):
        """This will test the class rectangle"""
        a = Rectangle(1, 2, 3, 4)
        b = Rectangle(1, 2, 3, 4)
        b.save_to_file([])
        self.assertIsNotNone(b)
        self.assertIsNotNone(a)

    def test_kwargs4(self):
        """This will test the class rectangle"""
        self.r1.update(**self.rDict)
        self.assertIn(self.r1.__str__(), '[Rectangle] ({}) 1/9 - 10/2'
                      .format(self.r1.id))

    def test_kwargs4(self):
        """This will test the class rectangle"""
        a = Rectangle(1, 2, 3, 4)
        a.save_to_file([])
        self.assertGreaterEqual(a.id, 100)
