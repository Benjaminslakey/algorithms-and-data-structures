"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
    such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [10,7,9,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

[10,7,9,5,0,4,6]
[10,7,9,5,0,10]
"""
from typing import List

import pytest


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.linear(nums)

    def linear(self, nums):
        first_num = float("inf")
        second_num = float("inf")
        for num in nums:
            if num > second_num:
                return True
            if num <= first_num:
                first_num = num
            elif num < second_num:
                second_num = num
        return False

    def tis(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            longest_from_i = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest_from_i = max(longest_from_i, dp[j])
            dp[i] = 1 + longest_from_i
            if longest_from_i + 1 >= 3:
                return True
        return False

    def naive(self, nums):
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False


@pytest.mark.parametrize('nums, expected', [
    pytest.param([1, 2, 3, 4, 5], True),
    pytest.param([5, 4, 3, 2, 1], False),
    pytest.param([2, 1, 5, 0, 4, 6], True),
    pytest.param([20, 100, 10, 12, 5, 13], True),
    pytest.param([1, 1, -2, 6], False)
])
def test(nums, expected):
    solver = Solution()
    result = solver.increasingTriplet(nums)
    assert result == expected
