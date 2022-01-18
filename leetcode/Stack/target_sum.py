# @tags: [stack]

from collections import deque

import pytest


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass


@pytest.mark.parametrize('nums, target, expected', [
    pytest.param([], []),
])
def test_target_sum(nums, target, expected):
    solver = Solution()
    result = solver.findTargetSumWays(nums, target)
    assert result == expected
