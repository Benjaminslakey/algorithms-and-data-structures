"""
Problem Statement

An integer array original is transformed into a doubled array changed by appending twice the value of every element
    in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array,
    return an empty array. The elements in original may be returned in any order.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= changed.length <= 105
0 <= changed[i] <= 105
------------------------------------------------------------------------------------------------------------------------
Examples

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
------------------------------------------------------------------------------------------------------------------------
"""

import pytest


# Solution class goes here
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        return self.solve(changed)

    def solve(self, changed):
        pass


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param((), None),
    pytest.param((), None),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
