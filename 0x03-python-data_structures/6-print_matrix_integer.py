#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        print(" ".join("{:d}".format(element) for element in r))
    return
