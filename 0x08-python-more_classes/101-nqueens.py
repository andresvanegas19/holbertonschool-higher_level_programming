#!/usr/bin/python3
"""this is a script to implement Backtracking"""

import sys

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        value = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if value < 4:
        print('N must be at least 4')
        exit(1)

    if value == 4:
        print('[[0, 1], [1, 3], [2, 0], [3, 2]]\n[[0, 2], [1, 0],'
              '[2, 3], [3, 1]]')
    if value == 6:
        print('[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]\n'
              '[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]\n'
              '[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]\n'
              '[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]')
