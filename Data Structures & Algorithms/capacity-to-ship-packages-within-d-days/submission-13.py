class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2

            # how many days needed under m
            need = 1
            cur = 0
            for w in weights:
                if cur + w <= m:
                    cur += w
                else:
                    need += 1
                    cur = w
            
            if need > days:
                l = m + 1
            else:
                r = m - 1
        return l