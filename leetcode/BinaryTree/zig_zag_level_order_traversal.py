# @tags: [binary_tree, queue, stack, breadth_first_search]

import pytest

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                zig_zag = []
                while level:
                    if level_num % 2 == 0:
                        n = level.pop()
                    else:
                        n = level.popleft()
                    zig_zag.append(n.val)
                levels.append(zig_zag)
                level = deque([])
                queue.appendleft(None)
            if node and node.left:
                queue.appendleft(node.left)
                level.appendleft(node.left)
            if node and node.right:
                queue.appendleft(node.right)
                level.appendleft(node.right)
        return levels


@pytest.mark.parametrize('input_tree, expected_level_order', [
    pytest.param([], []),
    pytest.param([1], [1]),
    pytest.param([3,9,20,None,None,15,7], [[3],[20,9],[15,7]]),
])
def test_zig_zag_level_order(input_tree, expected_level_order):
    root = deserialize_leetcode_tree(input_tree)
    solver = Solution()
    result = solver.zigzagLevelOrder(root)
    assert result == expected_level_order
