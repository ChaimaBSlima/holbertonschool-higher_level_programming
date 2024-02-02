#!/usr/bin/python3
"""
    task 2 class square
"""


class Square:
    """ Defining a Square size """
    def __init__(self, size=0):
        """Initialize a Square.
        Args:
            size: The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
