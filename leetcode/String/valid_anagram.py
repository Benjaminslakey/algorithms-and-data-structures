"""
Problem Statement

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
------------------------------------------------------------------------------------------------------------------------
Constraints

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
------------------------------------------------------------------------------------------------------------------------
"""

import pytest

from collections import Counter


# Solution class goes here
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.hashmap_solution(s, t)

    def hashmap_solution(self, s, t):
        s_counts, t_counts = Counter(s), Counter(t)
        for char in s:
            if s_counts[char] != t_counts[char]:
                return False
        return len(s_counts.keys()) == len(t_counts.keys())


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(("anagram", "nagaram"), True),
    pytest.param(("dfkjls", "jds"), False),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.isAnagram(*input_args)
    assert result == expected_output
