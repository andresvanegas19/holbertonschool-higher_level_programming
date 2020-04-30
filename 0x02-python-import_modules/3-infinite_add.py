#!/usr/bin/python
import sys as s

if __name__ == '__main__':
    total = 0
    for num in s.argv[1:]:
        total = total + int(num)
    print('{:d}'.format(total))
