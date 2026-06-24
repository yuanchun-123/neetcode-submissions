class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(r, c):
            if r == m-1 and c == n-1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            key = (r, c)
            if key in memo:
                return memo[key]

            memo[key] = dp(r+1, c) + dp(r, c+1)
            return memo[key]
        return dp(0, 0)

            
            