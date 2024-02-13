# Definition for a binary tree node.
import pytest

from yekals.trees.binary_tree.binary_tree import BinaryTreeNode
from yekals.trees.binary_tree.traversals import level_order_traversal


def deserialize_leetcode_tree(tree_arr):
    def get_node():
        if tree_arr:
            for val in tree_arr:
                yield BinaryTreeNode(val) if val is not None else None
        else:
            yield None

    if not tree_arr:
        return None

    tree_generator = get_node()
    root = next(tree_generator)
    parents = [root]
    while True:
        children = []
        for parent in parents:
            if parent is None:
                continue
            try:
                parent.left = next(tree_generator)
                parent.right = next(tree_generator)
                children.extend([parent.left, parent.right])
            except StopIteration:
                return root
        parents = children
    return root
