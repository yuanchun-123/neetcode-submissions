class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(i, j):
            if i > j:
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            memo[key] = max(piles[i]-dp(i+1,j), piles[j]-dp(i,j-1))
            return memo[key]
        return dp(0, len(piles)-1) > 0
