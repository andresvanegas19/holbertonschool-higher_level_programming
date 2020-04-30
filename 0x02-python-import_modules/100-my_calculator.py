#!/usr/bin/python3
import calculator_1 as cal
import sys as s

if __name__ == '__main__':
    operators = '+-*/'
    if (len(s.argv) is 4 and (s.argv[2] in operators)):
        op1 = int(s.argv[1])
        op2 = int(s.argv[3])
        if (operators[0] is s.argv[2]):
            print('{:d} + {:d} = {:d}'.format(op1, op2, cal.add(op1, op2)))
        if (operators[1] is s.argv[2]):
            print('{:d} - {:d} = {:d}'.format(op1, op2, cal.sub(op1, op2)))
        if (operators[2] is s.argv[2]):
            print('{:d} * {:d} = {:d}'.format(op1, op2, cal.mul(op1, op2)))
        if (operators[3] is s.argv[2]):
            print('{:d} / {:d} = {:d}'.format(op1, op2, cal.div(op1, op2)))
    else:
        if (len(s.argv) is 4):
            print('Unknown operator. Available operators: +, -, * and /')
        else:
            print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
