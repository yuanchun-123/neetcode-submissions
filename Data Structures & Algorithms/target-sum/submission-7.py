class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, cur):
            if i == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0
            key = (i, cur)
            if key in memo:
                return memo[key]
            memo[key] = dp(i+1, cur+nums[i])+dp(i+1, cur-nums[i])
            return memo[key]
        return dp(0, 0)