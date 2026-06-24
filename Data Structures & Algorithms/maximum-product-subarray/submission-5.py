class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cmax = cmin = nums[0]
        for i in range(1, len(nums)):
            prex = cmax
            pren = cmin
            cmax = max(prex*nums[i], pren*nums[i], nums[i])
            cmin = min(prex*nums[i], pren*nums[i], nums[i])
            res = max(cmax, res)
        return res