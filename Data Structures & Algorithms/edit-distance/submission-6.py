class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            key = (i, j)
            if key in memo:
                return memo[key]
            if word1[i] == word2[j]:
                memo[key] = dp(i+1, j+1)
            else:
                memo[key] = min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1)) + 1
            return memo[key]
        return dp(0, 0)
