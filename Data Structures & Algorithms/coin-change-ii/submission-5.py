class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, cur):
            if cur > amount or i == len(coins) :
                return 0
            if amount == cur:
                return 1
            key = (i, cur)
            if key in memo:
                return memo[key]
            memo[key] = dp(i+1, cur) + dp(i, cur+coins[i])
            return memo[key]
        return dp(0, 0)