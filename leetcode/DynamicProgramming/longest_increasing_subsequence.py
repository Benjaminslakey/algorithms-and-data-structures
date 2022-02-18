"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

from typing import List

import pytest


class Solution:
    """
    subproblem:
        if j > i:
            1 + LIS(A[i], j)
    recurrence relation:

            1 + max(
            for j in i...n
                if A[i] < A[j]:
                    LIS(A[i], j)
            )
    topology:
        right to left, base case is all the way on the right
    base cases:
        i == n
    original:
        LIS(0)
    time complexity:
        time per subproblem:
            linear O(n), because we check the LIS of every element in sequence that comes after I
            # of subproblems, N because we check if the LIS starts at every index
        overall: n (time per subproblem) * n (number of problems) => O(n^2)
    """
    def __init__(self):
        self.memo = {}

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.bottom_up_dp(nums)
        # return self.top_down_dp(nums, 0)

    def bottom_up_dp(self, nums):
        dp = [1] * (len(nums))
        for i in range(len(dp) - 2, -1, -1):
            longest_from_i = 0
            for j in range(len(dp) - 1, i, -1):
                if nums[i] < nums[j]:
                    longest_from_i = max(longest_from_i, dp[j])
            dp[i] = 1 + longest_from_i
        return max(dp)

    def top_down_dp(self, nums, i):
        if i in self.memo:
            return self.memo[i]

        if i == len(nums) - 1:
            return 1

        max_extension_subsequence = 0
        for idx in range(i, len(nums)):
            for j in range(idx + 1, len(nums)):
                if nums[idx] < nums[j]:
                    lis_starting_at_j = self.top_down_dp(nums, j)
                    max_extension_subsequence = max(max_extension_subsequence, lis_starting_at_j)
        self.memo[i] = max_extension_subsequence
        return max_extension_subsequence + 1


@pytest.mark.parametrize('nums, expected', [
    pytest.param([10, 9, 2, 5, 3, 7, 101, 18], 4),
    pytest.param([0, 1, 0, 3, 2, 3], 4),
    pytest.param([7, 7, 7, 7, 7, 7, 7], 1),
])
def test_longest_increasing_subsequence(nums, expected):
    solver = Solution()
    result = solver.lengthOfLIS(nums)
    assert result == expected
