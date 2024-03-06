import pytest

"""
# Problem Statement

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

------------------------------------------------------------------------------------------------------------------------

# Constraints

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

------------------------------------------------------------------------------------------------------------------------

# Examples

## Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

## Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.


------------------------------------------------------------------------------------------------------------------------

# Walk Through

------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.removeStars(input_args)

    def removeStars(self, s):
        stack = []
        for chr in s:
            if chr == "*":
                stack.pop()
            else:
                stack.append(chr)
        return "".join(stack)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param("leet**cod*e", "lecoe"),
    pytest.param("erase*****", ""),
    pytest.param("nostars", "nostars"),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


