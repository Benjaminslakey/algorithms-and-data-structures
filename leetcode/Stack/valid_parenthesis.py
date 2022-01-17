# @tags: [string, stack]

from collections import deque

import pytest

BRACES = {
    ')': '(',
    '}': '{',
    ']': '[',
}

OPENING = {'[', '(', '{'}
CLOSING = {']', ')', '}'}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])

        for char in s:
            if char in OPENING:
                stack.appendleft(char)
            elif char in CLOSING and stack and stack[0] == BRACES[char]:
                stack.popleft()
            else:
                return False
        return len(stack) == 0


@pytest.mark.parametrize('string, validity', [
    pytest.param('[', False),
    pytest.param(']', False),
    pytest.param('{', False),
    pytest.param('}', False),
    pytest.param('(', False),
    pytest.param(')', False),
    pytest.param('[(])', False),
    pytest.param('[()]{}{}()[[[]', False),
    pytest.param('[({}()])', False),
    pytest.param('{}', True),
    pytest.param('()', True),
    pytest.param('[]', True),
    pytest.param('[(()()[]){}]', True),
    pytest.param('[](()[]){}[]', True),
    pytest.param('[()]{}{}()[[[]]]', True),
])
def test_is_valid_parenthesis(string, validity):
    solver = Solution()
    result = solver.isValid(string)
    assert result == validity
