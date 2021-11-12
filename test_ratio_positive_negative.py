#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    p = 0
    n = 0
    zero = 0
    for num in arr:
        if num > 0:
            p += 1
        elif num < 0:
            n += 1
        else:
            zero += 1
    return (p / len(arr), round(n / len(arr), 6), round(zero / len(arr), 6))


def test_pnr():
    arr = [-4, 3, -9, 0, 4, 1]
    assert plusMinus(arr) == (0.500000, 0.333333, 0.166667)
