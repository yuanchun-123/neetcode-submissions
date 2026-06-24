class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        # dp(i) the maximum value you can rob starting from i
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i+1), dp(i+2)+nums[i])
            return memo[i]
        return max(dp(0), dp(1))