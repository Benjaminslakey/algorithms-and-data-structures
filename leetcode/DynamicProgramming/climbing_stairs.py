class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fib(n, {1: 1, 2: 2})

    def fib(self, n, memo):
        if n in memo:
            return memo[n]
        distinct_from_here = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        memo[n] = distinct_from_here
        return distinct_from_here

# @todo add unit tests
