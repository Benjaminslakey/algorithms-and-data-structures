from typing import List

import pytest


class Solution:
    """
    [ 1, 2, 3, 4, 5, 6, 7] => 28
    [3, 1, 6, 0, 35, 5, 2] => 17
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        for i, num in enumerate(nums):
            while 0 < num < len(nums) - 1 and num != i + 1:
                nums[num - 1], nums[i], num = num, nums[num - 1], nums[num - 1]
        for idx, num in enumerate(nums):
            if idx + 1 != num:
                return idx + 1
        return len(nums) + 1


@pytest.mark.parametrize('nums, expected', [
    pytest.param([1], 2),
    pytest.param([-1], 1),
    pytest.param([1, 1], 2),
    pytest.param([1, 2, 3, 4, 5], 6),
    pytest.param([5, 4, 3, 2, 1], 6),
    pytest.param([3, 4, -1, 1], 2),
])
def test_first_missing_positive(nums, expected):
    solver = Solution()
    result = solver.firstMissingPositive(nums)
    assert result == expected
