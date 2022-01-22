from collections import defaultdict, deque
from typing import List

import pytest


class NonBipartiteException(Exception):
    ...


class Solution:
    UNCOLORED = 0
    RED = 1
    BLACK = 2

    def __init__(self):
        self.visited = set()
        self.vertices = {}
        self.graph = None

    def opposite_color(self, vertex):
        color = self.vertices[vertex]
        return self.BLACK if color == self.RED else self.RED

    def initialize_graph(self, graph):
        self.graph = graph
        # mark all vertices as uncolored
        for vertex in range(0, len(graph)):
            self.vertices[vertex] = self.UNCOLORED

    def proccess_edge(self, vertex_one, vertex_two):
        opposite_color = self.opposite_color(vertex_one)
        if self.vertices[vertex_two] == self.UNCOLORED:
            self.vertices[vertex_two] = opposite_color
        if self.vertices[vertex_two] != opposite_color:
            raise NonBipartiteException()

    def breadth_first_search(self, start):
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            self.visited.add(vertex)
            for adjacent_vertex in self.graph[vertex]:
                self.proccess_edge(vertex, adjacent_vertex)
                if adjacent_vertex not in self.visited:
                    queue.append(adjacent_vertex)

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.initialize_graph(graph)
        for vertex in list(self.vertices.keys()):
            vertex_color = self.vertices[vertex]
            if vertex_color == self.UNCOLORED:
                # it will only be uncolored if this vertex is in an undiscovered connected component
                # if so, none of that component should be colored, we could start this with red or black if we wanted
                self.vertices[vertex] = self.RED
                try:
                    self.breadth_first_search(vertex)
                except NonBipartiteException:
                    return False
        return True


@pytest.mark.parametrize('graph, expected_is_bipartite', [
    pytest.param([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
    pytest.param([[1, 3], [0, 2], [1, 3], [0, 2]], True),
])
def test_graph_is_bipartite(graph, expected_is_bipartite):
    solver = Solution()
    is_bipartite = solver.isBipartite(graph)
    assert is_bipartite == expected_is_bipartite
