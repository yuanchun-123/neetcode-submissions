import math
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        nums = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        def dp(cur):
            if cur == n:
                return 0
            if cur > n:
                return float('inf')
            if cur in memo:
                return memo[cur]
            memo[cur] = float('inf')
            for x in nums:
                memo[cur] = min(memo[cur], dp(cur+x)+1)
            return memo[cur]
        return dp(0)

