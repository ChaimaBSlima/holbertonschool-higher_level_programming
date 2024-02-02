#!/usr/bin/python3
"""
    task 3 class square
"""


class Square:
    """ Defining a Square """
    def __init__(self, size=0):
        """ Initialize a square.

        Args:
            size: The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the current area of the square. """
        return (self.__size * self.__size)
