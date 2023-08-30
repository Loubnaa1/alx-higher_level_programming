#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ Square class is created"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize.
        Args:
                size (int): size of new square
                position : position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the value"""
        if isinstance(value, int):
            self.__size = value
        else:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the new position of a square """
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and
                value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the square area"""
        return self.__size ** 2

    def my_print(self):
        """ Print the square with the carracter #"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)