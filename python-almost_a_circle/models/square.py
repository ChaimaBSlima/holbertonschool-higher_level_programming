#!/usr/bin/python3
""" python-almost_a_circle project: Module for square
    starting at task 10
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            size (int): size of the side of the square.
            x (int): x
            y(int): y
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "Task 10:  return string informations"
        return ('[{}] ({}) {}/{} - {}'.format(
            type(self).__name__,
            self.id, self.x,
            self.y, self.width,))

    @property
    def size(self):
        """Get the size of the square."""
        return self.__width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value
