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
            if nums[prev] < nums[i] or prev == -1:
                memo[key] = max(memo[key], dp(i+1, i)+1)
            return memo[key]
        return dp(0, -1)


