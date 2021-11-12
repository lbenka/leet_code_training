from typing import List
import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        first_word = strs.pop()

        while len(first_word) > 0:
            success = False

            for word in strs:
                if not word.startswith(first_word):
                    success = False
                    break
            
                success = True

            if not success:
                first_word = first_word[:-1]
            else:
                return first_word

        return ""


@pytest.mark.parametrize(
    "input, output", [(["dog", "racecar", "car"], ""), (["flower", "flow", "flight"], "fl"), (["a"], "a"), (["aaa","aa","aaa"], "aa")]
)
def test_solution(input, output):
    assert Solution().longestCommonPrefix(input) == output
