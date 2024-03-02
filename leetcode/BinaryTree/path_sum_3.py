import pytest
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from yekals.trees.binary_tree.print_tree import print_tree 


"""
# Problem Statement

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

### Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 
------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, *input_args):
        return self.pathSum(*input_args)

    def pathSum(self, root, targetSum):
        def helper(node, )

    def doesntwork(self, root, targetSum):
        print_tree(root)
        if root is None:
            return 0

        def helper(node, prev_sum):
            if node is None:
                return 0
            count_at_node = 1 if prev_sum + node.val == targetSum else 0
            print(f"prev_sum: {prev_sum}, node.val: {node.val}")
            print_tree(node)
            l1_count = helper(node.left, node.val)
            l2_count = helper(node.left, prev_sum + node.val)
            r1_count = helper(node.right, node.val)
            r2_count = helper(node.right, prev_sum + node.val)
            return max(l1_count, l2_count) + max(r1_count, r2_count) + count_at_node
        return helper(root, 0)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    # pytest.param([[10,5,-3,3,2,None,11,3,-2,None,1], 8], 3),
    pytest.param([[5,4,8,11,None,13,4,7,2,None,None,5,1], 22], 3),
    pytest.param([[], 0], 0),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree = deserialize_leetcode_tree(input_args.pop(0))
    result = solver.solve(tree, *input_args)
    assert result == expected_output


