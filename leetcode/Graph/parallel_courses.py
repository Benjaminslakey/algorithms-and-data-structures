from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    """
    parse edge list into graph but reverse direction of the edge
    do breadth first search from each vertex with no incoming edges, (once flipped)
        ie all courses who are not prerequisites for any others
    return the max depth of all searches
    we expect this graph to be a dag
    if there are any cycles in the graph, which would represent circular depencies w pre-reqs, then we return -1
    """

    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre_reqs = defaultdict(set)
        children = defaultdict(set)
        # parse dag into parents and children, with relationships between both
        for pre_req, course in relations:
            pre_reqs[course].add(pre_req)
            children[pre_req].add(course)
        no_prereq_courses = []
        # any course that has pre_reqs should be in our adj list, if it's not then it is a starting course
        # if every course has pre_reqs than we have a cycle in our graph
        for course in range(1, n + 1):
            if not pre_reqs.get(course):
                no_prereq_courses.append(course)
        if not no_prereq_courses:
            return -1
        courses_taken = set()
        queue = deque([(course, 1) for course in no_prereq_courses])
        max_semester = 1
        while queue:
            course, semester = queue.popleft()
            max_semester = max(max_semester, semester)
            courses_taken.add(course)
            for child in children[course]:
                # before selecting a course to take next semester check that we have taken all pre_requisite courses
                if all([prq in courses_taken for prq in pre_reqs[child]]):
                    queue.append((child, semester + 1))
        # if we didn't take every course, then we encountered a circular dep between courses / cycle in the dag
        # preventing us from signing up for a class in the next semester
        if len(courses_taken) != n:
            return -1
        return max_semester


@pytest.mark.parametrize('n, relations, expected_semesters', [
    pytest.param(3, [[1, 3], [2, 3]], 2),
    pytest.param(3, [[1, 3], [2, 3], [3, 1]], -1),
])
def test_parallel_courses(n, relations, expected_semesters):
    solver = Solution()
    result = solver.minimumSemesters(n, relations)
    assert result == expected_semesters
