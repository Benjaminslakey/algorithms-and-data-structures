"""
Problem Statement

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
    The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,5]
------------------------------------------------------------------------------------------------------------------------
"""
from typing import List

import pytest


# Solution class goes here
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return self.solve(arr, k, x)

    def solve(self, arr, k, x):
        def get_closeness(idx):
            if -1 < idx < len(arr):
                return abs(arr[idx] - x)
            return float('inf')

        start, end = 0, len(arr)
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] == x and (mid == start or arr[mid - 1] < x):
                start = mid
                break
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid

        # if the item is not present in the array, bisect will end up to the right of where the item should be
        if arr[start] == x:
            left, right = start, start + 1
        else:
            left, right = start - 1, start

        while k > 0:
            l, r = get_closeness(left), get_closeness(right)
            if l < r or (l == r and arr[left] <= arr[right]):
                left -= 1
            else:
                right += 1
            k -= 1
        return [arr[i] for i in range(left + 1, right)]


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5), [3, 3, 4]),
    pytest.param(([1, 2, 3, 4, 4, 4, 4, 5, 5], 3, 3), [2, 3, 4]),
    pytest.param(([1, 1, 1, 10, 10, 10], 1, 9), [10]),
    pytest.param(([1, 1, 2, 3, 4, 7, 8, 8, 8, 13, 15], 5, 6), [4, 7, 8, 8, 8]),
    pytest.param(([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4]),
    pytest.param(([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4]),
    pytest.param(([3, 4, 7, 11, 13, 14, 15, 17, 21], 4, 12), [11, 13, 14, 15]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
