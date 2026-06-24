class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = l + (r-l)//2
            curr = 0
            for pile in piles:
                hour = math.ceil(pile/mid)
                curr += hour
            if curr > h:
                l = mid + 1
            else: 
                res = mid
                r = mid - 1
        return res
