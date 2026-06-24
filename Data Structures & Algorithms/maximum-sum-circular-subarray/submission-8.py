class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max, cur_min = nums[0], nums[0]
        global_max, global_min = nums[0], nums[0]
        for n in nums[1:]:
            cur_max = max(n + cur_max, n)
            cur_min = min(n + cur_min, n)
            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)
        if max(nums) < 0:
            return max(nums)
        return max(global_max, total - global_min)