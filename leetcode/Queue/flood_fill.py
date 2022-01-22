from collections import deque
from typing import List

import pytest


class Solution:
    def __init__(self):
        self.image = None
        self.original_color = None
        self.new_color = None

    def process_vertex(self, vertex):
        vertex_row, vertex_column = vertex
        self.image[vertex_row][vertex_column] = self.new_color

    def get_neighbors(self, vertex):
        row, col = vertex
        top_bound, bottom_bound, left_bound, right_bound = -1, len(self.image), -1, len(self.image[0])
        directions = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, -1),  # left
            (0, 1),  # right
        ]
        neighbors = []
        for row_delta, col_delta in directions:
            n_row, n_col = row + row_delta, col + col_delta
            if (
                    top_bound < n_row < bottom_bound and left_bound < n_col < right_bound
                    and self.image[n_row][n_col] == self.original_color
            ):
                neighbors.append((n_row, n_col))
        return neighbors

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.new_color = newColor
        self.original_color = image[sr][sc]
        start = (sr, sc)
        queue = deque([start])
        visited = set()
        while queue:
            vertex = queue.popleft()
            for adjacent_vertex in self.get_neighbors(vertex):
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
            self.process_vertex(vertex)
            visited.add(vertex)
        return image


@pytest.mark.parametrize('image, sr, sc, new_color, expected_painted_image', [
    pytest.param([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]]),
    pytest.param([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
])
def test_flood_fill(image, sr, sc, new_color, expected_painted_image):
    solver = Solution()
    modified_image = solver.floodFill(image, sr, sc, new_color)
    assert modified_image == expected_painted_image
