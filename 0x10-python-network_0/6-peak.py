#!/usr/bin/python3
""" contains find_peak function """

def find_peak(list_of_integers):
    """ Function to find a peak element in an unsorted list of integers. """

    leng = len(list_of_integers)
    if leng == 0:
        return None
    if leng == 1:
        return nums[0]
    if leng == 2:
        return max(list_of_integers)

    tmp = leng // 2

    if list_of_integers[tmp] >= list_of_integers[tmp - 1] and list_of_integers[tmp] >= list_of_integers[tmp + 1]:
        return list_of_integers[tmp]

    if tmp > 0 and list_of_integers[tmp] < list_of_integers[tmp - 1]:
        return find_peak(list_of_integers[:tmp])

    if tmp < leng - 1 and list_of_integers[tmp] < list_of_integers[tmp + 1]:
        return find_peak(list_of_integers[tmp + 1:])

