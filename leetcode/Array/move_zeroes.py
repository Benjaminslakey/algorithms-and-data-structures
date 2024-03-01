from collections import defaultdict, deque
import pytest

"""
Problem Statement

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

------------------------------------------------------------------------------------------------------------------------
Walk Through 

[0,1,0,3,12]
 ^ ^
[1,0,0,3,12]
   ^ ^
[1,0,0,3,12]
     ^ ^
[1,0,3,0,12]
       ^  ^
[1,0,3,12,0]
   ^ ^
[1,3,0,12,0]
     ^  ^
[1,3,12,0,0]
        ^ ^


Follow up: Could you minimize the total number of operations done?
"""

def swap_to_end(idx, end, nums):
    while idx < end - 1:
        nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
        idx += 1

# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.moveZeroes(input_args)

    def moveZeroes(self, nums):
        self.leetcode_editorial(nums)

    def brute_force(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                swap_to_end(i, end, nums)
                end -= 1
            if nums[i] != 0: # if we had consecutive 0s, our current place will still have a 0 after moving the previous one to the end of the array
                i += 1

    def optimized(self, nums):
        correct_places = defaultdict(deque)
        spot_used = 0
        for n in nums:
            if n != 0:
                correct_places[n].append(spot_used)
                spot_used += 1
        if len(correct_places.keys()):
            i = 0
            while i < len(nums):
                n = nums[i]
                if n != 0:
                    correct_idx = correct_places[n][0]
                    nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
                    correct_places[n].popleft()
                i += 1

    def leetcode_editorial(self, nums):
        """
            [1, 2, 0, 3, 4, 5, 0, 0, 0, 6, 5, 0]
            i,n
            [1, 2, 0, 3, 4, 5, 0, 0, 0, 6, 5, 0]
               i,n
            [1, 2, 0, 3, 4, 5, 0, 0, 0, 6, 5, 0]
                n  i
            [1, 2, 0, 3, 4, 5, 0, 0, 0, 6, 5, 0]
                n     i
            [1, 2, 3, 0, 4, 5, 0, 0, 0, 6, 5, 0]
                   n     i
            [1, 2, 3, 4, 0, 5, 0, 0, 0, 6, 5, 0]
                      n  i
            [1, 2, 3, 4, 0, 5, 0, 0, 0, 6, 5, 0]
                      n     i
            [1, 2, 3, 4, 5, 0, 0, 0, 0, 6, 5, 0]
                         n     i
        """
        i, n = 0, -1
        while i < len(nums):
            if nums[i] != 0:
                n += 1
                nums[n], nums[i] = nums[i], nums[n]
            i += 1



# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([0], [0]),
    pytest.param([1, 0, 1], [1, 1, 0]),
    pytest.param([0,1,0,3,12], [1, 3, 12, 0, 0]),
    pytest.param([0, 0, 0, 6, 1, 0, 7, 0, 0, 5, 0], [6, 1, 7, 5, 0, 0, 0, 0, 0, 0, 0]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    solver.solve(input_args)
    assert input_args == expected_output

