#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x, y, id)
