class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(cur):
            if cur == 1:
                return 1
            if cur in memo:
                return memo[cur]
            memo[cur] = 1
            for x in range(1, cur):
                memo[cur] = max(x*(cur-x), x*dp(cur-x), memo[cur])
            return memo[cur]
        return dp(n)
                