# depth first search, if we've visited all nodes, no path can be found

from collections import deque, defaultdict
from typing import List


def parse_graph(edge_list):
    adjacency_lookup = defaultdict(list)
    for src_node, dest_node in edge_list:
        adjacency_lookup[src_node].append(dest_node)
        adjacency_lookup[dest_node].append(src_node)
    return adjacency_lookup


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited_locations = set()
        neighbors_for_nodes = parse_graph(edges)
        explore_from = deque([start])
        while explore_from and len(visited_locations) < n:
            current_location = explore_from.pop()
            if current_location in visited_locations:  # don't duplicate exploration work
                continue
            node_neighbors = neighbors_for_nodes[current_location]
            for neighbor in node_neighbors:
                if neighbor not in visited_locations:  # don't duplicate exploration work
                    explore_from.appendleft(neighbor)
            visited_locations.add(current_location)
            if current_location == end:
                return True
        return False
