class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(cur):
            if cur == target:
                return 1
            if cur > target:
                return 0
            if cur in memo:
                return memo[cur]
            memo[cur] = 0
            for x in nums:
                memo[cur] += dp(cur+x)
            return memo[cur]
        return dp(0)
                