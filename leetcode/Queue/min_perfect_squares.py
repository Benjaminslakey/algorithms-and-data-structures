"""
start node is 0
each node's neighbors are every perfect square less target - node's value
"""
from collections import deque
from math import sqrt, floor

from typing import List

import pytest


class Solution:
    @staticmethod
    def perfect_squares_less_than_n(n) -> List[int]:
        i = floor(sqrt(n))
        while i ** 2 <= n:
            yield i ** 2
            i -= 1

    def numSquares(self, n: int) -> int:
        queue = deque([(0, 0)])
        visited = set()
        min_squares = -1
        while queue:
            current, num_squares = queue.pop()
            if current == n:
                min_squares = num_squares
                break
            if num_squares == 3 and sqrt(n - current) % 1 > 0.0:
                continue
            for neighbor in self.perfect_squares_less_than_n(n - current):
                if current + neighbor not in visited:
                    queue.appendleft((current + neighbor, num_squares + 1))
                    # add before visiting so we can pre-prune  / prevent creation of duplicated nodes
                    visited.add(current + neighbor)
        return min_squares


@pytest.mark.parametrize('n, num_squares', [
    pytest.param(12, 3),
    pytest.param(13, 2),
    pytest.param(7168, 4),
    pytest.param(2876, 4),
    pytest.param(8441, 3),
])
def test_num_perfect_squares(n, num_squares):
    solver = Solution()
    assert solver.numSquares(n) == num_squares

