import pytest

from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, houses: List[int]) -> int:
        if len(houses) == 0:
            return 0
        elif len(houses) == 1:
            return houses[0]
        return self.helper__bottom_up(houses)

    def helper__top_down(self, houses, idx, money):
        key = f"{idx}:{money}"
        if key in self.memo:
            return self.memo[key]

        if idx >= len(houses):
            return money

        house1 = self.helper__top_down(houses, idx + 1, money)
        house2 = self.helper__top_down(houses, idx + 2, money + houses[idx])
        best = max(house1, house2)
        self.memo[key] = best
        return best

    def helper__bottom_up(self, houses):
        dp = [0 for _ in range(0, len(houses))]
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for idx in range(2, len(houses)):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + houses[idx])
        return dp[-1]


@pytest.mark.parametrize('houses, max_money', [
    pytest.param([1, 2, 3, 1], 4),
    pytest.param([2, 7, 9, 3, 1], 12)
])
def test_house_robber(houses, max_money):
    solver = Solution()
    money = solver.rob(houses)
    assert money == max_money
