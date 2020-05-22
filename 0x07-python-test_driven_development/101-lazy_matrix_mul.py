#!/usr/bin/python3
"""Script to multiplicate a square
Attributes:
    size(int): is the function to multiplicate a square
    if it fails raise a error
Example: ./4-main.py"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """return a new square
    :argument
        m_a(list): is the size of the square
        m_b(list): is the size of the square
    :return
        the square"""
    return np.dot(m_a, m_b)
