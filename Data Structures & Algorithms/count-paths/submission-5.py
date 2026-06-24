class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(x, y):
            if x == m-1 and y == n-1:
                return 1
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return 0
            key = (x,y)
            if key in memo:
                return memo[key]
            memo[key] = dp(x, y+1) + dp(x+1, y)
            return memo[key]
        return dp(0, 0)