#!/usr/bin/python3

"""Defining matrix mul"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the result

    Args:
        m_a: a list of lists of the first matrix
        m_b: a list of lists of the second matrix
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or \
       not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(n, (int, float)) for row in m_a for n in row) or \
       not all(isinstance(n, (int, float)) for row in m_b for n in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1 or \
       len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            e = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(e)
        res.append(row)
    return res

