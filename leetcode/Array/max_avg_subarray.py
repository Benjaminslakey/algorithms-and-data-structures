import pytest

"""
# Problem Statement

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10^-5 will be accepted.

------------------------------------------------------------------------------------------------------------------------

# Constraints

n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

### Example 2:
Input: nums = [5], k = 1
Output: 5.00000

------------------------------------------------------------------------------------------------------------------------

# Walk Through


------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, *input_args):
        return self.findMaxAverage(*input_args)

    def findMaxAverage(self, nums, k):
        if len(nums) == k:
            return sum(nums) / k

        l, r = 0, k - 1
        window_sum = 0
        for idx in range(0, k):
            window_sum += nums[idx]
        max_avg = window_sum / k
        while r + 1 < len(nums):
            r += 1
            window_sum = window_sum - nums[l] + nums[r]
            l += 1
            max_avg = max(max_avg, window_sum / k)
        return max_avg


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([[1,12,-5,-6,50,3], 4], 12.75),
    pytest.param([[5], 1], 5.0),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output


