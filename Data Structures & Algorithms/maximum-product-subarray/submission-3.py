class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cmax = cmin = nums[0]
        for i in range(1, len(nums)):
            premax, premin = cmax, cmin
            cmax = max(premax*nums[i], premin*nums[i], nums[i])
            cmin = min(premax*nums[i], premin*nums[i], nums[i])
            res = max(res, cmax)
        return res
