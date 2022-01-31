import pytest

"""
initial approach brute force
seems like a combinations / permutations problem
brute force generation via dfs, children of tree are possible rolls of nth die
leaves of tree are complete combinations where all dice have been rolled

optimization
optimized with memoization so as to not calculate / traverse duplicate subtrees

prune additional searches with that knowledge these statements being true prevents candidate extension
    current_sum too low: current_sum + remainingDice * k < target
    current_sum too high: current_sum + remainingDice > target

exponential algorithm, I think O(k^n)
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        key = f"{n}:{target}"
        if key in self.memo:
            return self.memo[key]
        if n == 0:
            return 1 if target == 0 else 0
        elif n > target or n * k < target:
            return 0

        ways_from_here = 0
        for die in range(1, k + 1):
            ways_from_here += self.numRollsToTarget(n - 1, k, target - die)
        self.memo[key] = ways_from_here
        return ways_from_here % ((10 ** 9) + 7)


@pytest.mark.parametrize('n, k, target, answer', [
    pytest.param(1, 6, 3, 1),
    pytest.param(2, 6, 7, 6),
    pytest.param(30, 30, 500, 222616187),
])
def test_dice_rolls(n, k, target, answer):
    solver = Solution()
    result = solver.numRollsToTarget(n, k, target)
    assert result == answer
