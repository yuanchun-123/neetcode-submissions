class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            if n in memo:
                return memo[n]
            best = float('inf')
            for c in coins:
                memo[n] = min(best, 1 + dp(n-c))
                best = memo[n]
            return memo[n]
        if dp(amount) == float('inf'):
            return -1
        else:
            return dp(amount)

