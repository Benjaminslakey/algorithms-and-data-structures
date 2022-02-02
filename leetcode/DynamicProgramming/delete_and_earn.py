import cProfile
from collections import Counter, defaultdict
from typing import List

import pytest


class Solution:
    def __init__(self):
        self.memo = {}
        self.max_points = -1
        self.counts = {}

    def deleteAndEarn(self, nums: List[int]) -> int:
        self.counts = Counter(nums)
        # return self.top_down(sorted(set(nums)), 0, 0)
        return self.bottom_up(nums)

    def top_down(self, nums, idx, points):
        key = f"{idx}:{points}"
        if key in self.memo:
            return self.memo[key]

        if idx >= len(nums):
            return points

        num = nums[idx]
        if idx + 1 < len(nums) and nums[idx + 1] > nums[idx] + 1:
            j = 1
        else:
            j = 2
        skip_points_earned = self.top_down(nums, idx + 1, points)
        take_points_earned = self.top_down(nums, idx + j, points + num * self.counts[num])
        max_points_from_state = max(take_points_earned, skip_points_earned)
        self.memo[key] = max_points_from_state
        return max_points_from_state

    def bottom_up(self, nums):
        # @todo not correct still
        frequency = Counter(nums)
        numbers = sorted(list(frequency.keys()))

        dp = [0] * (len(numbers) + 1)
        dp[1] = numbers[0]
        for idx in range(2, len(numbers) + 1):
            num = numbers[idx - 1]
            take = num * frequency[num]
            dp[idx] = max(dp[idx - 2] + take, dp[idx - 1])
        return dp[-1]


@pytest.mark.parametrize('nums, max_points', [
    pytest.param([3, 1], 4),
    pytest.param([3, 4, 2], 6),
    pytest.param([2, 2, 3, 3, 3, 4], 9),
    pytest.param([6, 5, 10, 2, 8, 6, 6, 5, 2, 9, 9, 4, 6, 3, 3, 7, 7, 8, 9, 5], 62),
    pytest.param(
        [94, 27, 27, 27, 34, 82, 97, 93, 62, 10, 78, 25, 23, 41, 53, 16, 81, 93, 52, 53, 74, 78, 18, 27, 66, 62, 40, 50,
         8, 20, 31, 77, 26, 82, 28, 60, 98, 94, 26, 30, 23, 49, 54, 80, 69, 28, 25, 32, 78, 7, 1, 73, 2, 31, 99, 78, 50,
         95, 28, 53, 60, 78, 71, 52, 25, 85, 21, 16, 20, 78, 96, 96, 65, 1, 19, 18, 24, 18, 55, 69, 88, 76, 14, 23, 58,
         17, 83, 43, 63, 9, 41, 6, 71, 7, 2, 20, 21, 63, 18, 36, 53, 95, 36, 11, 32, 64, 52, 48, 52, 11, 50, 48, 35, 49,
         24, 89, 72, 33, 60, 57, 46, 3, 24, 90, 20, 95, 87, 8, 93, 1, 47, 2, 66, 45, 57, 75, 18, 76, 96, 67, 65, 92, 92,
         41, 57, 60, 98, 98, 10, 64, 23, 86, 100, 20, 21, 93, 49, 54, 77, 77, 34, 98, 94, 4, 9, 75, 67, 4, 31, 82, 87,
         26, 70, 26, 59, 86, 100, 22, 15, 61, 57, 73, 54, 54, 76, 82, 56, 63, 49, 46, 53, 71, 32, 1, 64, 48, 20, 71, 2,
         60, 83, 80, 97, 30, 2, 57, 31, 82, 21, 63, 52, 46, 71, 55, 58, 94, 16, 9, 62, 67, 74, 79, 87, 31, 53, 27, 80,
         11, 33, 52, 73, 2, 88, 80, 9, 38, 37, 3, 79, 24, 89, 75, 10, 97, 24, 63, 24, 47, 80, 56, 75, 23, 32, 58, 72,
         80, 95, 28, 57, 37, 17, 48, 14, 85, 58, 61, 58, 1, 37, 14, 34, 76, 11, 63, 67, 7, 9, 8, 74, 38, 97, 56, 25, 67,
         9, 34, 62, 58, 72, 77, 15, 15, 90, 36, 60, 39, 95, 61, 28, 44, 43, 56, 22, 12, 81, 13, 10, 91, 84, 46, 39, 35,
         39, 65, 82, 41, 51, 19, 76, 99, 75, 88, 43, 89, 21, 83, 6, 35, 21, 47, 4, 21, 51, 76, 63, 43, 71, 39, 43, 16,
         36, 78, 35, 68, 75, 81, 91, 97, 7, 82, 44, 73, 56, 39, 76, 21, 76, 87, 98, 6, 38, 96, 84, 96, 77, 84, 83, 28,
         52, 100, 6, 52, 78, 7, 91, 96, 97, 62, 32, 26, 7, 80, 71, 25, 58, 23, 54, 74, 81, 4, 84, 35, 83, 58, 64, 42,
         38, 30, 88, 87, 52, 95, 23, 31, 31, 55, 7, 20, 18, 84, 40, 14, 93, 40, 45, 69, 84, 30, 66, 6, 88, 41, 88, 98,
         80, 69, 64, 1, 100, 48, 2, 89, 6, 21, 45, 73, 77, 31, 20, 70, 89, 30, 53, 33, 59, 8, 82, 63, 17, 10, 46, 49,
         86, 9, 14, 68, 6, 15, 55, 36, 71, 64, 80, 59, 40, 60, 46, 24, 49, 45, 78, 38, 92, 43, 99, 78, 5, 83, 57, 76,
         34, 11, 93, 71, 71, 54, 54, 29, 29, 74, 83, 72, 1, 6, 56, 22, 85, 35, 48, 29], 14251)
])
def test_delete_and_earn(nums, max_points):
    solver = Solution()
    result = solver.deleteAndEarn(nums)
    assert result == max_points
