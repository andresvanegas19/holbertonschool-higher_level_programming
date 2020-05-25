#!/usr/bin/python3
""" Just a script that contains a class"""


class Rectangle:
    """ The rectangle object contains the information about
    a rectanlge"""

    number_of_instances = 0
    print_symbol = '#'

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
        """
        This method return a string with a perfect rectangle
        with certain string
        :return: a string with jump file"""
        if self.__width is 0 or self.__height is 0:
            return ''
        self.print_symbol = str(self.print_symbol)
        result = ''
        for high in range(self.__height):
            for long in range(self.__width):
                result = result + self.print_symbol
            if high is not self.__height - 1:
                result = result + '\n'

        return result

    def __repr__(self):
        """
        This method return a string with a information to the developer
        :return: a string more information"""
        return 'Rectangle(' + str(self.__height) + ', ' \
               + str(self.__width) + ')'

    def __del__(self):
        """This method delete the class"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """this evaluated which attribute is most bigger
        :return the attribute much bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        rec1 = len(str(rect_1))
        rec2 = len(str(rect_2))

        if rec1 is rec2 or rec1 > rec2:
            return rect_1
        if rec2 > rec1:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """this method call again the class to reajustar el size
        :return the new class with the much bigger size or other
        """
        if not isinstance(size, int):
            return Rectangle(0, 0)
        return Rectangle(size, size)
