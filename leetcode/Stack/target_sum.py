# @tags: [stack]

from collections import deque
from typing import List

import pytest


class Solution:
    def __init__(self):
        self.paths = 0

    def traverse(self, nums, signs, target):
        if len(signs) == len(nums):
            if sum([n * signs[idx] for idx, n in enumerate(nums)]) == target:
                self.paths += 1
            return

        self.traverse(nums, signs + [-1], target)
        self.traverse(nums, signs + [1], target)

    def findTargetSumWays__recursive(self, nums: List[int], target: int) -> int:
        self.traverse(nums, [], target)
        return self.paths

    def findTargetSumWays__iterative(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if abs(nums[0]) == abs(target) else 0

        num_ways = 0
        stack = deque([])
        signs = []
        while stack or len(signs) < len(nums):
            while len(signs) <= len(nums):
                stack.append(signs)
                signs = signs + [1]
            signs = stack.pop()
            if sum([n * signs[idx] for idx, n in enumerate(nums)]) == target:
                num_ways += 1
            signs = signs + [-1]
        return num_ways


@pytest.mark.parametrize('nums, target, expected', [
    pytest.param([1, 1, 1, 1, 1], 3, 5),
    pytest.param([1], 1, 1),
    pytest.param([1], 2, 0),
    pytest.param([1000], -1000, 1),
])
def test_target_sum(nums, target, expected):
    solver = Solution()
    result = solver.findTargetSumWays__iterative(nums, target)
    assert result == expected
