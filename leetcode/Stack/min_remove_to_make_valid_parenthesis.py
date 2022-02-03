import pytest


class Solution:
    """
    use stack to record open parenthesis
    when we encounter a closing parenthesis,
        pop the stack to pair it with matching open
        if there is no match, record it as mismatched
    recreate string, skipping mismatched indices (those unmatched opens left in stack + unmatched closes)
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if not stack:
                    to_remove.add(idx)
                else:
                    stack.pop()
        for remaining in stack:
            to_remove.add(remaining)
        valid_string = ""
        for idx, char in enumerate(s):
            if idx not in to_remove:
                valid_string += char
        return valid_string


@pytest.mark.parametrize('stringy, expected', [
    pytest.param("lee(t(c)o)de)", "lee(t(c)o)de"),
    pytest.param("a)b(c)d", "ab(c)d"),
    pytest.param("))((", ""),
])
def test_min_remove_valid_parens(stringy, expected):
    solver = Solution()
    result = solver.minRemoveToMakeValid(stringy)
    assert result == expected
