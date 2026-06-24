class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, bs):
            if i >= len(prices):
                return 0
            key = (i, bs)
            if key in memo:
                return memo[key]
            if bs == 0:
                memo[key] = max(dp(i+1, 0), dp(i+1, 1)-prices[i])
            else:
                memo[key] = max(dp(i+1, 1), dp(i+2, 0)+prices[i])
            return memo[key]
        return dp(0, 0)