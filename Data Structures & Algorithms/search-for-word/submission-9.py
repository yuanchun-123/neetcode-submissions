class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r<0 or r>=m or c<0 or c>=n \
            or board[r][c] != word[i]:
                return False

            tmp = board[r][c]
            board[r][c] = "$"

            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or\
                  dfs(r,c+1,i+1) or dfs(r,c-1,i+1) 
            if res:
                return True
            board[r][c] = tmp
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False
        
            
