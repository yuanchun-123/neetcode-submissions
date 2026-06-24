class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, l):
            if l == k:
                res.append(cur[:])
                return
            if l > k or i > n:
                return 
            cur.append(i)
            dfs(i+1, cur, l+1)
            cur.pop()
            dfs(i+1, cur, l)
        dfs(1, [], 0)
        return res

        