from typing import List

import pytest


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l_idx = 0
        largest = 0
        second_largest = -1
        for idx, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                l_idx = idx
            elif num > second_largest:
                second_largest = num

        return -1 if second_largest * 2 > largest else l_idx


@pytest.mark.parametrize('nums, dominant_index', [
    pytest.param([3, 6, 1, 0], 1),
    pytest.param([1, 2, 3, 4], -1),
    pytest.param([1], 0)
])
def test_twice_others(nums, dominant_index):
    solver = Solution()
    result = solver.dominantIndex(nums)
    assert result == dominant_index
