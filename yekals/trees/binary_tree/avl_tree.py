from typing import (Optional, NoReturn, Iterable, Protocol)

from yekals.trees.binary_tree.binary_tree import BinaryTreeNode

BALANCED = 0
RIGHT_RIGHT = 1
LEFT_LEFT = 2
RIGHT_LEFT = 3
LEFT_RIGHT = 4


class AVLData(Protocol):
    def __eq__(self, other) -> bool:
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...


class AVLNode(BinaryTreeNode):
    def __init__(self, val: Optional[AVLData], left=None, right=None):
        super().__init__(val, left, right)
        self.val: Optional[AVLData] = val  # update Any types to a type that requires operators: >, <, ==
        self.count: int = 1  # store duplicate values in same node
        self.left: Optional[AVLNode] = left
        self.right: Optional[AVLNode] = right
        self.height: int = 1

    def __repr__(self) -> str:
        # could be useful for repr to show tree rooted at this node instead of just the node value
        return f"({self.val})"

    def __eq__(self, other):
        if not isinstance(other, AVLNode):
            raise TypeError(f"Cannot compare AVLNode instance with {other}")
        return self.val == other.val

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
    def __init__(self, initial: Optional[Iterable[AVLData]] = None):
        self.root = None

        if initial is not None:
            self._build_tree(initial)

    def _build_tree(self, tree_vals: Iterable[AVLData]) -> NoReturn:
        for val in tree_vals:
            self.insert(val)

    def insert(self, val: AVLData) -> NoReturn:
        def _insert_helper(root: AVLNode, insert_value: AVLData) -> AVLNode:
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
            root.height = max(root.left_height, root.right_height) + 1
            return AVLTree._re_balance(root)
        self.root = _insert_helper(self.root, val)

    def delete(self, val: AVLData) -> NoReturn:
        """
        the complicated part of deleting from a BST involves the case where the node to be deleted has two children
        if the tree is so large that we need to do this iteratively then the logic for deleting that node becomes very
        complex. if we are able to process the deletion recursively we can simplify the case of two children to a simpler
        case of a single child by swapping the target node's value / key with that of its subtree successor.
        the subtree successor by definition will have at most one right child since it is the leftmost node of the
        target's right child (or right child itself). we then recursively call delete on the subtree with the duplicated
        value as our target
        """
        def _delete_helper(root: AVLNode, delete_value: AVLData) -> NoReturn:
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

    def search(self, val: AVLData) -> Optional[AVLNode]:
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
        only use single letter variables because they correspond with above diagrams, making it easier to visualize
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
        only use single letter variables because they correspond with above diagrams, making it easier to visualize
        """
        b = root
        d = root.right
        c = d.left
        b.right = c
        d.left = b
        b.update_height()
        d.update_height()
        return d

    def successor(self, value: AVLData) -> Optional[AVLNode]:
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
        return successor

    def predecessor(self, value: AVLData) -> Optional[AVLNode]:
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
        elif parent and node.val > parent.val:
            predecessor = parent
        return predecessor
