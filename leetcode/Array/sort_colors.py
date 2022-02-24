"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

# goals
# sort array in one pass
# partition array into 3 groups, 0s left, 1s middle 2s right
# have all numbers smaller than the middle number, to the left of it
# all numbers greater than middle number to the right of it

Input: nums = [2,0,0,1,1,2,0,0,1,0]
[2, 0, 0, 1, 1, 2, 0, 0, 1, 0] p = 1
 l                          r
[0, 0, 0, 1, 1, 2, 0, 0, 1, 2] p = 1
    l                    r
       l                 r
          l              r


l m r
I want l < m < r
as I move them in I know:
    everything right of R is >= r
    everything left of L is <= l


1, 1, 2, 1, 0, 1, 2
lc                r
1, 1, 2, 1, 0, 1, 2
l        m     r
l     m  r

left middle right
left > right
    swap left and right
left > mid
    swap left and mid
right < mid
    swap right and mid


Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""
from typing import List

import pytest


class Solution:
    """
    formula

    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.one_pass(nums)

    def one_pass(self, nums):
        """
        [1, 1, 2, 1, 0, 1, 2]
       L ^                   R
       L    ^                R
       L       ^             R
       L       ^          R
        [1, 1, 2, 1, 0, 1, 2]
       L       ^          R
        [1, 1, 1, 1, 0, 2, 2]
       L       ^       R
       L          ^    R
       L             ^ R
        [0, 1, 1, 1, 1, 2, 2]
           L           R

        """
        pivot = 1
        idx = 0
        left_bound, right_bound = 0, len(nums) - 1
        while idx <= right_bound:
            if nums[idx] < pivot:
                nums[left_bound], nums[idx] = nums[idx], nums[left_bound]
                left_bound += 1
                idx += 1
            elif nums[idx] > pivot:
                nums[right_bound], nums[idx] = nums[idx], nums[right_bound]
                right_bound -= 1
            else:
                idx += 1

    def two_pass(self, nums):
        pivot = 1
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            if pivot <= nums[r]:
                r -= 1
            if nums[l] < pivot:
                l += 1
        # 2nd pass
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            if pivot < nums[r]:
                r -= 1
            if nums[l] <= pivot:
                l += 1


@pytest.mark.parametrize('nums', [
    pytest.param([1, 1, 2, 1, 0, 1, 2]),
    pytest.param([2, 0, 0, 2, 1, 0, 1, 0]),
    pytest.param([1, 0, 2]),
    pytest.param([2, 0, 1])
])
def test_sort_colors(nums):
    solver = Solution()
    solver.sortColors(nums)
    assert nums == sorted(nums)
