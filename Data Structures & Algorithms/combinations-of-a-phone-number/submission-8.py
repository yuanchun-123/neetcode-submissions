class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'
                }
        res = []
        def dfs(cur, i):
            if i == len(digits):
                res.append(cur)
                return
            alphas = mapp[digits[i]]
            for c in alphas:
                dfs(cur+c, i+1)
        if digits:
            dfs('', 0)
        return res