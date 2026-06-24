class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        memo1, memo2 = {}, {}
        def dp(i, n, memo):
            if i >= len(n):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i+1, n, memo), dp(i+2, n, memo)+n[i])
            return memo[i]
        
        return max(dp(0, nums[:-1], memo1),
                   dp(0, nums[1:], memo2))

            
            