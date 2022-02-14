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

    def bottom_up_dp(self, nums, mult):
        """ important note
        we iterate backwards in our DP because our base case is: 1 element remaining in multipliers, which happens when
        mult_idx == m - 1
        """
        n, m = len(nums), len(mult)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for mult_idx in range(m - 1, -1, -1):
            for left in range(mult_idx, -1, -1):
                right = -1 * (mult_idx + left - n)
                dp[mult_idx][left] = max(
                    dp[mult_idx + 1][left] + nums[right] * mult[mult_idx],
                    dp[mult_idx + 1][left - 1] + nums[left] * mult[mult_idx]
                )
        for row in dp:
            print(row)
        return dp[-1][-1]


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
