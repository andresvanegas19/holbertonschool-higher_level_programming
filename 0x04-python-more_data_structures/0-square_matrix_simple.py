#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    square = list(map
                  (lambda arr:
                   list(map(
                       lambda n: n ** 2, arr)),
                matrix))
#    a = [[0 for x in range(n)] for x in range(m)]
    return square
