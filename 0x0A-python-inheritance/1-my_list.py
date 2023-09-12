#!/usr/bin/python3
""" contains MyList class"""


class MyList(list):
    """ Created list"""

    def print_sorted(self):
        """function that prints a sorted list"""
        print(sorted(self))
