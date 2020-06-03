#!/usr/bin/python3
""" a simple script that create a json from input"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle """
    if n <= 0:
        return []
    return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
