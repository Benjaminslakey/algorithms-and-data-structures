from collections import namedtuple
from typing import List

import pytest

ContainerWall = namedtuple('ContainerWall', ['height', 'idx'])


class Solution:
    """
    need to determine containers and volume of each container then sum volumes
    container is defined by left wall and right wall
    volume = (height * width) - sum of non zero heights between left index and right index
    width = right index - left index
    height = min(left height, right height)

    determine containers from left to right then right to left
    use monotonic increasing stack to find container walls

    O(N) -- 4N
    1 pass left to right to build first stack
    1 pass right to left to build second stack
    1 pass to reverse the right to left stack
    1 pass to calculate volume from container endpoints
    """
    def __init__(self):
        self.height = []

    def calc_water(self, stack):
        right_wall = stack.pop()
        total = 0
        while stack:
            left_wall = stack.pop()
            container_height = min(left_wall.height, right_wall.height)
            container_width = (right_wall.idx - left_wall.idx - 1)
            volume = container_height * container_width
            for i in range(left_wall.idx + 1, right_wall.idx):
                volume -= self.height[i]
            total += volume
            right_wall = left_wall
        return total

    def find_containers(self, start, left, right, step):
        idx = start
        stack = []
        while left <= idx <= right:
            h = self.height[idx]
            if h > 0 and not stack:
                stack.append(ContainerWall(h, idx))
            elif stack and h >= stack[-1].height:
                stack.append(ContainerWall(h, idx))
            idx += step
        return stack

    def trap(self, height: List[int]) -> int:
        self.height = height
        total_water = 0
        start = 0
        stack = self.find_containers(start, 0, len(height) - 1, 1)
        if stack:
            left_bound = stack[-1].idx
            total_water += self.calc_water(stack)
        else:
            left_bound = 0
        stack = self.find_containers(len(height) - 1, left_bound, len(height) - 1, -1)
        if stack:
            stack.reverse()
            total_water += self.calc_water(stack)
        return total_water


@pytest.mark.parametrize('height, expected_total_water', [
    pytest.param([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    pytest.param([4, 2, 0, 3, 2, 5], 9),
    pytest.param([4, 2, 3], 1)
])
def test_trap_rain_water(height, expected_total_water):
    solver = Solution()
    total_water = solver.trap(height)
    assert total_water == expected_total_water
