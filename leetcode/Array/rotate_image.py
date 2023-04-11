"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from typing import List

import pytest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        boundaries = {'top': 0, 'right': size - 1, 'bottom': size - 1, 'left': 0}
        while boundaries['left'] < boundaries['right']:
            # move each value in a side clockwise, determine by side length
            for i in range(boundaries['right'] - boundaries['left']):
                position = (boundaries['top'], boundaries['left'] + i)
                r, c = position
                previous_value = matrix[r][c]
                # do one loop around the boundary of matrix
                for _ in range((boundaries['right'] - boundaries['left']) * 4):
                    position = self.get_next_clockwise(position, boundaries)
                    r, c = position
                    previous_value, matrix[r][c] = matrix[r][c], previous_value
            # update size length after full rotation, ie, do inner rotations
            boundaries['top'] += 1
            boundaries['bottom'] -= 1
            boundaries['left'] += 1
            boundaries['right'] -= 1

    def get_next_clockwise(self, position, boundaries):
        r, c = position
        if r == boundaries['top'] and boundaries['left'] <= c < boundaries['right']:
            return r, c + 1
        elif c == boundaries['right'] and boundaries['top'] <= r < boundaries['bottom']:
            return r + 1, c
        elif r == boundaries['bottom'] and boundaries['right'] >= c > boundaries['left']:
            return r, c - 1
        elif c == boundaries['left'] and boundaries['bottom'] >= r > boundaries['top']:
            return r - 1, c
        raise Exception("non boundary position given")


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    pytest.param(([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
                 [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    solver.rotate(*input_args)
    assert input_args[0] == expected_output
