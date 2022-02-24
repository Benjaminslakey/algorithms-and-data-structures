"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

from collections import defaultdict

import pytest


class Solution:
    """
    record last seen location of each character, if we see a repeated character
    skip foward past the last occurrence of it
    record maximum achieved length
    "pwwkew"
    "abcabcbb"
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        last_position = {}
        l, r = 0, 0
        while r < len(s):
            if s[r] not in last_position:
                longest = max(longest, r - l + 1)
                last_position[s[r]] = r
                r += 1
            else:
                next_l = last_position[s[r]] + 1
                for i in range(l, next_l):
                    del last_position[s[i]]
                l = next_l
        return longest


@pytest.mark.parametrize('s, expected', [
    pytest.param("abcabcbb", 3),
    pytest.param("bbbbb", 1),
    pytest.param("pwwkew", 3),
    pytest.param("wwwwxpzjwbpdx", 7),
])
def test_longest_unique_char_substring(s, expected):
    solver = Solution()
    result = solver.lengthOfLongestSubstring(s)
    assert result == expected
