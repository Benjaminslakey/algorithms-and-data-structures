import pytest

from bts_lib.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from bts_lib.trees.binary_tree.traversals import level_order_traversal


@pytest.mark.parametrize('input_tree, expected_level_order', [
    pytest.param([], []),
    pytest.param([1], [[1]]),
    pytest.param([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
])
def test_deserialize_tree(input_tree, expected_level_order):
    root = deserialize_leetcode_tree(input_tree)
    level_order = level_order_traversal(root)
    assert level_order == expected_level_order
