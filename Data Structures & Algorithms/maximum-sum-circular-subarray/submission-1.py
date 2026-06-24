class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        best = cur_max = nums[0]
        worst = cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max+nums[i])
            cur_min = min(nums[i], cur_min+nums[i])
            best = max(cur_max, best)
            worst = min(cur_min, worst)
        if max(nums) < 0:
            return max(nums)
        return max(best, total-worst)