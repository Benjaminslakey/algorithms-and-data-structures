from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        appeared_most = max(list(counts.items()), key=lambda item: item[1])
        return appeared_most[0]

# @todo add unit tests
# @leetcode: https://leetcode.com/problems/majority-element/
# @tags: [hashmap, array]
