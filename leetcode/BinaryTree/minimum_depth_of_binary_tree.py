# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        to_visit = deque([(root, 1)])
        while to_visit:
            current, depth = to_visit.pop()
            if current.left is None and current.right is None:
                return depth
            if current.left:
                to_visit.appendleft((current.left, depth + 1))
            if current.right:
                to_visit.appendleft((current.right, depth + 1))
        raise Exception("Should not happen")

# @todo add unit tests
# @tags: [binary_tree, breadth_first_search, queue]
