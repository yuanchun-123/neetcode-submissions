class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in memo:
                return memo[i]
            best = float('inf')
            for c in coins:
                best = min(best, dp(i-c)+1)
                memo[i] = best
            return memo[i]
        if dp(amount) == float('inf'):
            return -1
        return dp(amount)