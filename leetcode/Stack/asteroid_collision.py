import pytest

"""
# Problem Statement

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

------------------------------------------------------------------------------------------------------------------------

# Constraints

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

### Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

### Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

------------------------------------------------------------------------------------------------------------------------
# Walk Through

[-8, 15, 10, -10, 5, 5, -5, 3, 4]
 ^
      ^                          s: [-8, 15]
         ^                       s: [-8, 15, 10]
              ^                  s: [-8, 15]
                  ^              s: [-8, 15, 5]
                     ^           s: [-8, 15, 5, 5]
                         ^       s: [-8, 15, 5]
                            ^    s: [-8, 15, 5, 3]
                               ^ s: [-8, 15, 5, 3, 4]

[-8, 15, 10, -12, -5, -8, 5, 3, -4]
  ^
      ^                              s: [-8, 15]
          ^                          s: [-8, 15, 10]
              ^                      s: [-8, 15] 
                   ^                 s: [-8, 15] 
                       ^             s: [-8, 15]
                          ^          s: [-8, 15, 5]
                              ^      s: [-8, 15, 5, 3]
                                 ^   s: [-8, 15, 5]
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.asteroidCollision(input_args)

    def asteroidCollision(self, asteroids):
        result = []
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue
            elif len(stack) == 0:
                result.append(a)
                continue

            while len(stack) > 0 and stack[-1] < abs(a):
                stack.pop()
            if len(stack) > 0 and stack[-1] == abs(a):
                stack.pop()
            elif len(stack) == 0:
                result.append(a)
        result.extend(stack)
        return result


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([5, 10, -5], [5, 10]),
    pytest.param([8, -8], []),
    pytest.param([10, 2, -5], [10]),
    pytest.param([-8, 15, 10, -12, -5, -8, 5, 3, -4], [-8, 15, 5]),
    pytest.param([-8, 15, 10, -10, 5, 5, -5, 3, 4], [-8, 15, 5, 3, 4])
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


