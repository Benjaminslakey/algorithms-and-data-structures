"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index Math 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index Math 1 where the peak element is 2,
                or index Math 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

"""

import pytest

from typing import List


class Solution:
    """
    key insight here is that because we know consecutive elements will never be equal
    we can check to see whether or not the sequence is increasing left -> right
    if it is then we search to the right because either:
        1. the sequence continues increasing for the length of the array,
            in which case our oob = -inf. -inf creates our peak
            (since the sequence was increasing we know the number to the left of end is smaller than it)
        2. the sequence decreases at some point, creating a peak
    """
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        def get_num(idx):
            if -1 < idx < len(nums):
                return nums[idx]
            return float("-inf")

        while start <= end:
            mid = start + (end - start) // 2
            left, right = get_num(mid - 1), get_num(mid + 1)
            if left < nums[mid] > right:
                return mid
            elif left < nums[mid] < right:
                start = mid + 1
            else:
                end = mid - 1


@pytest.mark.parametrize('nums, expected', [
    pytest.param([1, 2, 3, 1], [2]),
    pytest.param([1, 2, 1, 3, 5, 6, 8], [1, 6]),
])
def test_find_peak(nums, expected):
    solver = Solution()
    result = solver.findPeakElement(nums)
    assert result in expected
