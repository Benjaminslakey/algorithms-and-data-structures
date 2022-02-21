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
from collections import Counter, defaultdict
from typing import List

import pytest


class Solution:
    """
    would be good to clarify whether or not all strings in the input are of the same length
        if not would want to pre process the strings and bucket them into same length buckets
    will the letters in the strings be unique within a given string
        (probably not but if they are then we can simplify comparison between strings)

    convert each word into a count dict and compare that way
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.optimized__w_hashing(strs)

    def optimized__w_hashing(self, strs):
        hash_map = defaultdict(list)
        for idx, possible_anagram in enumerate(strs):
            hash_map["".join(sorted(possible_anagram))].append(strs[idx])
        return list(hash_map.values())

    def naive(self, strs):
        letter_counts = [Counter(possible_anagram) for possible_anagram in strs]
        result = []
        used = set()
        for i, count in enumerate(letter_counts):
            bucket = []
            for j in range(i, len(letter_counts)):
                if j in used:
                    continue
                elif count == letter_counts[j]:
                    bucket.append(strs[j])
                    used.add(j)
            if bucket:
                result.append(bucket)
        return result


@pytest.mark.parametrize('strs, expected', [
    pytest.param(["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    pytest.param([""], [[""]]),
    pytest.param(["a"], [["a"]]),
])
def test_group_anagrams(strs, expected):
    solver = Solution()
    result = solver.groupAnagrams(strs)
    assert not strs[0] or sorted(
        [sorted(sub_expected, key=lambda x: x[0]) for sub_expected in expected],
        key=lambda x: x[0]
    ) == sorted(
        [sorted(sub_result, key=lambda x: x[0]) for sub_result in result],
        key=lambda x: x[0]
    )
