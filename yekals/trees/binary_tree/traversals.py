from collections import deque
from typing import Optional, List

from yekals.trees.binary_tree.binary_tree import BinaryTreeNode
from trees.binary_tree import PREORDER, INORDER, POSTORDER


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


def depth_first_traversal(root: BinaryTreeNode, process: callable, process_order: int = INORDER) -> None:
    if root is None:
        return
    if process_order == PREORDER:
        process(root)
    depth_first_traversal(root.left, process)
    if process_order == INORDER:
        process(root)
    depth_first_traversal(root.right, process)
    if process_order == POSTORDER:
        process(root)
