import pytest

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints: 

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


@pytest.mark.parametrize('nums, expected', [
    pytest.param([1, 2, 3, 4, 5], False),
    pytest.param([1, 1, 3, 4, 5], True),
])
def test_contains_duplicate(nums, expected):
    solver = Solution()
    result = solver.containsDuplicate(nums)
    assert result == expected
