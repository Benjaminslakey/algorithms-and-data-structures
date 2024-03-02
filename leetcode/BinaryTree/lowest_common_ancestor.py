import random

import pytest

from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from yekals.trees.binary_tree.traversals import level_order_traversal, capture_flat_level_order 

"""
# Problem Statement

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.

------------------------------------------------------------------------------------------------------------------------

# Examples

## Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

## Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

## Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, *input_args):
        return self.lowestCommonAncestor(*input_args)

    def lowestCommonAncestor(self, root, p, q):
        if root is None or root is q or root is p:
            return root 

        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)
        if left_ancestor and right_ancestor:
            return root
        elif left_ancestor:
            return left_ancestor
        elif right_ancestor:
            return right_ancestor



# Tests
@pytest.mark.parametrize('input_args', [
    pytest.param([3,5,1,6,2,0,8,None,None,7,4]),
    pytest.param([3,5,1,6,2,0,8,None,None,7,4]),
])
def test_solution(input_args):
    random.seed()
    solver = Solution()
    root = deserialize_leetcode_tree(input_args)
    lo = []
    level_order_traversal(root, capture_flat_level_order(lo, get_nodes=True))
    lca = None
    for idx in range(len(lo) - 1, -1, -1):
        node = lo[idx] 
        if node is not None and node.left and node.right:
            lca = node
            break

    result = solver.solve(root, lca.left, lca.right)
    assert result is lca

