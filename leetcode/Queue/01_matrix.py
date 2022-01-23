# @tags: [queue, breadth_first_search, matrix]

import json
import time
from collections import deque
from typing import List

import pytest


class Solution:
    def __init__(self):
        self.matrix = None
        self.processed = set()
        self.zeros = set()

    def get_neighbors(self, vertex):
        v_row, v_col = vertex
        top_bound, left_bound, bottom_bound, right_bound = -1, -1, len(self.matrix), len(self.matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = []
        for row_delta, col_delta in directions:
            n_row, n_col = v_row + row_delta, v_col + col_delta
            if top_bound < n_row < bottom_bound and left_bound < n_col < right_bound:
                neighbors.append((n_row, n_col))
        return neighbors

    def bfs_shortest_path(self, start):
        discovered = set([start])
        queue = deque([(start, 0)])
        while queue:
            vertex, distance = queue.popleft()
            v_row, v_col = vertex
            if vertex not in self.processed or distance < self.matrix[v_row][v_col]:
                # if this is our first time seeing this vertex OR our shortest path from a 0 to this vertex
                self.matrix[v_row][v_col] = distance
                self.processed.add(vertex)
            else:
                # we don't need to continue exploring from this vertex because we already know it won't yield
                # updates to any of it's neighbors since our current path is longer than a previous one
                continue
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                if neighbor not in self.zeros and neighbor not in discovered:
                    queue.append((neighbor, distance + 1))
                    discovered.add(neighbor)

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.matrix = mat
        for r, row in enumerate(mat):
            for c, square in enumerate(row):
                if square == 0:
                    self.zeros.add((r, c))
        for start in self.zeros:
            self.bfs_shortest_path(start)
        return self.matrix


@pytest.mark.parametrize('matrix, expected_matrix', [
    pytest.param([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    pytest.param([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
    pytest.param(
        [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
         [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]],
        #
        [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
         [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
         [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]
    )
])
def test_update_matrix(matrix, expected_matrix):
    solver = Solution()
    result_matrix = solver.updateMatrix(matrix)
    assert result_matrix == expected_matrix


def test_exec_time_large_input():
    solver = Solution()
    with open("bf_matrix.json") as big_ass_matrix:
        matrix = json.load(big_ass_matrix)
        num_zeros = 0
        start = time.time()
        for row in matrix:
            for square in row:
                if square == 0:
                    num_zeros += 1
        result_matrix = solver.updateMatrix(matrix)
        end = time.time()
        exec_time = end - start
        print(f"exec time: {exec_time * 1000}ms")
