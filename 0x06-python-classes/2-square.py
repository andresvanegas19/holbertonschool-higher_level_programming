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
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
