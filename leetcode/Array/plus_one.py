from typing import List

import pytest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        incremented = int("".join([str(d) for d in digits])) + 1
        return [int(d) for d in str(incremented)]


@pytest.mark.parametrize('nums, expected_result', [
    pytest.param([1, 2, 3], [1, 2, 4]),
    pytest.param([4, 3, 2, 1], [4, 3, 2, 2]),
    pytest.param([9], [1, 0])
])
def test_plus_one(nums, expected_result):
    solver = Solution()
    result = solver.plusOne(nums)
    assert result == expected_result
