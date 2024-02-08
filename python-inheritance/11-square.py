#!/usr/bin/python3
"""task 11: 11. Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
