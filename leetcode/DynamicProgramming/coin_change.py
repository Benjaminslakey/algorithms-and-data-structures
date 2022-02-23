"""
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest Math of coins that you need to make up that amount. If that amount of money cannot be made up
by any combination of the coins, return -1.

You may assume that you have an infinite Math of each kind of coin.
----------------------------------------------------------------------------------------------------
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
----------------------------------------------------------------------------------------------------
Example 2:

Input: coins = [2], amount = 3
Output: -1
----------------------------------------------------------------------------------------------------
Example 3:

Input: coins = [1], amount = 0
Output: 0
----------------------------------------------------------------------------------------------------
Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
import sys
from typing import List

import pytest


class Solution:
    """
    subproblems:
        amount - chosen coin
    recurrence:
        min(
            f(amount - coin1, coins_used + 1), f(amount - coin2, coins_used + 1)... coinN
        )
    topology:
        pass
    base case:
        amount == 0
    original:
        f(amount, 0)
    time complexity:
        time per subproblem:
            O(1) because Math of coins is bounded at a small constant 12
        # of subproblems:
            N -> where K is the amount of money
        O(N) after memoization / dp... before is O(K^N)
    """

    def __init__(self):
        self.memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = self.top_down_dp(sorted(coins), amount)
        return -1 if min_coins == float("inf") else min_coins

    def bottom_up_dp(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        def get_dp_val(idx):
            if -1 < idx < amount + 1:
                return dp[idx]
            return float("inf")

        for i in range(1, amount + 1):
            dp[i] = min([get_dp_val(i - coin) + 1 for coin in coins])
        return -1 if dp[amount] == float("inf") else dp[amount]

    def top_down_dp(self, coins, amount):
        if amount in self.memo:
            return self.memo[amount]

        if amount == 0:
            return 0
        elif amount < 0:
            return float("inf")
        min_coins = float("inf")
        for coin in coins:
            min_coins = min(min_coins, self.top_down_dp(coins, amount - coin) + 1)
        self.memo[amount] = min_coins
        return min_coins


tests = [
    pytest.param([1, 2, 5], 11, 3),
    pytest.param([2], 3, -1),
    pytest.param([1], 0, 0),
    pytest.param([3, 7, 405, 436], 8839, 25),
]


@pytest.mark.parametrize('coins, amount, expected', tests)
def test_coin_change(coins, amount, expected):
    solver = Solution()
    sys.setrecursionlimit(50000)
    result = solver.coinChange(coins, amount)
    assert result == expected


@pytest.mark.parametrize('coins, amount, expected', tests)
def test_bottom_up_dp(coins, amount, expected):
    solver = Solution()
    result = solver.bottom_up_dp(coins, amount)
    assert result == expected
