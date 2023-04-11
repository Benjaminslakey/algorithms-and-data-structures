from collections import defaultdict


def kahns_algorithm(graph):
    sorted_vertices = []
    vertex_in_degrees = defaultdict(int)
    for vertex in graph.vertices:
        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            vertex_in_degrees[adjacent_vertex] += 1
    for vertex, in_degree in vertex_in_degrees.items():
        if in_degree == 0:
            sorted_vertices.append(vertex)
    i = 0
    while i < len(sorted_vertices):
        vertex = sorted_vertices[i]
        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            vertex_in_degrees[adjacent_vertex] -= 1
            if vertex_in_degrees[adjacent_vertex] == 0:
                sorted_vertices.append(adjacent_vertex)
        i += 1
    return sorted_vertices


def dfs_sort(graph):

    def dfs():
        pass

    return sorted_vertices
