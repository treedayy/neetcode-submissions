class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = prices[0]
        result = 0
        for i in range(n-1):
            profit = prices[i+1] - minPrice
            result = max(result, profit)
            minPrice = min(minPrice, prices[i+1])

        return result