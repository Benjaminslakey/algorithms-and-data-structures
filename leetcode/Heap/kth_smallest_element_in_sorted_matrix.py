"""
Problem Statement

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).
------------------------------------------------------------------------------------------------------------------------
Constraints

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
------------------------------------------------------------------------------------------------------------------------
"""
import heapq
from typing import List

import pytest


class ArrIter:
    def __init__(self, arr):
        self.arr = arr
        self.idx = 0

    def next(self):
        self.idx += 1
        if self.idx >= len(self.arr):
            raise StopIteration

    def current(self):
        if self.idx < len(self.arr):
            return self.arr[self.idx]
        return float("inf")

    def __lt__(self, rhs_arr):
        return self.current() < rhs_arr.current()

    def __gt__(self, rhs_arr):
        return self.current() > rhs_arr.current()

    def __eq__(self, rhs_arr):
        return self.current() == rhs_arr.current()


# Solution class goes here
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.solve(matrix, k)

    def solve(self, matrix, k):
        min_heap = [ArrIter(row) for row in matrix]
        heapq.heapify(min_heap)
        while k > 1:
            kth = heapq.heappop(min_heap)
            try:
                kth.next()
            except StopIteration:
                pass
            else:
                heapq.heappush(min_heap, kth)
            k -= 1
        return min_heap[0].current()


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13),
    pytest.param(([[-5]], 1), -5),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
