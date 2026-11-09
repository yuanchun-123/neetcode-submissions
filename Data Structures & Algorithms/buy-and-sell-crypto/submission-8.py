class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        p_min = prices[0]
        for p in prices:
            p_min = min(p, p_min)
            cur = p - p_min
            res = max(res, cur)
        return res