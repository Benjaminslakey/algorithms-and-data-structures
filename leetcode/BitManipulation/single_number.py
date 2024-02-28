import pytest

"""
Problem Statement

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def singleNumber(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result

# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([2, 2, 1],), 1),
    pytest.param(([4, 1, 2, 1, 2],), 4),
    pytest.param(([1],), 1),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.singleNumber(*input_args)
    assert result == expected_output
