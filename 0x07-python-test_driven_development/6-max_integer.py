#!/usr/bin/python3
"""
containing function that return the max integer in a list
"""


def max_integer(list=[]):
    """returning the maximum of a list"""
    if len(list) == 0:
        return None
    max = list[0]
    i = 1
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max
