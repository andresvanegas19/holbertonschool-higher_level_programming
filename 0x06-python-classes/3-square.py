#!/usr/bin/python3
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
        self.__size = size


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Method for validated is a number"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
