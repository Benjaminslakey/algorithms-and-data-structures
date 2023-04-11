"""
Problem Statement

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
    and you may return the result in any order.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
------------------------------------------------------------------------------------------------------------------------
Examples


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
------------------------------------------------------------------------------------------------------------------------
"""

from collections import Counter
from typing import List

import pytest


# Solution class goes here
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.hashmap_approach(nums1, nums2)

    def hashmap_approach(self, nums1, nums2):
        output = []
        counts = Counter(nums2)
        for num in nums1:
            if num in counts and counts[num] > 0:
                counts[num] -= 1
                output.append(num)
        return output

    def sort_approach(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        output = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return output


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([1, 2, 2, 1], [2, 2]), [2, 2]),
    pytest.param(([4, 4, 9, 9, 5, 1], [4, 9, 11]), [4, 9]),
    pytest.param(([1, 2, 3, 4, 5], [6, 7, 11]), []),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.intersect(*input_args)
    assert result == expected_output
