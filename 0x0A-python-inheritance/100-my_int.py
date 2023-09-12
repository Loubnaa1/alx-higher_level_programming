#!/usr/bin/python3
""" contains a class  MyInt that inherits from int"""


class MyInt(int):
    """ MyInt class is created """
    def __eq__(self, value):
        """ with != behavior """
        return not super().__eq__(value)

    def __ne__(self, value):
        """ with == behavior """
        return not super().__ne__(value)
