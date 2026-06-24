class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if total % 2 != 0:
            return False
        memo = {}
        def dp(i, cur):
            if cur == half:
                return True
            if cur > half or i >= len(nums):
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