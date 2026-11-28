class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        b = prices[0]

        for p in prices[1:]:
            if p > b:
                res += p - b
                b = p
            else:
                b = min(b, p)
        return res