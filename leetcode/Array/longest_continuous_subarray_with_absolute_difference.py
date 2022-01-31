# @tags: [sliding_window, array, bst]

from typing import List

import pytest
from sortedcontainers import SortedList

"""
clarifying questions
is the array ordered: probably not
can the integers be negative? probably
can the array of integers be empty? probably
I'm guaranteed santizied input, ie, all integers no nulls or string, never null instead of an array? almost certainly


limit is a range, find the largest array where all numbers are within the difference of each other

sort array
sliding window
left pointer starts at 0, right also starts at 0 -- add 1 to the length before returning to account for window size
increase right pointer until going past limit
slide window from left to right across the array and check left and right bounds, right - left <= limit
if within limit, increase size, and test again, once test fails continue sliding window

WRONG APPROACH
cant sort because the subarray must maintain order

need to ask if order is matters

2nd approach

sliding window where you keep track of the min and max
use balanced BST for sliding window so we can quickly delete the elements on the left that are no longer in the window
and quickly add those on the right, while also quickly finding min / max O(logN)

"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1

        left = 0
        right = 1
        bst = SortedList([nums[0]])
        largest_valid_size = 0
        while right < len(nums):
            bst.add(nums[right])
            window_max = bst[-1]
            window_min = bst[0]
            if window_max - window_min <= limit:
                right += 1
                largest_valid_size = right - left
            else:
                bst.remove(nums[left])
                left += 1
                right += 1
        return largest_valid_size


@pytest.mark.parametrize('nums, limit, expected_largest', [
    pytest.param([8, 2, 4, 7], 4, 2),
    pytest.param([10, 1, 2, 4, 7, 2], 5, 4),
    pytest.param([4, 2, 2, 2, 4, 4, 2, 2], 0, 3),
])
def test_longest_subarray(nums, limit, expected_largest):
    solver = Solution()
    largest = solver.longestSubarray(nums, limit)
    assert largest == expected_largest
