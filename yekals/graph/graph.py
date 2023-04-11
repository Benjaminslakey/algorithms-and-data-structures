from collections import defaultdict
from typing import Protocol, Any, List, Iterable


class Vertex(Protocol):
    val: Any


class Edge(Protocol):
    vertex_one: Vertex
    vertex_two: Vertex
    weight: int
    directed: bool


class Graph(Protocol):
    adjacency_matrix: dict
    vertices: Iterable[Vertex]
    edges: Iterable[Edge]
    weighted: bool
    directed: bool

    def get_adjacent_vertices(self, vertex: Vertex) -> Iterable[Vertex]:
        ...

    def get_edge(self, vertex_one: Vertex, vertex_two: Vertex) -> Edge:
        ...


class DagVertex(Vertex):
    def __init__(self, value):
        self.val = value


class DagEdge(Edge):
    directed = True

    def __init__(self, vertex_one, vertex_two, weight=1):
        self.vertex_one = vertex_one
        self.vertex_two = vertex_two
        self.weight = weight


class DAG(Graph):
    directed = True

    def __init__(self, vertices, edges):
        self.adjacency_matrix = self.create_adjacency_matrix(vertices, edges)
        self.vertices = vertices
        self.edges = edges

    @staticmethod
    def create_adjacency_matrix(vertices, edges):
        adjacency_matrix = defaultdict(list)
        for edge in edges:
            adjacency_matrix[edge.vertex_one].append(edge)
        return adjacency_matrix

    def get_adjacent_vertices(self, vertex: Vertex) -> List[Vertex]:
        adjacent_vertices = []
        for outgoing_edge in self.adjacency_matrix.get(vertex, []):
            adjacent_vertices.append(outgoing_edge.vertex_two)
        return adjacent_vertices

    def get_edge(self, vertex_one, vertex_two):
        pass  # @todo figure out best way to quickly get edge based on it's two vertices


