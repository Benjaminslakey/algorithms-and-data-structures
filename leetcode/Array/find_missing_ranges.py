"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums,
where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly.
That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.


Constraints:

-109 <= lower <= upper <= 109
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.
"""

from typing import List

import pytest


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            missing_range = f"{lower}->{upper}" if lower < upper else f"{lower}"
            return [missing_range]
        nums.append(upper + 1)
        start = lower - 1
        output = []
        for num in nums:
            if start + 1 < num - 1:
                output.append(f"{start + 1}->{num - 1}")
            elif start + 1 == num - 1:
                output.append(f"{start + 1}")
            start = num
        return output


@pytest.mark.parametrize('nums, lower, upper, expected', [
    pytest.param([0, 1, 3, 50, 75], 0, 99, ["2", "4->49", "51->74", "76->99"]),
    pytest.param([0, 1, 3, 50, 75, 98, 99], 0, 99, ["2", "4->49", "51->74", "76->97"]),
    pytest.param([-1], -1, -1, []),
    pytest.param([], 1, 1, ["1"]),
    pytest.param([], -3, -1, ["-3->-1"]),
    pytest.param([-1], -2, -1, ["-2"])
])
def test_missing_ranges(nums, lower, upper, expected):
    solver = Solution()
    result = solver.findMissingRanges(nums, lower, upper)
    assert result == expected
