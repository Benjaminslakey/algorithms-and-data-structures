import pytest
from typing import List

from collections import deque

"""
# Problem Statement

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

------------------------------------------------------------------------------------------------------------------------

# Constraints

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

### Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

------------------------------------------------------------------------------------------------------------------------

# Walk Through



------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.findCircleNum(input_args)

    def find_connected(self, adj_matrix, start):
        province = set()
        to_visit = deque([start])
        while to_visit:
            city = to_visit.pop()
            for other, is_connected in enumerate(adj_matrix[city]):
                if not is_connected:
                    continue
                if other not in province:
                    to_visit.appendleft(other)
            province.add(city)
        return province 

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        num_provinces = 0
        for city, _ in enumerate(isConnected):
            if city in visited:
                continue
            province = self.find_connected(isConnected, city)
            visited.update(province)
            num_provinces +=1 
        return num_provinces


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([[1,1,0],[1,1,0],[0,0,1]], 2),
    pytest.param([[1,0,0],[0,1,0],[0,0,1]], 3),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output

