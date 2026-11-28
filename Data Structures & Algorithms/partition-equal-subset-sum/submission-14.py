class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)
        if t % 2 != 0:
            return False
        target = t / 2

        memo = {}

        def dp(i, cur):
            if cur > target or i >= len(nums):
                return False
            if (i, cur) in memo:
                return memo[(i, cur)]
            if cur == target:
                return True
            memo[(i, cur)] = dp(i+1, cur) or dp(i+1, cur+nums[i])
            return memo[(i, cur)]
        
        return dp(0, 0)
