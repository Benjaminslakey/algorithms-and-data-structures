import pytest
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree

"""
Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is a path where the values increase by one along the path.

Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.



Example 1:


Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:


Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-3 * 104 <= Node.val <= 3 * 104
"""

"""
the potential answers seem more easily enumerated using depth first search traversals
a path can start at any node in the tree so we want to be able to discard previous sequences as we're exploring paths
and we really only need to keep track of the longest seq length, curr seq length, and prev elem value

do dfs
    if curr seq length > max seq length
        set max seq length = curr seq length
        
    if curr val is in seq
        incr curr seq length
    else
        reset curr seq length to 0
    prev val = curr val 

"""


class Solution:
    def __init__(self):
        self.max_seq_len = 0

    def longestConsecutive(self, root):
        self.traversal(root, self.record_seq, 0, None)
        return self.max_seq_len

    def record_seq(self, node, curr_seq_len, prev_val):
        seq_len = 1
        if prev_val is not None and node.val == prev_val + 1:
            seq_len = curr_seq_len + 1
        if seq_len > self.max_seq_len:
            self.max_seq_len = seq_len
        return seq_len

    def traversal(self, node, f, curr_seq_len, prev_val):
        """pre order traversal"""
        if node is None:
            return
        seq_len = f(node, curr_seq_len, prev_val)
        self.traversal(node.left, f, seq_len, node.val)
        self.traversal(node.right, f, seq_len, node.val)


@pytest.mark.parametrize('tree_arr, expected', [
    pytest.param([1], 1),
    pytest.param([1, None, 3, 2, 4, None, None, None, 5], 3),
    pytest.param([2, None, 3, 2, None, 1], 2)
])
def test_solution(tree_arr, expected):
    solver = Solution()
    tree_root = deserialize_leetcode_tree(tree_arr)
    result = solver.longestConsecutive(tree_root)
    assert result == expected
