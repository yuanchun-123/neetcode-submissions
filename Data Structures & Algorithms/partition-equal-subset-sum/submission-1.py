class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        total = sum(nums) // 2
        memo = {}
        def dp(i, cur):
            if cur == total:
                return True
            if i >= len(nums):
                return False
            key = (i, cur)
            if key in memo:
                return memo[key]
            if dp(i+1, cur) or dp(i+1, cur+nums[i]):
                memo[key] = True
                return True
            memo[key] = False
            return False
        return dp(0, 0)