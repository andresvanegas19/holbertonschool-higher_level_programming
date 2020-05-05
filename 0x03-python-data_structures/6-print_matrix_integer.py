#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lista in matrix:
        i = 0
        for num in lista:
            i += 1
            if (i <= len(lista) - 1):
                print("{} ".format(num), end="")
            else:
                print("{}".format(num), end="")
        print()
