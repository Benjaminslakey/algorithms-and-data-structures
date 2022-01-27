from collections import defaultdict
from typing import List

import pytest

from bts_lib.disjoint_set import DisjointSet


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjoint_set = DisjointSet()
        for idx in range(0, len(s)):
            disjoint_set.add(idx)
        for vertex_one, vertex_two in pairs:
            disjoint_set.union(vertex_one, vertex_two)

        components = defaultdict(list)
        for idx in range(0, len(s)):
            parent = disjoint_set.find(idx)
            components[parent].append(s[idx])
        for key in components.keys():
            components[key].sort(reverse=True)
        output = ""
        for idx in range(0, len(s)):
            parent = disjoint_set.find(idx)
            output += components[parent].pop()
        return output


@pytest.mark.parametrize('string, pairs, expected_smallest_string', [
    pytest.param("dcab", [[0, 3], [1, 2]], "bacd"),
    pytest.param("dcab", [[0, 3], [1, 2], [0, 2]], "abcd"),
    pytest.param("cba", [[0, 1], [1, 2]], "abc"),
])
def test_smallest_string_with_swaps(string, pairs, expected_smallest_string):
    solver = Solution()
    result = solver.smallestStringWithSwaps(string, pairs)
    assert result == expected_smallest_string
