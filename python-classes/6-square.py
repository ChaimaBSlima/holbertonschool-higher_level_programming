#!/usr/bin/python3
"""
    task 6 class square
"""


class Square:
    """ Define a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """position method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""
        if (type(value) is not tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (type(value[0]) and type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """return square area"""
        return (self.__size**2)

    def my_print(self):
        """prints square with the char #"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end='')
                print('#' * self.size)
