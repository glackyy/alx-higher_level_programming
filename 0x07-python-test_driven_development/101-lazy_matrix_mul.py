#!/usr/bin/python3

"""Defining a matrix multiplication using NumPy"""
import numpy as np



def lazy_matrix_mul(m_a, m_b):
    """Return the mul of two matrices

    Args:
        m_a list: the first matrix
        m_b list: the second matrix
    """
    return np.matmul(m_a, m_b)
