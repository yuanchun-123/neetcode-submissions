class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        m, n = len(text1), len(text2)
        def dp(i, j):
            if i == m or j == n:
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]

            if text1[i] == text2[j]:
                memo[key] = 1 + dp(i+1, j+1)
            else:
                memo[key] = max(dp(i+1, j), dp(i, j+1))
            return memo[key] 
        return dp(0, 0)

                