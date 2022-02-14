from typing import List


class Solution:
    """
    31,32,5,17,26,28,29  -> 31
    [6,7,0,1,2,3,4,5] 7
             ^
    [3,4,5,6,7,0,1] 7
           ^
    [4,5,6,7,0,1,2] 0
           ^
    """

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1  # this is sorted and target is in here
                else:
                    end = mid - 1
            else:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
