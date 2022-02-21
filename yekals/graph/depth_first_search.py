from typing import Dict

from graph.graph import Graph, Vertex


def depth_first_search(graph: Graph, parents: Dict[Vertex, Vertex], start_vertex: Vertex):
    """
    starting from a given vertex
    for each vertex adjacent to the current vertex
        if adjacent vertex doesn't have a parent yet
            mark current vertex as parent of adjacent vertex
        recursively call depth first search on adjacent vertex
    """
    time = 0

    def dfs(vertex):
        time += 1
        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            parent_of_adjacent_vertex = parents.get(adjacent_vertex)
            if parent_of_adjacent_vertex is None:
                parents[adjacent_vertex] = vertex
                depth_first_search(graph, parents, adjacent_vertex)
    return dfs(start_vertex)
