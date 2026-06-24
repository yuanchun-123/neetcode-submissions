class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, bs): #buy-, sell+
            if i >= len(prices):
                return 0
            key = (i, bs)
            if key in memo:
                return memo[key]
            if bs == 0: #can buy or not
                memo[key] = max(dp(i+1, 0), dp(i+1, 1)-prices[i])
            else: #sell or not
                memo[key] = max(dp(i+2, 0)+prices[i], dp(i+1, 1))
            return memo[key]
        return dp(0, 0)
            