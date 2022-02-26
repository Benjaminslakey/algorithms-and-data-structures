"""
Problem Statement

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of
    a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


------------------------------------------------------------------------------------------------------------------------
Constraints

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

------------------------------------------------------------------------------------------------------------------------
"""
from typing import List

import pytest


# Solution class goes here
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.solve(nums, target)

    def solve(self, nums, target):
        def bisect_left(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if start == end and nums[mid] != target:
                    return -1
                if nums[mid] == target and (mid == start or nums[mid - 1] < target):
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid
            return -1

        def bisect_right(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if start == end and nums[mid] != target:
                    return -1
                if nums[mid] == target and (mid == end or nums[mid + 1] > target):
                    return mid
                elif nums[mid] > target:
                    end = mid
                else:
                    start = mid + 1
            return -1

        range_start = bisect_left(nums, target)
        range_end = bisect_right(nums, target)
        return [range_start, range_end]


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    pytest.param(([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    pytest.param(([], 0), [-1, -1]),
    pytest.param(([2, 2], 2), [0, 1]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
