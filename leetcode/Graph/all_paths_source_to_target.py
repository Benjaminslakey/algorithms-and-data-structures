from collections import deque
from typing import List

import pytest


class Solution:
    def __init__(self):
        self.paths_to_target = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.dfs(0, len(graph) - 1, graph, [0])
        return self.paths_to_target

    def dfs(self, node, target_node, adj_list, path):
        """
        base cases:
            node == target_node:
                append path to output
                return
        """
        if node == target_node:
            self.paths_to_target.append(path)
            return
        for child in adj_list[node]:
            self.dfs(child, target_node, adj_list, path + [child])

    def bfs(self, graph):
        """ input is adjacency matrix, graph is dag
        breadth first search but we don't need to record visited since we are trying to enumerate all paths
        a given node can, and will (if the end node's in degree is 1), be in multiple pathsxcdx
        since this is a dag, the end node will have an out degree of 0, ie, no neighbors to explore and will naturally
        end the breadth first search when each path that can be taken from the root reaches the end
        """
        dest = len(graph) - 1
        to_explore = deque([(0, [0])])
        paths = []
        while to_explore:
            current_location, path_to_location = to_explore.pop()
            neighbors = graph[current_location]
            for neighbor in neighbors:
                path_to_neighbor = path_to_location + [neighbor]
                to_explore.appendleft((neighbor, path_to_neighbor))
                if neighbor == dest:
                    paths.append(path_to_neighbor)
        return paths


@pytest.mark.parametrize('graph, expected_paths', [
    pytest.param([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
    pytest.param([[4, 3, 1], [3, 2, 4], [3], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])
])
def test_all_paths(graph, expected_paths):
    solver = Solution()
    result = solver.allPathsSourceTarget(graph)
    assert result == expected_paths
