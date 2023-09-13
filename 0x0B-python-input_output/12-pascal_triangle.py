#!/usr/bin/python3
"""containing function called pascal_triangle"""


def pascal_triangle(n):
    """ pascal triangle function """

    if n <= 0:
        return []
    list_1 = [[1]]
    for i in range(n-1):
        list_2 = [1]
        for j in range(i):
            list_2.append(list_1[-1][j] + list_1[-1][j+1])
        list_2.append(1)
        list_1.append(list_2)
    return list_1
