import pytest

"""
# Problem Statement

There is a biker going on a road trip.
The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.

------------------------------------------------------------------------------------------------------------------------

# Constraints

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

### Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

------------------------------------------------------------------------------------------------------------------------

# Walk Through
[-5 , 1 , 5 , 0 , -7]
  ^                    a = -5, max =  0
      ^                a = -4, max =  0
          ^            a =  1, max =  1
              ^        a =  1, max =  1
                   ^   a = -6, max =  1
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.largestAltitude(input_args)

    def largestAltitude(self, gain):
        altitude = 0
        max_altitude = 0
        for delta in gain:
            altitude += delta
            max_altitude = max(max_altitude, altitude)
        return max_altitude


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([-5,1,5,0,-7], 1),
    pytest.param([-4, -3, -2, -1, 4, 3, 2], 0),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


