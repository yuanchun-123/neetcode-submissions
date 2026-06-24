class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapp = {
            '2': 'ABC',
            '3': 'DEF',
            '4': 'GHI',
            '5': 'JKL',
            '6': 'MNO',
            '7': 'PQRS',
            '8': 'TUV',
            '9': 'WXYZ',
            }
        def dfs(cur, i):
            if i == len(digits):
                res.append(cur.lower())
                return
            alphas = mapp[digits[i]]
            for c in alphas:
                dfs(cur+c, i+1)
        if digits:
            dfs('', 0)
        return res




        