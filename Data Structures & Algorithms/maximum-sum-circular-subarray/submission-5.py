class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, cur_min = nums[0], nums[0]
        global_max, global_min = nums[0], nums[0]
        for n in nums[1:]:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)
        if global_max < 0:
            return global_max
        return max(global_max, sum(nums)-global_min)