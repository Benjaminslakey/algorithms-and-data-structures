import pytest

"""
Problem Statement

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

------------------------------------------------------------------------------------------------------------------------
Constraints

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

------------------------------------------------------------------------------------------------------------------------
Examples

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 4

[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 4

[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1] 4

[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1] 5
       1              1     1      1
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.canPlaceFlowers(*input_args)

    def can_place_flower(self, pot, flowerbed):
        if flowerbed[pot] == 1:
            return False
        left_has_flower = flowerbed[pot - 1] == 1 if pot - 1 >= 0 else False
        right_has_flower = flowerbed[pot + 1] == 1 if pot + 1 < len(flowerbed) else False
        return not left_has_flower and not right_has_flower

    def canPlaceFlowers(self, flowerbed, num_new_flowers):
        pot = 0
        flowersPlaced = 0
        while pot < len(flowerbed):
            if self.can_place_flower(pot, flowerbed):
                flowerbed[pot] = 1
                flowersPlaced += 1
                pot += 2
            else:
                pot += 1
        return flowersPlaced >= num_new_flowers


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param(([1,0,0,0,1], 1), True),
    pytest.param(([1,0,0,0,1], 2), False),
    pytest.param(([0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 3), True),
    pytest.param(([0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 4), False),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output

