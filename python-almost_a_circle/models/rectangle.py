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
            raise TypeError("{} must be an integer".format(variable))
        if test and value < 0:
            raise ValueError("{} must be >= 0".format(variable))
        elif not test and value <= 0:
            raise ValueError("{} must be > 0".format(variable))

    def area(self):
        """ task 4: calculate the rectangle area """
        return (self.width * self.height)

    def display(self):
        "Task 5 and 7: represent the rectangle with #"
        A = '\n' * self.y
        B = ' ' * self.x
        C = '#' * self.width
        D = A + (B + C + '\n') * self.height
        print(D, end='')

    def __str__(self):
        "Task 6: return string informations"
        return ('[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__,
            self.id, self.x,
            self.y, self.width,
            self.height))

    def hidden_update(self, id=None, width=None, height=None, x=None, y=None):
        """ update instance attributes via */**args"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Task 8 and 9 : update instance attributes
        via no-keyword and keyword argument
        """

        if args:
            self.hidden_update(*args)
        elif kwargs:
            self.hidden_update(**kwargs)

    def to_dictionary(self):
        """ Task 13: Return the dictionary representation
        of a Rectangle
        """
        chaima = {"id": self.id, "width": self.__width,
                  "height": self.__height, "x": self.__x, "y": self.__y}
        return (chaima)
