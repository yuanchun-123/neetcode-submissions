class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            memo[i] = dp(i+1)
            if int(s[i:i+2]) in range(10, 27):
                memo[i] += dp(i+2)
            return memo[i]
        return dp(0)
                

        