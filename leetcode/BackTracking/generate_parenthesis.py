from typing import List

import pytest


class Solution:
    """
    2 ^ n

    """

    def __init__(self):
        self.combinations = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(n, 0, 0, [])
        return self.combinations

    def dfs(self, n, num_opened: int, num_closed: int, parenthesis: List):
        if num_closed == n:
            self.combinations.append("".join(parenthesis))
            return

        if num_opened < n:
            parenthesis.append("(")
            self.dfs(n, num_opened + 1, num_closed, parenthesis)
            parenthesis.pop()
        if num_opened > num_closed:
            parenthesis.append(")")
            self.dfs(n, num_opened, num_closed + 1, parenthesis)
            parenthesis.pop()


@pytest.mark.parametrize('n, valid_parenthesis', [
    pytest.param(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    pytest.param(0, [])
])
def test_generate_parens(n, valid_parenthesis):
    solver = Solution()
    result = solver.generateParenthesis(n)
    assert result == valid_parenthesis
