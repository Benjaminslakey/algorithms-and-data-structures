import pytest

"""
# Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

------------------------------------------------------------------------------------------------------------------------

# Constraints

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.replace(*input_args)

    def replace(self):
        return


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param((), None),
    pytest.param((), None),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


