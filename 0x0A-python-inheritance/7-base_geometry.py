#!/usr/bin/python3
""" Contains class BaseGeometry."""


class BaseGeometry:
    """class base geometry."""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks a parameter as an integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
