# @tags: [stack]

from collections import deque
from typing import List

import pytest


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        previous_colder_days = deque([])
        days_until_warmer = [0 for _ in range(0, len(temperatures))]
        for todays_date, todays_temp in enumerate(temperatures):
            while previous_colder_days and todays_temp > previous_colder_days[0][0]:
                _, previous_date = previous_colder_days.popleft()
                days_until_warmer[previous_date] = todays_date - previous_date
            previous_colder_days.appendleft((todays_temp, todays_date))
        return days_until_warmer


@pytest.mark.parametrize('temperatures, expected', [
    pytest.param([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    pytest.param([30, 40, 50, 60], [1, 1, 1, 0]),
    pytest.param([30, 60, 90], [1, 1, 0]),
    pytest.param([30, 30, 29, 16, 14, 10, 15, 28, 30, 35], [9, 8, 6, 4, 2, 1, 1, 1, 1, 0]),
])
def test_daily_temperatures(temperatures, expected):
    solver = Solution()
    result = solver.dailyTemperatures(temperatures)
    assert result == expected
