from collections import deque, defaultdict

import pytest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    """ this algorithm is for a connected & undirected graph, with unique values"""

    def __init__(self):
        # this is our new graph
        self.adjacency_list = defaultdict(set)

    def depth_first_search(self, root):
        discovered = {root.val}
        processed = set()
        stack = deque([])
        vertex = root
        while stack or vertex:
            prev = vertex
            for idx, neighbor in enumerate(vertex.neighbors):
                if neighbor.val not in discovered:
                    discovered.add(neighbor.val)
                    stack.append(vertex)
                    vertex = neighbor
                    break
            # we have visited all neighbors and are done exploring this vertex
            if prev == vertex:
                self.process_vertex(vertex)
                processed.add(vertex.val)
                # go to "parent" in tree of discovery
            if vertex.val in processed:
                if stack:
                    vertex = stack.pop()
                else:
                    break

    def process_vertex(self, vertex):
        for neighbor in vertex.neighbors:
            self.adjacency_list[vertex.val].add(neighbor.val)

    @staticmethod
    def create_graph(adjacency_list, root_val):
        node_map = {}
        if not adjacency_list:  # null graph
            return None

        for key in adjacency_list.keys():
            node_map[key] = Node(key)
        for key, neighbors in list(adjacency_list.items()):
            node = node_map[key]
            for adjacent_vertex in neighbors:
                neighbor = node_map[adjacent_vertex]
                node.neighbors.append(neighbor)
        return node_map[root_val]

    def recreate_graph(self, root_val):
        return self.create_graph(self.adjacency_list, root_val)

    def cloneGraph(self, node):
        if node is None:
            return None
        elif not node.neighbors:
            return Node(node.val)

        self.depth_first_search(node)
        return self.recreate_graph(node.val)


# need some util functions for converting leetcode input & output to usable input & output
def util__adj_list_to_adj_dict(adj_list):
    adj_dict = defaultdict(set)
    for vertex, neighbors in enumerate(adj_list):
        adj_dict[vertex + 1] = set()
        for adj_vertex in neighbors:
            adj_dict[vertex + 1].add(adj_vertex)
    return adj_dict


def util__graph_root_to_adj_list(graph_root):
    if graph_root is None:
        return []

    visited = set()
    queue = deque([graph_root])
    adj_dict = defaultdict(set)
    while queue:
        vertex = queue.popleft()
        for neighbor in vertex.neighbors:
            # process edge
            adj_dict[vertex.val].add(neighbor.val)
            if neighbor.val not in visited:
                queue.append(neighbor)
        visited.add(vertex.val)
    # convert dict to list
    adj_list = []
    for idx in range(0, len(visited)):
        neighbors = sorted(list(adj_dict[idx + 1]))
        adj_list.append(neighbors)
    return adj_list


@pytest.mark.parametrize('adj_list', [
    pytest.param([[2, 4], [1, 3], [2, 4], [1, 3]]),
    pytest.param([[]]),
    pytest.param([]),
])
def test_clone_graph(adj_list):
    solver = Solution()
    in_ = util__adj_list_to_adj_dict(adj_list)
    original_graph_root = solver.create_graph(in_, 1)
    new_root = solver.cloneGraph(original_graph_root)
    new_adj_list = util__graph_root_to_adj_list(new_root)
    assert new_adj_list == adj_list











