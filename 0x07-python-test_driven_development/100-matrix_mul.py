#!/usr/bin/python3

matrix_a = [[1, 2, 3], [1, 2, 3]]

matrix_b = [[2, 3], [5, 6], [7, 8]]

for list_a in matrix_a:
    for num_a in list_a:
        for list_b in matrix_b:
            for num_b in list_b:
                print(num_b, end='')
                print('({} * {})'.format(num_a, num_b), end='')
            print()
        print()
    print()


