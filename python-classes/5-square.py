#!/usr/bin/python3
"""
    task 5 class square
"""


class Square:
    """ Define a class Square."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size
        """
        if (type(value) != int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return (self.__size**2)

    def my_print(self):
        if self.__size is 0:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                print('{}'.format('#'), end="")
            print()
