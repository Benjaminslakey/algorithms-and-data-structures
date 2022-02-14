###
# Largest Island
# Given a two dimensional array/list of characters (limited to 'L' and 'W', land and water), and
# given that two pieces of land are adjacent if they are up/down/left/right from each other.
# Given the following example:

# WWWWLLWL
# WWWLLLLLL
# WWLWWWLW
# WLLWLLWW
# LLLLWLWW


from collections import deque

import pytest


def get_neighbors(vertex, graph):
    neighbors = []
    left_bound = -1
    top_bound, bottom_bound = -1, len(graph)
    r, c = vertex
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        delta_r, delta_c = direction
        neighbor = (r + delta_r, c + delta_c)
        nr, nc = neighbor
        if top_bound < nr < bottom_bound and left_bound < nc < len(graph[nr]) and graph[nr][nc] == "L":
            neighbors.append(neighbor)
    return neighbors


def bfs(island_map, vertex, visited) -> int:
    queue = deque([vertex])
    discovered = {vertex}
    while queue:
        current = queue.popleft()
        for neighbor in get_neighbors(current, island_map):
            if neighbor not in visited:
                queue.append(neighbor)
                discovered.add(neighbor)
                visited.add(neighbor)
    return len(discovered)


def find_largest_island(island_map):
    visited = set()
    max_island_size = 0
    for r, row in enumerate(island_map):
        for c, cell in enumerate(row):
            start_v = (r, c)
            if cell == "L" and start_v not in visited:
                island_size = bfs(island_map, start_v, visited)
                visited.add(start_v)
                max_island_size = max(island_size, max_island_size)
    return max_island_size


@pytest.mark.parametrize('graph, expected_largest', [
    pytest.param(["LLLL"], 4),
    pytest.param(["WWWW"], 0),
    pytest.param([
        "WWWWLLWL",
        "WWWLLLLLL",
        "WWLWWWLW",
        "WLLWLLWW",
        "LLLLWLWW"
    ], 10),
])
def test_largest_island(graph, expected_largest):
    largest_island = find_largest_island(graph)
    assert largest_island == expected_largest
