class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, search_space, target, start, end):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if search_space[mid] < target:
            return self.binary_search(search_space, target, start, mid - 1)
        elif search_space[mid] > target:
            return self.binary_search(search_space, target, mid + 1, end)
        elif search_space[mid] == target:
            return mid
        return -1

# @todo add unit tests
# @tags: [array, binary_search, recursion]
