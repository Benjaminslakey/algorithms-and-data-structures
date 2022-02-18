"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List

import pytest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass


@pytest.mark.parametrize('strs, expected', [
    pytest.param(["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    pytest.param([""], [[""]]),
    pytest.param(["a"], [["a"]]),
])
def test_group_anagrams(strs, expected):
    solver = Solution()
    result = solver.groupAnagrams(strs)
    assert result == expected
