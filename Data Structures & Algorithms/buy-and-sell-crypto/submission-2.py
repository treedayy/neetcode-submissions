class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #n = len(prices)
        #minPrice = prices[0]
        #result = 0
        #for i in range(n-1):
        #    profit = prices[i+1] - minPrice
        #    result = max(result, profit)
        #    minPrice = min(minPrice, prices[i+1])

        l, r = 0, 1
        result = 0
        maxP = 0

        while r < len(prices):
            if (prices[l] < prices[r]):
                result = prices[r]-prices[l]
                maxP = max(maxP, result)
            else:
                l = r
            r+=1
        return maxP