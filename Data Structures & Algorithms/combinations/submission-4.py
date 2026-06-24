class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, count):
            if count == k:
                res.append(cur.copy())
                return
            if i > n:
                return
            dfs(i + 1, cur + [i], count + 1)
            dfs(i + 1, cur, count)
            
        dfs(1, [], 0)
        return res