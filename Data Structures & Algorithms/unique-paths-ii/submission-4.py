class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        memo = {}
        m, n = len(grid), len(grid[0])
        def dp(x, y):
            if x > m-1 or y > n-1 or grid[x][y]==1:
                return 0
            if x == m-1 and y == n-1:
                return 1
            key = (x, y)
            if key in memo:
                return memo[key]
            memo[key] = dp(x+1, y) + dp(x, y+1)
            return memo[key]
        return dp(0, 0)
            
