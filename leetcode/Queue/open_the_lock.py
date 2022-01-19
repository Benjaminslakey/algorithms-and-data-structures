from collections import deque
from typing import List

import pytest


class Solution:
    @staticmethod
    def get_neighbors(current_combination):
        neighbors = []
        digits = [int(lock) for lock in current_combination]
        for change in [
            [0, 0, 0, 1],
            [0, 0, 0, -1],
            [0, 0, 1, 0],
            [0, 0, -1, 0],
            [0, 1, 0, 0],
            [0, -1, 0, 0],
            [1, 0, 0, 0],
            [-1, 0, 0, 0],
        ]:
            output = ""
            for lock_num, current in enumerate(digits):
                result = current + change[lock_num]
                if result > 9:
                    result = 0
                elif result < 0:
                    result = 9
                output += str(result)
            neighbors.append(output)
        return neighbors

    def openLock(self, deadends: List[str], target: str) -> int:
        min_moves = -1
        quick_access_deadends = set(deadends)
        start = '0000'
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            current, distance = queue.pop()
            if current == target:
                min_moves = distance
                break
            elif current in visited:
                continue
            elif current in quick_access_deadends:
                continue
            for neighbor in self.get_neighbors(current):
                if neighbor not in quick_access_deadends and neighbor not in visited:
                    queue.appendleft((neighbor, distance + 1))
            visited.add(current)
        return min_moves


@pytest.mark.parametrize('deadends, target, expected', [
    pytest.param(["0201", "0101", "0102", "1212", "2002"], '0202', 6),
    pytest.param(['8888'], '0009', 1),
    pytest.param(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], '8888', -1),
    pytest.param(["0000"], "8888", -1)
])
def test_open_lock(deadends, target, expected):
    solver = Solution()
    result = solver.openLock(deadends, target)
    assert result == expected
