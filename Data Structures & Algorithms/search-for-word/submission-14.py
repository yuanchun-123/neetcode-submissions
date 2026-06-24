class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r >= m or c >= n or r < 0 or c < 0 \
            or board[r][c] != word[i] or board[r][c] == "!":
                return False
            tmp = board[r][c]
            board[r][c] = "!"
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or\
                  dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            board[r][c] = tmp
            return res
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False
            
            