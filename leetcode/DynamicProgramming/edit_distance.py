from collections import deque
from typing import List

import pytest


class Solution:
    """
    subproblem:
        f(word1[i:], word2[j:]) => suffixes
    recurrence relation:
        f(word1[i + 1])
    topological order:
    base cases:
        if
    original:
    time complexity:
    """

    def minDistance(self, word1: str, word2: str) -> int:
        pass

    def top_down_dp(self, word1, word2, i, j):
        pass

    def bottom_up_dp(self):
        pass


@pytest.mark.parametrize('word1, word2, expected_distance', [
    pytest.param('horse', 'ros', 3),
    pytest.param('intention', 'execution', 5),
])
def test_edit_distance(word1, word2, expected_distance):
    solver = Solution()
    distance = solver.minDistance(word1, word2)
    assert distance == expected_distance
