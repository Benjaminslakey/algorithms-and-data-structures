from typing import List, Optional, NoReturn, Tuple, Any

import pytest
from sortedcontainers import SortedList

from data_structures.avl_tree import AVLTree


def create_avl(nums: List[int], start: int, end: int) -> AVLTree:
    avl_tree = AVLTree()
    for idx in range(start, end + 1):
        if idx >= len(nums):
            break
        avl_tree.insert(nums[idx])
    return avl_tree


class Solution:
    def containsNearbyAlmostDuplicate__using_avl_tle(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0 or len(nums) <= 1:
            return False
        left = 0
        right = k
        # use self balancing BST for logN: search, insert, deletion
        # to make sorted sliding window operations quick
        window_avl = create_avl(nums, left, right)
        while left < len(nums):
            # just to skip the first insert which would duplicate initial right
            if k < right < len(nums):
                window_avl.insert(nums[right])
            idx = left
            while idx <= right and idx < len(nums):
                node = window_avl.search(nums[idx])
                successor = window_avl.successor(nums[idx])
                predecessor = window_avl.predecessor(nums[idx])
                # successor and predecessor are nearest values
                # ie, they will minimize value being compared to T, if they don't work
                # then no other values in the tree will. though if they do work there could be other
                # nodes that also work, but we are only trying to determine if a solution exists
                # not all possible solutions
                if predecessor is not None and abs(node.val - predecessor.val) <= t:
                    return True
                elif successor is not None and abs(node.val - successor.val) <= t:
                    return True
                elif node is not None and node.count > 1:
                    return True
                idx += 1
            window_avl.delete(nums[left])
            left += 1
            right += 1
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0 or len(nums) <= 1:
            return False
        left = 0
        right = k
        # use self balancing BST for logN: search, insert, deletion
        # to make sorted sliding window operations quick
        window_avl = SortedList([nums[idx] for idx in range(0, min(len(nums), k + 1))])
        while left < len(nums):
            # just to skip the first insert which would duplicate initial right
            if k < right < len(nums):
                window_avl.add(nums[right])
            idx = left
            while idx <= right and idx < len(nums):
                curr = window_avl.index(nums[idx])
                val = nums[idx]
                try:
                    successor = window_avl[curr + 1]
                    if abs(val - successor) <= t:
                        return True
                except IndexError:
                    successor = None
                try:
                    predecessor = window_avl[curr - 1]
                    if abs(val - predecessor) <= t:
                        return True
                except IndexError:
                    predecessor = None

                if window_avl.count(val) > 1:
                    return True
                idx += 1
            window_avl.remove(nums[left])
            left += 1
            right += 1
            if right >= len(nums):
                break
        return False


@pytest.mark.parametrize('input_array, k, t, expected_output', [
    pytest.param([1], 1, 1, False),
    pytest.param([6, 2, 3, 5], 2, 1, True),
    pytest.param([2147483646, 2147483647], 3, 3, True),
    pytest.param([1, 5, 9, 1, 5, 9], 2, 3, False),
    pytest.param([1, 2, 3, 1], 3, 0, True),
    pytest.param([1, 0, 1, 1], 1, 2, True),
    pytest.param([2147483647, -1, 2147483647], 1, 2147483647, False),
    pytest.param([1, 5, 9, 1, 5, 9], 2, 3, False),
])
def test_leetcode_problem(input_array, k, t, expected_output):
    solver = Solution()
    result = solver.containsNearbyAlmostDuplicate(input_array, k, t)
    print(f"k: {k}, t: {t}, nums: {input_array}\nresult: {result}\nexpected: {expected_output}")
    assert result == expected_output
