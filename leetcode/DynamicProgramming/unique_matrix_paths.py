"""
There is a robot on an m x n grid. The robot is initially located in the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n,
return the Math of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100

"""

import pytest


class Solution:
    """
    keep shrinking size of matrix until we get to a matrix of 1 x 1  in which there is a single path
    to the end
    """

    def __init__(self):
        self.memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        return self.bottom_up_dp(m, n)

    def bottom_up_dp(self, m, n):
        dp = [[0] * (m - 1) + [1]] * n
        dp[-1][-1] = 1

        def get_dp_val(r, c):
            if -1 < r < n and -1 < c < m:
                return dp[r][c]
            return 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[i][j] = get_dp_val(i, j + 1) + get_dp_val(i + 1, j)
        return dp[0][0]

    def top_down_dp(self, m: int, n: int) -> int:
        key = f"{m}:{n}"
        if key in self.memo:
            return self.memo[key]

        if m == 1 and n == 1:
            return 1
        right, down = 0, 0
        if m > 1:
            right = self.uniquePaths(m - 1, n)
        if n > 1:
            down = self.uniquePaths(m, n - 1)
        paths_from_here = right + down
        self.memo[key] = paths_from_here
        return paths_from_here


@pytest.mark.parametrize('m, n, unique_paths', [
    pytest.param(3, 2, 3),
    pytest.param(3, 7, 28)
])
def test_unique_paths(m, n, unique_paths):
    solver = Solution()
    result = solver.uniquePaths(m, n)
    assert result == unique_paths
