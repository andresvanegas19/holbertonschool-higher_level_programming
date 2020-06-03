#!/usr/bin/python3
""" a wirdo class"""


class MyInt(int):
    """this invert a string"""
    def __init__(self, value):
        if type(value) is not str:
            self.__value = str(value)
        else:
            self.__value = int(value)

    def __str__(self):
        return self.__value

