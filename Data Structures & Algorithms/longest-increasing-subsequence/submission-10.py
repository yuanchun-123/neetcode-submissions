class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            if prev == -1 or nums[i] > nums[prev]:
                memo[(i, prev)] = 1 + dp(i+1, i)
                memo[(i, prev)] = max(memo[(i, prev)], dp(i+1, prev))
            else:
                memo[(i, prev)] = dp(i+1, prev)
            return memo[(i, prev)]
        return dp(0, -1)
