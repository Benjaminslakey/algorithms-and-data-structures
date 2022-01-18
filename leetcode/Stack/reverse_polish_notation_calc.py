# @tags: [stack]

from collections import deque
from typing import List

import pytest

OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: int(a / b),  # problem spec states integer division should truncate towards 0
    '*': lambda a, b: a * b,
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        result = int(tokens[0])
        for token in tokens:
            if token in OPERATORS:
                right_operand = stack.pop()
                left_operand = stack.pop()
                result = OPERATORS[token](left_operand, right_operand)
                stack.append(result)
            else:
                stack.append(int(token))
        return result


@pytest.mark.parametrize('tokens, expected', [
    pytest.param(["2", "1", "+", "3", "*"], 9),
    pytest.param(["4", "13", "5", "/", "+"], 6),
    pytest.param(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    pytest.param(["15", "10", "*", "15", "/", "10", "/"], 1),
    pytest.param(["-2", "2", "+", "-5", "-"], 5),
    pytest.param(["1", "2", "3", "4", "5", "6", "7", "-", "+", "*", "+", "18", "-", "/", "+"], 3),
    pytest.param(["17"], 17),
    pytest.param([
        "-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16",
        "/", "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*",
        "-60", "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-",
        "*", "86", "132", "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-",
        "+", "28", "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*",
        "196", "-", "-59", "+", "187", "-", "143", "/", "-79", "-89", "+", "-"
    ], 165),
])
def test_rpn_calc(tokens, expected):
    solver = Solution()
    result = solver.evalRPN(tokens)
    assert result == expected
