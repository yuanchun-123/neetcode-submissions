class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                result = max(result, diff)
            else:
                l = r
            r += 1
        return result
            
