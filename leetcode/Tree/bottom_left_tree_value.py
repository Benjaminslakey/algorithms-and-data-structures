from collections import deque
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
import pytest

"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

class Solution:
    def findBottomLeftValue(self, root):
        # do a breadth first search / level order traversal
        # take first non null array element from last level
        levels = []
        current_level = []
        queue = deque([root, None])
        while queue:
            node = queue.popleft()
            if node is None: # use none as end of level marker
                levels.append(current_level)
                current_level = []
                if queue: # don't append a level marker if there isn't anything left in the queue or we'll end up in an infinite loop
                    queue.append(None) # if we've processed everything in this level, mark the end of the level with a null value
                continue

            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return levels[-1][0]


@pytest.mark.parametrize('tree, expected', [
    pytest.param([2, 1, 3], 1),
    pytest.param([1,2,3,4,None,5,6,None,None,7], 7),
])
def test_solution(tree, expected):
    solver = Solution()
    root = deserialize_leetcode_tree(tree)
    blv = solver.findBottomLeftValue(root)
    assert blv == expected

