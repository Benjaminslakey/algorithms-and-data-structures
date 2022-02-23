"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target Math.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.


[-4, 0, 2, 6, 11, 19, 20, 21, 22, 24, 26, 27, 28, 31, 54]  => 25
 ^                                                     ^
                                                   ^
                                               ^
     ^

key intuition is that once -4 has been evaluated we never need to look at it again, so left only moves right
same thing for 54, we know it is too large when matched with anything to the left, so we never need to consider it again
"""

from typing import List

import pytest


class Solution:
    """
    binary search for complement of each Math, moving from left to right
    N logN
    """

    def binary_search(self, space, target, start, end):
        while start <= end:
            mid = start + (end - start) // 2
            if space[mid] == target:
                return mid
            elif space[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def twoSum__nlogn(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            complement = target - num
            complement_idx = self.binary_search(numbers, complement, idx + 1, len(numbers) - 1)
            if complement_idx != -1:
                return [idx + 1, complement_idx + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1




@pytest.mark.parametrize('numbers, target, expected', [
    pytest.param([2, 7, 11, 15], 9, [1, 2]),
    pytest.param([2, 3, 4], 6, [1, 3]),
    pytest.param([-1, 0], -1, [1, 2]),
])
def test_two_sum(numbers, target, expected):
    solver = Solution()
    result = solver.twoSum(numbers, target)
    assert result == expected
