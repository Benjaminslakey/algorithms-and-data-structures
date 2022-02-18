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
        pass

    def three_sum__two_pointers(self, nums: List[int]) -> List[List[int]]:
        pass


    def three_sum__no_sort(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        complements = defaultdict(set)
        seen = set()
        for idx, n in enumerate(nums):
            complements[n].add(idx)

        for i in range(0, len(nums)):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                pair = tuple(sorted([num1, num2]))
                if pair in seen:
                    continue
                else:
                    seen.add(pair)
                complement = (num1 + num2) * -1
                complement_idxs = complements.get(complement, set())
                if complement_idxs and complement_idxs - {i, j}:
                    triplets.append(sorted([num1, num2, complement]))
                    seen.add(tuple(sorted([num1, complement])))
                    seen.add(tuple(sorted([num2, complement])))
        return triplets


@pytest.mark.parametrize('nums, expected_triplets', [
    pytest.param([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
])
def test_3sum(nums, expected_triplets):
    solver = Solution()
    result = solver.threeSum(nums)
    assert sorted(result) == sorted(expected_triplets)
