#!/usr/bin/python3
"""task 3: 3. String representation"""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """


    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialize a  Rectangle.

        Args:
            width (int): The width of the  rectangle.
            height (int): The height of the  rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        chaima = []
        for i in range(self.__height):
            [chaima.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                chaima.append("\n")
        return ("".join(chaima))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        chaima = "Rectangle(" + str(self.__width)
        chaima += ", " + str(self.__height) + ")"
        return (chaima)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
