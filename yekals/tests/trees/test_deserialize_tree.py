import pytest

from yekals.trees.binary_tree.deserialize_tree import deserialize_leetcode_tree
from yekals.trees.binary_tree.traversals import level_order_traversal, capture_level_order, capture_flat_level_order


@pytest.mark.parametrize('input_tree, expected_level_order', [
    pytest.param([], []),
    pytest.param([1], [[1]]),
    pytest.param([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    pytest.param([1, None, 3, 2, 4, None, None, None, 5], [[1], [3], [2, 4], [5]]),
    pytest.param([2, None, 3, 2, None, 1], [[2], [3], [2], [1]])
])
def test_deserialize_tree(input_tree, expected_level_order):
    root = deserialize_leetcode_tree(input_tree)
    level_order = []
    level_order_traversal(root, capture_level_order(level_order))
    assert level_order == expected_level_order


@pytest.mark.parametrize('tree_arr', [
    pytest.param([1]),
    pytest.param([1, None, 3, 2, 4, None, None, None, 5]),
    pytest.param([2, None, 3, 2, None, 1, None]),
])
def test_deserialize_leetcode_tree(tree_arr):
    tree_root = deserialize_leetcode_tree(tree_arr)
    lo_result = []
    level_order_traversal(tree_root, capture_flat_level_order(lo_result))
    assert lo_result == tree_arr
