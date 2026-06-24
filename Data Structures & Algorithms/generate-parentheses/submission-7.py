class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, c, cur):
            if len(cur) == 2*n:
                if o != c:
                    return
                res.append(cur[:])
                return
            if c > o or o > n or c > n:
                return
            dfs(o+1, c, cur+"(")
            dfs(o, c+1, cur+")")
        dfs(0, 0, '')
        return res
