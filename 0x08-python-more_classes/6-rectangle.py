#!/usr/bin/python3
""" Just a script that contains a class"""


class Rectangle:
    """ The rectangle object contains the information about
    a rectanlge"""

    number_of_instances = 0


    # Instantiation with optional width and height
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    # Public instance method
    def area(self):
        """ calculate the area
        :return the area of the square"""
        return self.__width * self.__height

    # Public instance method
    def perimeter(self):
        """ Calculate the perimeter of a square
        :return the perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__height + self.__width)

    # print() and str() should print the rectangle with the character
    # if width or height is equal to 0, return an empty string
    def __str__(self):
        if self.__width is 0 or self.__height is 0:
            return ''
        result = ''
        for high in range(self.__height):
            for long in range(self.__width):
                result = result + Rectangle.print_symbol
            if high is not self.__height - 1:
                result = result + '\n'

        return result

    def __repr__(self):
        return 'Rectangle(' + str(self.__height) + ', ' + str(self.__width) + ')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
