class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(l, r):
            if l == r:
                return piles[l]
            key = (l, r)
            if key in memo:
                return memo[key]
            memo[key] = max(piles[l]-dp(l+1, r), piles[r]-dp(l, r-1))
            return memo[key]
        return dp(0, len(piles)-1) > 0