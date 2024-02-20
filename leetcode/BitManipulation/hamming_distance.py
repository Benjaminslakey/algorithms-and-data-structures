import pytest

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1
"""

class Solution:
    def hammingDistance(self, x, y):
        x_bin = format(x, 'b')[::-1]
        y_bin = format(y, 'b')[::-1]
        dist = 0
        # adding padding to smaller num so binary representations are equal length, will make comparison simpler
        pad = "0" * abs(len(x_bin) - len(y_bin))
        if len(x_bin) < len(y_bin):
            x_bin += pad
        elif len(y_bin) < len(x_bin):
            y_bin += pad
        # actual hamming distance code
        for idx in range(0, len(x_bin)):
            if x_bin[idx] != y_bin[idx]:
                dist += 1
        return dist

@pytest.mark.parametrize('x, y, expected', [
    pytest.param(1, 4, 2),
    pytest.param(3, 1, 1),
])
def test_hamming_distance(x, y, expected):
    solver = Solution()
    result = solver.hammingDistance(x, y)
    assert result == expected

