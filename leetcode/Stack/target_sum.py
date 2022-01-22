# @tags: [stack]

from collections import deque
from typing import List

import pytest

from algorithms.trees.binary_tree.print_tree import print_tree
from data_structures.trees.binary_tree import BinaryTreeNode


class Solution:
    def __init__(self):
        self.paths = 0
        self.unique_paths = set()
        self.memo = {}

    def traverse(self, nums, idx, current_sum, target):
        key = f"{idx}:{current_sum}"
        if key in self.memo:
            return self.memo[key]
        # we have reached a leaf node
        if idx == len(nums):
            return 1 if current_sum == target else 0

        negative = self.traverse(nums, idx + 1, current_sum - nums[idx], target)
        positive = self.traverse(nums, idx + 1, current_sum + nums[idx], target)
        self.memo[key] = negative + positive
        return negative + positive

    def findTargetSumWays__recursive(self, nums: List[int], target: int) -> int:
        """fast correct version to validate iterative version against"""
        return self.traverse(nums, 0, 0, target)

    def findTargetSumWays__iterative__debug(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if abs(nums[0]) == abs(target) else 0

        def make_node(path_sum, item):
            return BinaryTreeNode(f"{item}:{path_sum}")

        memo = {}
        num_ways = 0
        idx = -1
        current_sum = 0
        root = make_node(0, -1)
        prev = root
        stack = deque([(0, -1, root)])
        node = make_node(current_sum, nums[0])
        while stack or idx < len(nums) - 1:
            while idx < len(nums) - 1:
                # visit left child
                idx += 1
                current_sum += nums[idx]
                node = make_node(current_sum, nums[idx])
                stack.append((current_sum, idx, node))
                prev.left = node
                prev = node
            current_sum, idx, node = stack.pop()
            if idx == len(nums) - 1 and stack:  # this is a leaf node
                if current_sum == target:
                    num_ways += 1
                current_sum, idx, node = stack.pop()
            idx += 1
            current_sum -= nums[idx]
            node.right = make_node(current_sum, nums[idx] * -1)
            prev = node.right
            if idx < len(nums) - 1:
                stack.append((current_sum, idx, prev))
            if idx == len(nums) - 1 and current_sum == target:
                num_ways += 1
        print_tree(root)
        return num_ways

    def findTargetSumWays__iterative(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if abs(nums[0]) == abs(target) else 0

        parents = {}

        num_ways = 0
        idx = -1
        current_sum = 0
        stack = deque([(0, -1, (0, -1))])
        while stack or idx < len(nums) - 1:
            while idx < len(nums) - 1:
                # remember parent for memoization
                parent = (current_sum, idx)
                # go to left child
                current_sum += nums[(idx := idx + 1)]
                stack.append((current_sum, idx, parent))
            current_sum, idx, parent = stack.pop()
            if idx == len(nums) - 1 and stack:  # this is a leaf node
                if current_sum == target:
                    num_ways += 1
                # pop back to lowest leftmost, incomplete subtree root
                current_sum, idx, parent = stack.pop()
            # go to right child
            parent = (current_sum, idx)
            current_sum -= nums[(idx := idx + 1)]
            # if right child is a subtree and not a leaf, put it on the stack
            if idx < len(nums) - 1:
                stack.append((current_sum, idx, parent))
            if idx == len(nums) - 1 and current_sum == target:
                num_ways += 1
        return num_ways


target_sum_test_cases = [
    pytest.param([1, 1, 1, 1, 1], 3, 5),
    pytest.param([1], 1, 1),
    pytest.param([1], 2, 0),
    pytest.param([1000], -1000, 1),
    pytest.param([12, 51, 16, 3, 4, 8, 4], 60, 4),
    pytest.param([42, 24, 30, 14, 38, 27, 12, 29, 43, 42, 5, 18, 0, 1, 12, 44, 45, 50, 21, 47], 38, 5602),
    pytest.param([44, 20, 38, 6, 2, 47, 18, 50, 41, 38, 32, 24, 38, 38, 30, 5, 26, 15, 37, 35], 44, 4983),
    pytest.param([45, 18, 27, 39, 42, 19, 1, 35, 32, 16, 7, 6, 25, 41, 27, 18, 38, 6, 42, 10], 49, 0),
]


@pytest.mark.parametrize('nums, target, expected', target_sum_test_cases)
def test_target_sum__recursive(nums, target, expected):
    solver = Solution()
    result = solver.findTargetSumWays__recursive(nums, target)
    assert result == expected


@pytest.mark.parametrize('nums, target, expected', target_sum_test_cases)
def test_target_sum__iterative(nums, target, expected):
    solver = Solution()
    result = solver.findTargetSumWays__iterative(nums, target)
    assert result == expected
