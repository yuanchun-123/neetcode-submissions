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

        def dfs(cur, i):
            if i == len(s):
                res.append(cur[:])
                return
            for j in range(i, len(s)):
                if ispar(i, j):
                    dfs(cur+[s[i:j+1]], j+1)

        dfs([], 0)
        return res
            