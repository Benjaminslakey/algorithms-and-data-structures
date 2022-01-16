class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        prev = low
        max_profit = 0
        for price in prices:
            if price > low:
                max_profit = max(max_profit, price - low)
            elif price < low:
                low = price
        return max_profit

# @todo add unit tests
# tags: array
