#!/usr/bin/python3
"""Task 12: 12. Pascal's Triangle """


def pascal_triangle(n):
    """a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if (n <= 0):
        return []

    triangles = [[1]]
    while len(triangles) != n:
        chaima = triangles[-1]
        tmp = [1]
        for i in range(len(chaima) - 1):
            tmp.append(chaima[i] + chaima[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
