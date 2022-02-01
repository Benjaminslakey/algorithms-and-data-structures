from collections import deque
from typing import Optional

from bts_lib.graph.graph import Graph


def bread_first_search(
        graph: Graph,
        process_vertex: Optional[callable],
        process_edge: Optional[callable]
):
    visited = set()
    queue = deque([])
    while queue:
        current_vertex = queue.popleft()
        if process_vertex:
            process_vertex(current_vertex)
        for adjacent_vertex in graph.get_adjacent_vertices(current_vertex):
            if process_edge:
                edge = graph.get_edge(current_vertex, adjacent_vertex)
                process_edge(edge)
            if adjacent_vertex not in visited:
                queue.append(adjacent_vertex)
        visited.add(current_vertex)
