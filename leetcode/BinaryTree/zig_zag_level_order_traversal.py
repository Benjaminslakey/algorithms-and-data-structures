# @tags: [binary_tree, queue, stack, breadth_first_search]
from collections import deque
from typing import (Optional, List)

import pytest


from bts_lib.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from bts_lib.trees.binary_tree.binary_tree import BinaryTreeNode


class Solution:
    @staticmethod
    def zig_zag_level(level_num, level):
        if level_num % 2 == 0:
            return [level[idx].val for idx in range(0, len(level))]
        return [level[idx].val for idx in range(len(level) - 1, -1, -1)]

    def zigzagLevelOrder(self, root: Optional[BinaryTreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([None, root])
        levels = [[root.val]]
        level = deque([])
        level_num = 0
        while queue:
            node = queue.pop()
            if node is None and len(queue):
                level_num += 1
                levels.append(self.zig_zag_level(level_num, level))
                level = []
                queue.appendleft(None)
            if node and node.left:
                queue.appendleft(node.left)
                level.append(node.left)
            if node and node.right:
                queue.appendleft(node.right)
                level.append(node.right)
        return levels


@pytest.mark.parametrize('input_tree, expected_level_order', [
    pytest.param([], []),
    pytest.param([1], [[1]]),
    pytest.param([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
])
def test_zig_zag_level_order(input_tree, expected_level_order):
    root = deserialize_leetcode_tree(input_tree)
    solver = Solution()
    result = solver.zigzagLevelOrder(root)
    assert result == expected_level_order
