from collections import deque
from typing import Optional, List, Any

from data_structures.trees.binary_tree import BinaryTreeNode


def level_order_traversal(root: Optional[BinaryTreeNode]) -> List[List[int]]:
    if root is None:
        return []

    queue = deque([None, root])
    levels = [[root.val]]
    current_level = []
    while queue:
        node = queue.pop()
        if node is None and len(queue):
            levels.append(current_level)
            current_level = []
            queue.appendleft(None)
        if node and node.left:
            queue.appendleft(node.left)
            current_level.append(node.left.val)
        if node and node.right:
            queue.appendleft(node.right)
            current_level.append(node.right.val)
    return levels


def preorder_traversal(root: BinaryTreeNode) -> List[Any]:
    if root is None:
        return []
    left = preorder_traversal(root.left)
    right = preorder_traversal(root.right)
    return [root.val] * root.count + left + right


def inorder_traversal(root: BinaryTreeNode) -> List[Any]:
    if root is None:
        return []
    left = inorder_traversal(root.left)
    right = inorder_traversal(root.right)
    return left + [root.val] * root.count + right


def postorder_traversal(root: BinaryTreeNode) -> List[Any]:
    if root is None:
        return []
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    return left + right + [root.val] * root.count

