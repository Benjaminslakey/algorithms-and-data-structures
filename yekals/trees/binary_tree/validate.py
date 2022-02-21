from typing import Tuple

from yekals.trees.binary_tree.binary_tree import BinaryTreeNode


def is_balanced(tree_root: BinaryTreeNode) -> bool:
    def helper(root: BinaryTreeNode) -> Tuple[int, bool]:
        if root is None:
            return 0, True
        left_height, left_balanced = helper(root.left)
        right_height, right_balanced = helper(root.right)
        return (
            max(left_height, right_height) + 1,
            abs(right_height - left_height) < 2 and left_balanced and right_balanced
        )
    _, balanced = helper(tree_root)
    return balanced
