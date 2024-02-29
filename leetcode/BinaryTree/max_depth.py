import pytest
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree

"""

Problem Statement

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

------------------------------------------------------------------------------------------------------------------------
Constraints

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.maxDepth(input_args)

    def maxDepth(self, root):
        def _helper(node, depth):
            if node is None:
                return depth - 1

            l_depth = _helper(node.left, depth + 1)
            r_depth = _helper(node.right, depth + 1)
            return max(l_depth, r_depth)
        return _helper(root, 1)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([3,9,20,None,None,15,7],), 3),
    pytest.param(([1,None,2],), 2),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree = deserialize_leetcode_tree(*input_args)
    result = solver.solve(tree)
    assert result == expected_output

