class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i):
            if i == amount:
                return 0
            if i > amount:
                return float('inf')
            if i in memo:
                return memo[i]
            memo[i] = float('inf')
            for c in coins:
                memo[i] = min(dp(i+c)+1, memo[i])
            return memo[i]
        if dp(0) == float('inf'):
            return -1
        return dp(0)
            