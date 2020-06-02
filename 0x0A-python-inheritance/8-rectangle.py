#!/usr/bin/python3
"""Test if the object is inherent of a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ is a class that it seems to be a rectangle"""

    def __init__(self, width, height):
        # para heredar los metodos de la clase se necesita
        # usar self para hacer referencia  a estos metodos
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
