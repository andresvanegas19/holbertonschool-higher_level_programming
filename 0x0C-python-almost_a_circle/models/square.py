#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a kinf of figure but it has another specifics"""
    # def __init__(self, width, height, x=0, y=0, id=None):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        super().evaluated(value, 'width')
        self._size = value

    def __str__(self):
        # [Square] (<id>) <x>/<y> - <size>
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self._size)

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute and update it"""
        a = [self.id, self.size, self.x, self.y]
        err = ['id', 'size', 'x', 'y']
        if args:
            for num in range(len(args)):
                self.evaluated(args[num], err[num])
                a[num] = args[num]
        else:
            for key, val in kwargs.items():
                self.evaluated(val, key)
                if key in err:
                    a[err.index(key)] = val
        # to unpacking the variables and save it
        self.id, self.size, self.x, self.y = a