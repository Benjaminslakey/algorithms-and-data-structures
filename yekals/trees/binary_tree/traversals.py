from collections import deque
from typing import Optional, List

from yekals.trees.binary_tree.binary_tree import BinaryTreeNode
from yekals.trees.binary_tree import PREORDER, INORDER, POSTORDER

LEVEL_MARKER = 0


def level_order_traversal(root: Optional[BinaryTreeNode], process: callable):
    """
    we track the number of nulls in a given level so we can tell that when we're on a level with all nulls
    if we're on a level with all nulls, we have nothing left to process because we've already hit all the leaves
    """
    if root is None:
        return

    nulls_in_level = 0
    queue = deque([LEVEL_MARKER, root])
    while queue:
        node = queue.pop()
        if node == LEVEL_MARKER and len(queue):
            if len(queue) == nulls_in_level:
                return
            nulls_in_level = 0
            queue.appendleft(LEVEL_MARKER)

        if process is not None:
            process(node)

        if node != LEVEL_MARKER and node is not None:
            if node.left is None:
                nulls_in_level += 1
            if node.right is None:
                nulls_in_level += 1
            queue.appendleft(node.left)
            queue.appendleft(node.right)


def capture_flat_level_order(capture_arr):
    def wrapped(node):
        if node == LEVEL_MARKER:
            return
        if node is None:
            capture_arr.append(None)
        else:
            capture_arr.append(node.val)

    return wrapped


def capture_level_order(capture_arr):
    prev_node = None

    def wrapped(node):
        nonlocal prev_node
        if prev_node == LEVEL_MARKER:
            capture_arr.append([])
        prev_node = node
        if node == LEVEL_MARKER:
            return
        if not capture_arr:
            capture_arr.append([])
        if node is not None:
            capture_arr[-1].append(node.val)
    return wrapped


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
