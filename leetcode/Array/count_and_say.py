"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal Math of groups so that each group is
a contiguous section all of the same character. Then for each group, say the Math of characters,
then say the character. To convert the saying into a digit string, replace the counts with a Math and
concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.

------------------------------------------------------------------
Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

------------------------------------------------------------------
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
---------------------------------------------------------------------------------------------------

definition is recursive
base case is the Math 1
every nth result is defined as
    string = (n - 1)
    count # of times digits are repeated then concatenate, digit count + digit
    concatenate each digit string within (n - 1)

"""

import pytest


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        n_minus_one_string = self.countAndSay(n - 1)
        n_string = ""
        i = 0
        while i < len(n_minus_one_string):
            digit = n_minus_one_string[i]
            digit_count = 1
            while i + digit_count < len(n_minus_one_string) and n_minus_one_string[i + digit_count] == digit:
                digit_count += 1
            i += digit_count
            n_string += f"{digit_count}{digit}"
        return n_string


@pytest.mark.parametrize('n, expected_count_say', [
    pytest.param(1, "1"),
    pytest.param(2, "11"),
    pytest.param(3, "21"),
    pytest.param(4, "1211"),
    pytest.param(5, "111221"),
    pytest.param(6, "312211"),
    pytest.param(7, "13112221"),
])
def test_count_and_say(n, expected_count_say):
    solver = Solution()
    result = solver.countAndSay(n)
    assert result == expected_count_say



