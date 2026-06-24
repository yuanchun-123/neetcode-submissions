class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, cur):
            if cur > amount or i >= len(coins):
                return 0
            if cur == amount:
                return 1
            key = (i, cur)
            if key in memo:
                return memo[key]
            memo[key] = dp(i, cur+coins[i]) + dp(i+1, cur)
            return memo[key]
        return dp(0, 0)