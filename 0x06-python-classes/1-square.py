#!/usr/bin/python3
""" This is the class of the square"""


class Square:
    """
    Class that contain a size of the square
    """
    def __init__(self, size):
        """ __init__ method.
                The __init__ method may be documented in either the class level
                docstring, or as a docstring on the __init__ method itself.

                Args:
                    size (str): is the size of the square
        """
        self.__size = size
