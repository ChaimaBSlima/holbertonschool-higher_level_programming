#!/usr/bin/python3
"""
    task 4 class square
"""


class Square:
    """
    Define a class Square.
    """

    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return (self._Square__size)

    @size.setter
    def size(self, value):
        """
        size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        return (self._Square__size**2)
