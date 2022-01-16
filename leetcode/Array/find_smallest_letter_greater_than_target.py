class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return self.binary_search(letters, target, 0, len(letters) - 1)

    def binary_search(self, search_space, target, start, end):
        if start > end:
            return search_space[start] if start < len(search_space) else search_space[0]
        mid = start + (end - start) // 2
        if search_space[mid] <= target:
            return self.binary_search(search_space, target, mid + 1, end)
        elif search_space[mid] > target:
            return self.binary_search(search_space, target, start, mid - 1)


# @todo add unit tests
# @tags: binary_search, array
