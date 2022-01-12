from typing import List


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = -1, n, -1, n
        row, column = 0, 0
        num = 1
        matrix = [[-1 for _ in range(0, n)] for _ in range(0, n)]
        # go right
        while num <= n ** 2:
            while num <= n ** 2 and column < right:
                matrix[row][column] = num
                num += 1
                if column + 1 == right:
                    top += 1
                    row += 1
                    break
                else:
                    column += 1
            print_matrix(matrix)
            # go down
            while num <= n ** 2 and row < bottom:
                matrix[row][column] = num
                num += 1
                if row + 1 == bottom:
                    right -= 1
                    column -= 1
                    break
                else:
                    row += 1
            print_matrix(matrix)
            # go left
            while num <= n ** 2 and column > left:
                matrix[row][column] = num
                num += 1
                if column - 1 == left:
                    bottom -= 1
                    row -= 1
                    break
                else:
                    column -= 1
            print_matrix(matrix)
            # go up
            while num <= n ** 2 and row > top:
                matrix[row][column] = num
                num += 1
                if row + 1 == top:
                    left += 1
                    column += 1
                    break
                else:
                    row -= 1
            print_matrix(matrix)
        return matrix
