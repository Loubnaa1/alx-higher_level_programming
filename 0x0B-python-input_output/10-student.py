#!/usr/bin/python3
""""contains a class Student"""


class Student:
    """represent student"""

    def __init__(self, first_name, last_name, age):
        """initialization with arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving a dictionary representation
        of a Student"""
        if attrs is None:
            return self.__dict__
        new_dic = {}
        for attr in attrs:
            if attr in self.__dict__:
                new_dic = getattr(self, attr)
        return new_dic
