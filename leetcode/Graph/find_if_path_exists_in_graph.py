from collections import deque, defaultdict
from typing import List

import pytest


def parse_graph(edge_list):
    adjacency_lookup = defaultdict(list)
    for src_node, dest_node in edge_list:
        adjacency_lookup[src_node].append(dest_node)
        adjacency_lookup[dest_node].append(src_node)
    return adjacency_lookup


class Solution:
    def __init__(self):
        self.discovered = set()

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = parse_graph(edges)
        # return self.bfs(n, adj_list, start, end)
        return self.dfs(start, end, adj_list)

    def dfs(self, node, target_node, adj_list):
        """
        base cases:
            - node == end
                return True
            - all node children in discovered
                return False
        from a node
            for each child recursively call dfs on the child
            if any of the calls to dfs on a child return true, return true otherwise keep going
        return false
        """
        if node == target_node:
            return True
        for child in adj_list[node]:
            if child not in self.discovered:
                self.discovered.add(child)
                if self.dfs(child, target_node, adj_list):
                    return True
        return False

    def bfs(self, n: int, adj_list: dict, start: int, end: int) -> bool:
        """ breadth first search, if we've visited all nodes, no path can be found """
        visited_locations = set()
        explore_from = deque([start])
        while explore_from and len(visited_locations) < n:
            current_location = explore_from.pop()
            if current_location in visited_locations:  # don't duplicate exploration work
                continue
            node_neighbors = adj_list[current_location]
            for neighbor in node_neighbors:
                if neighbor not in visited_locations:  # don't duplicate exploration work
                    explore_from.appendleft(neighbor)
            visited_locations.add(current_location)
            if current_location == end:
                return True
        return False


@pytest.mark.parametrize('n, edge_list, start, end, path_exists', [
    pytest.param(3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
    pytest.param(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False)
])
def test_find_path_if_exists(n, edge_list, start, end, path_exists):
    solver = Solution()
    result = solver.validPath(n, edge_list, start, end)
    assert result == path_exists
