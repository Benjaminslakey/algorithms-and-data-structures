from typing import List, Optional, NoReturn, Tuple, Any

import pytest

from data_structures.avl_tree import AVLTree


def create_avl(nums: List[int], start: int, end: int) -> AVLTree:
    avl_tree = AVLTree()
    for idx in range(start, end + 1):
        avl_tree.insert(nums[idx % len(nums)])
    return avl_tree


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False
        left = 0
        right = k
        # use self balancing BST for logN: search, insert, deletion
        # to make sorted sliding window operations quick
        window_avl = create_avl(nums, left, right)
        while left < len(nums):
            r = right % len(nums)
            if right > k and window_avl.search(nums[r]) is None:  # just to skip the first insert which would duplicate initial right
                window_avl.insert(nums[r])
            idx = left
            i = idx % len(nums)
            while i <= right:
                i = idx % len(nums)
                successor = window_avl.successor(nums[i])
                predecessor = window_avl.predecessor(nums[i])
                # successor and predecessor are nearest values
                # ie, they will minimize value being compared to T, if they don't work
                # then no other values in the tree will. though if they do work there could be other
                # nodes that also work, but we are only trying to determine if a solution exists
                # not all possible solutions
                if predecessor is not None and abs(nums[i] - predecessor.val) <= t:
                    return True
                if successor is not None and abs(nums[i] - successor.val) <= t:
                    return True
                idx += 1
            window_avl.delete(nums[left])
            left += 1
            right += 1
        return False


@pytest.mark.parametrize('input_array, k, t, expected_output', [
    pytest.param([1], 1, 1, False),
    pytest.param([6, 2, 3, 5], 2, 1, True),
    pytest.param([2147483646, 2147483647], 3, 3, True),
    pytest.param([1, 5, 9, 1, 5, 9], 2, 3, False)
])
def test_leetcode_problem(input_array, k, t, expected_output):
    solver = Solution()
    result = solver.containsNearbyAlmostDuplicate(input_array, k, t)
    print(f"k: {k}, t: {t}, nums: {input_array}\nresult: {result}\nexpected: {expected_output}")
    assert result == expected_output
