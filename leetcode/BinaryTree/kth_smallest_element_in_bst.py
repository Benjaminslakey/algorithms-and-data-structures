# @tags: [stack, binary_tree]
# @todo add unit tests
import pytest

from collections import deque
from typing import Optional

from data_structures.trees.binary_tree import BinaryTreeNode


class Solution:
    def kthSmallest(self, root: Optional[BinaryTreeNode], k: int) -> int:
        stack = deque([])
        kth = 0
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            kth += 1
            if kth == k:
                return node.val
            node = node.right
