#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda arr: list(map(lambda n: n ** 2, arr)), matrix))
