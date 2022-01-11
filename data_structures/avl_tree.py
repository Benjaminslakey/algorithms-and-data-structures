import random
from collections import (namedtuple, deque)
from typing import List, Optional, NoReturn, Tuple, Any, Iterable

import pytest

BALANCED = 0
RIGHT_RIGHT = 1
LEFT_LEFT = 2
RIGHT_LEFT = 3
LEFT_RIGHT = 4


class AVLNode(object):
    def __init__(self, val: Any, left=None, right=None):
        self.val: Any = val  # update Any types to a type that requires operators: >, <, ==
        self.count: int = 1  # store duplicate values in same node
        self.left: AVLNode = left
        self.right: AVLNode = right
        self.height: int = 1

    def __repr__(self) -> str:
        # could be useful for repr to show tree rooted at this node instead of just the node value
        return f"({self.val})"

    def update_height(self) -> NoReturn:
        self.height = max(self.left_height, self.right_height) + 1

    @property
    def balance_factor(self) -> int:
        return self.right_height - self.left_height

    @property
    def left_height(self) -> int:
        if self.left is None:
            return 0
        return self.left.height

    @property
    def right_height(self) -> int:
        if self.right is None:
            return 0
        return self.right.height


class AVLTree:
    def __init__(self, initial: Optional[Iterable[Any]] = None):
        self.root = None

        if initial is not None:
            self._build_tree(initial)

    def _build_tree(self, tree_vals: Iterable[Any]) -> NoReturn:
        for val in tree_vals:
            self.insert(val)

    @staticmethod
    def inorder(root: AVLNode) -> List[AVLNode]:
        if root is None:
            return []
        left = AVLTree.inorder(root.left)
        right = AVLTree.inorder(root.right)
        return left + [root.val] * root.count + right

    @staticmethod
    def is_balanced(root: AVLNode) -> Tuple[int, bool]:
        if root is None:
            return 0, True
        left_height, left_balanced = AVLTree.is_balanced(root.left)
        right_height, right_balanced = AVLTree.is_balanced(root.right)
        return (
            max(left_height, right_height) + 1,
            abs(right_height - left_height) < 2 and left_balanced and right_balanced
        )

    @staticmethod
    def print_tree(root: AVLNode) -> NoReturn:
        """
        inorder: [11, 20, 23, 26, 29, 50, 65]
        outputs ->
                          ----------------- 29  -----------------
                         /                                       \
                ------- 20  -------                     ------- 55  -------
               /                   \                   /                   \
           -- 11  --           -- 26  --           -- 50  --           -- 65  --
          /         \         /         \         /         \         /         \
        None      None       23       None      None      None      None      None
        """

        def format_node(data):
            node_len = len(str(data))
            # start with 0.01 base so that .5 will round up to 1 instead of to 0
            return f"{' ' * ((max_node_size - node_len) // 2)}{data}{' ' * round(0.01 + (max_node_size - node_len) / 2)}"

        max_node_size = 5
        traversal = AVLTree.level_order(root)
        tree_height = len(traversal)
        output = ""
        for level_depth, level_nodes in enumerate(traversal):
            level_height = tree_height - level_depth
            level_indent = max_node_size * (2 ** (level_height - 1)) - 1  # size of left subtree
            gap_between_nodes = max_node_size * ((2 ** level_height) - 1)  # size of parent left subtree
            node_strings = [format_node(node) for node in level_nodes]
            if level_height > 1:  # should have children
                link_length = (level_indent // 2) - 2
                between_nodes = f"{'-' * link_length}{' ' * (gap_between_nodes - link_length * 2)}{'-' * link_length}"
            else:
                link_length = 0
                between_nodes = ' ' * gap_between_nodes
            level_repr = between_nodes.join(node_strings)
            outter_link = f"{' ' * (level_indent - link_length)}{'-' * link_length}"
            parent_links = ""
            for idx, _ in enumerate(level_nodes):
                link_type = "/" if idx % 2 == 0 else "\\"
                parent_links += f"{format_node(link_type)}{' ' * gap_between_nodes}"
            if level_depth > 0:
                output += f"{' ' * level_indent}{parent_links}\n"
            output += f"{outter_link}{level_repr}{outter_link[::-1]}\n"
        print(f"\n{output}")

    @staticmethod
    def level_order(root: AVLNode) -> Iterable[Iterable[Any]]:
        q = deque([root])
        traversal = []
        while q:
            level = []
            next_lvl = deque()
            while q:
                node = q.pop()
                if node:
                    next_lvl.appendleft(node.left)
                    next_lvl.appendleft(node.right)
                    level.append(node.val)
                else:
                    for i in range(0, 2):
                        next_lvl.appendleft(None)
                    level.append(None)
            q = next_lvl
            traversal.append(level)
            if all(map(lambda x: x is None, next_lvl)):
                break
        return traversal

    def insert(self, val: Any) -> NoReturn:
        def _insert_helper(root: AVLNode, insert_value: Any) -> AVLNode:
            # base case, do insert
            if root is None:
                return AVLNode(insert_value)
            # find insertion point
            if insert_value < root.val:
                root.left = _insert_helper(root.left, insert_value)
            elif insert_value > root.val:
                root.right = _insert_helper(root.right, insert_value)
            else:
                root.count += 1
            # re-balance if necessary, we may want to return the new root here
            root.height = max(root.left_height, root.right_height) + 1
            return AVLTree._re_balance(root)
        self.root = _insert_helper(self.root, val)

    def delete(self, val: Any) -> NoReturn:
        """
        the complicated part of deleting from a BST involves the case where the node to be deleted has two children
        if the tree is so large that we need to do this iteratively then the logic for deleting that node becomes very
        complex. if we are able to process the deletion recursively we can simplify the case of two children to a simpler
        case of a single child by swapping the target node's value / key with that of its subtree successor.
        the subtree successor by definition will have at most one right child since it is the leftmost node of the
        target's right child (or right child itself). we then recursively call delete on the subtree with the duplicated
        value as our target
        """
        def _delete_helper(root: AVLNode, delete_value: Any) -> NoReturn:
            if root is None:  # value to delete did not exist in tree
                return

            if delete_value < root.val:
                root.left = _delete_helper(root.left, delete_value)
            elif delete_value > root.val:
                root.right = _delete_helper(root.right, delete_value)
            else:  # delete target found, perform deletion
                if root.count > 1:
                    root.count -= 1
                    return root
                # if node has only 1 child, replace it with the child
                # this will also handle the case where node is a leaf by returning null
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                # if the node has two children
                # step 1: find successor of node to be deleted
                successor = root.right
                while successor.left:
                    successor = successor.left
                # step 2: swap successor with node to be deleted by swapping stored value / key
                root.val = successor.val
                root.right = _delete_helper(root.right, successor.val)
            # re-balance the tree on the way back up the recursion
            root.height = max(root.left_height, root.right_height) + 1
            new_root = AVLTree._re_balance(root)
            return new_root
        self.root = _delete_helper(self.root, val)

    def search(self, val: Any) -> Optional[AVLNode]:
        node = self.root
        while node:
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
            else:
                break
        return node

    @staticmethod
    def _check_balance(root) -> Optional[int]:
        if root.balance_factor < -1:  # left heavy
            return LEFT_LEFT if root.left.balance_factor == -1 else LEFT_RIGHT
        elif root.balance_factor > 1:  # right heavy
            return RIGHT_RIGHT if root.right.balance_factor == 1 else RIGHT_LEFT
        return BALANCED

    @staticmethod
    def _re_balance(root) -> AVLNode:
        balance_type = AVLTree._check_balance(root)
        if balance_type == RIGHT_RIGHT:
            return AVLTree._left_rotation(root)
        elif balance_type == LEFT_LEFT:
            return AVLTree._right_rotation(root)
        elif balance_type == RIGHT_LEFT:
            root.right = AVLTree._right_rotation(root.right)
            return AVLTree._left_rotation(root)
        elif balance_type == LEFT_RIGHT:
            root.left = AVLTree._left_rotation(root.left)
            return AVLTree._right_rotation(root)
        return root

    @staticmethod
    def _right_rotation(root: AVLNode) -> NoReturn:
        """
             d          ->     b
          b     e       ->  a     d
        a   c           ->      c   e
        inorder: abcde  ->  inorder: abcde
        ----------------------------------
        """
        d = root
        b = root.left
        c = b.right
        d.left = c
        b.right = d
        d.update_height()
        b.update_height()
        return b

    @staticmethod
    def _left_rotation(root: AVLNode) -> NoReturn:
        """
           b            ->       d
        a     d         ->    b     e
            c   e       ->  a   c
        inorder: abcde  ->  inorder: abcde
        -----------------------------------
        """
        b = root
        d = root.right
        c = d.left
        b.right = c
        d.left = b
        b.update_height()
        d.update_height()
        return d

    def successor(self, value) -> Optional[AVLNode]:
        successor, parent, grandparent = None, None, None
        node = self.root
        while node:
            if node.val == value:
                break
            grandparent = parent
            parent = node
            if value < node.val:
                node = node.left
            else:
                node = node.right
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
        elif value < self.root.val:
            if value < parent.val:  # leaf on left side of parent, parent is successor
                successor = parent
            else:  # leaf on right side of parent, successor is grandparent
                successor = grandparent
        else:
            successor = parent
        return successor

    def predecessor(self, value) -> Optional[AVLNode]:
        predecessor, parent = None, None
        node = self.root
        while node:
            if node.val == value:
                break
            parent = node
            if value < node.val:
                node = node.left
            else:
                node = node.right
        if node.left:
            predecessor = node.left
            while predecessor.left:
                predecessor = predecessor.left
        elif node.val > parent.val:
            predecessor = parent
        return predecessor


@pytest.mark.parametrize('initial_tree', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55])
])
def test_avl_print_tree(initial_tree):
    avl = AVLTree(initial_tree)
    AVLTree.print_tree(avl.root)


