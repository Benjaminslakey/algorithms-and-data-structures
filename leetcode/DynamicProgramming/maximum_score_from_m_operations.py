from typing import List

import pytest


class Solution:
    """
    can't be greedy because the indices between nums & multipliers are related
    find max so we want to use dynamic programming

    base case: having used all of the multipliers
    state: is our index in each list
    return value: result of multiplication operations + solution to subproblem

    nums: [1, 2, 3, 4, 5]
    mult: [5, 4, 3, 2, 2]

    MIT - SRTBOT
    subproblem:
        substrings nums[l:r], suffixes: multipliers[:i]
    recurrence relation:
        max(
            (nums[l] * multi[i]) + f(l + 1, r, i + 1),
            (nums[r] * multi[i]) + f(l, r - 1, i + 1)
        )
    topological order:
        i...len(mult)
    base case:
        i >= len(multi)
    original problem:
        f(0, 0, 0)
    time complexity:
        # of subproblems => len(multi) * 2
    """

    def __init__(self):
        self.memo = {}
        self.multipliers = []
        self.nums = []

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.multipliers = multipliers
        self.nums = nums
        # return self.top_down_dp(0, 0, len(nums) - 1)
        return self.bottom_up_dp(nums, multipliers)

    def top_down_dp(self, mult_idx, left, right):
        """ Leetcode TimeLimitExceeded: though exact implementations in other languages do not"""
        key = f"{left}:{right}"
        if key in self.memo:
            return self.memo[key]

        if mult_idx == len(self.multipliers) - 1:
            return max(
                self.nums[left] * self.multipliers[mult_idx],
                self.nums[right] * self.multipliers[mult_idx]
            )
        left_choice = (self.nums[left] * self.multipliers[mult_idx]) + self.top_down_dp(mult_idx + 1, left + 1, right)
        right_choice = (self.nums[right] * self.multipliers[mult_idx]) + self.top_down_dp(mult_idx + 1, left, right - 1)
        best_choice = max(left_choice, right_choice)
        self.memo[key] = best_choice
        return best_choice

    def bottom_up_dp(self, nums, multipliers):
        """ not correct """
        dp = [[0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]
        dp[0] = multipliers[0] * nums[0]
        dp[1] = multipliers[0] * nums[-1]
        l, r = 0, len(nums) - 1
        for idx in range(2, len(dp)):
            dp[idx] = max(
                dp[idx - 1] + nums[r - idx + 1] * multipliers[idx - 1],
                dp[idx - 2] + nums[l + idx - 1] * multipliers[idx - 1]
            )
        return dp[0][0]


@pytest.mark.parametrize('nums, multipliers, expected_best_score', [
    pytest.param([1, 2, 3], [3, 2, 1], 14),
    pytest.param([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102),
])
def test_max_score(nums, multipliers, expected_best_score):
    solver = Solution()
    result = solver.maximumScore(nums, multipliers)
    assert result == expected_best_score


slow_test_case = pytest.param(
    [555, 526, 732, 182, 43, -537, -434, -233, -947, 968, -250, -10, 470, -867, -809, -987, 120, 607, -700, 25,
     -349, -657, 349, -75, -936, -473, 615, 691, -261, -517, -867, 527, 782, 939, -465, 12, 988, -78, -990, 504,
     -358, 491, 805, 756, -218, 513, -928, 579, 678, 10],
    [783, 911, 820, 37, 466, -251, 286, -74, -899, 586, 792, -643, -969, -267, 121, -656, 381, 871, 762, -355, 721,
     753, -521], 6861161
)
