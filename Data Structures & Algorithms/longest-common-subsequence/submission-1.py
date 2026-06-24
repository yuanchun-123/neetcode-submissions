class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}
        def dp(x, y):
            if x == m or y == n:
                return 0
            key = (x, y)
            if key in memo:
                return memo[key]
            if text1[x] == text2[y]:
                memo[key] = 1 + dp(x+1, y+1)
            else:
                memo[key] = max(dp(x+1, y), dp(x, y+1))
            return memo[key]
        return dp(0, 0)