class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, prev):
            if i >= len(nums):
                return 0
            key = (i, prev)
            if key in memo:
                return memo[key]
            memo[key] = dp(i+1, prev)
            if prev == -1 or nums[i] > nums[prev]:
                memo[key] = max(memo[key], dp(i+1, i) + 1)
            return memo[key]
        return dp(0, -1)
