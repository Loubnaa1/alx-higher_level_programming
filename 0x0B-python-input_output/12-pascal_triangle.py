#!/usr/bin/python3
"""containing function called pascal_triangle"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []
    list = [[1]]
    for i in range(n-1):
        triangle = [1]
        for j in range(i):
            triangle.append(list[i-1][j-1] + list[i-1][j])
        triangle.append(1)
        list.append(triangle)
    return list