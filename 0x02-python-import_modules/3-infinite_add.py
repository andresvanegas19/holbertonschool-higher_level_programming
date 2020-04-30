#!/usr/bin/python
import sys as s

if __name__ == '__main__':
    total = 0
    lista = [int(num) for num in s.argv[1:]]
    for num in lista:
        total = total + num
    print(total)
