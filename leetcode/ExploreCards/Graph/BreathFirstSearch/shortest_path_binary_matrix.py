from collections import deque
from typing import List


BLOCKED = 1
EMPTY = 0


class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        if not isinstance(other, Square):
            raise TypeError("Invalid type to compare instance of Square with")
        return self.row == other.row and self.column == other.column

    def __add__(self, other):
        row_diff, column_diff = other
        return Square(self.row + row_diff, self.column + column_diff)


def get_neighbors(square: Square, grid: List[List[int]]):
    left_bound, right_bound, top_bound, bottom_bound = -1, len(grid), -1, len(grid)
    directions = [
        (-1, 0),  # above
        (-1, 1),  # top_right
        (0, 1),  # right
        (1, 1),  # bottom_right
        (1, 0),  # bottom
        (1, -1),  # bottom_left
        (0, -1),  # left
        (-1, -1),  # top_left
    ]
    for direction in directions:
        neighbor = square + direction
        if (
                top_bound < neighbor.row < bottom_bound and left_bound < neighbor.column < right_bound
                and grid[neighbor.row][neighbor.column] != BLOCKED
        ):
            yield neighbor


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        parse graph
        start = (0, 0)
        end = (len(graph) - 1, len(graph) - 1)
        shorted_path = Breadth First Search(graph, start, end)
        return shorted path
        """
        if grid[0][0] == BLOCKED or grid[-1][-1] == BLOCKED:
            return -1
        elif len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == EMPTY:
            return 1
        visited = set()
        start = Square(0, 0)
        end = Square(len(grid) - 1, len(grid) - 1)
        to_explore = deque([(start, 1)])
        while to_explore:
            current_location, path_length = to_explore.pop()
            if current_location in visited:
                continue
            for neighbor in get_neighbors(current_location, grid):
                if neighbor == end:
                    return path_length + 1
                to_explore.appendleft((neighbor, path_length + 1))
            visited.add(current_location)
        return -1




