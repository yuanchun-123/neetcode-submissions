class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, prev):
            if i >= len(nums):
                return 0
            key = (i, prev)
            if key in memo:
                return memo[key]
            memo[i] = dp(i+1, prev)
            if prev == -1 or nums[i] > nums[prev]:
                memo[i] = max(memo[i], 1 + dp(i+1, i))
            return memo[i]
        return dp(0, -1)