@pytest.mark.parametrize('initial_tree, to_delete, expected_inorder', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, [11, 20, 23, 26, 29, 50, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 29, [11, 20, 23, 26, 50, 55, 65]),
    pytest.param([11, 20, 26, 65, 50, 23], 11, [20, 23, 26, 50, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 11, [20, 23, 26, 29, 50, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 55, 55], 55, [11, 20, 23, 26, 29, 50, 55, 55, 65]),
])
def test_avl_delete(initial_tree, to_delete, expected_inorder):
    avl = AVLTree(initial_tree)
    avl.delete(to_delete)
    assert AVLTree.inorder(avl.root) == expected_inorder
    AVLTree.print_tree(avl.root)
    _, is_balanced = AVLTree.is_balanced(avl.root)
    assert is_balanced


@pytest.mark.parametrize('initial_tree, to_insert, expected_inorder', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 105, [11, 20, 23, 26, 29, 50, 55, 65, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 82, [11, 20, 23, 26, 29, 50, 55, 65, 82]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 105], 82, [11, 20, 23, 26, 29, 50, 55, 65, 82, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 3, [3, 11, 20, 23, 26, 29, 50, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 105, 82], 3, [3, 11, 20, 23, 26, 29, 50, 55, 65, 82, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 17, [11, 17, 20, 23, 26, 29, 50, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 105, 82, 3], 17, [3, 11, 17, 20, 23, 26, 29, 50, 55, 65, 82, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, [11, 20, 23, 26, 29, 50, 55, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 55], 55, [11, 20, 23, 26, 29, 50, 55, 55, 55, 65]),
])
def test_avl_insert(initial_tree, to_insert, expected_inorder):
    avl = AVLTree(initial_tree)
    avl.insert(to_insert)
    assert AVLTree.inorder(avl.root) == expected_inorder
    _, is_balanced = AVLTree.is_balanced(avl.root)
    assert is_balanced


def test_avl_successor():
    pass


def test_avl_predecessor():
    pass
