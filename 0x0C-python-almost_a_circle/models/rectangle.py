#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ This is for get the value
        :return return the private value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This will check the value if is a int otherwise raise error"""
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ This is for get the value
        :return return the private value"""
        return self.__width

    @height.setter
    def height(self, value):
        """ This will check the value if is a int otherwise raise error"""
        if not type(value) is int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        """This will set the value"""
        return self.__x

    @x.setter
    def x(self, value):
        """ This will check the value if is a int otherwise raise error"""
        if not type(value) is int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """acces to the function"""
        return self.__y

    @y.setter
    def y(self, value):
        """ This will check the value if is a int otherwise raise error"""
        if not type(value) is int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
