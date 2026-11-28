class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]

        for p in prices:
            low = min(low, p)
            cur = p - low
            res = max(cur, res)

        return res
