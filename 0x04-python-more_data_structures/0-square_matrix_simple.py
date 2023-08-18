#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        res = []
        for j in i:
            res.append(j**2)
        new_matrix.append(res)
    return new_matrix
