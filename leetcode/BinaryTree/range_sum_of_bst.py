from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        l = self.rangeSumBST(root.left, low, high)
        r = self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            return l + r + root.val
        return l + r


# @todo add unit tests