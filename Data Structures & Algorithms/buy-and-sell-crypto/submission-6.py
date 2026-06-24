class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        res = 0
        for p in prices:
            min_p = min(p, min_p)
            cur = p - min_p
            res = max(res, cur)
        return res