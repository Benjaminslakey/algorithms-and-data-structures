from collections import defaultdict

import pytest


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        s1_positions = defaultdict(list)
        s2_positions = defaultdict(list)
        for idx, char in enumerate(str1):
            s1_positions[char].append(idx)
        for idx, char in enumerate(str2):
            s2_positions[char].append(idx)
        # we need to be able to use an additional character as a go between when translating from two strings
        # of entirely unique characters with the same ordering, that may be rotated, if we don't have an additional char
        # we can't do that
        if set(s1_positions.keys()) == set(s2_positions.keys()) and len(str1) == 26:
            return False
        # speed up matching up equal index sets by O(1) dict access by same first index instead of iterating through
        # each list to compare
        idx_list_by_first = {}
        for idx_list in s2_positions.values():
            first_idx = idx_list[0]
            idx_list_by_first[first_idx] = idx_list
        # remove characters that can be directly mapped to another, determined by having occurrences at the same indices
        for s1_char, s1_idx_list in list(s1_positions.items()):
            first = s1_idx_list[0]
            s2_idx_list = idx_list_by_first[first]
            if not s2_idx_list:
                continue
            s2_char = str2[s2_idx_list[0]]
            if len(s1_idx_list) != len(s2_idx_list):
                continue
            if s1_idx_list == s2_idx_list:
                s2_positions.pop(s2_char)
                s1_positions.pop(s1_char)
        # convert back to regular dict to we don't re-add deleted mappings by accessing them later on
        s1_positions = dict(s1_positions)
        s2_positions = dict(s2_positions)
        # see if any combinations of two sets match a set in the other string
        # ex 'yz': {y: {0}, z: {1}} 'zz': {z: {0, 1}}
        s1_keys = list(s1_positions.keys())
        for i, s1_char in enumerate(s1_keys):
            s1_idx_list_1 = s1_positions[s1_char]
            s1_set_1 = set(s1_idx_list_1)

            while i < len(s1_keys):
                if i + 1 < len(s1_keys):
                    s1_idx_list_2 = s1_positions[s1_keys[i + 1]]
                    s1_set_1 |= set(s1_idx_list_2)
                for s2_char, s2_idx_list in s2_positions.items():
                    if s1_set_1 == set(s2_idx_list):
                        s2_positions.pop(s2_char)
                        s1_positions.pop(s1_char)
                        if i + 1 < len(s1_keys):
                            s1_positions.pop(s1_keys[i + 1])
                        break
                i += 1
        return not s1_positions and not s2_positions


@pytest.mark.parametrize('str1, str2, expected', [
    pytest.param("ab", "ba", True),
    pytest.param("aabcc", "ccdee", True),
    pytest.param("leetcode", "codeleet", False),
    pytest.param("abcdefghijklmnopqrstuvwxyz", "bcadefghijklmnopqrstuvwxzz", True),
    pytest.param("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza", False),
    pytest.param("abcdefghijklmnopqrstuvwxyz", "bcdefghijkamnopqrstuvwxyzl", False),

])
def test_can_convert(str1, str2, expected):
    solver = Solution()
    result = solver.canConvert(str1, str2)
    assert result == expected

