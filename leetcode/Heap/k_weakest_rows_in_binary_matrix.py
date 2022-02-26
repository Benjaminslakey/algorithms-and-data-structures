"""
Problem Statement

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
------------------------------------------------------------------------------------------------------------------------

Constraints

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:
Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].
------------------------------------------------------------------------------------------------------------------------
"""
import heapq
from typing import List

import pytest


# Solution class goes here
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return self.solve(mat, k)

    def solve(self, mat, k):
        weakest_rows = []
        for idx, row in enumerate(mat):
            heapq.heappush(weakest_rows, (row.count(1), idx))
        return [idx for strength, idx in heapq.nsmallest(k, weakest_rows)]


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([[1, 1, 0, 0, 0],
                   [1, 1, 1, 1, 0],
                   [1, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0],
                   [1, 1, 1, 1, 1]], 3), [2, 0, 3]),
    pytest.param(([[1, 0, 0, 0],
                   [1, 1, 1, 1],
                   [1, 0, 0, 0],
                   [1, 0, 0, 0]], 2), [0, 2]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
