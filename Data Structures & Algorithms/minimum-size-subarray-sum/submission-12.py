class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                res = min(res, r-l+1)
                cur -= nums[l]
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res