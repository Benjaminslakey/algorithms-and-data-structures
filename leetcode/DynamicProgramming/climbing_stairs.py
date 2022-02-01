import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fib(n, {0: 0, 1: 1, 2: 2})

    def fib(self, n, memo):
        if n in memo:
            return memo[n]
        distinct_from_here = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        memo[n] = distinct_from_here
        return distinct_from_here


@pytest.mark.parametrize('num_stairs, expected_num_ways', [
    pytest.param(0, 0),
    pytest.param(1, 1),
    pytest.param(2, 2),
    pytest.param(5, 8),
    pytest.param(6, 13),
    pytest.param(7, 21),
    pytest.param(8, 34),
])
def test_climb_stairs(num_stairs, expected_num_ways):
    solver = Solution()
    num_ways = solver.climbStairs(num_stairs)
    assert num_ways == expected_num_ways
