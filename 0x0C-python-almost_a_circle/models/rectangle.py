#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """This will a iritante of Base and contain some usefull funtions"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this is for start the variables"""
        super().__init__(id)
        self.width = self.evaluated(width, 'width')
        self.height = self.evaluated(height, 'height')
        self.x = self.evaluated(x, 'x')
        self.y = self.evaluated(y, 'y')

    @staticmethod
    def evaluated(value, name):
        """ This will check the value if is a int otherwise raise error"""
        val = ['x', 'y']
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            if name in val:
                if value == 0:
                    return value
                else:
                    raise ValueError('{} must be >= 0'.format(name))
            else:
                raise ValueError('{} must be > 0'.format(name))
        return value

    @staticmethod
    def evaluatedXY(value, name):
        """ This will check the value if is a int otherwise raise error"""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        return value

    @property
    def width(self):
        """ This is for get the value
        :return return the private value"""
        return self.__width

    @property
    def height(self):
        """ This is for get the value
        :return return the private value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ This will check the value if is a int otherwise raise error"""
        self.evaluated(value, 'height')
        self.__height = value

    @property
    def x(self):
        """This will set the value"""
        return self.__x

    @x.setter
    def x(self, value):
        """ This will check the value if is a int otherwise raise error"""
        self.evaluated(value, 'x')
        self.__x = value

    @property
    def y(self):
        """acces to the function"""
        return self.__y

    @width.setter
    def width(self, value):
        """ This will check the value if is a int otherwise raise error"""
        self.evaluated(value, 'width')
        self.__width = value

    @y.setter
    def y(self, value):
        """ This will check the value if is a int otherwise raise error"""
        self.evaluated(value, 'y')
        self.__y = value

    def area(self):
        """find th area
        :return the area value of the Rectangle instance."""
        return self.__width * self.__height

    def __str__(self):
        """this is for return a string"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """This print a rectangle"""
        for _ in range(self.__y):
            print(end='\n')
        for _ in range(self.__height):
            spaces = ''.join(' ' for _ in range(self.__x))
            char = ''.join('#' for _ in range(self.__width))
            # print('space', spaces, 'char',char)
            print('{}{}'.format(spaces, char))
        return

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute and update it"""
        a = [self.id, self.__width, self.__height, self.__x, self.__y]
        err = ['id', 'width', 'height', 'x', 'y']
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
        self.id, self.__width, self.__height, self.__x, self.__y = a

    def to_dictionary(self):
        """it will make a dictionary with keys"""
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
