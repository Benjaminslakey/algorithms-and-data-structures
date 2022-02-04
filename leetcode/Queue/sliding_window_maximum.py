from typing import List

import pytest
from sortedcontainers import SortedList


class Solution:
    """
    operations we need to do on the window
    insert, delete, find max
    options:
        - max_heap
            - insert: O(logn)
            - delete: O(n)
            - max: O(1)
        - double ended queue:
            - insert: O(1)
            - delete (from end): 0(1)
            - max: O(n)
        - Balanced Search Tree:
            - insert: O(logN)
            - delete: O(logN)
            - max: O(logN)

       at face value a balanced BST seems best because all operations will be logN

       number of windows (n - k) * (insert + max + delete)
       Time Complexity:
            max_heap: O((n - k) * (n + logn + 1) => (n^2 + N*logN + n) - (nk + k*logN + k) => n^2 upper
            deque: O((n - k) * (1 + 1 + n)) => n^2 + 2N - kn - 2k => n^2 upper bound
            bst: O((n - k) * (3logN)) => 3(n logN - k logn) => (n - k)logN upper bound

    Clarifications:
        what are the bounds on # of nums and size of k => can k be as large as N or always a constant factor smaller
        bounds on values in nums: can they be negative (this should effect algorithm so not important actually)
        the window will always slide 1 position to the right?
        can there be duplicate values in nums

    create initial window
    init output
    compute 1st max and add to output
    slide window to the right n-k number of times
        remove previous leftmost #
        add rightmost number
        search for max
        add max to output
    return output
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = SortedList()
        maxes = []
        left, right = 0, k - 1
        # init window
        for idx in range(0, right):
            window.add(nums[idx])
        while right < len(nums):
            window.add(nums[right])
            curr_max = window[-1]
            maxes.append(curr_max)
            window.remove(nums[left])
            # slide window
            left += 1
            right += 1
        return maxes


@pytest.mark.parametrize('nums, k, maxes', [
    pytest.param([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    pytest.param([1], 1, [1])
])
def test_window_maxes(nums, k, maxes):
    solver = Solution()
    result = solver.maxSlidingWindow(nums, k)
    assert result == maxes
