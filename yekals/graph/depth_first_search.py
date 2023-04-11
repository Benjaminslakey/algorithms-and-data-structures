from typing import Dict, Callable

from graph.graph import Graph, Vertex


DISCOVERED = 1
PROCESSED = 2


def depth_first_search(
        graph: Graph,
        start_vertex: Vertex,
        process_vertex_early: Callable,
        process_vertex_late: Callable,
        process_edge: Callable
):
    time = 0
    parents = {}
    vertex_states = {}
    vertex_enters = {}
    vertex_exits = {}

    def dfs(vertex):
        nonlocal time
        time += 1
        vertex_enters[vertex] = time

        if process_vertex_early:
            process_vertex_early(vertex)

        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            if adjacent_vertex not in vertex_states:  # vertex not yet discovered
                parents[adjacent_vertex] = vertex
                depth_first_search(graph, adjacent_vertex, process_vertex_early, process_vertex_late, process_edge)
            elif graph.directed or (vertex_states[adjacent_vertex] != PROCESSED and parents[vertex] != adjacent_vertex):
                edge = graph.get_edge(vertex, adjacent_vertex)
                process_edge(edge)

        if process_vertex_late:
            process_vertex_late(vertex)
        vertex_states[vertex] = PROCESSED
        time += 1
        vertex_exits[vertex] = time

    return dfs(start_vertex)
