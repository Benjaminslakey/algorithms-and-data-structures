from collections import deque
from typing import List

import pytest


BLOCKED = 0


class DisjointNodesError(Exception):
    pass


class Solution:
    """
    we want to minimize the Math of steps: ie path length
    we need to cut down trees in order from shortest to tallest

    all move: north east west south cost 1
    unweighted graph, bfs will give us the shortest path between any two points

    find shortest path from start (0, 0) to shortest tree
    then find shortest path to each tree in sorted order
    summing paths the entire time
    if we cannot get to a tree because the trees are disjoint return -1

    we shouldn't need to check beforehand whether or not trees are disjoint because we will find out during breadth first search

    first, sort trees by height so we know order to target them in => N logN
    then do bfs between each tree in sorted order => bfs O(n) * # trees n
    O(n^2) in the case of a dense graph
    """

    def __init__(self):
        self.grid = [[]]
        self.left_bound = -1
        self.top_bound = -1
        self.bottom_bound = 0
        self.right_bound = 0

    def get_neighbors(self, node):
        r, c = node
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = []
        for dr, dc in directions:
            if self.top_bound < r + dr < self.bottom_bound and self.left_bound < c + dc < self.right_bound:
                if self.grid[r + dr][c + dc] != BLOCKED:
                    neighbors.append((r + dr, c + dc))
        return neighbors

    def bfs(self, start, end):
        discovered = set()
        queue = deque([(start, 0)])
        while queue:
            current, distance = queue.popleft()
            if current == end:
                return distance
            for neighbor in self.get_neighbors(current):
                if neighbor not in discovered:
                    queue.append((neighbor, distance + 1))
                    # use discovered instead of visited so we don't add duplicate vertices to queue
                    discovered.add(neighbor)
        raise DisjointNodesError()

    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.grid = forest
        self.bottom_bound = len(forest)
        self.right_bound = len(forest[0])
        trees = []
        # gather trees
        for r, row in enumerate(forest):
            for c, height in enumerate(row):
                if height > 1:
                    trees.append((height, r, c))
        # sort trees
        trees.sort(key=lambda x: x[0])
        num_steps = 0
        # find shortest path between trees, sum path length
        start = (0, 0)
        for idx in range(0, len(trees)):
            height, r, c = trees[idx]
            next_tree = (r, c)
            try:
                distance = self.bfs(start, next_tree)
            except DisjointNodesError:
                return -1
            num_steps += distance
            start = next_tree
        return num_steps


@pytest.mark.parametrize('forest, expected_shortest_path', [
    pytest.param([[1, 2, 3], [0, 0, 4], [7, 6, 5]], 6),
    pytest.param([[1, 2, 3], [0, 0, 0], [7, 6, 5]], -1),
    pytest.param([[69438, 55243, 0, 43779, 5241, 93591, 73380], [847, 49990, 53242, 21837, 89404, 63929, 48214],
                  [90332, 49751, 0, 3088, 16374, 70121, 25385], [14694, 4338, 87873, 86281, 5204, 84169, 5024],
                  [31711, 47313, 1885, 28332, 11646, 42583, 31460], [59845, 94855, 29286, 53221, 9803, 41305, 60749],
                  [95077, 50343, 27947, 92852, 0, 0, 19731], [86158, 63553, 56822, 90251, 0, 23826, 17478],
                  [60387, 23279, 78048, 78835, 5310, 99720, 0], [74799, 48845, 60658, 29773, 96129, 90443, 14391],
                  [65448, 63358, 78089, 93914, 7931, 68804, 72633], [93431, 90868, 55280, 30860, 59354, 62083, 47669],
                  [81064, 93220, 22386, 22341, 95485, 20696, 13436], [50083, 0, 89399, 43882, 0, 13593, 27847],
                  [0, 12256, 33652, 69301, 73395, 93440, 0], [42818, 87197, 81249, 33936, 7027, 5744, 64710],
                  [35843, 0, 99746, 52442, 17494, 49407, 63016], [86042, 44524, 0, 0, 26787, 97651, 28572],
                  [54183, 83466, 96754, 89861, 84143, 13413, 72921], [89405, 52305, 39907, 27366, 14603, 0, 14104],
                  [70909, 61104, 70236, 30365, 0, 30944, 98378], [20124, 87188, 6515, 98319, 78146, 99325, 88919],
                  [89669, 0, 64218, 85795, 2449, 48939, 12869], [93539, 28909, 90973, 77642, 0, 72170, 98359],
                  [88628, 16422, 80512, 0, 38651, 50854, 55768], [13639, 2889, 74835, 80416, 26051, 78859, 25721],
                  [90182, 23154, 16586, 0, 27459, 3272, 84893], [2480, 33654, 87321, 93272, 93079, 0, 38394],
                  [34676, 72427, 95024, 12240, 72012, 0, 57763], [97957, 56, 83817, 45472, 0, 24087, 90245],
                  [32056, 0, 92049, 21380, 4980, 38458, 3490], [21509, 76628, 0, 90430, 10113, 76264, 45840],
                  [97192, 58807, 74165, 65921, 45726, 47265, 56084], [16276, 27751, 37985, 47944, 54895, 80706, 2372],
                  [28438, 53073, 0, 67255, 38416, 63354, 69262], [23926, 75497, 91347, 58436, 73946, 39565, 10841],
                  [34372, 69647, 44093, 62680, 32424, 69858, 68719], [24425, 4014, 94871, 1031, 99852, 88692, 31503],
                  [24475, 12295, 33326, 37771, 37883, 74568, 25163], [0, 18411, 88185, 60924, 29028, 69789, 0],
                  [34697, 75631, 7636, 16190, 60178, 39082, 7052], [24876, 9570, 53630, 98605, 22331, 79320, 88317],
                  [27204, 89103, 15221, 91346, 35428, 94251, 62745], [26636, 28759, 12998, 58412, 38113, 14678, 0],
                  [80871, 79706, 45325, 3861, 12504, 0, 4872], [79662, 15626, 995, 80546, 64775, 0, 68820],
                  [25160, 82123, 81706, 21494, 92958, 33594, 5243]], 20)
])
def test_cut_trees(forest, expected_shortest_path):
    solver = Solution()
    result = solver.cutOffTree(forest)
    assert result == expected_shortest_path
