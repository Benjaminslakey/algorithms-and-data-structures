from typing import List

import pytest


class Solution:
    """
    subproblem:
        is there a square of 1 smaller width here than my current width
        f(l - 1)

    recurrence relation:
        if each == square size - 1 in ((r, c), (r, c + t), (r + 1, c), (r + 1, c + 1)
            square_size
        else
            max all
    topological order:
        left -> right
        top -> bottom
    base cases:
        f(1)
    original:
        f(min(m, n), (0, 0))
    time complexity:
        time per subproblem => 2m - 1
        # of subproblems => n*m

    if square of size 1
        return is square
    dp(square size - 1) => is square
    if not square
        return
    """

    def __init__(self):
        self.memo = {}

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # return self.top_down_dp(matrix)
        return self.bottom_up_dp(matrix)

    def bottom_up_dp(self, matrix):
        max_size = 0
        matrix[-1][-1] = int(matrix[-1][-1])

        def get_value(i, j):
            if -1 < i < len(matrix) and -1 < j < len(matrix[0]):
                return int(matrix[i][j])
            return 0

        for r in range(len(matrix) - 1, -1, -1):
            for c in range(len(matrix[0]) - 1, -1, -1):
                cell_val = get_value(r, c)
                squares = min((
                    get_value(r + 1, c),
                    get_value(r + 1, c + 1),
                    get_value(r, c + 1),
                ))
                matrix[r][c] = squares + 1 if squares > 0 and cell_val > 0 else cell_val
                max_size = max(matrix[r][c], max_size)
        return max_size ** 2

    def top_down_dp(self, matrix):
        max_possible = min(len(matrix), len(matrix[0]))
        max_size = 0

        def recurse(row, col, square_size):
            key = f"{row}:{col}:{square_size}"
            if key in self.memo:
                return self.memo[key]
            if not -1 < row < len(matrix) or not -1 < col < len(matrix[0]):
                return 0
            if square_size == 1:
                return int(matrix[row][col])
            tl = recurse(row, col, square_size - 1)
            tr = recurse(row, col + 1, square_size - 1)
            dl = recurse(row + 1, col, square_size - 1)
            dr = recurse(row + 1, col + 1, square_size - 1)
            size = tl
            if all([s == square_size - 1 for s in [tl, tr, dl, dr]]):
                size = square_size
            self.memo[key] = size
            return size

        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                max_size = max(max_size, recurse(r, c, max_possible))
        return max_size ** 2


@pytest.mark.parametrize('matrix, expected_max_area', [
    pytest.param(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
        4
    ),
    pytest.param([["0", "1"], ["1", "0"]], 1),
    pytest.param([["0"]], 0),
    pytest.param([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"]
    ], 16)
])
def test_max_square(matrix, expected_max_area):
    solver = Solution()
    max_sq_area = solver.maximalSquare(matrix)
    assert max_sq_area == expected_max_area
