# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 and root2 is None:
            return root1
        elif root2 and root1 is None:
            return root2

        l = self.mergeTrees(root1.left, root2.left)
        r = self.mergeTrees(root1.right, root2.right)
        root1.val += root2.val
        root1.left = l
        root1.right = r
        return root1

# @todo add unit tests
# @tags: [binary_tree, recursion]

