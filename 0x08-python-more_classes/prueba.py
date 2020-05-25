#!/usr/bin/python3
""" Just a script that contains a class"""


class Rectangle:
    @staticmethod
    def hola(mino, mino2):
        print(type(mino))
        print(type(Rectangle))

class Pt:
    pass

p = Rectangle()
a = Pt()

if not isinstance(a, Rectangle):
    print('passaaaaa')

Rectangle.hola(p, 'H')

print(type(Rectangle))
