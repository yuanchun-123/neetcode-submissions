class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def dp(x, y):
            if x == m-1 and y == n-1:
                return grid[x][y]
            if x > m-1 or y > n-1:
                return float('inf')
            key = (x, y)
            if key in memo:
                return memo[key]
            memo[key] = min(dp(x+1, y), dp(x, y+1)) + grid[x][y]
            return memo[key]
        return dp(0, 0)
        