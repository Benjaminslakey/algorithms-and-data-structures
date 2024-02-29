import pytest

"""
Problem Statement

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

------------------------------------------------------------------------------------------------------------------------
Constraints


1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

------------------------------------------------------------------------------------------------------------------------
Examples


Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
          ^     ^
          e     e
           ^  ^
           e  o
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.reverseVowels(*input_args)

    def reverseVowels(self, s):
        lower_vowels = ['a', 'e', 'i', 'o', 'u']
        vowels = set()
        for v in lower_vowels:
            vowels.add(v)
            vowels.add(v.upper())
        i, j = 0, len(s) - 1
        to_reverse = list(s)
        while i < j:
            if to_reverse[i] not in vowels:
                i += 1
            if to_reverse[j] not in vowels:
                j -= 1
            if to_reverse[i] in vowels and to_reverse[j] in vowels:
                to_reverse[i], to_reverse[j] = to_reverse[j], to_reverse[i]
                i, j = i + 1, j - 1
        return ''.join(to_reverse)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(('leetcode',), 'leotcede'),
    pytest.param(('worde',), 'werdo'),
    pytest.param(('hello',), 'holle'),
    pytest.param(('responsibility',), 'rispinsibolety'),
    pytest.param((' ',), ' '),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output

