import pytest

"""
# Problem Statement

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

------------------------------------------------------------------------------------------------------------------------

# Constraints

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

------------------------------------------------------------------------------------------------------------------------

# Examples

### Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2:
Input: height = [1,1]
Output: 1

------------------------------------------------------------------------------------------------------------------------

# Walk Through


------------------------------------------------------------------------------------------------------------------------
"""


# Solution class goes here
class Solution:
    def solve(self, input_args):
        return self.maxArea(input_args)

    def maxArea(self, heights):
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            lheight, rheight = heights[l], heights[r]
            height = min(lheight, rheight)
            max_area = max(max_area, height * (r - l))
            if lheight < rheight:
                l += 1
            else:
                r -= 1
        return max_area

    def brute_force(self, heights):
        max_water = 0
        i, j = 0, 1
        while i < len(heights) - 1:
            j = i + 1
            while j < len(heights):
                height = min(heights[i], heights[j])
                max_water = max(max_water, height * (j - i))
                j += 1
            i += 1
        return max_water


# Tests
@pytest.mark.parametrize('input_args, expected_output', [
    pytest.param([1,8,6,2,5,4,8,3,7], 49),
    pytest.param([1, 1], 1),
])
def test_solution(input_args, expected_output):
    solver = Solution()
    result = solver.solve(input_args)
    assert result == expected_output


