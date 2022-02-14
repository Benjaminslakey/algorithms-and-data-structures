from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def canJump(self, nums: List[int]) -> bool:
        return self.bottom_up_dp(nums)
        # return self.top_down_dp(nums, 0)

    def top_down_dp(self, nums, idx):
        if idx in self.memo:
            return self.memo[idx]
        if idx >= len(nums) - 1:
            return True
        max_jumps = nums[idx]
        for jump_dist in range(1, max_jumps + 1):
            if self.top_down_dp(nums, idx + jump_dist):
                return True
        self.memo[idx] = False
        return False

    def bottom_up_dp(self, nums):
        oob = len(nums)
        dp = [False for _ in range(oob)]
        dp[oob - 1] = True
        for idx in range(oob - 2, -1, -1):
            max_j = nums[idx]
            if idx + max_j >= oob - 1:
                dp[idx] = True
            else:
                for jump in range(1, max_j + 1):
                    if dp[idx + jump]:
                        dp[idx] = True
                        break
        return dp[0]
