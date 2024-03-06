import pytest

"""
# Problem Statement



------------------------------------------------------------------------------------------------------------------------

# Constraints



------------------------------------------------------------------------------------------------------------------------

# Examples



------------------------------------------------------------------------------------------------------------------------

# Walk Through



------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, *input_args):
        return self.replace(*input_args)

    def replace(self):
        return


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([], None),
    pytest.param([], None),
    pytest.param([], None),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output

