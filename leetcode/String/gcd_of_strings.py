import pytest

"""
Problem Statement

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
------------------------------------------------------------------------------------------------------------------------
"""

# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.gcdOfStrings(*input_args)

    def gcdOfStrings(self, str1, str2):
        prefixes = {}
        seen = set()
        for char in str1:
            if char in seen:
                pass
        return


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(("ABCABC", "ABC"), "ABC"),
    pytest.param(("ABABAB", "ABAB"), "AB"),
    pytest.param(("LEET", "CODE"), ""),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
