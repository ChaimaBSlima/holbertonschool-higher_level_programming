#!/usr/bin/python3
""" python-almost_a_circle project: Module for Rectangle
    starting at task 2
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): x
            y(int): y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.testing_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.testing_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ the unknown x """
        return self.__x

    @x.setter
    def x(self, value):
        self.testing_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """ the unknown y """
        return self.__y

    @y.setter
    def y(self, value):
        self.testing_integer("y", value)
        self.__y = value

    def testing_integer(self, variable, value, test=True):
        """ Testing the integers and tracking
        errors like it was demanded in task 3
        """
        if type(value) is not int:
            raise TypeError(variable, "must be an integer")
        if test and value < 0:
            raise ValueError(variable, "must be >= 0")
        elif not test and value <= 0:
            raise ValueError(variable, "must be >= 0")
