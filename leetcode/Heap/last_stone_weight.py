"""
Problem Statement

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= stones.length <= 30
1 <= stones[i] <= 1000
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

------------------------------------------------------------------------------------------------------------------------
"""
import heapq
from typing import List

import pytest


# Solution class goes here
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return self.solve(stones)

    def solve(self, stones):
        max_heap = [-1 * weight for weight in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            heaviest, second_heaviest = heapq.heappop(max_heap) * -1, heapq.heappop(max_heap) * -1
            if heaviest != second_heaviest:
                remaining_stone_weight = heaviest - second_heaviest
                heapq.heappush(max_heap, -1 * remaining_stone_weight)
        return max_heap[0] * -1 if max_heap else 0


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([2, 7, 4, 1, 8, 1],), 1),
    pytest.param(([1],), 1),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
