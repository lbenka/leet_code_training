# import pytest
# https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true

def rotateLeft(d, arr):
    if d > len(arr): 
        start_index = len(arr) % d
    else: 
        start_index = d

    return arr[start_index:] + arr[:start_index]



def test_rotate():
    d = 2
    arr = [1, 2, 3, 4, 5]

    assert rotateLeft(d, arr) == [
        3,
        4,
        5,
        1,
        2,
    ]
