# Definition for a binary tree node.
# class BinaryTreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        return root

# @todo add unit tests
# @tags: [binary_tree, recursion]
