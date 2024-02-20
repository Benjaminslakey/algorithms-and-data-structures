import copy
import sys
import pytest
import random
from typing import List

"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
 

Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

 

Constraints:

1 <= nums.length <= 50
-106 <= nums[i] <= 106
All the elements of nums are unique.
At most 10^4 calls in total will be made to reset and shuffle.
"""

class Solution:
    def __init__(self, nums: List[int]):
        random.seed()
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        shuffled = copy.copy(self.original)
        bound = len(self.original) - 1
        for i in range(0, len(self.original)):
            swap_idx = random.randint(0, bound)
            shuffled[i], shuffled[swap_idx] = shuffled[swap_idx], shuffled[i]
        return shuffled


@pytest.mark.parametrize('nums', [
    pytest.param([1, 2, 3]),
    pytest.param([4, 5, 6, 7, 8, 9, 10]),
])
def test_array_shuffler(nums):
    solver = Solution(nums)
    result = solver.shuffle()
    assert solver.reset() == nums
    # because the shuffler is random there is a very very small chance that the shuffle produces the same array as the original so these tests are non-deterministic, though still generally useful
    assert solver.shuffle() != nums
    assert solver.shuffle() != nums
    assert solver.shuffle() != nums


