# import pytest


def diagonalDifference(arr):
    size_of_matrix = len(arr) - 1
    r = 0
    r2 = 0
    for index, x in enumerate(arr):
        r += x[index]
        r2 += x[size_of_matrix - index]

    return abs(r - r2)



def test_ds():
    inp = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    assert diagonalDifference(inp) == 15
