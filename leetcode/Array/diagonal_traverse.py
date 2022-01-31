from typing import List

import pytest


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


@pytest.parametrize('matrix, expected', [
    pytest.param([])
])
def test_find_diagonal_order(matrix, expected):
    solver = Solution()
    result = solver.findDiagonalOrder(matrix)
    assert result == expected
