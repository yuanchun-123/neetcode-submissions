import numpy as np
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i*i for i in range(1, int(np.sqrt(n))+1)]
        memo = {}
        def dp(cur):
            if cur == n:
                return 0
            if cur > n:
                return n
            if cur in memo:
                return memo[cur]
            memo[cur] = n
            for x in nums:
                memo[cur] = min(memo[cur], dp(cur+x)+1)
            return memo[cur]
        return dp(0)
