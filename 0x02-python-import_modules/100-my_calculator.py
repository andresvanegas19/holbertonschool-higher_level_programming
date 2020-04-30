#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys as s
    operators = '+-*/'
    if (len(s.argv) is 4 and (s.argv[2] in operators)):
        op1 = int(s.argv[1])
        op2 = int(s.argv[3])
        if (operators[0] is s.argv[2]):
            print('{:d} + {:d} = {:d}'.format(op1, op2, add(op1, op2)))
        if (operators[1] is s.argv[2]):
            print('{:d} - {:d} = {:d}'.format(op1, op2, sub(op1, op2)))
        if (operators[2] is s.argv[2]):
            print('{:d} * {:d} = {:d}'.format(op1, op2, mul(op1, op2)))
        if (operators[3] is s.argv[2]):
            print('{:d} / {:d} = {:d}'.format(op1, op2, div(op1, op2)))
    else:
        if (len(s.argv) is 4):
            print('Unknown operator. Available operators: +, -, * and /')
        else:
            print('Usage: {} <a> <operator> <b>'.format(s.argv[0]))
        exit(1)
