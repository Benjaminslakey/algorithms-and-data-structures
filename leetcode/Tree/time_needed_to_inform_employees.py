"""
CLARIFYING QUESTIONS

is it the number of total man minutes or elapsed minutes,
example, if we only had 1 manager with 5 employ
can an employee have multiple manager: probably not based on definiton of array

enumerate all paths in tree using bfs
as we reach leaf nodes, sum path weights and compare to maximum
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    """
    
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for employee, parent in enumerate(manager):
            tree[parent].append(employee)

        root = tree[-1][0]

        queue = deque([(root, 0)])
        visited = set()
        max_path_sum = 0
        while queue:
            employee, cost = queue.pop()
            if not tree[employee]:
                max_path_sum = max(max_path_sum, cost)
            else:
                for reportee in tree[employee]:
                    queue.appendleft((reportee, cost + informTime[employee]))
            visited.add(employee)
        return max_path_sum
