class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(cur):
            if cur in memo:
                return memo[cur]
            best = 0
            for x in range(1, cur):
                best = max(x*(cur-x), x*dp(cur-x), best)
            memo[cur] = best
            return memo[cur]
        return dp(n)

        

            
            

        