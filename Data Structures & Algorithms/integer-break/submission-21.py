class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(x):
            if x <= 0:
                return -n
            if x in memo:
                return memo[x]
            memo[x] = -n
            for m in range(1, x):
                memo[x] = max(memo[x], m * dp(x-m), m * (x-m))
            return memo[x]
        return dp(n)

