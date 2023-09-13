#!/usr/bin/python3
"""containing function called pascal_triangle"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []
    list_n = [[1]]
    for i in range(n-1):
        triangle_l = [1]
        for j in range(i):
            triangle_l.append(list_n[-1][j] + list_n[1][j+1])
        triangle_l.append(1)
        list_n.append(triangle_l)
    return list_n
