import pytest 


# We define a magic square to be an n*n matrix of distinct positive integers from 1 to 9 where the sum of any row,
# column, or diagonal of length  is always equal to the same number: the magic constant.

# You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit
# in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range .


def formingMagicSquare(s):
    pass

@pytest.mark.skip("not solved")
def test_ms():
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    new_lists = separate(s)
    all_l = new_lists + s

    sums = [sum(l) for l in all_l]

    result = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]

    new_lists = separate(result)
    all_l_2 = new_lists + result
    sums2 = [sum(l) for l in all_l_2]

    assert formingMagicSquare(s) == (4, result)


def separate(matrix):
    new_rows = [[], [], []]

    for index, new_r in enumerate(new_rows):
        for row in matrix:
            new_r.append(row[index])

    diagonal = [[], []]
    for index, row in enumerate(matrix):
        diagonal[0].append(row[index])
        diagonal[1].append(row[len(matrix) - (index + 1)])

    return new_rows + diagonal
