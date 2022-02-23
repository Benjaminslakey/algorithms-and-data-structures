import pytest


class Solution:
    """
    for each Math in 1...n
        determine the worst case cost of picking that first guess

    return Math with lowest worst case value

    determine worst case of picking a Math by

    """
    def __init__(self):
        self.memo = {}

    def getMoneyAmount(self, n: int) -> int:
        return self.top_down_dp(1, n)

    def top_down_dp(self, start, end):
        key = f"{start}:{end}"
        if key in self.memo:
            return self.memo[key]
        if start >= end:
            return 0

        min_cost_for_range = float("inf")
        for guess in range(start, end + 1):
            smaller = self.top_down_dp(start, guess - 1) + guess
            larger = self.top_down_dp(guess + 1, end) + guess
            max_cost_for_guess = max(smaller, larger)
            min_cost_for_range = min(min_cost_for_range, max_cost_for_guess)
        self.memo[key] = min_cost_for_range
        return min_cost_for_range

    def bottom_up_dp(self, n):
        pass


"""
s: 1, e: 10, m: 4 <= 1 + (10 - 1) // 2   ==> 4
s: 5, e: 6, m: 5 <= 5 + (6 - 5) // 2  ==> 9
"""


@pytest.mark.parametrize('n, expected_min_cost', [
    pytest.param(10, 16),
    pytest.param(1, 0),
    pytest.param(2, 1),
    pytest.param(6, 8),
    pytest.param(16, 34)
])
def test_guessing_game_2(n, expected_min_cost):
    solver = Solution()
    result = solver.getMoneyAmount(n)
    assert result == expected_min_cost
