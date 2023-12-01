#!/usr/bin/python3
"""find_peak function script"""

def find_peak(list_of_integers):
    """
    Function to find a peak element in an unsorted list of integers.
    Uses a binary search approach, giving a time complexity of O(log(n)).
    """

    left, right = 0, len(list_of_integers) - 1

    if right == -1:  # This will be true if list_of_integers is empty
        return None

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

