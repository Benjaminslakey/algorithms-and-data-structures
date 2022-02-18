"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

from typing import List

import pytest


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        two pass approach
            first pass
                leftshift all values by 1 bit
            second pass
                if a 0 is encountered
                    bitwise OR all values in row and column with 1
            third pass
                bitwise and all values with 1
                    if the result is 1
                    set value to 0
        """
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(1, len(matrix)):
                    matrix[row][col] = 0
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(1, len(matrix[0])):
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
            for r in range(len(matrix)):
                matrix[r][0] = 0

    def setZeroes__bit_operations(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        two pass approach
            first pass
                leftshift all values by 1 bit
            second pass
                if a 0 is encountered
                    bitwise OR all values in row and column with 1
            third pass
                bitwise and all values with 1
                    if the result is 1
                    set value to 0
        this is not constant space if the max value of the integers uses the maximum allowed bits for the type
        ex. only "constant" space complexity if max integer values for cells were 1-10 and we used a short or something
        because then we are shifting the values into unused bits, if we can potentially use all bits then we would need
        to copy values into larger sized integers else risk losing data when left shifting
        """
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                matrix[r][c] = cell << 1

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 0:
                    for col_in_zero_row in range(len(matrix[r])):
                        matrix[r][col_in_zero_row] |= 1
                    for row_in_zero_col in range(len(matrix)):
                        matrix[row_in_zero_col][c] |= 1
                    break
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell & 1 == 1:
                    matrix[r][c] = 0
                else:
                    matrix[r][c] = cell >> 1


@pytest.mark.parametrize('matrix, expected', [
    pytest.param(
        [
            [1, 1, 1],
            [1, 1, 1]
        ],
        [
            [1, 1, 1],
            [1, 1, 1]
        ]),
    pytest.param(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]),
    pytest.param(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ],
        [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
    )
])
def test_set_matrix_zeroes(matrix, expected):
    solver = Solution()
    solver.setZeroes(matrix)
    assert matrix == expected
