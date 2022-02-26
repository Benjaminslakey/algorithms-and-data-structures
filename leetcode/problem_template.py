"""
Problem Statement

------------------------------------------------------------------------------------------------------------------------
Constraints

------------------------------------------------------------------------------------------------------------------------
Examples

------------------------------------------------------------------------------------------------------------------------
"""

import pytest

# Solution class goes here


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param((), None),
    pytest.param((), None),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(*input_args)
    assert result == expected_output
