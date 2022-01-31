from typing import Optional

import pytest

from bts_lib.trees.binary_tree.binary_tree import BinaryTreeNode
from bts_lib.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree


class Solution:
    """
    determine tree height
    total nodes in perfect tree = 2^h - 1
    determine number of nodes on last level
    answer = (2 ^ (h - 1)) - 1 +  num nodes in last level would be (2 ^ h - 1) in perfect tree

    I can binary search the last level
    if we think of the last level as nodes labeled 1 - 2^ h - 1

    1 2 3 4 5 6 7 8

    1 2 3 4 5 6

    start by looking for 5
    if it exists partition to the right


    4 + (8 - 4) / 2 -> 6

    4

    go to middle, if present set as # of nodes

           1
       2       3
     1   2   3   4

    """

    def node_exists(self, root, height, idx):
        depth = 1
        node = root
        start = 1
        end = 2 ** (height - 1)
        while depth < height:
            mid = start + (end - start) / 2
            if mid >= idx:
                node = node.left
                end = mid - 1
            else:
                node = node.right
                start = mid + 1
            depth += 1
        return node is not None

    def countNodes(self, root: Optional[BinaryTreeNode]) -> int:
        if root is None:
            return 0

        tree_height = 1
        node = root
        while node.left:
            node = node.left
            tree_height += 1

        most = 1
        start = 0
        end = 2 ** (tree_height - 1)
        mid = (end - start) / 2
        while start <= end:
            if self.node_exists(root, tree_height, mid):
                most = max(mid, most)
                start = mid + 1
            else:
                end = mid - 1
            mid = start + (end - start) // 2
        # binary search bottom level
        return (2 ** (tree_height - 1) - 1) + int(most)


@pytest.mark.parametrize('expected', [
    pytest.param(6),
    pytest.param(8),
    pytest.param(9),
    pytest.param(5),
])
def test_count_nodes(expected):
    solver = Solution()
    tree = list([num for num in range(1, expected + 1)])
    tree_root = deserialize_leetcode_tree(tree)
    result = solver.countNodes(tree_root)
    assert result == expected
