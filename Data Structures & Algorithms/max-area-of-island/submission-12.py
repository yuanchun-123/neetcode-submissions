class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def bfs(i,j):
            q = deque([(i,j)])
            area = 1
            grid[i][j] = 0
            while q:
                qi, qj = q.popleft()
                for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni, nj = qi+x, qj+y
                    
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]==1:
                        area += 1
                        grid[ni][nj] = 0
                        q.append((ni,nj))
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i,j))
        return res
