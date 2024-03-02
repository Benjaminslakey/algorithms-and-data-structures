import pytest
from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from yekals.trees.binary_tree.print_tree import print_tree


"""
# Problem Statement

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.


Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

------------------------------------------------------------------------------------------------------------------------

# Walk Through
(c): current location in tree

      -------- 3(c)  --------
     /                       \
 --  1   --              --  4   --
/           \           /           \
3          None         1           5

good node count: 1
----------------------------------------------
                  
        -------- 3  --------
      /                      \
 -- 1(c) --              --  4   --
/           \           /           \
3          None         1           5

good node count: 1
----------------------------------------------
        -------- 3  --------
      /                      \
 --  1   --              --  4   --
/           \           /           \
3(c)       None         1           5

good node count: 2
----------------------------------------------
        ------- 3(c) --------
      /                      \
  --  1  --              --  4  --
/           \           /           \
3          None         1           5

good node count: 2
----------------------------------------------
        -------  3   --------
      /                      \
  --  1  --              -- 4(c) --
/           \           /           \
3          None         1           5

good node count: 3
----------------------------------------------
        -------  3   --------
      /                      \
  --  1  --               --  4  --
/           \           /           \
3          None         1(c)         5

good node count: 3
----------------------------------------------
        -------  3   --------
      /                      \
  --  1  --               -- 4(c) --
/           \           /           \
3          None         1           5

good node count: 3
----------------------------------------------
        -------  3   --------
      /                      \
  --  1  --               --  4  --
/           \           /           \
3          None         1           5(c)

good node count: 4
---------------------------------------------- 
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.goodNodes(input_args)

    def goodNodes(self, root):
        if root is None:
            return 0

        def helper(node, path_max, good_count):
            if node is None:
                return good_count
            curr_max = max(path_max, node.val)
            ltree_count = helper(node.left, curr_max, 0)
            rtree_count = helper(node.right, curr_max, 0)
            count_from_node = 1 if node.val >= path_max else 0
            return ltree_count + rtree_count + count_from_node 
        return helper(root, root.val, 0)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([3,1,4,3,None,1,5], 4),
    pytest.param([], 0),
    pytest.param([15], 1),
    pytest.param([3, 3, None, 4, 2], 3),
    pytest.param([15, 41, 12, 4, 1, 23, 512, 51, 2, 124, 612], 7)
])
def test_solution(input_args, expected_output):
    solver = Solution()
    tree = deserialize_leetcode_tree(input_args)
    # print_tree(tree)
    result = solver.solve(tree)
    assert result == expected_output

