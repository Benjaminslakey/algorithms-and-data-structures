

def deserialize_leetcode_tree():
    pass

# Definition for a binary tree node.

from collections import deque
import json

from data_structures.trees.binary_tree import BinaryTreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None or root.val is None:
            return json.dumps([])

        tree_arr = [root.val]
        q = deque()
        q.appendleft(root)
        while len(q):
            n = q.pop()
            if n is None:
                continue

            for child in [n.left, n.right]:
                tree_arr.append("null" if child is None else child.val)
                if child:
                    q.appendleft(child)
        return json.dumps(tree_arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        tree_arr = json.loads(data)

        def get_node():
            if tree_arr:
                val = tree_arr.pop(0)
                return BinaryTreeNode(val)
            return None

        root = get_node()
        parents = [root]
        while tree_arr:
            children = []
            for parent in parents:
                parent.left = get_node()
                parent.right = get_node()
                children.extend([parent.left, parent.right])
            parents = children
        return root
