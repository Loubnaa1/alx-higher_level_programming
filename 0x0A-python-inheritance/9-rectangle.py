#!/usr/bin/python3
""" contains Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class is created """

    def __init__(self, width, height):
        """ initialization """

        super().integer_validator("height", height)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculates the area of a rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ returns representation of a rectangle """

        return f"[Rectangle] {self.__width}/{self.__height}"
