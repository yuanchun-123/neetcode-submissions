class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin = cmax = res = nums[0]
        for i in range(1, len(nums)):
            pmin, pmax = cmin, cmax
            cmin = min(pmin*nums[i], pmax*nums[i], nums[i])
            cmax = max(pmin*nums[i], pmax*nums[i], nums[i])
            res = max(cmax, res)
        return res

        