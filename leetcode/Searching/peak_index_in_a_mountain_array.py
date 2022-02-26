# important thing to ask about
# is there only a single peak if there isn't then the solution seems much more complex

# pick the mid
#     if the item to the right of mid is greater
#         the peak is to the right
#     if the item to the right is smaller
#         the peak is to the left of is the current item

# walk through example
# [3,4,5,1], 1, 2
# 1  => f(arr, 2, 2)
#     2 + (2 - 2) // 2 ==> 2


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.binary_search(arr, 1, len(arr) - 2)

    def binary_search(self, search_space, start, end):
        mid = start + (end - start) // 2
        current = search_space[mid]
        if search_space[mid - 1] < current and search_space[mid + 1] < current:
            return mid
        if search_space[mid - 1] > current:
            return self.binary_search(search_space, start, mid - 1)
        return self.binary_search(search_space, mid + 1, end)


# @todo add unit tests
# @tags: [array, binary_search]
