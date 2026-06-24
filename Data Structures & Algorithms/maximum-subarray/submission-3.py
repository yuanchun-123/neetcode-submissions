class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(cur+nums[i], nums[i])
            best = max(best, cur)
        return best