class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        now = 0
        
        for r in range(len(nums)):
            now += nums[r]
            while now >= target:
                res = min(res, r-l+1)
                now -= nums[l]
                l += 1
        
        if res != float("inf"):
            return res
        else:
            return 0




