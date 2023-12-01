#!/usr/bin/python3
"""find_peak function script"""

def find_peak(list_of_integers):
    """Function to find a peak element in an unsorted list."""

    a, b = 0, len(list_of_integers) - 1

    if b == -1:
        return None

    while a < b:
        tmp = (a + b) // 2
        if list_of_integers[tmp] < list_of_integers[tmp + 1]:
            a = tmp + 1
        else:
            b = tmp

    return list_of_integers[a]
