#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultant = a / b
    except ZeroDivisionError:
        resultant = None
    finally:
        print('Inside result: {}'.format(resultant))
        return resultant
