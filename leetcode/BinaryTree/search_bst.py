import pytest
from yekals.trees.binary_tree import PREORDER
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from yekals.trees.binary_tree.traversals import depth_first_traversal

"""
Problem Statement

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

------------------------------------------------------------------------------------------------------------------------
Constraints

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.searchBST(*input_args)

    def searchBST(self, node, target):
        if node is None:
            return None
        
        if node.val == target:
            return node
        if node.val > target:
            return self.searchBST(node.left, target)
        else:
            return self.searchBST(node.right, target)



# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([4,2,7,1,3], 2), [2, 1, 3]),
    pytest.param(([4,2,7,1,3], 5), []),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree_root = deserialize_leetcode_tree(input_args[0])

    preorder = []

    def add_to_preorder(node):
        if node is not None:
            preorder.append(node.val)

    result = solver.solve((tree_root, input_args[1]))
    if result is not None:
        depth_first_traversal(result, add_to_preorder, process_order=PREORDER)

    assert preorder == expected_output 

