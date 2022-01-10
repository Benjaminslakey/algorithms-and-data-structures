import random
from collections import (namedtuple, deque)
from typing import List, Optional, NoReturn, Tuple, Any

BALANCED = 0
RIGHT_RIGHT = 1
LEFT_LEFT = 2
RIGHT_LEFT = 3
LEFT_RIGHT = 4


class AVLNode(object):
    def __init__(self, val: Any, left=None, right=None):
        self.val: Any = val
        self.count = 1
        self.left: AVLNode = left
        self.right: AVLNode = right
        self.height: int = 1

    def __repr__(self):
        return f"({self.val})"

    def update_height(self):
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
    def __init__(self):
        self.root = None

    @staticmethod
    def inorder(root) -> List[AVLNode]:
        if root is None:
            return []
        left = AVLTree.inorder(root.left)
        right = AVLTree.inorder(root.right)
        return left + [root.val] * root.count + right

    @staticmethod
    def print_tree(root):
        traversal = AVLTree.level_order(root)
        space = (len(traversal[-1]) * 4) // 2
        output = ""
        for lvl in traversal:
            lstr = f"{'   '.join([str(x) if x is not None else 'N' for x in lvl])}"
            output += ''.rjust(space, ' ') + lstr + "\n"
            space = space // 2
        print(output)

    @staticmethod
    def level_order(root):
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

    def insert(self, val) -> NoReturn:
        def _insert_helper(root, insert_value) -> AVLNode:
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

    def delete(self, val) -> NoReturn:
        """
        the complicated part of deleting from a BST involves the case where the node to be deleted has two children
        if the tree is so large that we need to do this iteratively then the logic for deleting that node becomes very
        complex. if we are able to process the deletion recursively we can simplify the case of two children to a simpler
        case of a single child by swapping the target node's value / key with that of its subtree successor.
        the subtree successor by definition will have at most one right child since it is the leftmost node of the
        target's right child (or right child itself). we then recursively call delete on the subtree with the duplicated
        value as our target
        """
        def _delete_helper(root, delete_value) -> NoReturn:
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

    def search(self, val) -> Optional[AVLNode]:
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
    def _right_rotation(root) -> NoReturn:
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
    def _left_rotation(root) -> NoReturn:
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


def create_avl(nums: List[int], start: int, end: int) -> AVLTree:
    avl_tree = AVLTree()
    for idx in range(start, end + 1):
        avl_tree.insert(nums[idx % len(nums)])
    return avl_tree


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False
        left = 0
        right = k
        # use self balancing BST for logN: search, insert, deletion
        # to make sorted sliding window operations quick
        window_avl = create_avl(nums, left, right)
        while left < len(nums):
            r = right % len(nums)
            if right > k and window_avl.search(nums[r]) is None:  # just to skip the first insert which would duplicate initial right
                window_avl.insert(nums[r])
            idx = left
            i = idx % len(nums)
            while i <= right:
                i = idx % len(nums)
                successor = window_avl.successor(nums[i])
                predecessor = window_avl.predecessor(nums[i])
                # successor and predecessor are nearest values
                # ie, they will minimize value being compared to T, if they don't work
                # then no other values in the tree will. though if they do work there could be other
                # nodes that also work, but we are only trying to determine if a solution exists
                # not all possible solutions
                if predecessor is not None and abs(nums[i] - predecessor.val) <= t:
                    return True
                if successor is not None and abs(nums[i] - successor.val) <= t:
                    return True
                idx += 1
            window_avl.delete(nums[left])
            left += 1
            right += 1
        return False


def test_avl():
    TestCase = namedtuple('TestCase', ['initial_vals', 'operation', 'input'])
    avl_tree_test_cases = [
        TestCase([11, 20, 29, 26, 65, 50, 23, 55], 'delete', [55, 29, 11]),
        TestCase([11, 20, 29, 26, 65, 50, 23, 55], 'insert', [105, 82, 3, 17]),
        TestCase([11, 20, 29, 26, 65, 50, 23, 55, 55, 55], 'insert', [55, 29, 11]),
        TestCase([11, 20, 29, 26, 65, 50, 23, 55, 55, 55], 'delete', [55, 29, 11]),
    ]

    for case in avl_tree_test_cases:
        avl = create_avl(case.initial_vals, 0, len(case.initial_vals) - 1)
        print(AVLTree.inorder(avl.root))
        AVLTree.print_tree(avl.root)
        for val in case.input:
            handler = getattr(avl, case.operation)
            handler(val)
            AVLTree.print_tree(avl.root)
        if case.operation == 'delete':
            expected_inorder = sorted(list(set(case.initial_vals) - set(case.input)))
        else:
            expected_inorder = sorted(case.initial_vals + case.input)
        assert AVLTree.inorder(avl.root) == expected_inorder


def test_leetcode_problem():
    TestCase = namedtuple('TestCase', ['input_array', 'k', 't', 'expected_output'])

    contains_duplicate_test_cases = [
        # TestCase([1], 1, 1, False),
        # TestCase([6, 2, 3, 5], 2, 1, True),
        TestCase([2147483646, 2147483647], 3, 3, True),
        TestCase([1, 5, 9, 1, 5, 9], 2, 3, False)
    ]
    solver = Solution()
    for case in contains_duplicate_test_cases:
        result = solver.containsNearbyAlmostDuplicate(case.input_array, case.k, case.t)
        print(f"k: {case.k}, t: {case.t}, nums: {case.input_array}\nresult: {result}\nexpected: {case.expected_output}")
        assert result == case.expected_output


if __name__ == '__main__':
    test_avl()
    # test_leetcode_problem()
