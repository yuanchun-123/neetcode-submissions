class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            i, j = q.popleft()
            for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+x, j+y
                if 0 <= ni < m and 0 <= nj < n \
                and grid[ni][nj] == 2147483647:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))
                
        
                    