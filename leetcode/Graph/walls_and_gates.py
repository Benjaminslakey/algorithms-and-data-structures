from collections import deque

WALL = -1
GATE = 0
EMPTY = 2147483647


class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __hash__(self):
        return hash((self.row, self.column))

    def __add__(self, other):
        row, column = other
        return Square(self.row + row, self.column + column)


class Solution:
    def get_gate_positions(self, grid):
        gate_positions = []
        for r, row in enumerate(grid):
            for c, square in enumerate(row):
                if square == GATE:
                    gate_positions.append(Square(r, c))
        return gate_positions

    def get_neighbors(self, square, rooms):
        neighbors = []
        for dir_ in [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1),  # right
        ]:
            neighbor = square + dir_
            if 0 <= neighbor.row < len(rooms) and 0 <= neighbor.column < len(rooms[0]):
                neighbors.append(neighbor)
        return neighbors

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gate_positions = self.get_gate_positions(rooms)
        to_explore = deque([(gate, 0) for gate in gate_positions])
        visited = set()
        while to_explore:
            current, distance = to_explore.pop()
            for n in self.get_neighbors(current, rooms):
                if n not in visited and distance + 1 < rooms[n.row][n.column]:
                    if not rooms[n.row][n.column] in {WALL, GATE}:
                        rooms[n.row][n.column] = distance + 1
                        to_explore.appendleft((n, distance + 1))
            visited.add(current)

# @todo add unit tests
# @tags: [breadth_first_search, graph, queue]

