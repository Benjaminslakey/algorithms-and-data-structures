from collections import deque
from typing import List

import pytest


class Solution:
    """
    first solution that comes to mind
    breadth first search, word1 is start vertex word2 is target vertex
    neighbors of each node 
    """
    def __init__(self):
        self.replace_or_insert = set()

    def get_neighbors(self, word: str) -> List[str]:
        neighbors = []
        # delete_neighbors
        for
        replace_neighbors = []
        insert_neighbors = []
        return neighbors


    def minDistance(self, word1: str, word2: str) -> int:
        self.replace_or_insert = set(list(word2))
        queue = deque([(word1, 0)])
        visited = set()
        while queue:
            current, distance = queue.popleft()
            if current == word2:
                return distance
            for neighbor in self.get_neighbors(current):
                queue.append((neighbor, distance + 1))
            visited.add(current)
        return 0


@pytest.mark.parametrize('word1, word2, expected_distance', [
    pytest.param('horse', 'ros', 3),
    pytest.param('intention', 'execution', 5),
])
def test_edit_distance(word1, word2, expected_distance):
    solver = Solution()
    distance = solver.minDistance(word1, word2)
    assert distance == expected_distance
