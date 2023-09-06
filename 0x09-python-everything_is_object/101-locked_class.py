#!/usr/bin/python3
"""Defining a class called LockedClass."""


class LockedClass:
    """
    Preventing the user from creation new LockedClass attributes
    for anything except for'first_name'.
    """

    __slots__ = ["first_name"]
