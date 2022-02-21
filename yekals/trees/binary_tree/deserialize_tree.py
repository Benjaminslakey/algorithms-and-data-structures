# Definition for a binary tree node.

from yekals.trees.binary_tree.binary_tree import BinaryTreeNode


def deserialize_leetcode_tree(tree_arr):
    def get_node():
        if tree_arr:
            for val in tree_arr:
                yield BinaryTreeNode(val) if val is not None else None
        else:
            yield None

    tree_generator = get_node()
    root = next(tree_generator)
    parents = [root]
    while True:
        children = []
        for parent in parents:
            try:
                parent.left = next(tree_generator)
                parent.right = next(tree_generator)
                children.extend([parent.left, parent.right])
            except StopIteration:
                return root
        parents = children
    return root
