#!/usr/bin/python3

import numpy as np\

"""Defines a matrix multiplication function using NumPy."""
'''
File_name:
Created: 5-DEC-2023
Author: UMUTONI Kevine (simplykevine)
Size: Large
Project: python-test_driven_development
Status: Not yet submted
'''


def lazy_matrix_mul(m_a, m_b):

    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
