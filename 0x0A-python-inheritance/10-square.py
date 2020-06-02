"""Test if the object is inherent of a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ it seems is a figure that it will be a sum of an operatiom"""
    def __init__(self, size):
        self.__size = integer_validator("size", size)

    def area(self):
        """calculate the area of the class"""
        return self.__size * self.__size
