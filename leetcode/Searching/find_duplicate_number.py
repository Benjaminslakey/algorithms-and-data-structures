"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated Math in nums, return this repeated Math.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:
How can we prove that at least one duplicate Math must exist in nums?

by checking that the sum of the array is lower than the expected sum

Can you solve the problem in linear runtime complexity?

tortoise and hare, fast and slow pointer algorithm
treating values in array as pointers to other array indices
"""
from typing import List

import pytest


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.floyds_tortoise_and_hare(nums)

    def two_loops(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

    def floyds_tortoise_and_hare(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        # find cycle
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        # determine link that begins cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise


@pytest.mark.parametrize('nums, repeated', [
    pytest.param([1, 3, 4, 2, 2], 2),
    pytest.param([1, 2, 3, 3, 4], 3),
    pytest.param([1, 1, 1, 1, 3], 1),
    pytest.param([3, 1, 3, 4, 2], 3),
])
def test_find_duplicate(nums, repeated):
    solver = Solution()
    result = solver.findDuplicate(nums)
    assert result == repeated
