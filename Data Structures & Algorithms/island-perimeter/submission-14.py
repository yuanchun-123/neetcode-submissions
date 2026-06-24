class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        seen = set()
        direction = [(1,0), (0,1), (-1,0), (0,-1)]


        def bfs(i, j):
            peri = 0
            queue = deque([(i, j)])
            seen.add((i, j))
            while queue:
                iq, jq = queue.popleft()
                for x, y in direction:
                    ni = iq + x
                    nj = jq + y
                    if ni < 0 or nj < 0 or ni >= m or nj >= n \
                    or grid[ni][nj] == 0:
                        peri += 1
                    elif (ni, nj) not in seen: 
                        seen.add((ni,nj))
                        queue.append((ni,nj))

            return peri
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    return bfs(i,j)
        return 0





            

        