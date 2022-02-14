from typing import List

import pytest


class Solution:
    def __init__(self):
        self.permutations = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.permutations

    def backtrack(self, nums, selected):
        if not nums:
            self.permutations.append([_ for _ in selected])
            return

        for idx in range(len(nums)):
            val = nums.pop(idx)
            selected.append(val)
            self.backtrack(nums, selected)
            nums.insert(idx, val)
            selected.pop()


@pytest.mark.parametrize('digits, expected_permutations', [
    pytest.param([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    pytest.param([0, 1], [[0, 1], [1, 0]]),
    pytest.param([1], [[1]]),
])
def test_letter_combos(digits, expected_permutations):
    solver = Solution()
    result = solver.permute(digits)
    assert result == expected_permutations
