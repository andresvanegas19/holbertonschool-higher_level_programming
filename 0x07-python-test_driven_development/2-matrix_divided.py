#!/usr/bin/python3
"""Script to contain a  function that divides all elements of a matrix.
Attributes:
    matrix_divided(matrix, div): it return a new list divided by 2 and
    recive an list with specific parameters
Example: ./1-main.py"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.
        matrix (list): Is for divided whole matrix
        div (int): Is the value it will divided"""
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    matrix_int = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(matrix_int)
    new_matrix = [[] for _ in range(len(matrix))]
    next_size = len(matrix[0])
    position = 0
    for lists in matrix:
        prev_size = len(lists)
        if not isinstance(lists, list):
            raise TypeError(matrix_int)
        if prev_size is not next_size:
            raise TypeError('Each row of the matrix must have the same size')
        for num in lists:
            if type(num) not in [int, float]:
                raise TypeError('div must be a number')
            new_matrix[position].append(round(num / div, 2))
        position += 1
        next_size = len(lists)

    return new_matrix
