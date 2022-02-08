# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    """
    find all root -> leaf paths and their sums
    filter paths down to those with sum less than limit
    find common nodes between all paths

    depth first search
        base case:
            node is none
                return 0

    """

    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if root is None:
            return None
        sums = self.dfs(root, root.val, limit)
        return None if all([s < limit for s in sums]) else root

    def dfs(self, node, path_sum, limit):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [path_sum + node.val]
        left_sums = self.dfs(node.left, path_sum + node.val, limit)
        right_sums = self.dfs(node.right, path_sum + node.val, limit)
        if all([s < limit for s in left_sums]):
            node.left = None
        if all([s < limit for s in right_sums]):
            node.right = None
        return left_sums + right_sums
