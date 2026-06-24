class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones) // 2
        memo = {}
        def dp(i, cur):
            if cur > total:
                return -float('inf')
            if cur == total or i == len(stones):
                return cur
            
            key = (i, cur)
            if key in memo:
                return memo[key]
            memo[key] = max(dp(i+1, cur+stones[i]), dp(i+1, cur))
            return memo[key]
        return sum(stones) - 2 * dp(0, 0)