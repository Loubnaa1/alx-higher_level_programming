#!/usr/bin/python3
"""contains a subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """definning a square."""

    def __init__(self, size):
        """Initialization """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
