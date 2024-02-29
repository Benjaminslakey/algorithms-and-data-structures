import pytest
from yekals.trees.binary_tree.traversals import capture_flat_level_order, level_order_traversal

"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""

Solution:
    def buildTree(self, inorder, postorder):
        return


@pytest.mark.parametrize('inorder, postorder, expected', [
    pytest.param([9,3,15,20,7], [9,15,7,20,3], [3,9,20,None, None, 15,7]),
    pytest.param([-1], [-1], [-1])
])
def test_build_tree():
    solver = Solution()
    result = solver.buildTree(inorder, postorder)
    lo = []
    p_order = level_order_traversal(result, capture_flat_level_order(lo)) 
    assert p_order == postorder

