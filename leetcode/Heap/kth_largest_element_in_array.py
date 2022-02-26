"""
Problem Statement

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
------------------------------------------------------------------------------------------------------------------------
"""
import heapq
from typing import List

import pytest


# Solution class goes here
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k)

    def solve(self, nums, k):
        min_heap = [nums[i] for i in range(k)]
        heapq.heapify(min_heap)
        for idx in range(k, len(nums)):
            if nums[idx] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[idx])
        return min_heap[0]


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    pytest.param(([3, 2, 1, 5, 6, 4], 2), 5),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
