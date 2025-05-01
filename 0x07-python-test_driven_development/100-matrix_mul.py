#!/usr/bin/python3
"""This module is for the matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""
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

    final_result = []
    i = 0
    j = 0
    k = 0
    p = 0
    for m in range(len(m_a)):
        final_result_row = []
        for n in range(len(m_b[0])):
            result = 0
            for b in range(len(m_b)):
                result += m_a[i][j]*m_b[k][p]
                j += 1
                k += 1
            j = 0
            k = 0
            p += 1
            final_result_row.append(result)
        final_result.append(final_result_row)
        p = 0
        i += 1
    return final_result
