import pytest
from collections import deque

from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree

"""
# Problem Statement

Given the root of a binary tree, imagine yourself standing on the right side of it.
return the values of the nodes you can see ordered from top to bottom.

------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

### Example 2:
Input: root = [1,null,3]
Output: [1,3]

### Example 3:
Input: root = []
Output: []

------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.rightSideView(input_args)

    def rightSideView(self, root):
        if root is None:
            return []

        result = []
        q = deque([root, None])
        prev = None
        while q:
            node = q.popleft()
            if node is None: # marker for end of the level
                result.append(prev.val)
                if len(q) > 0: # there are still nodes left to process, we aren't on the last level
                    # everything currently in the queue are children of the level we just processed
                    # since we're done with this level, all nodes from the next level are already in the queue
                    # mark the end of that level with a null
                    q.append(None)  
                continue
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            prev = node
        return result


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([1,2,3,None,5,None,4], [1, 3, 4]),
    pytest.param([1,None,3], [1, 3]),
    pytest.param([], [])
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree = deserialize_leetcode_tree(input_args)
    result = solver.solve(tree)
    assert result == expected_output


