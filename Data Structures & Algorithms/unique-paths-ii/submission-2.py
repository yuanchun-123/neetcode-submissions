class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def dp(x, y):
            if x == m-1 and y == n-1 and obstacleGrid[x][y] == 0:
                return 1
            if x > m-1 or y > n-1 or obstacleGrid[x][y] == 1:
                return 0
            key = (x, y)
            if key in memo:
                return memo[key]
            memo[key] = dp(x+1, y) + dp(x, y+1)
            return memo[key]
        return dp(0, 0)