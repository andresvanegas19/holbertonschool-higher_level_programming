#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a kinf of figure but it has another specifics"""

    def __init__(self, size, x=0, y=0, id=None):
        """this is for start the variables"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is for string"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """the getter to get the value"""
        return self.width

    @size.setter
    def size(self, value):
        """the setter to set the value"""
        self.evaluated(value, 'width')
        self.width = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute and update it"""
        a = [self.id, self.width, self.x, self.y]
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
        self.id, self.width, self.x, self.y = a

    def to_dictionary(self):
        """it will make a dictionary with keys"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
