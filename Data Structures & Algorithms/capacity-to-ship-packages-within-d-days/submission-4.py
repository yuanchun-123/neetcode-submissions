class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = sum(weights)
        while l <= r:
            mid = l + (r-l)//2
            curr = 1
            i = 0
            ca = 0
            while i < len(weights):
                ca += weights[i]
                if ca > mid:
                    ca = 0
                    curr += 1
                    i -= 1
                i += 1
            
            if curr > days:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res


                


                
