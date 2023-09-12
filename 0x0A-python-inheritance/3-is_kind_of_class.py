#!/usr/bin/python3
""" contains is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ function that return True if :
    obj is an instance or inherited instance of a_class

    else it return False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
