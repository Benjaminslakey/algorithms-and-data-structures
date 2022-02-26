"""
Problem Statement

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
    return the minimum number of conference rooms required.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= intervals.length <= 104
0 <= starti < endi <= 106
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
------------------------------------------------------------------------------------------------------------------------
"""
import heapq
from typing import List

import pytest


# Solution class goes here
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return self.solve(intervals)

    def solve(self, meetings):
        """
        time complexity:
            sort => nlogn
            iterating over meeting in loop => n * cost per iteration
                cost per iteration: heappop + heappush => 2logn .. n is the size of the heap
            overall:
                nlogn + nlog n => O(n log n), bounded by our sort
        space complexity
            O(n) (where we add all meetings to the heap
        """
        meetings.sort(key=lambda m: m[0])
        ongoing_meetings = []
        max_ongoing_meetings = 0
        for start, end in meetings:
            while ongoing_meetings and ongoing_meetings[0] <= start:
                # the meeting we are checking on ended so mark it as completed
                heapq.heappop(ongoing_meetings)
            max_ongoing_meetings = max(max_ongoing_meetings, len(ongoing_meetings) + 1)
            heapq.heappush(ongoing_meetings, end)
        return max_ongoing_meetings


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([[0, 30], [5, 10], [15, 20]],), 2),
    pytest.param(([[7, 10], [2, 4]],), 1),
    pytest.param(([[13, 15], [1, 13]],), 1),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
