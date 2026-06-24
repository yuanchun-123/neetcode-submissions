class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = 0
        while l <= r:
            mid = l + (r-l)//2
            need = 1
            curr = 0
            for w in weights:
                if curr + w > mid:
                    curr = 0
                    need += 1
                curr += w
            if need > days:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res
                


                


                
