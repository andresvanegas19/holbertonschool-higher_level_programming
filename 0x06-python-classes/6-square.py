#!/usr/bin/python3
""" This is the class of the square"""


class Square:
    """
    Class that contain a size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method.
                The __init__ method may be documented in either the class level
                docstring, or as a docstring on the __init__ method itself.

                Args:
                    size (str): is the size of the square
        """
        self.size = size
        self.__position = position

    @property
    def position(self):
        """str: Is the size of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """str: Is the size of the square"""
        if not isinstance(value, tuple) or len(value) is not 2 \
                or not isinstance(value[0], int) or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

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

    def my_print(self):
        """
        that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print(end='\n')

        for down in range(self.__size):
            for _ in range(self.__position[0]):
                print(' ', end='')
            for _ in range(self.__size):
                print('#', end='')
            print(end='\n')
        # if self.__size < self.__position[1]:
        # for _ in range(self.__position[1] - self.__size):
        # print(end='\n')
