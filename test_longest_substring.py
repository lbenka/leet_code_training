import pytest 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_len = 0 
        
        for c in s: 
            if c not in substring: 
                substring += c 
            else:
                new_sub = ""
                for s in substring[::-1]:
                    if s != c: 
                        new_sub += s 
                    else: 
                        break

                substring = new_sub[::-1] + c 
        
            if len(substring) > max_len:
                max_len = len(substring)

        return max_len 

@pytest.mark.parametrize(
    "input, output", [("pwwkew", 3), ("aab", 2), ("dvdf", 3), ("abcabcbb", 3)]
)
def test_solution(input, output):
    assert Solution().lengthOfLongestSubstring(input) == output
