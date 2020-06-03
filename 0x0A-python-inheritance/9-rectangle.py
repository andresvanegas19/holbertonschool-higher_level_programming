#!/usr/bin/python3
"""Test if the object is inherent of a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ is a class that it seems to be a rectangle"""

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        """functio that return the are of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
