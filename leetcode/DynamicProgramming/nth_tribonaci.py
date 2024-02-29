import pytest

"""
Problem Statement

The Tribonacci sequence Tn is defined as follows: T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

------------------------------------------------------------------------------------------------------------------------
Constraints

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def __init__(self):
        self.memo = {}

    def solve(self, input_args):
        return self.tribonacci(*input_args)

    def tribonacci(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        if n in self.memo:
            return self.memo[n]
        trib = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.memo[n] = trib
        return trib


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param((0,), 0),
    pytest.param((1,), 1),
    pytest.param((2,), 1),
    pytest.param((3,), 2),
    pytest.param((4,), 4),
    pytest.param((5,), 7),
    pytest.param((6,), 13),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output

