import pytest
from collections import defaultdict

"""
# Problem Statement

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
------------------------------------------------------------------------------------------------------------------------

# Constraints

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

------------------------------------------------------------------------------------------------------------------------

# Examples

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

------------------------------------------------------------------------------------------------------------------------

# Walk Through
count occurences
[1,2,2,1,1,3] {}
 ^            {1: 1} 
   ^          {1: 1, 2: 1}
     ^        {1: 1, 2: 2}
       ^      {1: 2, 2: 2}
         ^    {1: 3, 2: 2}
           ^  {1: 3, 2: 2, 3: 1}
check unique counts
{1: 3, 2: 2, 3: 1}
    ^              set(3)
{1: 3, 2: 2, 3: 1}
          ^        set(3, 2)
{1: 3, 2: 2, 3: 1}
                ^  set(3, 2, 1)
------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.uniqueOccurrences(input_args)

    def uniqueOccurrences(self, arr):
        counts = defaultdict(int)
        for n in arr:
            counts[n] += 1
        distinct_counts = set()
        for c in counts.values():
            if c in distinct_counts:
                return False
            distinct_counts.add(c)
        return True


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([1, 2], False),
    pytest.param([1, 2, 2, 1, 1, 3], True),
    pytest.param([-3,0,1,-3,1,1,1,-3,10,0], True),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output

