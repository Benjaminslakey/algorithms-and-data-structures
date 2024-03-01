import pytest

"""
# Problem Statement

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.
------------------------------------------------------------------------------------------------------------------------

# Constraints

1 <= s.length <= 100
s consists only of '0' and '1'.
s contains at least one '1'.
------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

------------------------------------------------------------------------------------------------------------------------

# Walk Through
move first one all the way to the right, move all other ones as far left as we can
find first one from the right and move it all the way right
"000100010"
         ^ 
"000100010"
        ^ 
"000100010"
        ^^
"000100001"
        ^^
move all other ones left, starting from the right
"000100001"
        o
"000100001"
       o
"000100001"
      o
"000100001"
     o
"000100001"
    o
"000100001"
   ^^
"001000001"
  ^^o
"010000001"
  ^^o
"100000001"
 ^^ o
"100000001"
   o
"100000001"
  o
"100000001"
 o
------------------------------------------------------------------------------------------------------------------------
"""

def swap_left(start, arr):
    while start > 0:
        arr[start], arr[start - 1] = arr[start - 1], arr[start] 
        start -= 1

def swap_right(start, arr):
    while start < len(arr) - 1:
        arr[start], arr[start + 1] = arr[start + 1], arr[start] 
        start += 1

# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.maximumOddBinaryNumber(input_args)

    def maximumOddBinaryNumber(self, s):
        arr = list(s)
        i = len(arr) - 1
        while i >= 0:
            if arr[i] == "1":
                swap_right(i, arr)
                break
            i -= 1
        j = len(arr) - 2
        leftmost_one = 0
        print(arr)
        while j > leftmost_one:
            if arr[j] == "1":
                swap_left(j, arr)
                leftmost_one += 1
            else:
                j -= 1
        return "".join(arr)


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param("010", "001"),
    pytest.param("0101", "1001"),
    pytest.param("0011", "1001"),
    pytest.param("1000011", "1100001"),
    pytest.param("0111", "1101"),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


