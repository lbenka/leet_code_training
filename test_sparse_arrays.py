# https://www.hackerrank.com/challenges/sparse-arrays/problem
import pytest 

def matchingStrings(strings, queries):
    results = [0 for e in range(len(queries))]
    for index, q in enumerate(queries): 
        for s in strings: 
            if q == s: 
                results[index] += 1

    return results 


@pytest.mark.parametrize(
    "strings, queries, output", [
        (["aba","baba", "aba", "xzxb"], ["aba","xzxb","ab"], [2,1,0])
    ]
)
def test_match_strings(strings, queries, output):
    assert matchingStrings(strings, queries) == output