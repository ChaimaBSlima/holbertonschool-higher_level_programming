#!/usr/bin/python3
"""
    task 5 class square
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return (self.__size**2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        size
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
