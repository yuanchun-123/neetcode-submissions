class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(x):
            if x == amount:
                return 0
            if x > amount:
                return float('inf')
            if x in memo:
                return memo[x]
            memo[x] = float('inf')
            for c in coins:
                memo[x] = min(memo[x], dp(x+c)+1)
            return memo[x]
        if dp(0) == float('inf'):
            return -1
        else:
            return dp(0)


