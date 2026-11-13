class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob = dp(i+2) + nums[i]
            no = dp(i+1)
            memo[i] = max(rob, no)
            return memo[i]
        return dp(0)