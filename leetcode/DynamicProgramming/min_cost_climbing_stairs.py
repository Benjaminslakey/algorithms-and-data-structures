import pytest

from typing import List


class Solution:
    def __init__(self):
        self.memo = {}
        self.min_cost = float("inf")

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top_down = min(self.top_down(cost, 0, 0), self.top_down(cost, 1, 0))
        bottom_up = self.bottom_up(cost)
        return bottom_up

    def bottom_up(self, cost):
        dp = [0 for _ in range(0, len(cost) + 1)]
        for idx in range(2, len(cost) + 1):
            dp[idx] = min(dp[idx - 1] + cost[idx - 1], dp[idx - 2] + cost[idx - 2])
        return dp[-1]

    def top_down(self, cost, idx, incurred):
        key = f"{idx}:{incurred}"
        if key in self.memo:
            return self.memo[key]

        if idx >= len(cost):
            return incurred
        elif incurred >= self.min_cost:
            return float("inf")

        move_one_cost = self.top_down(cost, idx + 1, incurred + cost[idx])
        move_two_cost = self.top_down(cost, idx + 2, incurred + cost[idx])
        best = min(move_one_cost, move_two_cost)
        self.memo[key] = best
        self.min_cost = min(best, self.min_cost)
        return best


@pytest.mark.parametrize('cost, expected_min_cost', [
    pytest.param([10, 15, 20], 15),
    pytest.param([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
])
def test_min_cost_stairs(cost, expected_min_cost):
    solver = Solution()
    min_cost = solver.minCostClimbingStairs(cost)
    assert min_cost == expected_min_cost
