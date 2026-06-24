import math
class Solution:
    def numSquares(self, n: int) -> int:
        limit = int(math.sqrt(n))
        memo = {}
        def dp(cur):
            if cur == n:
                return 0
            if cur > n:
                return float('inf')
            if cur in memo:
                return memo[cur]
            memo[cur] = float('inf')
            for x in range(1, limit+2):
                memo[cur] = min(memo[cur], 1 + dp(cur+x*x))
            return memo[cur]
        return dp(0)

