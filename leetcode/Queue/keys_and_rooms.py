from collections import deque
from typing import List

import pytest


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = {0}
        while queue:
            vertex = queue.popleft()
            for neighbor in rooms[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
            visited.add(vertex)
        return len(visited) == len(rooms)


@pytest.mark.parametrize('rooms, can_visit_all', [
    pytest.param([[1], [2], [3], []], True),
    pytest.param([[1, 3], [3, 0, 1], [2], [0]], False)
])
def test_keys_and_rooms(rooms, can_visit_all):
    solver = Solution()
    result = solver.canVisitAllRooms(rooms)
    assert result == can_visit_all
