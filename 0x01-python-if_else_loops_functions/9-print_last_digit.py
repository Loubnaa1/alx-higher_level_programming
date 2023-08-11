#!/usr/bin/python3
def print_last_digit(number):
    a = abs(number) % 10
    print("{:d}".format(a), end='')
    return a
