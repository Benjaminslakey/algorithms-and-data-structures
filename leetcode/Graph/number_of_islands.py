# @todo add unit tests
# @tags: [graph, breadth_first_search, queue]

from collections import deque
from typing import List

WATER = "0"
LAND = "1"


class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __hash__(self):
        return hash((self.row, self.column))

    def __add__(self, other):
        row, column = other
        return Square(self.row + row, self.column + column)


def get_neighbors(square, map_):
    def on_map(location):
        return 0 <= location.row < len(map_) and 0 <= location.column < len(map_[0])

    neighbors = []
    for dir_ in [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
    ]:
        neighbor = square + dir_
        if on_map(neighbor) and map_[neighbor.row][neighbor.column] == LAND:
            neighbors.append(neighbor)
    return neighbors


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for r, row in enumerate(grid):
            for c, square in enumerate(row):
                if square == LAND:
                    num_islands += 1
                    # instead of a visited set, update grid in place marking visited areas with their island number
                    # could also eliminate queue memory usage but the code for counting islands numbers becomes ugly
                    to_explore = deque([(Square(r, c), num_islands * -1)])
                    while to_explore:
                        current, marker = to_explore.pop()
                        if grid[current.row][current.column] != LAND:
                            continue
                        grid[current.row][current.column] = marker
                        for neighbor in get_neighbors(current, grid):
                            to_explore.appendleft((neighbor, marker))
        return num_islands

