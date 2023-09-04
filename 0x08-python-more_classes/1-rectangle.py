#!/usr/bin/python3
"""Class defining a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """ initialization """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ returning width of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ setting a value to the width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returning the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting a value to the width """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
