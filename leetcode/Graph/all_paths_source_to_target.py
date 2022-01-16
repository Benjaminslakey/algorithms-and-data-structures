from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """ input is adjacency matrix, graph is dag
        breadth first search but we don't need to record visited since we are trying to enumerate all paths
        a given node can, and will (if the end node's in degree is 1), be in multiple paths
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

# @todo add unit tests
