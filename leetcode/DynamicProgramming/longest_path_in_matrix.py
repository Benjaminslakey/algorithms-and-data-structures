from typing import List

import pytest

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
UP_RIGHT = 'up-right'
UP_LEFT = 'up-left'
DOWN_RIGHT = 'down-right'
DOWN_LEFT = 'down-left'


class Solution:
    """
    for every cell that is a 1
    do a depth first search in each of the possible directions
    up, down, left, right, up-left, up-right, down-left, down-right
    record path length
    stop when we hit a 0 or matrix boundary

    memoize by returning length from current cell with direction if recorded before
    """
    DIRECTIONS = {
        UP: (-1, 0),
        DOWN: (1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1),
        UP_RIGHT: (-1, 1),
        UP_LEFT: (-1, -1),
        DOWN_RIGHT: (1, 1),
        DOWN_LEFT: (1, -1),
    }

    def __init__(self):
        self.memo = {}
        self.matrix = None
        self.left_bound = -1
        self.right_bound = 0
        self.top_bound = -1
        self.bottom_bound = 0

    def init_boundaries(self, matrix):
        self.matrix = matrix
        self.bottom_bound = len(matrix)
        self.right_bound = len(matrix[0])

    def check_bounds(self, r, c):
        return (
                self.left_bound < c < self.right_bound
                and self.top_bound < r < self.bottom_bound
                and self.matrix[r][c] == 1
        )

    def dfs(self, r, c, direction, length):
        key = f"{r}:{c}:{direction}"
        if key in self.memo:
            return self.memo[key]

        if not self.check_bounds(r, c):
            return length

        delta_r, delta_c = self.DIRECTIONS[direction]
        nr, nc = r + delta_r, c + delta_c
        longest_in_dir = self.dfs(nr, nc, direction, length + 1)
        self.memo[key] = longest_in_dir
        return longest_in_dir

    def longestLine(self, mat: List[List[int]]) -> int:
        self.init_boundaries(mat)
        max_path = 0
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                if cell == 1:
                    for dir_ in self.DIRECTIONS.keys():
                        max_path = max(
                            max_path,
                            self.dfs(r, c, dir_, 0)
                        )
        return max_path


@pytest.mark.parametrize('matrix, expected', [
    pytest.param([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]], 3),
    pytest.param([[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]], 4)
])
def test_longest_matrix_line(matrix, expected):
    solver = Solution()
    result = solver.longestLine(matrix)
    assert result == expected
