class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        m, n = len(text1), len(text2)
        def dp(l, r):
            if l >= m or r >= n:
                return 0
            key = (l, r)
            if key in memo:
                return memo[key]
            if text1[l] == text2[r]:
                memo[key] = 1 + dp(l+1, r+1)
            else:
                memo[key] = max(dp(l, r+1), dp(l+1, r))
            return memo[key]
        return dp(0, 0)
