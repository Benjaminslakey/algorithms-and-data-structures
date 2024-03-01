import pytest

"""
# Problem Statement

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

------------------------------------------------------------------------------------------------------------------------

# Constraints

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 
------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false 

------------------------------------------------------------------------------------------------------------------------

# Walk Through
"abc", "ahbgdc"
 ^      ^
"abc", "ahbgdc"
  ^      ^
"abc", "ahbgdc"
  ^       ^

"abc", "ahbgdc"
   ^       ^

"abc", "ahbgdc"
   ^        ^
"abc", "ahbgdc"
   ^         ^
------------------------------------------------------------------------------------------------------------------------

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

I think a trie would work here for the follow up, that way instead of having to check (s + t)k you could build the trie once and then only do s*k checks
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.isSubsequence(*input_args)

    def isSubsequence(self, s, t):
        return self.simple(s, t)

    def simple(self, s, t):
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        return si == len(s)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(("abc", "ahbgdc"), True),
    pytest.param(("axc", "ahbgdc"), False),
    pytest.param(("aalci", "ahbgdcaxiuslasdfkjclafdasilll"), True),
    pytest.param(("", ""), True),
    pytest.param(("", "T"), True),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output

