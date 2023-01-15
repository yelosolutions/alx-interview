#!/usr/bin/python3
'''
Pascal's triangle
'''


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing\
    the Pascal's triangle of n or an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
