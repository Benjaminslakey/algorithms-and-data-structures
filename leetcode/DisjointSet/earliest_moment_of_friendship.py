from typing import List

import pytest


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        pass


@pytest.mark.parametrize('meeting_logs, num_people, earliest_moment', [
    pytest.param([[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]], 6)
])
def test_earliest_total_friendship(meeting_logs, num_people, earliest_moment):
    solver = Solution()
    result = solver.earliestAcq(meeting_logs, num_people)
    assert result == earliest_moment
