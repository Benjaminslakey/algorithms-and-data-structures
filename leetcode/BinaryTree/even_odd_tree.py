import pytest
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from yekals.trees.binary_tree.print_tree import print_tree
from collections import deque

"""
Problem Statement

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


------------------------------------------------------------------------------------------------------------------------
Constraints

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 10^6

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.


Example 2:

Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.


Example 3:

Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.
------------------------------------------------------------------------------------------------------------------------
"""

def level_order_traversal(root):
    levels = []
    current_level = []
    queue = deque([root, None])
    while queue:
        node = queue.popleft()
        if node is None:
            levels.append(current_level) 
            if not queue:
                break
            current_level = []
            queue.append(None)
            continue

        current_level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return levels

# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.isEvenOddTree(input_args)

    def isEvenOddTree(self, root):
        # construct level order traversal
        levels = level_order_traversal(root)
        print(f"lo: {levels}")
        # evaluate even odd trees
        for idx, lvl in enumerate(levels):
            if idx % 2 == 0: # even levels
                prev = 0
                for num in lvl:
                    if num > prev and num % 2 == 1:
                        prev = num
                    else:
                        return False
            else: # odd levels
                prev = 10 ** 7
                for num in lvl:
                    if num < prev and num % 2 == 0:
                        prev = num
                    else:
                        return False
        return True

# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([1,10,4,3,None,7,9,12,8,6,None,None,2],), True),
    pytest.param(([5,4,2,3,3,7],), False),
    pytest.param(([5,9,1,3,5,7],), False),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree_root = deserialize_leetcode_tree(*input_args)
    # print_tree(tree_root)
    result = solver.solve(tree_root)
    assert result == expected_output

