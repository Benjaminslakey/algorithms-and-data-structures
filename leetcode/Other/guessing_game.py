# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my Math is lower, 1 if my Math is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            correct_number = guess(mid)
            if correct_number == -1:
                end = mid - 1
            elif correct_number == 1:
                start = mid + 1
            elif correct_number == 0:
                return mid
            else:
                raise Exception("api is broken")
        return -1
