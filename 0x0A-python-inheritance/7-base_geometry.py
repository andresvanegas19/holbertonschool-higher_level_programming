#!/usr/bin/python3
"""Test if the object is inherent of a class"""


class BaseGeometry:
    """function that validated if the object is
    a instace of a class in python"""

    def __init__(self):
        self.name = None

    def area(self):
        """Just raise a error"""
        raise Exception('area() is not implemented')

    @staticmethod
    def integer_validator(name, value):
        """ that validates value, name is a string and verificated value"""
        if type(value) is not int:
            raise Exception('{} must be an integer'.format(name))
        if value <= 0:
            raise Exception('{} must be greater than 0'.format(name))
        return value
