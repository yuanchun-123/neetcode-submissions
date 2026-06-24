class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def bfs(i,j):
            q = deque([(i,j)])
            while q:
                qi, qj = q.popleft()
                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = x+qi, y+qj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                        q.append((ni,nj))
                        grid[ni][nj] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i,j)
        return res

            
            
        