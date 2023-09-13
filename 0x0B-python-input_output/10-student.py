#!/usr/bin/python3
""""contains a class Student"""


class Student:
    """represent student"""

    def __init__(self, first_name, last_name, age):
        """initialization with arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieving a dictionary representation
        of a Student"""
        if attr is None:
            return self.__dict__
        new_dic = {}
        for attrs in attr:
            if attrs in self.__dict__:
                new_dic.update({attrs: self.__dict__[attrs]})
        return new_dic
