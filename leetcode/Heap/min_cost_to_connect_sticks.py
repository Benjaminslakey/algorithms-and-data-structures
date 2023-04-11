"""
Problem Statement
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.
------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= sticks.length <= 104
1 <= sticks[i] <= 104

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

Example 2:
Input: sticks = [1,8,3,5]
Output: 30
Explanation: You start with sticks = [1,8,3,5].
1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.

Example 3:
Input: sticks = [5]
Output: 0
Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.
------------------------------------------------------------------------------------------------------------------------
"""
import heapq
from typing import List

import pytest


# Solution class goes here
class Solution:
    """
    The important things to realize here is that
        to minimize total cost, you want to pay for connecting the expensive sticks as few times as possible
        to do that we only want to connect them at the very end
        once you have combined some sticks into a single stick, every combination you do from there, you will pay the
        cost of all previously connected sticks again. so to minimize uses of the expensive sticks we want to use the
        cheapest sticks available at every turn. This is a greedy algorithm
    """

    def connectSticks(self, sticks: List[int]) -> int:
        return self.solve(sticks)

    def solve(self, sticks):
        heapq.heapify(sticks)
        combine_cost = 0
        while len(sticks) > 1:
            cheapest_stick, second_cheapest_stick = heapq.heappop(sticks), heapq.heappop(sticks)
            new_stick = cheapest_stick + second_cheapest_stick
            combine_cost += new_stick
            heapq.heappush(sticks, new_stick)
        return combine_cost


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([2, 4, 3],), 14),
    pytest.param(([1, 8, 3, 5],), 30),
    pytest.param(([5],), 0),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
