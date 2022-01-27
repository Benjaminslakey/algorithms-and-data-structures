from typing import List

import pytest

from bts_lib.disjoint_set import DisjointSet


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        disjoint_set = DisjointSet()
        for v in range(0, n):
            disjoint_set.add(v)
        for vertex_one, vertex_two in edges:
            disjoint_set.union(vertex_one, vertex_two)
        # determine if graph has disjoint vertices, trees must be connected graphs
        for v in range(0, n):
            disjoint_set.find(v)
        # use graph theory rule, trees must have exactly n - 1 edges, where n is the number of vertices
        return len(set(list(disjoint_set.parents.values()))) == 1 and len(edges) == n - 1


@pytest.mark.parametrize('num_vertices, graph, is_valid_tree', [
    pytest.param(5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
    pytest.param(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    pytest.param(4, [[0, 1], [2, 3], [1, 2]], True)
])
def test_is_valid_tree(num_vertices, graph, is_valid_tree):
    solver = Solution()
    result = solver.validTree(num_vertices, graph)
    assert result == is_valid_tree
