import pytest

"""
Problem Statement

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
------------------------------------------------------------------------------------------------------------------------
Constraints

0 <= n <= 105
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
------------------------------------------------------------------------------------------------------------------------
"""

def number_of_one_bits(n):
    num_ones = 0
    while n:
        num_ones += (n & 1)
        n = n >> 1
    return num_ones

# Solution class goes here
class Solution:
    def countBits(self, n):
        result = []
        for i in range(0, n + 1):
            num_one_bits = number_of_one_bits(i)
            result.append(num_one_bits)
        return result


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param((2,), [0, 1, 1]),
    pytest.param((5,), [0, 1, 1, 2, 1, 2]),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.countBits(*input_args)
    assert result == expected_output

