from typing import Protocol, Any, List, Set


class Vertex(Protocol):
    val: Any

    def __hash__(self):
        ...


class Edge(Protocol):
    from_vertex: Vertex
    to_vertex: Vertex
    weight: int
    directed: bool

    def __hash__(self):
        ...


class Graph(Protocol):
    adjacency_matrix: dict
    vertices: Set[Vertex]
    edges: Set[Edge]
    weighted: bool
    directed: bool

    def get_adjacent_vertices(self, vertex: Vertex) -> List[Vertex]:
        ...

    def get_edge(self, vertex_one: Vertex, vertex_two: Vertex) -> Edge:
        ...
