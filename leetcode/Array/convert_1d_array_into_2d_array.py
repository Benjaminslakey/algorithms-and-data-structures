class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) % (m * n) != 0 or len(original) > (m * n):
            return []

        two_dimensional = []
        row = []
        for i, num in enumerate(original):
            row.append(original[i])
            if (i + 1) % n == 0:
                two_dimensional.append(row)
                row = []
        if row:
            two_dimensional.append(row)
        return two_dimensional

# @todo add unit tests
# @tags: [array]

