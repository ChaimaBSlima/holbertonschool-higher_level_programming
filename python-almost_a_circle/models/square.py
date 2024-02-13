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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def hidden_update(self, id=None, size=None, x=None, y=None):
        """ update instance attributes via */**args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Task 12 : update instance attributes
        via no-keyword and keyword argument
        """

        if args:
            self.hidden_update(*args)
        elif kwargs:
            self.hidden_update(**kwargs)

    def to_dictionary(self):
        """ Task 14: Return the dictionary representation
        of a square
        """
        chaima = {"id": self.id, "size": self.width,
                  "x": self.x, "y": self.y}
        return (chaima)
