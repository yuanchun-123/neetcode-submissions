class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix, prefix_m = nums[0], nums[0]
        best = nums[0]
        for n in nums:
            prefix += n
            best = max(best, prefix - prefix_m)
            prefix_m = min(prefix, prefix_m)
        return best
