from typing import List

import pytest


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        prev = 0
        for idx, num in enumerate(nums):
            left += prev
            right -= num
            if left == right:
                return idx
            prev = num
        return -1


@pytest.mark.parametrize('nums, middle', [
    pytest.param([1, 7, 3, 6, 5, 6], 3),
    pytest.param([1, 2, 3], -1),
    pytest.param([2, 1, -1], 0),
])
def test_pivot_index(nums, middle):
    solver = Solution()
    result = solver.pivotIndex(nums)
    assert result == middle
