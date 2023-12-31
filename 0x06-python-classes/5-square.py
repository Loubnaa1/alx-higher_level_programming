#!/usr/bin/python3
""" class Square that defines a square:"""


class Square:
    """ class Square """
    def __init__(self, size=0):
        """initial"""
        self.__size = size

    @property
    def size(self):
        """return the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * 2)

    def my_print(self):
        """print the square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
