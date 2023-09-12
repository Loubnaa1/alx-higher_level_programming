#!/usr/bin/python3
""" contains a class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """definning a square."""

    def __init__(self, size):
        """Initialization a new square."""
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
