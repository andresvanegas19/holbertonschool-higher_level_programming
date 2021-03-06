#!/usr/bin/python3
""" This is the class of the square"""


class Square:
    """
    Class that contain a size of the square
    """
    def __init__(self, size=0):
        """ __init__ method.
                The __init__ method may be documented in either the class level
                docstring, or as a docstring on the __init__ method itself.

                Args:
                    size (str): is the size of the square
        """
        self.size = size

    @property
    def size(self):
        """str: Is the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """str: Is the size of the square"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        is for return the square of the value into the structure
        :return: int the double of value
        """
        return self.__size ** 2
