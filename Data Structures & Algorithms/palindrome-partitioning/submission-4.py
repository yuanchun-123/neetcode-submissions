class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispar(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(cur, start):
            if start == len(s):
                res.append(cur)
            for j in range(start, len(s)):
                if not ispar(start, j):
                    continue
                dfs(cur+[s[start:j+1]], j+1)
           
        dfs([], 0)
        return res


