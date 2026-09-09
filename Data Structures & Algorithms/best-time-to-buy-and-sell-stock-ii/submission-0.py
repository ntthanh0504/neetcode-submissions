class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                max_profit += diff
        return max_profit