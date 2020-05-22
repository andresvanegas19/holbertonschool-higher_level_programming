#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def matrix_mul(m_a, m_b):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if not type(m_a) is list:
        raise TypeError('m_a must be a list')
    if not type(m_b) is list:
        raise TypeError('m_b must be a list')
    if all(isinstance(x, list) for x in m_a):
        raise TypeError('m_a must be a list of lists')
    if all(isinstance(x, list) for x in m_b):
        raise TypeError('m_b must be a list of lists')
    for list_a in m_a:
        if not list_a:
            raise ValueError('m_a can\'t be empty')

    for list_b in m_b:
        if not list_b:
            raise ValueError('m_b can\'t be empty')

    for list_a in m_a:
        for num in list_a:
            if not type(num) in (int, float):
                raise TypeError('m_a should contain only integers or floats')

    for list_b in m_b:
        for num in list_b:
            if not type(num) in (int, float):
                raise TypeError('m_b should contain only integers or floats')

    return [1, 2, 3]
