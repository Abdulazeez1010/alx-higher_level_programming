#!/usr/bin/python3
"""This module multiplies 2 matrices by using the module NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')
    if not (len(m_a[0]) == len(m_b)):
        raise ValueError('m_a and m_b can\'t be multiplied')
    return np.dot(m_a, m_b)
