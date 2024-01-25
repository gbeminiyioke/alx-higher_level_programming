#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_cpy = [row[:] for row in matrix]
    for i, row in enumerate(matrix_cpy):
        for j, col in enumerate(matrix_cpy):
            matrix_cpy[i][j] = row[j] ** 2
    return matrix_cpy
