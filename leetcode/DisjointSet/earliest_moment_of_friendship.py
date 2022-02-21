from typing import List

import pytest

from yekals.disjoint_set import DisjointSet


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        disjoint_set = DisjointSet()
        for person in range(0, n):
            disjoint_set.add(person)
        for idx, (timestamp, person_one, person_two) in enumerate(sorted(logs, key=lambda log: log[0])):
            disjoint_set.union(person_one, person_two)
            # for a graph to be connected it must have at least n - 1 edges
            # so we don't need to spend time checking whether or not the graph is fully connected until we have
            # processed at least that many edges
            if idx + 1 >= n - 1:
                all_connected = True
                for i in range(1, n):
                    all_connected = all_connected and disjoint_set.connected(0, i)
                    if not all_connected:
                        break
                if all_connected:
                    return timestamp
        return -1


@pytest.mark.parametrize('meeting_logs, num_people, earliest_moment', [
    pytest.param(
        [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
         [20190312, 1, 2], [20190322, 4, 5]], 6, 20190301),
    pytest.param([[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4, 3),
    pytest.param([[9, 3, 0], [0, 2, 1], [8, 0, 1], [1, 3, 2], [2, 2, 0], [3, 3, 1]], 4, 2),
])
def test_earliest_total_friendship(meeting_logs, num_people, earliest_moment):
    solver = Solution()
    result = solver.earliestAcq(meeting_logs, num_people)
    assert result == earliest_moment
