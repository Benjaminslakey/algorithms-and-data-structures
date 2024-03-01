import pytest

"""
# Problem Statement

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.leafSimilar(*input_args)

    def leafSimilar(self, root1, root2):
        gen1, gen2 = self.get_leaf(root1), self.get_leaf(root2)
        leafs1 = [l for l in gen1]
        leafs2 = [l for l in gen2]
        return leafs1 == leafs2

    def get_leaf(self, node):
        if node.left is None and node.right is None:
            yield node.val

        if node.left:
            yield from self.get_leaf(node.left)
        if node.right:
            yield from self.get_leaf(node.right)

# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]), True),
    pytest.param(([1,2,3], [1,3,2]), False),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


