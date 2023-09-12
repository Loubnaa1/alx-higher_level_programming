#!/usr/bin/python3
""" contains inherits_from function """


def inherits_from(obj, a_class):
    """ function that return True if :
    obj is an instance or inherited instance of a_class

    else it return False
    """

    if obj.__class__ == a_class:
        return False
    if issubclass(obj.__class__, a_class):
        return True
    else:
        return False
