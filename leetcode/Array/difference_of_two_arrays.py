import pytest

"""
Problem Statement

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.findDifference(*input_args)

    def findDifference(self, nums1, nums2):
        first_distincts = set(nums1)
        second_distincts = set(nums2)
        result_1 = []
        result_2 = []
        for n in nums1:
            if n not in second_distincts:
                result_1.append(n)
        for n2 in nums2:
            if n2 not in first_distincts:
                result_2.append(n2)
        return [list(set(result_1)), list(set(result_2))]


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([1,2,3], [2,4,6]), [[1,3],[4,6]]),
    pytest.param(([1,2,3,3], [1,1,2,2]), [[3],[]]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output
