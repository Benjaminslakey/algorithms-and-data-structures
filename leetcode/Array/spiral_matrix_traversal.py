"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List
import pytest

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [RIGHT, DOWN, LEFT, UP]


class Square:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Square<x: {self.x}, y: {self.y}>"

    def __repr__(self):
        return self.__str__()


class Solution:
    def __init__(self):
        self.direction_idx = 0
        self.matrix = None

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.matrix = matrix
        total_squares = len(matrix) * len(matrix[0])
        current_direction = DIRECTIONS[self.direction_idx]
        visited = set()
        spiral_order = [matrix[0][0]]
        current_square = Square(x=0, y=0)
        visited.add(current_square)

        while len(spiral_order) < total_squares:
            next_square = self.get_next_square(current_square, current_direction)
            if self.is_valid_choice(next_square, visited):
                current_square = next_square
            else:
                current_direction = self.get_next_direction()
                continue
            # record current
            val = self.get_square_value(current_square)
            spiral_order.append(val)
            visited.add(current_square)
        return spiral_order

    def get_next_square(self, sq, direction):
        delta_y, delta_x = direction
        return Square(x=sq.x + delta_x, y=sq.y + delta_y)

    def get_square_value(self, sq):
        return self.matrix[sq.y][sq.x]

    def get_next_direction(self):
        if self.direction_idx < len(DIRECTIONS) - 1:
            self.direction_idx += 1
        else:
            self.direction_idx = 0
        return DIRECTIONS[self.direction_idx]

    def is_valid_choice(self, sq, seen):
        if sq in seen:
            return False
        if sq.x < 0 or sq.x >= len(self.matrix[0]):
            return False
        if sq.y < 0 or sq.y >= len(self.matrix):
            return False
        return True


@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    pytest.param(([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.spiralOrder(*input_args)
    assert result == expected_output
