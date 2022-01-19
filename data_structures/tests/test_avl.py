import pytest

from algorithms.trees.binary_tree.traversals import inorder_traversal
from algorithms.trees.binary_tree.validate import is_balanced
from data_structures.trees.avl_tree import AVLTree


@pytest.mark.parametrize('initial_tree, to_delete, expected_inorder', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, [11, 20, 23, 26, 29, 50, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 29, [11, 20, 23, 26, 50, 55, 65]),
    pytest.param([11, 20, 26, 65, 50, 23], 11, [20, 23, 26, 50, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 11, [20, 23, 26, 29, 50, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 55, 55], 55, [11, 20, 23, 26, 29, 50, 55, 55, 65]),
])
def test_avl_delete(initial_tree, to_delete, expected_inorder):
    avl = AVLTree(initial_tree)
    avl.delete(to_delete)
    assert inorder_traversal(avl.root) == expected_inorder
    balanced = is_balanced(avl.root)
    assert balanced


@pytest.mark.parametrize('initial_tree, to_insert, expected_inorder', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 105, [11, 20, 23, 26, 29, 50, 55, 65, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 82, [11, 20, 23, 26, 29, 50, 55, 65, 82]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 105], 82, [11, 20, 23, 26, 29, 50, 55, 65, 82, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 3, [3, 11, 20, 23, 26, 29, 50, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 105, 82], 3, [3, 11, 20, 23, 26, 29, 50, 55, 65, 82, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 17, [11, 17, 20, 23, 26, 29, 50, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 105, 82, 3], 17, [3, 11, 17, 20, 23, 26, 29, 50, 55, 65, 82, 105]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, [11, 20, 23, 26, 29, 50, 55, 55, 65]),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55, 55], 55, [11, 20, 23, 26, 29, 50, 55, 55, 55, 65]),
])
def test_avl_insert(initial_tree, to_insert, expected_inorder):
    avl = AVLTree(initial_tree)
    avl.insert(to_insert)
    assert inorder_traversal(avl.root) == expected_inorder
    balanced = is_balanced(avl.root)
    assert balanced


@pytest.mark.parametrize('initial_tree, val, expected_successor', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 11, 20),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, 65),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 11, 20),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, 65),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 65, None),
    pytest.param([11, 20, 29, 26, 50, 23], 50, None),
    pytest.param([11], 11, None),
])
def test_avl_successor(initial_tree, val, expected_successor):
    avl = AVLTree(initial_tree)
    successor = avl.successor(val)
    assert successor is None and successor == expected_successor or successor.val == expected_successor


@pytest.mark.parametrize('initial_tree, val, expected_predecessor', [
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 11, None),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 55, 50),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 20, 11),
    pytest.param([11, 20, 29, 26, 65, 50, 23, 55], 65, 55),
    pytest.param([20, 29, 26, 65, 50, 23, 55], 20, None),
    pytest.param([11], 11, None),
])
def test_avl_predecessor(initial_tree, val, expected_predecessor):
    avl = AVLTree(initial_tree)
    predecessor = avl.predecessor(val)
    assert predecessor is None and predecessor == expected_predecessor or predecessor.val == expected_predecessor


def test_avl_node_counter():
    delete_val = 999999
    avl = AVLTree([1, delete_val])
    avl.delete(delete_val)
    assert avl.search(delete_val) is None
    avl.insert(38192)
    avl.delete(1)
    avl.insert(delete_val)
    assert avl.search(delete_val).count == 1