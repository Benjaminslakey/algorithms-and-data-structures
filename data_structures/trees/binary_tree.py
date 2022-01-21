

class BinaryTreeNode:
    """Leetcode Binary Tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 0

    def __repr__(self):
        return f"{self.val}"
