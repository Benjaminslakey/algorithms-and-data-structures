from collections import deque
from typing import NoReturn, Iterable, Any

from data_structures.trees.binary_tree import BinaryTreeNode


def _level_order(root: BinaryTreeNode) -> Iterable[Iterable[Any]]:
    """ include nulls in level order and add fake children for null nodes to make printing easier for now """
    q = deque([root])
    traversal = []
    while q:
        level = []
        next_lvl = deque()
        while q:
            node = q.pop()
            if node:
                next_lvl.appendleft(node.left)
                next_lvl.appendleft(node.right)
                level.append(node.val)
            else:
                for i in range(0, 2):
                    next_lvl.appendleft(None)
                level.append(None)
        q = next_lvl
        traversal.append(level)
        if all(map(lambda x: x is None, next_lvl)):
            break
    return traversal


def print_tree(root: BinaryTreeNode) -> NoReturn:
    """
    inorder: [11, 20, 23, 26, 29, 50, 65]
    outputs ->
                      ----------------- 29  -----------------
                     /                                       \
            ------- 20  -------                     ------- 55  -------
           /                   \                   /                   \
       -- 11  --           -- 26  --           -- 50  --           -- 65  --
      /         \         /         \         /         \         /         \
    None      None       23       None      None      None      None      None
    """

    def format_node(data):
        node_len = len(str(data))
        # start with 0.01 base so that .5 will round up to 1 instead of to 0
        return f"{' ' * ((max_node_size - node_len) // 2)}{data}{' ' * round(0.01 + (max_node_size - node_len) / 2)}"

    def get_max_node_size(lvl_order):
        max_node = ''
        for lvl in lvl_order:
            lvl_max = max(lvl, key=lambda x: len(str(x)))
            max_node = max(max_node, lvl_max, key=lambda x: len(str(x)))
        return len(max_node)

    traversal = _level_order(root)
    tree_height = len(traversal)
    max_node_size = get_max_node_size(traversal) + 2
    output = ""
    for level_depth, level_nodes in enumerate(traversal):
        level_height = tree_height - level_depth
        level_indent = max_node_size * (2 ** (level_height - 1)) - 1  # size of left subtree
        gap_between_nodes = max_node_size * ((2 ** level_height) - 1)  # size of parent left subtree
        node_strings = [format_node(node) for node in level_nodes]
        if level_height > 1:  # should have children
            link_length = (level_indent // 2) - 3
            between_nodes = f"{'-' * link_length}{' ' * (gap_between_nodes - link_length * 2)}{'-' * link_length}"
        else:
            link_length = 0
            between_nodes = ' ' * gap_between_nodes
        level_repr = between_nodes.join(node_strings)
        outter_link = f"{' ' * (level_indent - link_length)}{'-' * link_length}"
        parent_links = ""
        for idx, _ in enumerate(level_nodes):
            link_type = "/" if idx % 2 == 0 else "\\"
            parent_links += f"{format_node(link_type)}{' ' * gap_between_nodes}"
        if level_depth > 0:
            output += f"{' ' * level_indent}{parent_links}\n"
        output += f"{outter_link}{level_repr}{outter_link[::-1]}\n"
    print(f"\n{output}")
