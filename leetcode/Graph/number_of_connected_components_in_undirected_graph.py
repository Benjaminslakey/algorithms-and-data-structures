from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    def __init__(self):
        self.visited = set()
        self.adjacency_list = defaultdict(set)

    def initalize_graph(self, edge_list):
        for vertex_one, vertex_two in edge_list:
            self.adjacency_list[vertex_one].add(vertex_two)
            self.adjacency_list[vertex_two].add(vertex_one)

    def breadth_first_search(self, start):
        """ BFS from a given vertex will explore/visit all vertices within the same connected component"""
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            self.visited.add(vertex)
            for adjacent_vertex in self.adjacency_list[vertex]:
                if adjacent_vertex not in self.visited:
                    queue.append(adjacent_vertex)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_components = 0
        self.initalize_graph(edges)
        for vertex in range(0, n):
            if len(self.visited) == n:  # we have discovered all vertices, no need to check them again
                break
            if vertex not in self.visited:  # this vertex was not in a previously explored component of the graph
                num_components += 1
                self.breadth_first_search(vertex)
        return num_components


@pytest.mark.parametrize('num_nodes, edge_list, expected_num_components', [
    pytest.param(5, [[0, 1], [1, 2], [3, 4]], 2),
    pytest.param(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
    pytest.param(10, [[0, 1], [1, 2], [2, 3], [4, 5], [6, 7]], 5)
])
def test_count_components(num_nodes, edge_list, expected_num_components):
    solver = Solution()
    num_connected_components = solver.countComponents(num_nodes, edge_list)
    assert num_connected_components == expected_num_components
