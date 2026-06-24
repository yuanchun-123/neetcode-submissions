class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni, nj = x+i, j+y
                    if 0 <= ni < m and 0 <= nj < n \
                    and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append((ni,nj))
                        fresh -= 1
                    
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time




