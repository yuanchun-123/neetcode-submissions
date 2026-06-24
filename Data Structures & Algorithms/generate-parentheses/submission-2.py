class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur, o, c):
            if len(cur) == 2 * n:
                if o != c:
                    return
                res.append(cur[:])
                return
            if c > o:
                return
            dfs(cur+"(", o+1, c)
            dfs(cur+")", o, c+1)
        dfs("", 0, 0)
        return res