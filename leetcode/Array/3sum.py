from collections import defaultdict
from typing import List

import pytest


class Solution:
    """
    assumptions:
    a triplet is defined as a combination not a permutation, ie order doesn't matter when considering two triplets to be the same
    you can reuse a given item in separate triplets


    create a hash table of complements => O(n)
    enumerate all unique pairs
        look up complement
        if complement exists
        record triplet as pair + complement
        record triplet as seen
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        complements = defaultdict(list)
        seen = set()
        for idx, n in enumerate(nums):
            complements[n].append(idx)

        for i in range(0, len(nums)):
            num1 = nums[i]
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if tuple(sorted([i, j])) in seen:
                    continue
                num2 = nums[j]
                complement = (num1 + num2) * -1
                complement_idxs = complements.get(complement, [])
                if not complement_idxs:
                    continue
                triplet = sorted([num1, num2, complement])
                for c_idx in complement_idxs:
                    if c_idx != i and c_idx != j:
                        triplets.append(triplet)
                        break
        return triplets


@pytest.mark.parametrize('nums, expected_triplets', [
    pytest.param()
])
def test_3sum(nums, expected_triplets):
    solver = Solution()
    result = solver.threeSum(nums)
    assert result == expected_triplets

