from collections import deque
from typing import List

import pytest


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([])
        for idx, temp in enumerate(temperatures):
            if temp > stack[0]:


@pytest.mark.parametrize('temperatures, expected', [
    pytest.param([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    pytest.param([30,40,50,60], [1, 1, 1, 0]),
    pytest.param([30, 60, 90], [1, 1, 0]),
])
def test_daily_temperatures(temperatures, expected):
    solver = Solution()
    result = solver.dailyTemperatures(temperatures)
    assert result == expected
