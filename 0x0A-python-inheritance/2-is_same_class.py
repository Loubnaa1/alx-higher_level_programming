#!/usr/bin/python3
""" Contains is_same_class function """


def is_same_class(obj, a_class):
    """ function checking if the object is an instance or not

    Args:
    obj:  the object to check
    a_class: class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
