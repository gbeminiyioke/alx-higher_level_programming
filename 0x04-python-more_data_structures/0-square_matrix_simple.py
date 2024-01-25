#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [itm[:] for itm in matrix]
    for i, itm in enumerate(new_matrix):
        for j, itm2 in enumerate(new_matrix):
            new_matrix[i][j] = itm[j] ** 2
    return new_matrix
