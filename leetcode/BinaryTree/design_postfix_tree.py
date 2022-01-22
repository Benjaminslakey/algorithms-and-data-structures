from abc import ABC, abstractmethod
from typing import List

import pytest

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        ...


class PostFixNode(Node):
    operators = {
        '+': lambda left, right: int(left) + int(right),
        '-': lambda left, right: int(left) - int(right),
        '*': lambda left, right: int(left) * int(right),
        '/': lambda left, right: int(int(left) / int(right)),
    }

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

    def evaluate(self):
        return self.evaluate_tree(self)

    @staticmethod
    def evaluate_tree(root):
        """
        1. all nodes should have either 0 or 2 children, being a leaf or tree root
        2. only operators have 2 children -> tree root
        3. numeric values have 0 children -> leaf
        """
        if root.val in PostFixNode.operators:
            left_val = PostFixNode.evaluate_tree(root.left)
            right_val = PostFixNode.evaluate_tree(root.right)
            return PostFixNode.operators[root.val](left_val, right_val)
        else:
            return root.val


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    @staticmethod
    def build_tree(postfix, idx):
        index = idx
        node = PostFixNode(postfix[index])
        index -= 1
        if postfix[idx] in PostFixNode.operators:
            node.right, index = TreeBuilder.build_tree(postfix, index)
            node.left, index = TreeBuilder.build_tree(postfix, index)
        return node, index

    def buildTree(self, postfix: List[str]) -> 'Node':
        root, _ = self.build_tree(postfix, len(postfix) - 1)
        return root


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""


@pytest.mark.parametrize('postfix_expression, expected_result', [
    pytest.param(["3", "4", "+", "2", "*", "4", "7", "*", "+"], 42),
    pytest.param(["3", "4", "+", "2", "*", "7", "/"], 2),
    pytest.param(["4", "5", "2", "7", "+", "-", "*"], -16),
    pytest.param(["3", "4", "+", "2", "*", "7", "/"], 2),
])
def test_postfix_tree(postfix_expression, expected_result):
    builder = TreeBuilder()
    tree_root = builder.buildTree(postfix_expression)
    result = tree_root.evaluate()
    assert result == expected_result
