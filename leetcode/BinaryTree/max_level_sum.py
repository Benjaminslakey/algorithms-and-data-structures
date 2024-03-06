import pytest
from collections import deque

from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree

"""
# Problem Statement

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the tree is in the range [1, 104].
-10^5 <= Node.val <= 10^5

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

### Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.maxLevelSum(input_args)

    def maxLevelSum(self, root):
        current_lvl = 1
        lvl_w_max = 1
        level_sum = 0
        max_sum = float('-inf')
        q = deque([root, None])
        while q:
            node = q.popleft()
            if node is None:
                if level_sum > max_sum:
                    max_sum = level_sum
                    lvl_w_max = current_lvl
                if len(q) > 0:
                    q.append(None)
                current_lvl += 1
                level_sum = 0
                continue

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            level_sum += node.val
        return lvl_w_max


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([989,None,10250,98693,-89388,None,None,None,-32127], 2),
    pytest.param([1,7,0,7,-8,None,None], 2),
    pytest.param([1], 1),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree = deserialize_leetcode_tree(input_args)
    result = solver.solve(tree)
    assert result == expected_output

