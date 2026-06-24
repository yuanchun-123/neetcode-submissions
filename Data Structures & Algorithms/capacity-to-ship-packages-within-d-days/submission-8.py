class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = 0
        while l <= r:
            mid = l + (r-l)//2
            need = 1
            curr = 0
            i = 0
            while i < len(weights):
                curr += weights[i]
                if curr > mid:
                    i -= 1
                    curr = 0
                    need += 1
                i += 1
            if need > days:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res
                


                


                
