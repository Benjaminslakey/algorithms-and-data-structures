# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root):
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, vmin, vmax):
        if root is None:
            return True
        return (
                vmin < root.val < vmax
                and self.helper(root.left, vmin, root.val)
                and self.helper(root.right, root.val, vmax)
        )

# @todo add unit tests
