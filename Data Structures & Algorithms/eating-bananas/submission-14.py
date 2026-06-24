class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        while l < r-1:
            mid = l + (r-l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            if time > h:
                l = mid 
            else:
                r = mid
        return r
            

