#!/usr/bin/python3
""" contains a class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """definning a square."""

    def __init__(self, size):
        """Initialization a new square."""

        Rectangle.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """ calculates the square area """
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
